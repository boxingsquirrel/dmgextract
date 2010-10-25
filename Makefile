all:
	@echo "make <install-new/install-old>"
	@echo ""
	@echo "Note: install-old is for Debian Lenny or older."

install-old:
	rm -rf /usr/share/dmgextract
	mkdir /usr/share/dmgextract
	cp *.png /usr/share/dmgextract
	cp dmg.py /usr/lib/nautilus/extensions-1.0/python
	cp dmgwithchooser.py /usr/lib/nautilus/extensions-1.0/python
	nautilus -q

uninstall-old:
	rm -rf /usr/share/dmgextract
	rm /usr/lib/nautilus/extensions-1.0/python/dmg.py
	rm /usr/lib/nautilus/extensions-1.0/python/dmgwithchooser.py
	nautilus -q

install-new:
	rm -rf /usr/share/dmgextract
	mkdir /usr/share/dmgextract
	cp *.png /usr/share/dmgextract
	cp dmg.py /usr/lib/nautilus/extensions-2.0/python
	cp dmgwithchooser.py /usr/lib/nautilus/extensions-2.0/python
	nautilus -q

uninstall-old:
	rm -rf /usr/share/dmgextract
	rm /usr/lib/nautilus/extensions-1.0/python/dmg.py
	rm /usr/lib/nautilus/extensions-1.0/python/dmgwithchooser.py
	nautilus -q
