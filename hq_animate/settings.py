import logging
import json
from pathlib import Path
from hq_animate.convert import APNGOptions, AVIFOptions, AnimationMode, WebPOptions, GIFOptions, MP4Options, WebMOptions, VideoOptions, DerotationOptions, AnimationOptions, MP4Codec, WebMCodec


SCRIPT_PATH = Path(__file__).resolve().parent


LATITUDE_MIN = -90
LATITUDE_MAX = 90

LONGITUDE_MIN = -180
LONGITUDE_MAX = 180

QUALITY_MIN = 1
QUALITY_MAX = 100

FRAME_LENGTH_MIN = 1
FRAME_LENGTH_MAX = 100000


logger = logging.getLogger("app")


class Settings:
    _file_instances = {}

    def __init__(self, path: Path=Path(SCRIPT_PATH, "settings.json"), field_derotation: bool=False, \
                 do_apng: bool=False, do_avif: bool=False, do_webp: bool=False, do_gif: bool=False, do_mp4: bool=False, do_webm: bool=False, frame_length: int=10, animation_options: AnimationOptions=AnimationOptions(), show_folder: bool=True, ffmpeg_path: str="", \
                 derotation_options=DerotationOptions(), apng_options: APNGOptions=APNGOptions(), avif_options: AVIFOptions=AVIFOptions(), gif_options: GIFOptions=GIFOptions(), webp_options: WebPOptions=WebPOptions(), mp4_options: MP4Options=MP4Options(), webm_options: WebMOptions=WebMOptions(), video_options: VideoOptions=VideoOptions()):
        if not LATITUDE_MIN <= derotation_options.latitude and derotation_options.latitude <= LATITUDE_MAX:
            raise ValueError(f"latitude is {derotation_options.latitude}, but must be within the range of {LATITUDE_MIN} and {LATITUDE_MAX}.")
        if not LONGITUDE_MIN <= derotation_options.longitude and derotation_options.longitude <= LONGITUDE_MAX:
            raise ValueError(f"longitude is {derotation_options.longitude}, but must be within the range of {LONGITUDE_MIN} and {LONGITUDE_MAX}.")

        self.path = path
        self.field_derotation = field_derotation
        self.do_apng = do_apng
        self.do_avif = do_avif
        self.do_webp = do_webp
        self.do_gif = do_gif
        self.do_mp4 = do_mp4
        self.do_webm = do_webm
        self.frame_length = frame_length
        self.animation_options = animation_options
        self.derotation_options = derotation_options
        self.apng_options = apng_options
        self.avif_options = avif_options
        self.gif_options = gif_options
        self.webp_options = webp_options
        self.mp4_options = mp4_options
        self.webm_options = webm_options
        self.video_options = video_options
        self.show_folder = show_folder
        self.ffmpeg_path = ffmpeg_path

        logger.info(f"New Settings: {self.path}")
    
    def save(self):
        j = {
            'field_derotation': self.field_derotation,
            'do_apng': self.do_apng,
            'do_avif': self.do_avif,
            'do_webp': self.do_webp,
            'do_gif': self.do_gif,
            'do_mp4': self.do_mp4,
            'do_webm': self.do_webm,
            'frame_length': self.frame_length,
            'animation_options': self.animation_options.__dict__,
            'show_folder': self.show_folder,
            'ffmpeg_path': self.ffmpeg_path,
            'derotation_options': self.derotation_options.__dict__,
            'apng_options': self.apng_options.__dict__,
            'avif_options': self.avif_options.__dict__,
            'gif_options': self.gif_options.__dict__,
            'webp_options': self.webp_options.__dict__,
            'mp4_options': self.mp4_options.__dict__,
            'webm_options': self.webm_options.__dict__,
            'video_options': self.video_options.__dict__,
        }

        logger.info(f"Save Settings: {self.path}")
        
        with open(self.path, 'w') as f:
            json.dump(j, f)
    
    @staticmethod
    def from_file_or_default(path: Path):
        logger.info(f"Load settings file or use default: {path}")
        if path in Settings._file_instances.keys():
            logger.info(f"Found Settings instance: {path}")
            s = Settings._file_instances[path]
            return s
        if not path.exists():
            logger.info(f"Loaded new settings file: {path}")
            s = Settings(path)
            Settings._file_instances[path] = s
            return s
        with open(path, 'r') as f:
            logger.info(f"Found settings file: {path}")
            j = json.load(f)

            animation_options = j.get('animation_options', {})
            if 'animation_mode' in animation_options.keys():
                animation_options['animation_mode'] = AnimationMode(animation_options['animation_mode'])

            mp4_options = j.get('mp4_options', {})
            if 'codec' in mp4_options.keys():
                mp4_options['codec'] = MP4Codec(mp4_options['codec'])

            webm_options = j.get('webm_options', {})
            if 'codec' in webm_options.keys():
                webm_options['codec'] = WebMCodec(webm_options['codec'])

            s = Settings(
                path,
                j['field_derotation'],
                j['do_apng'],
                j['do_avif'],
                j['do_webp'],
                j['do_gif'],
                j['do_mp4'],
                j['do_webm'],
                j['frame_length'],
                AnimationOptions(**(animation_options)),
                j['show_folder'],
                j['ffmpeg_path'],
                DerotationOptions(**(j.get('derotation_options', {}))),
                APNGOptions(**(j.get('apng_options', {}))),
                AVIFOptions(**(j.get('avif_options', {}))),
                GIFOptions(**(j.get('gif_options', {}))),
                WebPOptions(**(j.get('webp_options', {}))),
                MP4Options(**(mp4_options)),
                WebMOptions(**(webm_options)),
                VideoOptions(**j.get('video_options', {})),
            )

            Settings._file_instances[path] = s
            return s
