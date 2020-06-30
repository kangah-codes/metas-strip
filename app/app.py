"""
Author = Joshua Akangah
"""

# importing modules
from tkinter import *
from tkinter import filedialog
import guizero
from PIL import ImageTk, Image
import os
from pyexiv2 import Image as Meta

# setting global varialbes
input_box = None
thumbnail = None
listbox = None
return_box = None

# creating app window and box widget
app = guizero.App(title="Metas-Strip")
buttons_box = guizero.Box(app, width="fill", align="bottom")

# about function
def about():
	pass

# function to clear screen
def clear_all():
	global return_box

	# destroy return box and all items in it
	return_box.destroy()

# fuction to clear metadata if item
def clear_meta(item):
	# ask for user choice before deleting metdata
	choice = guizero.yesno("Confirm", "Delete metadata?")
	if choice:
		guizero.info("Delete", "Deleting metadata")
		item.clear_exif()
		item.close()
		clear_all()
	else:
		app.error("Close", "Not deleted")

# function to open image from path
def open_image():
	global input_box
	global return_box
	metadata = None
	return_box = guizero.Box(app, width="fill")
	try:
		# using PIl to open image
		img = Image.open(input_box.value)
		# opening pyexiv2 instance from image
		meta = Meta(input_box.value)
		# opening the instance like this so that we don't close it after reading metadata so object is still in memory, although this can cause a memory leak

		# with Meta(input_box.value) as meta: -> using this method will delete the object and we will no longer have access to it in the clear meta function
		metadata = meta.read_exif()
		message = guizero.Text(return_box, text="")
		thumbnail = guizero.Picture(return_box, image=img, width=100, height=100)
		message = guizero.Text(return_box, text="")
		if not metadata:
			# picture has no metadata
			listbox = guizero.ListBox(return_box, items=["No metadata was extracted"], width="fill", height=50)
		else:
			listbox = guizero.ListBox(return_box, items=[], width="fill")
			cancel = guizero.PushButton(buttons_box, text="Strip Metadata", align="right", command=clear_meta, args=[meta])
			for _ in metadata.items():
				# add each item in metadata to listbox
				listbox.append(f"{_[0]}:     {_[1]}")
	except FileNotFoundError:
		message = guizero.Text(return_box, text="")
		thumbnail = guizero.Picture(return_box, image=f'error.jpeg', width=200, height=200)
		message = guizero.Text(return_box, text="")
		message = guizero.Text(return_box, text="Image not found")




menubar = guizero.MenuBar(app,
	toplevel = ['About'],
	options = [[['About Metas-Strip', about]]]
)

message = guizero.Text(app, text="")
message = guizero.Text(app, text="Metas-Strip")
message = guizero.Text(app, text="Enter image path")
message = guizero.Text(app, text="")
input_box = guizero.TextBox(app, width="70")
message = guizero.Text(app, text="")
button = guizero.PushButton(app, command=open_image, text="Open Image")
cancel = guizero.PushButton(buttons_box, text="Clear", align="right", command=clear_all)

app.display()
