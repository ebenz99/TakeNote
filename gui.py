import tkinter as tk
from recordbutton import *
from sicutter import *
from wavtoflac import convert
from quotachecker import check
from organizer import *
from parser import writer

root = tk.Tk()

global_recording_obj = None


def update_btn():
	if btn_text.get() == "Record":
		btn_text.set("Stop Recording")
		robj = my_start_recording()
		global global_recording_obj
		global_recording_obj = robj
	else:
		my_stop_recording(global_recording_obj)
		cut()
		convert()
		check()
		transcribe()
		writer()
		btn_text.set("Record")



btn_text = tk.StringVar()
btn = tk.Button(root, textvariable=btn_text, command=update_btn)
btn.config( height = 100, width = 100 )
btn_text.set("Record")

btn.pack()

root.mainloop()