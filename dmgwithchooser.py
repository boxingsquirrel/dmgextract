#!/usr/bin/env python

# Extract a DMG (ie an iPhone filesystem image) from Nautilus to a user defined directory
#
# Copyright 2010 boxingsquirrel. Private.
#
# See the README for additional information.

# Imports...
import nautilus
import pygtk
import gtk
import pynotify
import time
import urllib2
import urllib
import commands
import os

class dmgextwithchooser(nautilus.MenuProvider):

	def __init__(self):
		# Nautilus apparently crashes w/o this...
		pass

	def extract(self, menu, file):
		dialog=gtk.FileChooserDialog(title="Output directory...", parent=None, action=gtk.FILE_CHOOSER_ACTION_SELECT_FOLDER, buttons=(gtk.STOCK_CANCEL, gtk.RESPONSE_CANCEL, gtk.STOCK_OPEN, gtk.RESPONSE_OK), backend=None)
		if dialog.run()==gtk.RESPONSE_OK:
			folder=dialog.get_uri()
			dialog.destroy()
			gtk.main_iteration(block=True)
			commands.getstatusoutput("dmg extract "+urllib.unquote(file.get_uri()[7:])+" "+urllib.unquote(file.get_uri()[7:])+".sc");
			os.chdir(urllib.unquote(folder[7:]))
			commands.getstatusoutput("hfsplus "+urllib.unquote(file.get_uri()[7:])+".sc extractall")
			os.remove(urllib.unquote(file.get_uri()[7:])+".sc")
			pynotify.init("dmgextract")
			note=pynotify.Notification("Extraction Complete!", file.get_name()+" has been extracted to "+urllib.unquote(folder[7:])+".", "/usr/share/dmgextract/icon.png")
			note.show()
			time.sleep(3)
			note.close()
			return

	def get_file_items(self, window, files):
		if len(files) != 1:
			return

		filename = urllib.unquote(files[0].get_uri()[7:])

		if os.path.isdir(filename):
			return

		file = files[0]

		if file.get_name().endswith(".dmg"):
			item = nautilus.MenuItem("dmgextwithchooser::Extract","Extract","Extract the contents of %s to a directory you select" % file.get_name())
			item.set_property("icon", "/usr/share/dmgextract/icon2.png")
			item.connect('activate', self.extract, file)

			return [item]

		return
