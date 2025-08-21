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


import subprocess
import re
from pathlib import Path
from enum import Enum
from PIL import Image, ImageSequence
from astropy.io import fits
from astropy.time import Time
from astropy.coordinates import solar_system_ephemeris, EarthLocation, get_body, HADec
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


script_path = Path(__file__).resolve().parent


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
    
    def __str__(self):
        return self.path.name

class WebMCodec(str, Enum):
    VP9 = 0
    AV1 = 1

class MP4Codec(str, Enum):
    VP9 = 0
    AV1 = 1
    AVC = 2


def validate_ffmpeg(path: str):
    features = {"avc": False, "av1": False, "vp9": False}

    try:
        proc = subprocess.Popen([path, '-encoders'], stdout=subprocess.PIPE, text=True, creationflags=subprocess.CREATE_NO_WINDOW, encoding='utf-8')
        stdout, stderr = proc.communicate()
        features["avc"] = bool(re.search(r"^ V[\.FSXBD]{5} libx264", stdout, flags=re.MULTILINE))
        features["av1"] = bool(re.search(r"^ V[\.FSXBD]{5} librav1e", stdout, flags=re.MULTILINE))
        features["vp9"] = bool(re.search(r"^ V[\.FSXBD]{5} libvpx-vp9", stdout, flags=re.MULTILINE))
    except:
        pass

    return features


def save(tar: list[Frame], o: Path, d: int, gif: bool, webp: bool, apng: bool, avif: bool, mp4: bool, webm: bool, mp4_codec: MP4Codec, webm_codec: WebMCodec, quality: int, lossless: bool=True, derotate: bool=False, latitude: float=0, longitude: float=0, target: str=None):
    frames = []
    observer = EarthLocation(lat=latitude * u.deg, lon=longitude * u.deg)
    t1 = None
    for n in tar:
        rotation = 0
        if derotate:
            with solar_system_ephemeris.set('builtin'):
                t2 = n.date_time
                if t1 == None:
                    t1 = t2
                else:
                    a1 = get_body(target.lower(), t1, observer)
                    a2 = get_body(target.lower(), t2, observer)

                    hadec1 = a1.transform_to(HADec(obstime=t1, location=observer))
                    hadec2 = a2.transform_to(HADec(obstime=t2, location=observer))

                    ha1_rad = hadec1.ha.radian
                    dec1_rad = hadec1.dec.radian

                    ha2_rad = hadec2.ha.radian
                    dec2_rad = hadec2.dec.radian

                    tan_lat_rad = np.tan(np.radians(latitude))

                    q1 = np.degrees(np.arctan(np.sin(ha1_rad) / (tan_lat_rad) * np.cos(dec1_rad) - np.sin(dec1_rad) * np.cos(ha1_rad)))
                    q2 = np.degrees(np.arctan(np.sin(ha2_rad) / (tan_lat_rad) * np.cos(dec2_rad) - np.sin(dec2_rad) * np.cos(ha2_rad)))

                    rotation = q2 - q1

        image = Image.open(n.path)
        for frame in ImageSequence.Iterator(image):
            f = frame.convert('RGB').copy()
            if derotate:
                f = f.resize((f.width * 4, f.height * 4), resample=Image.BICUBIC)
                f = f.rotate(rotation, resample=Image.BICUBIC)
                f = f.resize((f.width // 4, f.height // 4), resample=Image.BICUBIC)
            frames.append(f)

    image = frames[0]

    duration = int(1000 / d)

    if apng:
        image.save(
            f"{o}.apng",
            format='PNG',
            save_all=True,
            append_images=frames[1:],
            duration=duration,
            loop=0,
            optimize=True
        )

    if avif:
        image.save(
            f"{o}.avif",
            format='AVIF',
            save_all=True,
            append_images=frames[1:],
            duration=duration,
            loop=0,
            quality=quality,
            subsampling="4:4:4",
        )

    if webp:
        image.save(
            f"{o}.webp",
            format='WebP',
            save_all=True,
            append_images=frames[1:],
            duration=duration,
            loop=0,
            lossless=lossless,
            quality=quality,
            method=3
        )

    if gif:
        image.save(
            f"{o}.gif",
            format='GIF',
            save_all=True,
            append_images=frames[1:],
            duration=duration,
            loop=0,
            optimize=True
        )
    
    if mp4 or webm:
        ffmpeg_options = [
            str(Path('ffmpeg')), '-y',
            '-f', 'rawvideo',
            '-pixel_format', 'rgb24',
            '-video_size', f'{image.width}x{image.height}',
            '-r', str(d),
            '-i', 'pipe:0',
        ]
        output_options = [
            '-frames:v', str(len(frames)),
            '-r', str(d),
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
            '-lossless', str(int(lossless)),
        ]
        
        if mp4:
            ffmpeg_options += output_options
            if mp4_codec == MP4Codec.AVC:
                ffmpeg_options += avc_options
            elif mp4_codec == MP4Codec.AV1:
                ffmpeg_options += av1_options
            elif mp4_codec == MP4Codec.VP9:
                ffmpeg_options += vp9_options
            ffmpeg_options += [f'{o}.mp4']
        
        if webm:
            ffmpeg_options += output_options
            if webm_codec == WebMCodec.AV1:
                ffmpeg_options += av1_options
            elif webm_codec == WebMCodec.VP9:
                ffmpeg_options += vp9_options
            ffmpeg_options += [f'{o}.webm']

        process = subprocess.Popen(ffmpeg_options, stdin=subprocess.PIPE)
        
        for f in frames:
            process.stdin.write(f.tobytes())
        process.stdin.close()
        process.wait()
