#!/usr/bin/env python

# Extract a DMG (ie an iPhone filesystem image) from Nautilus
#
# Copyright 2010 boxingsquirrel. Private.
#
# See the README for additional information.

# Imports...
import nautilus
import pygtk
import gtk
import gtk.glade
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

	def getLogin(self):
		# Load the login window
	        self.wTree = gtk.glade.XML("/usr/share/Cloudy/login.glade") 
		self.window = self.wTree.get_widget("dialog1")
		unamef = self.wTree.get_widget("entry1")
		passwdf = self.wTree.get_widget("entry2")

		# We need to toggle the visibility of the password field
		passwdf.set_visibility(False);

		# Run the dialog!
		self.window.run()

		# Make the password visible to fight a bug
		passwdf.set_visibility(True);

		# Trash the window...
		self.window.destroy()

		# Return the username/password
		l=(unamef.get_text(),passwdf.get_text())
		return l

	def extract(self, menu, file):
		commands.getstatusoutput("dmg extract "+urllib.unquote(file.get_uri()[7:])+" "+urllib.unquote(file.get_uri()[7:])+".sc");
		os.chdir(os.path.abspath(os.path.join(urllib.unquote(file.get_uri()[7:]), "..")))
		commands.getstatusoutput("hfsplus "+urllib.unquote(file.get_uri()[7:])+".sc extractall")
		os.remove(urllib.unquote(file.get_uri()[7:])+".sc")

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
