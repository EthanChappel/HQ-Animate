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


import os
import threading
import subprocess
import platform
from pathlib import Path
import wx
import wx.adv
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
        super().__init__(None, title="HQ Animate", size=(600, 500))
        if not self.settings.ffmpeg_path:
            exe_name = "ffmpeg.exe" if SYSTEM == "Windows" else "ffmpeg"

            for p in [Path(exe_name)] + [Path(p, exe_name) for p in os.environ["PATH"].split(os.pathsep)]:
                if p.is_file():
                    self.settings.ffmpeg_path = p.resolve()
                    break


        self.can_avc = False
        self.can_av1 = False

        spacing = 6

        self.paths = []

        self.wildcards = "; ".join(sorted({f"*{ex}" for ex, f in Image.registered_extensions().items() if f in Image.OPEN}))

        if SYSTEM == 'Windows':
            self.SetDoubleBuffered(True)

        dc = wx.MemoryDC()
        utc_width = dc.GetTextExtent("0000-00-00 00:00:00 UTC").Width + 20
        longitude_width = dc.GetTextExtent("-180.00").Width + 30

        self.panel = wx.Panel(self, wx.ID_ANY)
        self.wrapper_sizer = wx.BoxSizer(wx.VERTICAL)

        self.book = wx.Simplebook(self.panel)
        self.wrapper_sizer.Add(self.book, 1, wx.EXPAND | wx.ALL, spacing)

        self.main_panel = wx.Panel(self.book, wx.ID_ANY)

        self.grid_sizer = wx.GridBagSizer(hgap=spacing, vgap=spacing)
        self.main_panel.SetSizerAndFit(self.grid_sizer)
        self.book.AddPage(self.main_panel, "")

        self.in_label = wx.StaticText(self.main_panel, label="Frames")
        self.grid_sizer.Add(self.in_label, pos=(0, 0))

        self.in_listbox = MyListCtrl(self.main_panel, style=wx.LC_REPORT | wx.LC_HRULES | wx.LC_VRULES)
        self.in_listbox.InsertColumn(0, 'Name')
        self.in_listbox.setResizeColumn(0)
        self.in_listbox.InsertColumn(1, 'Time')
        self.in_listbox.SetColumnWidth(1, utc_width)
        self.grid_sizer.Add(self.in_listbox, pos=(0, 1), flag=wx.EXPAND)

        self.in_browse_button = wx.Button(self.main_panel, label="Browse...")
        self.in_browse_button.Bind(wx.EVT_BUTTON, self.set_input)
        self.grid_sizer.Add(self.in_browse_button, pos=(1, 1), flag=wx.ALIGN_RIGHT)

        self.altaz_sizer = wx.BoxSizer(wx.HORIZONTAL)
        self.grid_sizer.Add(self.altaz_sizer, pos=(2, 0), span=(1, 2), flag=wx.EXPAND)

        self.field_derotation_checkbox = wx.CheckBox(self.main_panel, label="Alt-az field derotation")
        self.field_derotation_checkbox.Bind(wx.EVT_CHECKBOX, self.on_field_derotation_checkbox_toggle)
        self.altaz_sizer.Add(self.field_derotation_checkbox, flag=wx.ALIGN_CENTER_VERTICAL)
        self.altaz_sizer.AddSpacer(spacing)

        self.altaz_sizer.Add(wx.StaticLine(self.main_panel, style=wx.LI_VERTICAL), flag=wx.EXPAND)
        self.altaz_sizer.AddSpacer(spacing)

        self.latitude_label = wx.StaticText(self.main_panel, label="Latitude")
        self.altaz_sizer.Add(self.latitude_label, flag=wx.ALIGN_CENTER_VERTICAL)
        self.altaz_sizer.AddSpacer(spacing)

        self.latitude_spinctrl = wx.SpinCtrlDouble(self.main_panel, min=-90, max=90, initial=0)
        self.latitude_spinctrl.SetDigits(2)
        self.latitude_spinctrl.SetMinSize(wx.Size(longitude_width, self.latitude_spinctrl.GetMinHeight())) 
        self.altaz_sizer.Add(self.latitude_spinctrl, flag=wx.EXPAND)
        self.altaz_sizer.AddSpacer(spacing // 2)

        self.lat_deg_label = wx.StaticText(self.main_panel, label="°")
        self.altaz_sizer.Add(self.lat_deg_label, flag=wx.ALIGN_CENTER_VERTICAL)
        self.altaz_sizer.AddSpacer(spacing)

        self.altaz_sizer.Add(wx.StaticLine(self.main_panel, style=wx.LI_VERTICAL), flag=wx.EXPAND)
        self.altaz_sizer.AddSpacer(spacing)

        self.longitude_label = wx.StaticText(self.main_panel, label="Longitude")
        self.altaz_sizer.Add(self.longitude_label, flag=wx.ALIGN_CENTER_VERTICAL)
        self.altaz_sizer.AddSpacer(spacing)

        self.longitude_spinctrl = wx.SpinCtrlDouble(self.main_panel, min=-180, max=180, initial=0)
        self.longitude_spinctrl.SetDigits(2)
        self.longitude_spinctrl.SetMinSize(wx.Size(longitude_width, self.longitude_spinctrl.GetMinHeight())) 
        self.altaz_sizer.Add(self.longitude_spinctrl, flag=wx.EXPAND)
        self.altaz_sizer.AddSpacer(spacing // 2)

        self.lon_deg_label = wx.StaticText(self.main_panel, label="°")
        self.altaz_sizer.Add(self.lon_deg_label, flag=wx.ALIGN_CENTER_VERTICAL)
        self.altaz_sizer.AddSpacer(spacing)

        self.altaz_sizer.Add(wx.StaticLine(self.main_panel, style=wx.LI_VERTICAL), flag=wx.EXPAND)
        self.altaz_sizer.AddSpacer(spacing)

        self.target_label = wx.StaticText(self.main_panel, label="Target")
        self.altaz_sizer.Add(self.target_label, flag=wx.ALIGN_CENTER_VERTICAL)
        self.altaz_sizer.AddSpacer(spacing)

        self.target_combobox = wx.ComboBox(self.main_panel, choices=list(convert.TARGETS.keys()), style=wx.CB_READONLY)
        self.target_combobox.Bind(wx.EVT_COMBOBOX, self.on_target_combobox_selection)
        self.altaz_sizer.Add(self.target_combobox, proportion=1, flag=wx.EXPAND)

        self.out_sizer = wx.BoxSizer(wx.HORIZONTAL)
        self.grid_sizer.Add(self.out_sizer, pos=(3, 1), flag=wx.EXPAND)

        self.out_label = wx.StaticText(self.main_panel, label="Output")
        self.grid_sizer.Add(self.out_label, pos=(3, 0), flag=wx.ALIGN_CENTER_VERTICAL)

        self.out_dir_textctrl = wx.TextCtrl(self.main_panel)
        self.out_dir_textctrl.Bind(wx.EVT_TEXT, self.on_output_text_changed_event)
        self.out_sizer.Add(self.out_dir_textctrl, proportion=1, flag=wx.EXPAND | wx.ALL)
        self.out_sizer.AddSpacer(spacing)
        
        self.out_name_textctrl = wx.TextCtrl(self.main_panel)
        self.out_name_textctrl.Bind(wx.EVT_TEXT, self.on_output_text_changed_event)
        self.out_sizer.Add(self.out_name_textctrl)
        self.out_sizer.AddSpacer(spacing)

        self.out_browse_button = wx.Button(self.main_panel, label="Browse...")
        self.out_browse_button.Bind(wx.EVT_BUTTON, self.set_output)
        self.out_sizer.Add(self.out_browse_button)

        self.format_label = wx.StaticText(self.main_panel, label="Formats")
        self.grid_sizer.Add(self.format_label, pos=(4, 0), flag=wx.ALIGN_CENTER_VERTICAL)

        self.checkbox_sizer = wx.BoxSizer(wx.HORIZONTAL)
        self.grid_sizer.Add(self.checkbox_sizer, pos=(4, 1), flag=wx.EXPAND)

        self.apng_checkbox = wx.CheckBox(self.main_panel, label="APNG")
        self.apng_checkbox.Bind(wx.EVT_CHECKBOX, self.on_format_checkbox_event)
        self.checkbox_sizer.Add(self.apng_checkbox, flag=wx.ALIGN_CENTER_VERTICAL)
        self.checkbox_sizer.AddSpacer(spacing)

        self.avif_checkbox = wx.CheckBox(self.main_panel, label="AVIF")
        self.avif_checkbox.Bind(wx.EVT_CHECKBOX, self.on_format_checkbox_event)
        self.checkbox_sizer.Add(self.avif_checkbox, flag=wx.ALIGN_CENTER_VERTICAL)
        self.checkbox_sizer.AddSpacer(spacing)

        self.webp_checkbox = wx.CheckBox(self.main_panel, label="WebP")
        self.webp_checkbox.Bind(wx.EVT_CHECKBOX, self.on_format_checkbox_event)
        self.checkbox_sizer.Add(self.webp_checkbox, flag=wx.ALIGN_CENTER_VERTICAL)
        self.checkbox_sizer.AddSpacer(spacing)

        self.gif_checkbox = wx.CheckBox(self.main_panel, label="GIF")
        self.gif_checkbox.Bind(wx.EVT_CHECKBOX, self.on_format_checkbox_event)
        self.checkbox_sizer.Add(self.gif_checkbox, flag=wx.ALIGN_CENTER_VERTICAL)

        self.checkbox_sizer.Add(wx.StaticLine(self.main_panel, style=wx.LI_VERTICAL), flag=wx.EXPAND)
        self.checkbox_sizer.AddSpacer(spacing)

        self.frame_duration_label = wx.StaticText(self.main_panel, label="Frame length")
        self.checkbox_sizer.Add(self.frame_duration_label, flag=wx.ALIGN_CENTER_VERTICAL)
        self.checkbox_sizer.AddSpacer(spacing)

        self.frame_duration_spinctrl = wx.SpinCtrl(self.main_panel, min=1, max=100000, initial=100)
        self.checkbox_sizer.Add(self.frame_duration_spinctrl, proportion=1, flag=wx.EXPAND)
        self.checkbox_sizer.AddSpacer(spacing // 2)

        self.ms_label = wx.StaticText(self.main_panel, label="ms")
        self.checkbox_sizer.Add(self.ms_label, flag=wx.ALIGN_CENTER_VERTICAL)
        self.checkbox_sizer.AddSpacer(spacing)

        self.checkbox_sizer.Add(wx.StaticLine(self.main_panel, style=wx.LI_VERTICAL), flag=wx.EXPAND)
        self.checkbox_sizer.AddSpacer(spacing)

        self.quality_label = wx.StaticText(self.main_panel, label="Quality")
        self.checkbox_sizer.Add(self.quality_label, flag=wx.ALIGN_CENTER_VERTICAL)
        self.checkbox_sizer.AddSpacer(spacing)

        self.quality_spinctrl = wx.SpinCtrl(self.main_panel, min=settings.QUALITY_MIN, max=settings.QUALITY_MAX)
        self.quality_spinctrl.SetValue(self.settings.quality)
        self.checkbox_sizer.Add(self.quality_spinctrl, proportion=1, flag=wx.EXPAND)

        self.video_book = wx.Simplebook(self.main_panel)
        self.grid_sizer.Add(self.video_book, pos=(5, 1), span=(1, 2))

        self.video_info_panel = wx.Panel(self.video_book)
        self.video_info_sizer = wx.BoxSizer(wx.HORIZONTAL)
        self.video_info_panel.SetSizerAndFit(self.video_info_sizer)
        self.video_book.AddPage(self.video_info_panel, "")

        self.video_support_label = wx.StaticText(self.video_info_panel, label="Conversion to MP4 video requires FFmpeg. ")
        self.video_info_sizer.Add(self.video_support_label)

        self.select_ffmpeg_label = wx.adv.HyperlinkCtrl(self.video_info_panel, label="Select FFmpeg executable...")
        self.select_ffmpeg_label.Bind(wx.adv.EVT_HYPERLINK, self.set_ffmpeg_path)
        self.video_info_sizer.Add(self.select_ffmpeg_label)

        self.video_panel = wx.Panel(self.video_book)
        self.video_book.AddPage(self.video_panel, "")

        self.video_sizer = wx.BoxSizer(wx.HORIZONTAL)
        self.video_panel.SetSizerAndFit(self.video_sizer)

        self.mp4_checkbox = wx.CheckBox(self.video_panel, label="MP4")
        self.mp4_checkbox.SetValue(self.settings.do_mp4)
        self.mp4_checkbox.Bind(wx.EVT_CHECKBOX, self.on_format_checkbox_event)
        self.video_sizer.Add(self.mp4_checkbox, flag=wx.ALIGN_CENTER_VERTICAL)
        self.video_sizer.AddSpacer(spacing)

        self.mp4avc_radio = wx.RadioButton(self.video_panel, label="AVC")
        self.mp4avc_radio.SetValue(self.settings.mp4_codec == convert.Codec.AVC)
        self.video_sizer.Add(self.mp4avc_radio, flag=wx.ALIGN_CENTER_VERTICAL)
        self.video_sizer.AddSpacer(spacing)

        self.mp4av1_radio = wx.RadioButton(self.video_panel, label="AV1")
        self.mp4av1_radio.SetValue(self.settings.mp4_codec == convert.Codec.AV1)
        self.video_sizer.Add(self.mp4av1_radio, flag=wx.ALIGN_CENTER_VERTICAL)
        self.video_sizer.AddSpacer(spacing)

        self.bottom_sizer = wx.BoxSizer(wx.HORIZONTAL)
        self.grid_sizer.Add(self.bottom_sizer, pos=(6, 0), span=(1, 2), flag=wx.EXPAND)

        self.about_button = wx.Button(self.main_panel, label="About")
        self.about_button.Bind(wx.EVT_BUTTON, self.on_about)
        self.bottom_sizer.Add(self.about_button)
        self.bottom_sizer.AddStretchSpacer(1)

        self.show_folder_checkbox = wx.CheckBox(self.main_panel, label="Show folder when done")
        self.show_folder_checkbox.SetValue(True)
        self.bottom_sizer.Add(self.show_folder_checkbox, flag=wx.ALIGN_CENTER_VERTICAL)
        self.bottom_sizer.AddSpacer(spacing)

        self.convert_book = wx.Simplebook(self.main_panel)
        self.bottom_sizer.Add(self.convert_book)

        self.convert_button = wx.Button(self.convert_book, label="Convert")
        self.convert_button.Bind(wx.EVT_BUTTON, self.on_convert_start)
        self.convert_book.AddPage(self.convert_button, "")

        self.activity_indicator = wx.ActivityIndicator(self.convert_book)
        self.convert_book.AddPage(self.activity_indicator, "")

        self.grid_sizer.AddGrowableRow(0, 1)
        self.grid_sizer.AddGrowableCol(1, 1)

        self.about_panel = wx.Panel(self.book, wx.ID_ANY)
        self.about_sizer = wx.GridBagSizer(hgap=spacing, vgap=spacing)
        self.about_panel.SetSizerAndFit(self.about_sizer)
        self.book.AddPage(self.about_panel, "")

        self.ffmpeg_label = wx.StaticText(self.about_panel, label="FFmpeg path")
        self.about_sizer.Add(self.ffmpeg_label, pos=(0, 0), flag=wx.ALIGN_CENTER_VERTICAL)

        self.ffmpeg_dir_textctrl = wx.TextCtrl(self.about_panel)
        self.ffmpeg_dir_textctrl.SetValue(str(self.settings.ffmpeg_path))
        self.ffmpeg_dir_textctrl.Bind(wx.EVT_KILL_FOCUS, self.on_ffmpeg_focus_lost_event)
        self.about_sizer.Add(self.ffmpeg_dir_textctrl, pos=(0, 1), flag=wx.EXPAND | wx.ALL)

        self.ffmpeg_browse_button = wx.Button(self.about_panel, label="Browse...")
        self.ffmpeg_browse_button.Bind(wx.EVT_BUTTON, self.set_ffmpeg_path)
        self.about_sizer.Add(self.ffmpeg_browse_button, pos=(0, 2))

        self.license_textctrl = wx.TextCtrl(self.about_panel, style=wx.TE_MULTILINE | wx.TE_READONLY | wx.VSCROLL | wx.BORDER_NONE)
        with open(Path("./dep-terms.txt"), "r", encoding='utf-16-le') as f:
            self.license_textctrl.ChangeValue(f.read())
        self.about_sizer.Add(self.license_textctrl, pos=(1, 0), span=(1, 3), flag=wx.EXPAND)

        self.back_button = wx.Button(self.about_panel, label="Back")
        self.back_button.Bind(wx.EVT_BUTTON, self.on_back)
        self.about_sizer.Add(self.back_button, pos=(2, 0))

        self.about_sizer.AddGrowableRow(1, 1)
        self.about_sizer.AddGrowableCol(1, 1)

        self.panel.SetSizerAndFit(self.wrapper_sizer)

        self.set_field_derotation_state()
        self.update_ffmpeg_widgets()
        self.set_convert_button_state()

        self.Show()
        self.in_listbox.PostSizeEventToParent()

    def set_input(self, event):
        wildcards = "Images|" + self.wildcards
        dialog = wx.FileDialog(self, "Select animation frames...",
            wildcard=wildcards,
            style=wx.FD_OPEN | wx.FD_MULTIPLE | wx.FD_FILE_MUST_EXIST,
        )

        if dialog.ShowModal() == wx.ID_OK:
            self.paths = [convert.Frame(p) for p in dialog.GetPaths()]
            self.in_listbox.DeleteAllItems()
            enable_field_rotation_option = True
            target = None
            for i, p in enumerate(self.paths):
                self.in_listbox.InsertItem(i, p.path.name)
                if not target:
                    target = p.target
                if p.date_time:
                    self.in_listbox.SetItem(i, 1, p.date_time.strftime("%Y-%m-%d %H:%M:%S %Z"))
                else:
                    enable_field_rotation_option = False
                    self.field_derotation_checkbox.SetValue(False)
            self.field_derotation_checkbox.Enable(enable_field_rotation_option)
            self.set_field_derotation_state()
            if target:
                self.target_combobox.SetValue(target)
            self.out_dir_textctrl.SetValue(str(self.paths[0].path.parent))
        dialog.Destroy()
        self.set_convert_button_state()
    
    def set_output(self, event):
        dialog = wx.DirDialog(None, "Select output directory...", style=wx.DD_DEFAULT_STYLE | wx.DD_DIR_MUST_EXIST)
        if dialog.ShowModal() == wx.ID_OK:
            chosen_dir = dialog.GetPath()
            self.out_dir_textctrl.SetValue(chosen_dir)
        dialog.Destroy()
        self.set_convert_button_state()
    
    def set_ffmpeg_path(self, event):
        wildcards = "Executable files|*.exe" if SYSTEM == 'Windows' else "Executable files|*"
        dialog = wx.FileDialog(None, "Select FFmpeg executable...", style=wx.FD_OPEN | wx.FD_FILE_MUST_EXIST, wildcard=wildcards)
        if dialog.ShowModal() == wx.ID_OK:
            chosen_path = dialog.GetPath()
            self.ffmpeg_dir_textctrl.SetValue(chosen_path)
            self.update_ffmpeg_widgets()
        dialog.Destroy()

    def on_format_checkbox_event(self, event):
        self.set_convert_button_state()
    
    def on_output_text_changed_event(self, event):
        self.set_convert_button_state()
    
    def on_ffmpeg_focus_lost_event(self, event):
        self.update_ffmpeg_widgets()
    
    def update_ffmpeg_widgets(self):
        is_valid_ffmpeg = convert.validate_ffmpeg(self.settings.ffmpeg_path)
        self.can_avc = is_valid_ffmpeg["avc"]
        self.can_av1 = is_valid_ffmpeg["av1"]
        if self.can_avc or self.can_av1:
            self.video_book.ChangeSelection(1)
        else:
            self.video_book.ChangeSelection(0)
        
        if self.can_avc and not self.can_av1:
            self.mp4avc_radio.SetValue(True)
        elif self.can_av1 and not self.can_avc:
            self.mp4av1_radio.SetValue(True)
    
    def set_convert_button_state(self):
        out_dir = Path(self.out_dir_textctrl.GetValue())

        do_apng = self.apng_checkbox.GetValue()
        do_avif = self.avif_checkbox.GetValue()
        do_webp = self.webp_checkbox.GetValue()
        do_gif = self.gif_checkbox.GetValue()
        do_mp4 = self.mp4_checkbox.GetValue()
        has_input = self.in_listbox.GetItemCount() > 0
        has_output_dir = out_dir.exists() and out_dir.is_absolute()
        has_output_name = len(self.out_name_textctrl.GetValue()) > 0
        do_derotate = self.field_derotation_checkbox.GetValue()
        derotate_and_target = (not do_derotate) or (do_derotate and not self.target_combobox.GetValue() not in convert.TARGETS.keys())

        self.convert_button.Enable((do_apng or do_avif or do_webp or do_gif or do_mp4) and has_input and has_output_dir and has_output_name and derotate_and_target)
        self.mp4avc_radio.Enable(do_mp4 and self.can_avc)
        self.mp4av1_radio.Enable(do_mp4 and self.can_av1)

    def on_convert_start(self, event):
        self.SetCursor(wx.Cursor(wx.CURSOR_WAIT))
        self.panel.Enable(False)
        self.activity_indicator.Start()
        self.convert_book.ChangeSelection(1)
        t = threading.Thread(target=self.convert)
        t.start()
    
    def on_field_derotation_checkbox_toggle(self, event):
        self.set_field_derotation_state()
        self.set_convert_button_state()
    
    def on_target_combobox_selection(self, event):
        self.set_convert_button_state()
    
    def on_about(self, event):
        self.book.ChangeSelection(1)
    
    def on_back(self, event):
        self.book.ChangeSelection(0)
    
    def set_field_derotation_state(self):
        is_checked = True

        for f in self.paths:
            if f.date_time:
                break
        else:
            is_checked = False
        
        is_checked = is_checked and self.field_derotation_checkbox.GetValue()

        self.latitude_label.Enable(is_checked)
        self.latitude_spinctrl.Enable(is_checked)
        self.lat_deg_label.Enable(is_checked)

        self.longitude_label.Enable(is_checked)
        self.longitude_spinctrl.Enable(is_checked)
        self.lon_deg_label.Enable(is_checked)

        self.target_label.Enable(is_checked)
        self.target_combobox.Enable(is_checked)
    
    def on_convert_end(self):
        out_dir = Path(self.out_dir_textctrl.GetValue())

        if not self.show_folder_checkbox.GetValue():
            pass
        elif SYSTEM == "Darwin":  # macOS
            subprocess.run(["open", out_dir])
        elif SYSTEM == "Windows":  # Windows
            subprocess.run(["explorer", out_dir])
        else:
            subprocess.run(["xdg-open", out_dir])
    
        self.activity_indicator.Stop()
        self.convert_book.ChangeSelection(0)
        self.Layout()
        self.panel.Enable(True)
        self.SetCursor(wx.NullCursor)

    def convert(self):
        try:
            convert.save(
                self.paths,
                Path(self.out_dir_textctrl.GetValue(), self.out_name_textctrl.GetValue()),
                self.frame_duration_spinctrl.GetValue(),
                self.gif_checkbox.GetValue(),
                self.webp_checkbox.GetValue(),
                self.apng_checkbox.GetValue(),
                self.avif_checkbox.GetValue(),
                self.mp4_checkbox.GetValue(),
                convert.Codec.AV1 if self.mp4av1_radio.GetValue() else convert.Codec.AVC,
                self.quality_spinctrl.GetValue(),
                self.field_derotation_checkbox.GetValue(),
                self.latitude_spinctrl.GetValue(),
                self.longitude_spinctrl.GetValue(),
                self.target_combobox.GetValue(),
            )
        finally:
            wx.CallAfter(self.on_convert_end)
    
