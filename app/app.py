"""
Author = Joshua Akangah
"""

from tkinter import *
from tkinter import filedialog
import guizero
from PIL import ImageTk, Image
import os

input_box = None
app = guizero.App(title="Metas-Strip")

def open_image(filename):
	global input_box
	a = '/home/pygod/Desktop/favicon.png'
	img = Image.open(a)
	message = guizero.Text(app, text="")
	thumbnail = guizero.Picture(app, image=img, width=100, height=100)
	message = guizero.Text(app, text="")
	listbox = guizero.ListBox(app, items=["Beef", "Chicken", "Fish", "Vegetarian"], width="70")



def about():
	pass



menubar = guizero.MenuBar(app,
	toplevel = ['About'],
	options = [[['About Metas-Strip', about]]]
)

message = guizero.Text(app, text="")
message = guizero.Text(app, text="Metas-Strip")
message = guizero.Text(app, text="")
input_box = guizero.TextBox(app, width="70")
message = guizero.Text(app, text="")
button = guizero.PushButton(app, command=open_image, args=[input_box.value])

app.display()
