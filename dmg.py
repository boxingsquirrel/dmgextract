#!/usr/bin/env python

# Extract a DMG (ie an iPhone filesystem image) from Nautilus
#
# Copyright 2010 boxingsquirrel. Private.
#
# See the README for additional information.

# Imports...
import nautilus
import pynotify
import time
import urllib2
import urllib
import commands
import os

class dmgext(nautilus.MenuProvider):

	def __init__(self):
		# Nautilus apparently crashes w/o this...
		pass

	def extract(self, menu, file):
		commands.getstatusoutput("dmg extract "+urllib.unquote(file.get_uri()[7:])+" "+urllib.unquote(file.get_uri()[7:])+".sc");
		os.chdir(os.path.abspath(os.path.join(urllib.unquote(file.get_uri()[7:]), "..")))
		commands.getstatusoutput("hfsplus "+urllib.unquote(file.get_uri()[7:])+".sc extractall")
		os.remove(urllib.unquote(file.get_uri()[7:])+".sc")
		pynotify.init("dmgextract")
		note=pynotify.Notification("Extraction Complete!", file.get_name()+" has been extracted to the current directory.", "/usr/share/dmgextract/icon.png")
		note.show()
		time.sleep(3)
		note.close()

	def get_file_items(self, window, files):
		if len(files) != 1:
			return

		filename = urllib.unquote(files[0].get_uri()[7:])

		if os.path.isdir(filename):
			return

		file = files[0]

		if file.get_name().endswith(".dmg"):
			item = nautilus.MenuItem("dmgext::Extract","Extract All Here","Extract the contents of %s to this diectory" % file.get_name())
			item.set_property("icon", "/usr/share/dmgextract/icon.png")
			item.connect('activate', self.extract, file)

			return [item]

		return
