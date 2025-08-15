import json
from pathlib import Path
from convert import Codec

LATITUDE_MIN = -90
LATITUDE_MAX = 90

LONGITUDE_MIN = -180
LONGITUDE_MAX = 180

QUALITY_MIN = 1
QUALITY_MAX = 100

FRAME_LENGTH_MIN = 1
FRAME_LENGTH_MAX = 100000


class Settings:
    def __init__(self, path: Path, field_derotation: bool=False, latitude: float=0, longitude: float=0, do_apng: bool=False, do_avif: bool=False, do_webp: bool=False, do_gif: bool=False, do_mp4: bool=False, frame_length: int=100, quality: int=100, mp4_codec: Codec = Codec.AVC, show_folder: bool=True, ffmpeg_path: str=""):
        if not LATITUDE_MIN <= latitude and latitude <= LATITUDE_MAX:
            raise ValueError(f"latitude is {latitude}, but must be within the range of {LATITUDE_MIN} and {LATITUDE_MAX}.")
        if not LONGITUDE_MIN <= longitude and longitude <= LONGITUDE_MAX:
            raise ValueError(f"longitude is {longitude}, but must be within the range of {LONGITUDE_MIN} and {LONGITUDE_MAX}.")
        if not FRAME_LENGTH_MIN <= frame_length and frame_length <= FRAME_LENGTH_MAX:
            raise ValueError(f"frame_length is {frame_length}, but must be within the range of {FRAME_LENGTH_MIN} and {FRAME_LENGTH_MAX}.")
        if not QUALITY_MIN <= quality and quality <= QUALITY_MAX:
            raise ValueError(f"quality is {quality}, but must be within the range of {QUALITY_MIN} and {QUALITY_MAX}.")
        if not Path(ffmpeg_path).exists():
            raise ValueError(f"ffmpeg path {ffmpeg_path} does not exist.")

        self.path = path
        self.field_derotation = field_derotation
        self.latitude = latitude
        self.longitude = longitude
        self.do_apng = do_apng
        self.do_avif = do_avif
        self.do_webp = do_webp
        self.do_gif = do_gif
        self.do_mp4 = do_mp4
        self.frame_length = frame_length
        self.quality = quality
        self.mp4_codec = mp4_codec
        self.show_folder = show_folder
        self.ffmpeg_path = ffmpeg_path
    
    def save(self):
        j = {
            'field_derotation': self.field_derotation,
            'latitude': self.latitude,
            'longitude': self.longitude,
            'do_apng': self.do_apng,
            'do_avif': self.do_avif,
            'do_webp': self.do_webp,
            'do_gif': self.do_gif,
            'do_mp4': self.do_mp4,
            'frame_length': self.frame_length,
            'quality': self.quality,
            'mp4_codec': self.mp4_codec,
            'show_folder': self.show_folder,
            'ffmpeg_path': self.ffmpeg_path,
        }
        with open(self.path, 'w') as f:
            json.dump(j, f)
    
    @staticmethod
    def from_file_or_default(path: Path):
        if not path.exists():
            return Settings(path)
        with open(path, 'r') as f:
            j = json.load(f)
            return Settings(
                path,
                j['field_derotation'],
                j['latitude'],
                j['longitude'],
                j['do_apng'],
                j['do_avif'],
                j['do_webp'],
                j['do_gif'],
                j['do_mp4'],
                j['frame_length'],
                j['quality'],
                j['mp4_codec'],
                j['show_folder'],
                j['ffmpeg_path'],
            )
