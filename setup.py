import platform
from cx_Freeze import setup, Executable

base = 'Win32GUI' if platform.system() == 'Windows' else None

options = {
    'build_exe': {
        'includes': ['atexit'],
        'packages': ['json', 'ctypes', 'pathlib', 'threading', 'platform', 'tkinter', 'PIL'],
        'include_files': ['__main__.py', 'LICENSE', 'dep-terms.json']
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