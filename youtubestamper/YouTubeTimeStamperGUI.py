import tkinter as tk
from YouTubeHandler import YouTubeHandler
from TimeStamper import TimeStamper
from pyperclip import copy


class YouTubeTimeStamper(tk.Frame):
    def __init__(self, parent):
        tk.Frame.__init__(self, parent)
        self.parent = parent

        # Youtube Handler Widgets and Variables
        self.yth = None
        self.yth_frame = tk.Frame(self.parent, relief=tk.RIDGE, borderwidth=3)
        self.title_lbl = tk.Label(self.yth_frame, text='Link Handler')
        self.link_lbl = tk.Label(self.yth_frame, text='Video Link:')
        self.link_entry = tk.Entry(self.yth_frame, width=38)
        self.get_vid_btn = tk.Button(self.yth_frame, text='Get Short Link', command=self.get_short_link)
        self.sl_lbl = tk.Label(self.yth_frame, text='Short Link:')
        self.sl_entry = tk.Entry(self.yth_frame, width=38)

        self.yth_frame.grid(row=0, column=0)
        self.title_lbl.grid(row=0, column=0, columnspan=3)
        self.link_lbl.grid(row=1, column=0)
        self.link_entry.grid(row=1, column=1)
        self.get_vid_btn.grid(row=1, column=2, pady=5)
        self.sl_lbl.grid(row=2, column=0)
        self.sl_entry.grid(row=2, column=1)

        # Time Stamper Widgets and Variables
        self.stamp_links_str = ''
        self.ts = TimeStamper()
        self.video_stamp_frame = tk.Frame(self.parent, relief=tk.RIDGE, borderwidth=3)
        self.title_lbl = tk.Label(self.video_stamp_frame, text='Link Stamper')
        self.pad_lbl = tk.Label(self.video_stamp_frame, text='Start Pad:')
        self.pad_ent = tk.Entry(self.video_stamp_frame, width=5)
        self.mult_lbl = tk.Label(self.video_stamp_frame, text='Multiplier:')
        self.mult_ent = tk.Entry(self.video_stamp_frame, width=5)
        self.delay_lbl = tk.Label(self.video_stamp_frame, text='Delay:')
        self.delay_ent = tk.Entry(self.video_stamp_frame, width=5)
        self.start_btn = tk.Button(self.video_stamp_frame, text='Start Timer', command=self.set_start)
        self.stamp_btn = tk.Button(self.video_stamp_frame, text='Stamp', command=self.stamp)
        self.output_lbl = tk.Label(self.video_stamp_frame, text='Output')
        self.output_txt = tk.Text(self.video_stamp_frame, width=35, height=12, state=tk.DISABLED)
        self.copy_button = tk.Button(self.video_stamp_frame, text='Copy Links', command=self.copy_links)

        self.pad_ent.insert(0, 0)
        self.mult_ent.insert(0, 1.0)
        self.delay_ent.insert(0, 0)

        self.video_stamp_frame.grid(row=1, column=0)
        self.title_lbl.grid(row=0, column=0, columnspan=2, pady=5)
        self.pad_lbl.grid(row=1, column=0, sticky=tk.E, padx=5)
        self.pad_ent.grid(row=1, column=1, sticky=tk.W, padx=5)
        self.mult_lbl.grid(row=2, column=0, sticky=tk.E, padx=5)
        self.mult_ent.grid(row=2, column=1, sticky=tk.W, padx=5)
        self.delay_lbl.grid(row=3, column=0, sticky=tk.E, padx=5)
        self.delay_ent.grid(row=3, column=1, sticky=tk.W, padx=5)
        self.start_btn.grid(row=4, column=1, padx=5)
        self.stamp_btn.grid(row=5, column=1, sticky=tk.E, padx=5)
        self.output_lbl.grid(row=0, column=2, padx=5)
        self.output_txt.grid(row=1, column=2, rowspan=5, padx=5, pady=5)
        self.copy_button.grid(row=6, column=2)

    def get_short_link(self):
        self.sl_entry.delete(0, tk.END)
        self.yth = YouTubeHandler(self.link_entry.get())
        self.sl_entry.insert(0, str(self.yth))

    def set_start(self):
        self.stamp_links_str = ''
        self.ts = TimeStamper(int(self.pad_ent.get()), float(self.mult_ent.get()), int(self.delay_ent.get()))
        self.output_txt.config(state=tk.NORMAL)
        self.output_txt.delete(1.0, tk.END)
        self.output_txt.insert(tk.END, 'START\n')
        self.output_txt.config(state=tk.DISABLED)
        self.ts.set_start()

    def stamp(self):
        stamp = self.ts.stamp()
        stamp = int(stamp)
        yt_stamp = '{}{}{}\n'.format(self.yth.link, self.yth.TIME_SUFFIX, stamp)
        self.stamp_links_str += yt_stamp
        self.output_txt.config(state=tk.NORMAL)
        self.output_txt.insert(tk.END, yt_stamp)
        self.output_txt.see(tk.END)
        self.output_txt.config(state=tk.DISABLED)

    def copy_links(self):
        copy(self.stamp_links_str)
