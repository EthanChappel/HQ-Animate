'''
MIT License

Copyright (c) 2025 Ethan Chappel

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
'''


import itertools
import os
import subprocess
import logging
import platform
import re
from pathlib import Path
from enum import Enum
from PIL import Image, ImageSequence, ImageMath
from astropy.io import fits
from astropy.time import Time
from astropy.coordinates import AltAz, Angle, EarthLocation, solar_system_ephemeris, get_body, position_angle
from astropy import units as u
import numpy as np


TARGETS = {
    "Sun": "sun",
    "Mercury": "mercury",
    "Venus": "venus",
    "Moon": "moon",
    "Mars": "mars",
    "Jupiter": "jupiter",
    "Saturn": "saturn",
    "Uranus": "uranus",
    "Neptune": "neptune",
}


SYSTEM = platform.system()
SCRIPT_PATH = Path(__file__).resolve().parent

logger = logging.getLogger("app")


class Frame:
    def __init__(self, path):
        self.path = Path(path)
        self.date_time = None
        self.target = None

        match = re.match(r"(.?)(\d{4})-(\d{2})-(\d{2})[-_](\d{2})-?(\d{2})[-_](\d{1,2})([\s\S]*)\.", self.path.name)

        if self.path.suffix.lower() in ('.fits', '.fit'):
            with fits.open(self.path) as hdul:
                header = hdul[0].header
                date_obs_string = header.get('DATE-OBS')
                time_scale = str(header.get('TIMESYS', 'UTC')).lower()
                if date_obs_string:
                    self.date_time = Time(date_obs_string, format='fits', scale=time_scale).utc
                    return

        if match:
            g1 = match.group(1)
            g8 = match.group(8)

            if g1.startswith("sun") or "Sun" in g8:
                self.target = "Sun"
            elif g1.startswith("mercury") or "Mer" in g8:
                self.target = "Mercury"
            elif g1.startswith("v") or "Ven" in g8:
                self.target = "Venus"
            elif g1.startswith("moon") or "Moon" in g8:
                self.target = "Moon"
            elif g1.startswith("mats") or "Mar" in g8:
                self.target = "Mars"
            elif g1.startswith("j") or "Jup" in g8:
                self.target = "Jupiter"
            elif g1.startswith("s") or "Sat" in g8:
                self.target = "Saturn"
            elif g1.startswith("u") or "Ura" in g8:
                self.target = "Uranus"
            elif g1.startswith("n") or "Nep" in g8:
                self.target = "Neptune"            

            year = match.group(2)
            month = match.group(3)
            day = match.group(4)
            hour = match.group(5)
            minute = match.group(6)
            second = match.group(7)
            if match.group(1) == "":
                second = str(int(second) * 6).rjust(2, "0")
            
            self.date_time = Time(f"{year}-{month}-{day} {hour}:{minute}:{second}", format="iso")

            logger.info(f"New Frame Path={self.path}, Target={self.target}, Time={self.date_time}")
    
    def __str__(self):
        return self.path.name

class WebMCodec(str, Enum):
    VP9 = 0
    AV1 = 1

class MP4Codec(str, Enum):
    VP9 = 0
    AV1 = 1
    AVC = 2

class SubtractMode(str, Enum):
    No = 0
    L = 1
    RGB = 2


class FormatOptions:
    pass


class APNGOptions(FormatOptions):
    def __init__(self, compression_level: int=9, optimize: bool=True):
        self.compression_level = compression_level
        self.optimize = optimize


class AVIFOptions(FormatOptions):
    def __init__(self, quality: int=95):
        self.quality = quality


class WebPOptions(FormatOptions):
    def __init__(self, quality: int=95, lossless: bool=False):
        self.quality = quality
        self.lossless = lossless


class GIFOptions(FormatOptions):
    def __init__(self, optimize: bool=True):
        self.optimize = optimize


class VideoOptions:
    def __init__(self, loop: int=1):
        self.loop = loop


class MP4Options(FormatOptions):
    def __init__(self, codec: MP4Codec|str=MP4Codec.AVC):
        if isinstance(codec, str):
            codec = MP4Codec(codec)
        self.codec = codec


class WebMOptions(FormatOptions):
    def __init__(self, codec: WebMCodec|str=WebMCodec.VP9):
        if isinstance(codec, str):
            codec = WebMCodec(codec)
        self.codec = codec


class DerotationOptions:
    def __init__(self, latitude: float, longitude: float, target: str):
        self.latitude = latitude
        self.longitude = longitude
        self.target = target

class ProcessOptions:
    def __init__(self, average_frames: int=1, subtract_frames: SubtractMode=SubtractMode.No):
        self.average_frames = average_frames
        self.subtract_frames = subtract_frames


def find_ffmpeg() -> list[Path]:
    exe_name = "ffmpeg.exe" if SYSTEM == "Windows" else "ffmpeg"

    ffmpeg_paths = []
    for p in [Path(SCRIPT_PATH, exe_name)] + [Path(p, exe_name) for p in os.environ["PATH"].split(os.pathsep)]:
        if p.is_file():
            ffmpeg_path = p.resolve()
            logger.info(f"Found FFmpeg: {ffmpeg_path}")
            ffmpeg_paths.append(ffmpeg_path)
    
    return ffmpeg_paths


def validate_ffmpeg(path: str) -> dict[str, bool]:
    features = {"avc": False, "av1": False, "vp9": False}

    try:
        logger.info(f"Validate FFmpeg Path={path}")
        popen_cmd = (path, '-encoders')
        popen_parameters = {'stdout': subprocess.PIPE, 'text': True, 'encoding': 'utf-8'}
        proc = subprocess.Popen(popen_cmd, creationflags=subprocess.CREATE_NO_WINDOW if SYSTEM == "Windows" else 0, **popen_parameters)
        stdout, stderr = proc.communicate()
        features["avc"] = bool(re.search(r"^ V[\.FSXBD]{5} libx264", stdout, flags=re.MULTILINE))
        features["av1"] = bool(re.search(r"^ V[\.FSXBD]{5} librav1e", stdout, flags=re.MULTILINE))
        features["vp9"] = bool(re.search(r"^ V[\.FSXBD]{5} libvpx-vp9", stdout, flags=re.MULTILINE))
        logger.info(f"FFmpeg features: {features}")
    except:
        logger.info("FFmpeg not validated.")

    return features


def get_body_angle(body_name: str, time: Time, location: EarthLocation) -> Angle | None:
    body = get_body(body_name, time, location).transform_to(AltAz(location=location, obstime=time))
    return position_angle(body.az, body.alt, 0, location.lat.value * u.deg)


def save(tar: list[Frame], out_path: Path, frame_duration: int, apng_options: APNGOptions=None, avif_options: AVIFOptions=None, gif_options: GIFOptions=None, webp_options: WebPOptions=None, mp4_options: MP4Options=None, webm_options: WebMOptions=None, derotation_options: DerotationOptions=None, video_options: VideoOptions=None, process_options: ProcessOptions=None, ffmpeg_path: Path=None):
    log_str = f"Start processing {len(tar)} frames, Output={out_path}, GIF={gif_options != None}, WebP={webp_options != None}, APNG={apng_options != None}, AVIF={avif_options != None}, MP4={mp4_options != None}, WebM={webm_options != None}"
    if derotation_options != None:
        log_str += f", Target={derotation_options.target}, Latitude={int(derotation_options.latitude)}, Longitude={int(derotation_options.longitude)}"
    logger.info(log_str)
    
    frames = []
    q1 = None
    icc_profile = None
    is_color = False
    for n in tar:
        rotation = 0
        if derotation_options != None:
            with solar_system_ephemeris.set('builtin'):
                observer = EarthLocation(lat=derotation_options.latitude * u.deg, lon=derotation_options.longitude * u.deg)
                if q1 == None:
                    q1 = get_body_angle(derotation_options.target.lower(), n.date_time, observer)
                else:
                    q2 = get_body_angle(derotation_options.target.lower(), n.date_time, observer)

                    rotation = q2.deg - q1.deg

        image = Image.open(n.path)
        for i, frame in enumerate(ImageSequence.Iterator(image)):
            f = frame.copy()

            icc = frame.info.get("icc_profile")
            if not icc_profile and icc:
                icc_profile = icc

            logger.info(f"Process frame {i} Mode={f.mode}, Rotation={rotation:0.2f}")

            if f.mode == 'I;16':
                f = ImageMath.eval('im >> 8', im=f.convert('I')).convert('L')
            if not is_color and 'RGB' in f.mode:
                is_color = True
            if derotation_options != None:
                f = f.resize((f.width * 4, f.height * 4), resample=Image.BICUBIC)
                f = f.rotate(rotation, resample=Image.BICUBIC)
                f = f.resize((f.width // 4, f.height // 4), resample=Image.BICUBIC)
            
            frames.append(f)
    
    average_frames = process_options.average_frames
    if process_options.average_frames > 1:
        tmp = []
        for i in range(average_frames - 1, len(frames)):
            cumulative = np.zeros((frames[0].height, frames[0].width, len(frames[0].getbands())), dtype=np.int32)
            for j in range(average_frames):
                print(f"{i} {j}")
                cumulative += np.array(frames[i - j])
            cumulative = (cumulative // np.int32(average_frames)).astype(np.int8)
            tmp.append(Image.fromarray(cumulative, mode="RGB" if is_color else "L"))
        frames = tmp

    image = frames[0]

    duration = int(1000 / frame_duration)

    if apng_options != None:
        filename = f"{out_path}.apng"

        logger.info(f"Create APNG Path={filename}, Compression={apng_options.compression_level}, Optimize={apng_options.optimize}")
        
        image.save(
            filename,
            format='PNG',
            save_all=True,
            append_images=frames[1:],
            duration=duration,
            loop=0,
            compress_level=apng_options.compression_level,
            optimize=apng_options.optimize,
            icc_profile=icc_profile,
        )

    if avif_options != None:
        filename = f"{out_path}.avif"
        subsampling = "4:4:4"

        logger.info(f"Create AVIF Path={filename}, Quality={avif_options.quality}, Subsampling={subsampling}")
        
        image.save(
            filename,
            format='AVIF',
            save_all=True,
            append_images=frames[1:],
            duration=duration,
            loop=0,
            quality=avif_options.quality,
            subsampling=subsampling,
            icc_profile=icc_profile,
        )

    if webp_options != None:
        filename = f"{out_path}.webp"
        method = 3

        logger.info(f"Create WebP Path={filename}, Quality={webp_options.quality}, Lossless={webp_options.lossless}, Method={method}")

        image.save(
            filename,
            format='WebP',
            save_all=True,
            append_images=frames[1:],
            duration=duration,
            loop=0,
            lossless=webp_options.lossless,
            quality=webp_options.quality,
            method=method,
            icc_profile=icc_profile,
        )

    if gif_options != None:
        filename = f"{out_path}.gif"

        logger.info(f"Create GIF Path={filename}, Optimize={gif_options.optimize}")

        image.save(
            filename,
            format='GIF',
            save_all=True,
            append_images=frames[1:],
            duration=duration,
            loop=0,
            optimize=gif_options.optimize,
        )
    
    if (mp4_options != None or webm_options != None) and ffmpeg_path != None:
        video_length = len(frames) * video_options.loop

        ffmpeg_options = [
            str(ffmpeg_path), '-y',
            '-f', 'rawvideo',
            '-pixel_format', 'rgb24' if is_color else 'gray',
            '-video_size', f'{image.width}x{image.height}',
            '-r', str(frame_duration),
            '-i', 'pipe:0',
        ]
        output_options = [
            '-frames:v', str(video_length),
            '-r', str(frame_duration),
        ]
        avc_options = [
            '-c:v', 'libx264',
            '-profile:v', 'main',
            '-pix_fmt', 'yuv420p',
            '-crf', '1',
        ]
        av1_options = [
            '-c:v', 'librav1e',
            '-qp', '0',
        ]
        vp9_options = [
            '-c:v', 'libvpx-vp9',
            '-row-mt', '1',
            '-b:v', '0',
            '-crf', '0',
            '-lossless', '1',
        ]
        
        if mp4_options != None:
            filename = f"{out_path}.mp4"
            codec = mp4_options.codec

            logger.info(f"Create MP4 Path={filename}, Codec={codec}")
            
            ffmpeg_options += output_options
            if codec == MP4Codec.AVC:
                ffmpeg_options += avc_options
            elif codec == MP4Codec.AV1:
                ffmpeg_options += av1_options
            elif codec == MP4Codec.VP9:
                ffmpeg_options += vp9_options
            ffmpeg_options += [filename]
        
        if webm_options != None:
            filename = f"{out_path}.webm"
            codec = webm_options.codec

            logger.info(f"Create WebM Path={filename}, Codec={codec}")

            ffmpeg_options += output_options
            if codec == WebMCodec.AV1:
                ffmpeg_options += av1_options
            elif codec == WebMCodec.VP9:
                ffmpeg_options += vp9_options
            ffmpeg_options += [filename]

        logger.info("Run FFmpeg: " + " ".join(ffmpeg_options))
        
        process = subprocess.Popen(ffmpeg_options, creationflags=subprocess.CREATE_NO_WINDOW if SYSTEM == "Windows" else 0, stdin=subprocess.PIPE)
        
        for f in itertools.islice(itertools.cycle(frames), video_length):
            process.stdin.write(f.tobytes())
        process.stdin.close()
        process.wait()
