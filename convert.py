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


import re
import datetime
import pathlib
from PIL import Image, ImageSequence
from skyfield.api import load, load_file, wgs84
import numpy as np


TARGETS = {
    "Sun": "SUN",
    "Mercury": "MERCURY",
    "Venus": "VENUS",
    "Moon": "MOON",
    "Mars": "MARS",
    "Jupiter": "JUPITER BARYCENTER",
    "Saturn": "SATURN BARYCENTER",
    "Uranus": "URANUS BARYCENTER",
    "Neptune": "NEPTUNE BARYCENTER",
}

script_path = pathlib.Path(__file__).resolve().parent

planets = load_file(str(pathlib.Path(script_path, 'de423.bsp')))
ts = load.timescale()


class Frame:
    def __init__(self, path):
        self.path = pathlib.Path(path)

        match = re.match(r"(.?)(\d{4})-(\d{2})-(\d{2})[-_](\d{2})-?(\d{2})[-_](\d{1,2})", self.path.name)

        self.date_time = None

        if match:
            year = match.group(2)
            month = match.group(3)
            day = match.group(4)
            hour = match.group(5)
            minute = match.group(6)
            second = match.group(7)
            if match.group(1) == "":
                second = str(int(second) * 6).rjust(2, "0")
            
            self.date_time = datetime.datetime.strptime(f"{year}{month}{day}{hour}{minute}{second}", "%Y%m%d%H%M%S").replace(tzinfo=datetime.timezone.utc)
    
    def __str__(self):
        return self.path.name


def save(tar: list[Frame], o: str, d: int, gif: bool, webp: bool, apng: bool, avif: bool, derotate=False, latitude=0, longitude=0, target=None):
    frames = []
    observer = planets["Earth"] + wgs84.latlon(latitude, longitude)
    t1 = None
    total_rotation = 0
    for n in tar:
        if derotate:
            t2 = ts.from_datetime(n.date_time)
            if t1 != None:
                a1 = observer.at(t1).observe(planets[TARGETS[target]])
                a2 = observer.at(t2).observe(planets[TARGETS[target]])

                ha1, dec1, _ = a1.apparent().hadec()
                ha2, dec2, _ = a2.apparent().hadec()

                q1 = np.degrees(np.arctan(np.sin(ha1.radians) / (np.tan(np.radians(latitude)) * np.cos(dec1.radians) - np.sin(dec1.radians) * np.cos(ha1.radians))))
                q2 = np.degrees(np.arctan(np.sin(ha2.radians) / (np.tan(np.radians(latitude)) * np.cos(dec2.radians) - np.sin(dec2.radians) * np.cos(ha2.radians))))

                total_rotation += q2 - q1

            t1 = t2

        image = Image.open(n.path)
        for frame in ImageSequence.Iterator(image):
            f = frame.convert('RGB').copy()
            if derotate:
                f = f.rotate(total_rotation, resample=Image.BICUBIC)
            frames.append(f)

    image = frames[0]

    if apng:
        image.save(
            f"{o}.apng",
            format='PNG',
            save_all=True,
            append_images=frames[1:],
            duration=d,
            loop=0,
            optimize=True
        )

    p = 1

    if avif:
        image.save(
            f"{o}.avif",
            format='AVIF',
            save_all=True,
            append_images=frames[1:],
            duration=d,
            loop=0,
            lossless=True,
            quality=100,
            speed=0
        )

    p = 2

    if webp:
        image.save(
            f"{o}.webp",
            format='WebP',
            save_all=True,
            append_images=frames[1:],
            duration=d,
            loop=0,
            lossless=True,
            quality=100,
            method=6
        )

    p = 3

    if gif:
        image.save(
            f"{o}.gif",
            format='GIF',
            save_all=True,
            append_images=frames[1:],
            duration=d,
            loop=0,
            optimize=True
        )

    p = 4
