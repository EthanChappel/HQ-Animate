import sys
from cx_Freeze import setup, Executable

base = None
if sys.platform == 'win32':
    base = 'Win32GUI'

options = {
    'build_exe': {
        'includes': ['atexit'],
        'packages': ['PIL', 'tkinter', 'sys', 'threading'],
        'include_files': ['__main__.py', 'LICENSE', 'dep-licenses.json']
    },
}

executables = [
    Executable('__main__.py', base=base, targetName='hqan')
]

setup(
    name='HQ-Animate',
    version='0.1.0',
    description='Create high quality APNG and WebP animations from a sequence of images.',
    options=options,
    executables=executables
)