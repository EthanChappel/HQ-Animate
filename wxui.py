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


import threading
import subprocess
import platform
import pathlib
import wx
from wx.lib.mixins.listctrl import ListCtrlAutoWidthMixin
from PIL import Image
import convert


SYSTEM = platform.system()


class MyApp(wx.App):
    def OnInit(self):
        frame = MainFrame()
        frame.Show()
        return True


class MyListCtrl(wx.ListCtrl, ListCtrlAutoWidthMixin):
    def __init__(self, parent, id=wx.ID_ANY, pos=wx.DefaultPosition, size=wx.DefaultSize, style=0):
        wx.ListCtrl.__init__(self, parent, id, pos, size, style)
        ListCtrlAutoWidthMixin.__init__(self)

        self.Bind(wx.EVT_LIST_COL_DRAGGING, self.on_col_dragging)

    def on_col_dragging(self, event):
        event.Veto()


class MainFrame(wx.Frame):
    def __init__(self):
        super().__init__(None, title="HQ Animate", size=(600, 400))

        self.paths = []

        self.wildcards = "; ".join(sorted({f"*{ex}" for ex, f in Image.registered_extensions().items() if f in Image.OPEN}))

        if SYSTEM == 'Windows':
            self.SetDoubleBuffered(True)

        dc = wx.MemoryDC()
        utc_width, _ = dc.GetTextExtent("0000-00-00 00:00:00 UTC")

        self.panel = wx.Panel(self, wx.ID_ANY)
        self.grid_sizer = wx.GridBagSizer(hgap=9, vgap=9)
        self.wrapper_sizer = wx.BoxSizer(wx.VERTICAL)
        self.wrapper_sizer.Add(self.grid_sizer, 1, wx.EXPAND | wx.ALL, 9)

        self.in_label = wx.StaticText(self.panel, label="Frames")
        self.grid_sizer.Add(self.in_label, pos=(0, 0))

        self.in_listbox = MyListCtrl(self.panel, style=wx.LC_REPORT | wx.LC_HRULES | wx.LC_VRULES)
        self.in_listbox.InsertColumn(0, 'Name')
        self.in_listbox.setResizeColumn(0)
        self.in_listbox.InsertColumn(1, 'Time')
        self.in_listbox.SetColumnWidth(1, utc_width + 20)
        self.grid_sizer.Add(self.in_listbox, pos=(0, 1), flag=wx.EXPAND)

        self.in_browse_button = wx.Button(self.panel, label="Browse...")
        self.in_browse_button.Bind(wx.EVT_BUTTON, self.set_input)
        self.grid_sizer.Add(self.in_browse_button, pos=(0, 2))

        self.out_sizer = wx.BoxSizer(wx.HORIZONTAL)
        self.grid_sizer.Add(self.out_sizer, pos=(1, 1), flag=wx.EXPAND)

        self.out_label = wx.StaticText(self.panel, label="Output")
        self.grid_sizer.Add(self.out_label, pos=(1, 0), flag=wx.ALIGN_CENTER_VERTICAL)

        self.out_dir_textctrl = wx.TextCtrl(self.panel)
        self.out_dir_textctrl.Bind(wx.EVT_TEXT, self.on_output_text_changed_event)
        self.out_sizer.Add(self.out_dir_textctrl, proportion=1,flag=wx.EXPAND | wx.ALL)
        self.out_sizer.AddSpacer(9)
        
        self.out_name_textctrl = wx.TextCtrl(self.panel)
        self.out_name_textctrl.Bind(wx.EVT_TEXT, self.on_output_text_changed_event)
        self.out_sizer.Add(self.out_name_textctrl)

        self.out_browse_button = wx.Button(self.panel, label="Browse...")
        self.out_browse_button.Bind(wx.EVT_BUTTON, self.set_output)
        self.grid_sizer.Add(self.out_browse_button, pos=(1, 2))

        self.format_label = wx.StaticText(self.panel, label="Formats")
        self.grid_sizer.Add(self.format_label, pos=(2, 0), flag=wx.ALIGN_CENTER_VERTICAL)

        self.checkbox_sizer = wx.BoxSizer(wx.HORIZONTAL)
        self.grid_sizer.Add(self.checkbox_sizer, pos=(2, 1), flag=wx.EXPAND)

        self.apng_checkbox = wx.CheckBox(self.panel, label="APNG")
        self.apng_checkbox.Bind(wx.EVT_CHECKBOX, self.on_format_checkbox_event)
        self.checkbox_sizer.Add(self.apng_checkbox, flag=wx.ALIGN_CENTER_VERTICAL)
        self.checkbox_sizer.AddSpacer(9)

        self.avif_checkbox = wx.CheckBox(self.panel, label="AVIF")
        self.avif_checkbox.Bind(wx.EVT_CHECKBOX, self.on_format_checkbox_event)
        self.checkbox_sizer.Add(self.avif_checkbox, flag=wx.ALIGN_CENTER_VERTICAL)
        self.checkbox_sizer.AddSpacer(9)

        self.webp_checkbox = wx.CheckBox(self.panel, label="WebP")
        self.webp_checkbox.Bind(wx.EVT_CHECKBOX, self.on_format_checkbox_event)
        self.checkbox_sizer.Add(self.webp_checkbox, flag=wx.ALIGN_CENTER_VERTICAL)
        self.checkbox_sizer.AddSpacer(9)

        self.gif_checkbox = wx.CheckBox(self.panel, label="GIF")
        self.gif_checkbox.Bind(wx.EVT_CHECKBOX, self.on_format_checkbox_event)
        self.checkbox_sizer.Add(self.gif_checkbox, flag=wx.ALIGN_CENTER_VERTICAL)
        self.checkbox_sizer.AddSpacer(9)

        self.seperator = wx.StaticLine(self.panel, style=wx.LI_VERTICAL)
        self.checkbox_sizer.Add(self.seperator, flag=wx.EXPAND)
        self.checkbox_sizer.AddSpacer(9)

        self.frame_duration_label = wx.StaticText(self.panel, label="Frame duration")
        self.checkbox_sizer.Add(self.frame_duration_label, flag=wx.ALIGN_CENTER_VERTICAL)
        self.checkbox_sizer.AddSpacer(9)

        self.frame_duration_spinctrl = wx.SpinCtrl(self.panel, min=1, max=100000, initial=20)
        self.checkbox_sizer.Add(self.frame_duration_spinctrl, proportion=1, flag=wx.EXPAND)

        self.ms_label = wx.StaticText(self.panel, label="ms")
        self.grid_sizer.Add(self.ms_label, pos=(2, 2), flag=wx.ALIGN_CENTER_VERTICAL)

        self.bottom_sizer = wx.BoxSizer(wx.HORIZONTAL)
        self.grid_sizer.Add(self.bottom_sizer, pos=(3, 0), span=(1, 3), flag=wx.EXPAND)

        self.about_button = wx.Button(self.panel, label="About...")
        self.bottom_sizer.Add(self.about_button)
        self.bottom_sizer.AddStretchSpacer(1)

        self.activity_indicator = wx.ActivityIndicator(self.panel)
        self.bottom_sizer.Add(self.activity_indicator)
        self.bottom_sizer.AddSpacer(9)

        self.convert_button = wx.Button(self.panel, label="Convert")
        self.convert_button.Bind(wx.EVT_BUTTON, self.on_convert_start)
        self.bottom_sizer.Add(self.convert_button)

        self.grid_sizer.AddGrowableRow(0, 1)
        self.grid_sizer.AddGrowableCol(1, 1)
        self.panel.SetSizerAndFit(self.wrapper_sizer)

        self.set_convert_button_state()

        self.Layout()
        self.activity_indicator.Hide()
        self.Layout()
        self.Show()
        self.in_listbox.PostSizeEventToParent()

    def set_input(self, event):
        wildcards = "Images|" + self.wildcards
        dialog = wx.FileDialog(self, "Choose animation frames",
            wildcard=wildcards,
            style=wx.FD_OPEN | wx.FD_MULTIPLE | wx.FD_FILE_MUST_EXIST,
        )

        if dialog.ShowModal() == wx.ID_OK:
            self.paths = [convert.Frame(p) for p in dialog.GetPaths()]
            self.in_listbox.DeleteAllItems()
            for i, p in enumerate(self.paths):
                self.in_listbox.InsertItem(i, p.path.name)
                self.in_listbox.SetItem(i, 1, p.date_time.strftime("%Y-%m-%d %H:%M:%S %Z") if p.date_time else "")
            self.in_listbox.Refresh()
            self.in_listbox.Update()
            self.out_dir_textctrl.SetValue(str(self.paths[0].path.parent))
        dialog.Destroy()
        self.set_convert_button_state()
    
    def set_output(self, event):
        dialog = wx.DirDialog(None, "Choose output directory", style=wx.DD_DEFAULT_STYLE | wx.DD_DIR_MUST_EXIST)
        if dialog.ShowModal() == wx.ID_OK:
            chosen_dir = dialog.GetPath()
            self.out_dir_textctrl.SetValue(chosen_dir)
        dialog.Destroy()
        self.set_convert_button_state()

    def on_format_checkbox_event(self, event):
        self.set_convert_button_state()
    
    def on_output_text_changed_event(self, event):
        self.set_convert_button_state()
    
    def set_convert_button_state(self):
        out_dir = pathlib.Path(self.out_dir_textctrl.GetValue())

        do_apng = self.apng_checkbox.GetValue()
        do_avif = self.avif_checkbox.GetValue()
        do_webp = self.webp_checkbox.GetValue()
        do_gif = self.gif_checkbox.GetValue()
        has_input = self.in_listbox.GetItemCount() > 0
        has_output_dir = out_dir.exists() and out_dir.is_absolute()
        has_output_name = len(self.out_name_textctrl.GetValue()) > 0

        self.convert_button.Enable((do_apng or do_avif or do_webp or do_gif) and has_input and has_output_dir and has_output_name)

    def on_convert_start(self, event):
        self.panel.Enable(False)
        self.activity_indicator.Start()
        self.activity_indicator.Show()
        t = threading.Thread(target=self.convert)
        t.start()
    
    def on_convert_end(self):
        out_dir = pathlib.Path(self.out_dir_textctrl.GetValue())

        if SYSTEM == 'Darwin':  # macOS
            subprocess.run(['open', out_dir])
        elif SYSTEM == 'Windows':  # Windows
            subprocess.run(['explorer', out_dir])
        elif SYSTEM.startswith('Linux'):  # Linux
            subprocess.run(['xdg-open', out_dir])
    
        self.activity_indicator.Stop()
        self.activity_indicator.Hide()
        self.Layout()
        self.panel.Enable(True)

    def convert(self):
        convert.save(
            self.paths,
            pathlib.Path(self.out_dir_textctrl.GetValue(), self.out_name_textctrl.GetValue()),
            self.frame_duration_spinctrl.GetValue(),
            self.gif_checkbox.GetValue(),
            self.webp_checkbox.GetValue(),
            self.apng_checkbox.GetValue(),
            self.avif_checkbox.GetValue(),
        )
        wx.CallAfter(self.on_convert_end)
