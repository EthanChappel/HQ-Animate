#!/usr/bin/env python3
'''
MIT License

Copyright (c) 2020 Ethan Chappel

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

import json
import ctypes
import pathlib
import threading
import platform
import tkinter as tk
from tkinter import messagebox
from tkinter import filedialog
from _tkinter import TclError
import tkinter.ttk as ttk
from PIL import Image


__version__ = '0.1.0'

SYSTEM = platform.system()

if SYSTEM == 'Windows':
    ctypes.windll.shcore.SetProcessDpiAwareness(1)

NAME = 'HQ Animate'

p = 0


def save(tar, o: str, d: int, gif: bool, webp: bool, apng: bool):
    global p
    p = 0
    frames = []
    for n in tar:
        frame = Image.open(n).convert('RGB')
        frames.append(frame)

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

    if webp:
        image.save(
            f"{o}.webp",
            format='WebP',
            save_all=True,
            append_images=frames[1:],
            duration=d,
            loop=0,
            lossless=True,
            quality=100
        )

    p = 2

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

    p = 3


class MainWindow(tk.Tk):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.gifvar = tk.IntVar(value=0)
        self.webpvar = tk.IntVar(value=1)
        self.apngvar = tk.IntVar(value=1)
        self.spinnervar = tk.IntVar(value=20)
        self.in_list = tk.Variable()
        self.out_dir = tk.StringVar()
        self.out_name = tk.StringVar()

        self.in_list.trace_add('write', self.set_convert_button_state)
        self.out_dir.trace_add('write', self.set_convert_button_state)
        self.out_name.trace_add('write', self.set_convert_button_state)

        self.title(NAME)

        self.master_frame = ttk.Frame(self)
        self.master_frame.grid_columnconfigure(1, weight=1)
        self.master_frame.grid_rowconfigure(0, weight=1)
        self.master_frame.pack(fill=tk.BOTH, expand=True)

        self.in_label = ttk.Label(self.master_frame, text='Frames')
        self.in_label.grid(row=0, column=0, padx=(9, 3), pady=(9, 3), sticky=tk.NW)

        self.in_frame = ttk.Frame(self.master_frame, relief=tk.SUNKEN)
        self.in_frame.grid_rowconfigure(0, weight=1)
        self.in_frame.grid_columnconfigure(0, weight=1)
        self.in_frame.grid(row=0, column=1, columnspan=2, padx=(3, 3), pady=(9, 0), sticky=tk.NSEW)

        self.in_listbox = tk.Listbox(self.in_frame, listvariable=self.in_list, borderwidth=0, highlightthickness=0)
        self.in_listbox.grid(row=0, column=0, padx=(2, 0), pady=(2, 0), sticky=tk.NSEW)

        self.in_xscrollbar = ttk.Scrollbar(self.in_frame, orient=tk.HORIZONTAL, command=self.in_listbox.xview)
        self.in_listbox.config(xscrollcommand=self.in_xscrollbar.set)
        self.in_xscrollbar.grid(row=1, column=0, padx=(2, 0), pady=(0, 2), sticky=tk.EW)

        self.in_yscrollbar = ttk.Scrollbar(self.in_frame, orient=tk.VERTICAL, command=self.in_listbox.yview)
        self.in_listbox.config(yscrollcommand=self.in_yscrollbar.set)
        self.in_yscrollbar.grid(row=0, column=1, padx=(0, 2), pady=(2, 0), sticky=tk.NS)

        self.in_browse = ttk.Button(self.master_frame, text='Browse...', command=self.set_input)
        self.in_browse.grid(row=0, column=3, padx=(3, 9), pady=(9, 3), sticky=tk.N)

        self.out_label = ttk.Label(self.master_frame, text='Output')
        self.out_label.grid(row=1, column=0, padx=(9, 3), pady=(3, 3), sticky=tk.W)

        self.out_entry = ttk.Entry(self.master_frame, textvariable=self.out_dir)
        self.out_entry.grid(row=1, column=1, padx=(3, 3), pady=(3, 3), sticky=tk.EW)

        self.out_name_entry = ttk.Entry(self.master_frame, textvariable=self.out_name)
        self.out_name_entry.grid(row=1, column=2, padx=(3, 3), pady=(3, 3), sticky=tk.EW)

        self.out_browse = ttk.Button(self.master_frame, text='Browse...', command=self.set_output)
        self.out_browse.grid(row=1, column=3, padx=(3, 9), pady=(3, 3))

        self.format_label = ttk.Label(self.master_frame, text='Formats')
        self.format_label.grid(row=4, column=0, padx=(9, 3), pady=(3, 3), sticky=tk.W)

        self.checkbutton_frame = ttk.Frame(self.master_frame)
        self.checkbutton_frame.columnconfigure(5, weight=1)
        self.checkbutton_frame.grid(row=4, column=1, columnspan=2, sticky=tk.EW)

        self.apng_checkbutton = ttk.Checkbutton(self.checkbutton_frame, variable=self.apngvar, text='APNG', offvalue=0, onvalue=1, command=self.set_convert_button_state)
        self.apng_checkbutton.grid(row=0, column=0, padx=(3, 3), pady=(3, 3), sticky=tk.W)

        self.webp_checkbutton = ttk.Checkbutton(self.checkbutton_frame, variable=self.webpvar, text='WebP', offvalue=0, onvalue=1, command=self.set_convert_button_state)
        self.webp_checkbutton.grid(row=0, column=1, padx=(3, 3), pady=(3, 3), sticky=tk.W)

        self.gif_checkbutton = ttk.Checkbutton(self.checkbutton_frame, variable=self.gifvar, text='GIF', offvalue=0, onvalue=1, command=self.set_convert_button_state)
        self.gif_checkbutton.grid(row=0, column=2, padx=(3, 3), pady=(3, 3), sticky=tk.W)

        self.separator = ttk.Separator(self.checkbutton_frame, orient=tk.VERTICAL)
        self.separator.grid(row=0, column=3, padx=(3, 3), pady=(3, 3), sticky=tk.NS)

        self.duration_label = ttk.Label(self.checkbutton_frame, text='Length')
        self.duration_label.grid(row=0, column=4, padx=(3, 3), pady=(3, 3), sticky=tk.W)

        self.duration_spinbox = ttk.Spinbox(self.checkbutton_frame, from_=1, to=100000, textvariable=self.spinnervar)
        self.duration_spinbox.grid(row=0, column=5, padx=(3, 3), pady=(3, 3), sticky=tk.EW)

        self.ms_label = ttk.Label(self.master_frame, text='ms')
        self.ms_label.grid(row=4, column=3, padx=(3, 9), pady=(3, 3), sticky=tk.W)

        self.bottom_frame = ttk.Frame(self.master_frame)
        self.bottom_frame.grid_columnconfigure(1, weight=1)
        self.bottom_frame.grid(row=7, column=0, columnspan=4, sticky=tk.EW)

        self.about_button = ttk.Button(self.bottom_frame, text='About...', command=self.show_about)
        self.about_button.grid(row=0, column=0, padx=(9, 3), pady=(3, 9))
        
        self.progress = ttk.Progressbar(self.bottom_frame, maximum=3)
        self.progress.grid(row=0, column=1, padx=(3, 3), pady=(3, 9), sticky=tk.EW)
        
        self.start = ttk.Button(self.bottom_frame, text='Convert', command=self.convert)
        self.start.config(state=tk.DISABLED)
        self.start.config(default=tk.ACTIVE)
        self.start.grid(row=0, column=2, padx=(3, 9), pady=(3, 9))
    
    def set_input(self):
        self.files = filedialog.askopenfilenames(title='Select input file', filetypes=(('Images', '*.bmp *.jp2 *.jpeg *.jpg *.png *.tif *.tiff *.webp'),))
        self.in_listbox.delete(0, tk.END)
        for f in self.files:
            self.in_listbox.insert(tk.END, f)
    
    def set_output(self):
        f = filedialog.askdirectory(title='Select ouput directory')
        self.out_entry.delete(0, tk.END)
        self.out_entry.insert(0, f)
    
    def set_convert_button_state(self, v1=None, v2=None, v3=None):
        if self.in_list.get() and pathlib.Path(self.out_entry.get()).exists() and self.out_name_entry.get() and (self.apngvar.get() or self.gifvar.get() or self.webpvar.get()):
            self.start.config(state=tk.NORMAL)
        else:
            self.start.config(state=tk.DISABLED)
    
    def show_about(self):
        AboutDialog(self)
    
    def convert(self):
        if (self.apngvar.get() and pathlib.Path(f'{self.out_entry.get()}/{self.out_name_entry.get()}.apng').exists()) \
                or (self.webpvar.get() and pathlib.Path(f'{self.out_entry.get()}/{self.out_name_entry.get()}.webp').exists()) \
                or (self.gifvar.get() and pathlib.Path(f'{self.out_entry.get()}/{self.out_name_entry.get()}.gif').exists()):
            if not messagebox.askyesno(f'Overwite - {NAME}', 'Creating animations will overwrite some files. Continue?', parent=self):
                return

        t = threading.Thread(
            target=save,
            args=(
                self.files,
                f'{self.out_entry.get()}/{self.out_name_entry.get()}',
                int(self.duration_spinbox.get()),
                bool(self.gifvar.get()),
                bool(self.webpvar.get()),
                bool(self.apngvar.get())
            ),
        )
        t.dameon = True

        self.in_label.config(state=tk.DISABLED)
        self.in_listbox.config(state=tk.DISABLED)
        self.in_browse.config(state=tk.DISABLED)
        self.out_label.config(state=tk.DISABLED)
        self.out_entry.config(state=tk.DISABLED)
        self.out_name_entry.config(state=tk.DISABLED)
        self.out_browse.config(state=tk.DISABLED)
        self.duration_label.config(state=tk.DISABLED)
        self.duration_spinbox.config(state=tk.DISABLED)
        self.ms_label.config(state=tk.DISABLED)
        self.format_label.config(state=tk.DISABLED)
        self.webp_checkbutton.config(state=tk.DISABLED)
        self.apng_checkbutton.config(state=tk.DISABLED)
        self.gif_checkbutton.config(state=tk.DISABLED)
        self.start.config(state=tk.DISABLED)

        t.start()
        while t.is_alive():
            self.progress.config(value=p)
            self.update()
        
        self.in_label.config(state=tk.NORMAL)
        self.in_listbox.config(state=tk.NORMAL)
        self.in_browse.config(state=tk.NORMAL)
        self.out_label.config(state=tk.NORMAL)
        self.out_entry.config(state=tk.NORMAL)
        self.out_name_entry.config(state=tk.NORMAL)
        self.out_browse.config(state=tk.NORMAL)
        self.duration_label.config(state=tk.NORMAL)
        self.ms_label.config(state=tk.NORMAL)
        self.format_label.config(state=tk.NORMAL)
        self.duration_spinbox.config(state=tk.NORMAL)
        self.webp_checkbutton.config(state=tk.NORMAL)
        self.apng_checkbutton.config(state=tk.NORMAL)
        self.gif_checkbutton.config(state=tk.NORMAL)
        self.start.config(state=tk.NORMAL)


class AboutDialog(tk.Toplevel):
    def __init__(self, master, *args, **kwargs):
        super().__init__(master, *args, **kwargs)

        self.title(f'About - {NAME}')
        self.transient(self.master)

        self.about_frame = ttk.Frame(self)
        self.about_frame.grid_columnconfigure(0, weight=1)
        self.about_frame.grid_rowconfigure(2, weight=1)
        self.about_frame.pack(fill=tk.BOTH, expand=True)

        self.title = ttk.Label(self.about_frame, text=f'{NAME} {__version__}')
        self.title.grid(row=0, column=0, padx=(9, 9), pady=(9, 3), sticky=tk.N)

        self.copyright_label = ttk.Label(self.about_frame, text='©2020 Ethan Chappel')
        self.copyright_label.grid(row=1, column=0, padx=(9, 9), pady=(3, 3), sticky=tk.N)

        self.licenses_frame = ttk.Frame(self.about_frame, relief=tk.SUNKEN)
        self.licenses_frame.grid_rowconfigure(0, weight=1)
        self.licenses_frame.grid_columnconfigure(0, weight=1)
        self.licenses_frame.grid(row=2, column=0, padx=(9, 9), pady=(3, 3), sticky=tk.NSEW)

        self.licenses_text = tk.Text(self.licenses_frame, wrap=tk.WORD, borderwidth=0, highlightthickness=0, font=('Courier New', 9))
        self.licenses_text.grid(row=0, column=0, padx=(2, 0), pady=(2, 2), sticky=tk.NSEW)

        self.licenses_content = f'{NAME}\n{__version__}\n{pathlib.Path("LICENSE").read_text()}\n'
        with open('dep-terms.json', 'r') as f:
            j = json.load(f)
        
        for d in j:
            self.licenses_content += f'\n\n{d["Name"]}\n{d["Version"]}\n{d["LicenseText"]}'
        
        self.licenses_text.insert(tk.END, self.licenses_content)
        self.licenses_text.config(state=tk.DISABLED)

        self.licenses_scrollbar = ttk.Scrollbar(self.licenses_frame, command=self.licenses_text.yview)
        self.licenses_text.config(yscrollcommand=self.licenses_scrollbar.set)
        self.licenses_scrollbar.grid(row=0, column=1, padx=(0, 2), pady=(2, 2), sticky=tk.NS)

        self.close_button = ttk.Button(self.about_frame, text='Close', command=self.ok)
        self.close_button.config(default=tk.ACTIVE)
        self.close_button.grid(row=3, column=0, padx=(9, 9), pady=(3, 9), sticky=tk.E)

    def ok(self):
        self.destroy()


root = MainWindow()
if SYSTEM != 'Windows' and SYSTEM != 'Darwin':
    try:
        root.style = ttk.Style()
        root.style.theme_use('clam')
    except TclError:
        pass
root.mainloop()
