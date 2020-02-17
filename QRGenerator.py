# Make a list/array of items, images to convert to QR codes 
# mailto:jevans@oculyze.de?subject=Re-Order%20Bellows&body=Re-Order%20Bellows%0A%0AAdd%20any%20extra%20information%20here......

import qrcode 
from PIL import Image
import sys

#add email address needed to link via QR code
emailAddress = 'jevans@oculyze.de'

qr = qrcode.QRCode(
	error_correction=qrcode.constants.ERROR_CORRECT_L,
	box_size=10,
	border=4,)


#make list of items here
listOfItems = ['Bellows',
			'Measuring Cylinder',
			'Stages',
			'Slide Fixes - LED',
			'Slide Fixes - LASER',
			'Cable Hiders',
			'Holder -LED',
			'Holder - Stage',
			'Holder - Camera',
			'Bolts - Rear Housing - M4x10',
			'Bolts - Camera - M2x8',
			'Nuts - Camera- M2',
			'Glue - UHU Alleskleber',
			'Glue - Pattex Sekundenkleber Gel',
			'Bolts - Button Board - M2.5x4',
			'Bolts - Motherboard - M2x4',
			'Packaging Boxes',
			'Sticky feet - 12mm Diameter',
			'Cables - USB A to USB C',
			'Cables - USB C to USB C',
			'Cables - microUSB - Female USB A',
			'Cables - USB A to USB B',
			'Cables - USB C to USB B',
			'Cleaning Swabs',
			'1ml Pipettes',
			'2ml Reaction Tubes',
			'Plastic Syringes',
			'Sample Chambers',
			'Haribo',
			'Stickers - BB Serial Label',
			'Stickers - FW Serial Label',
			'Stickers - AHSE Serial Label',
			'Stickers - Made in Germany',
			'Stickers - OCULYZE',
			'Bags - Slides',
			'Bags - Cleaning Swabs',
			'Bags - Reaction Tubes',
			'Coasters',
			'Quick Guide - FW',
			'Quick Guide - BB',
			'Quick Guide - EC',
			'Packing List - BB',
			'Packing List - FW',
			'Packing List - MC',
			'Stickers - BB Boxes',
			'Stickers - FW Boxes',
			'Stickers - AHSE Boxes',
			'AMV'
			]

sortedList = sorted(listOfItems)

#iterate through list of items and create links
listOfLinks = []

for item in listOfItems:
	link = 'mailto:' + emailAddress + '?subject=Re-Order%20-%20' + item + '&body=Re-Order%20-%20' + item + '%0A%0AAdd%20any%20extra%20information%20here......'
	newLink = link
	listOfLinks.append(newLink)



#insert URLS to make codes and save as listOfitem #
for links in listOfLinks:
		img = qrcode.make(links)
		#Delete all mush from "links" to get usable filename for code
		linkName = links.replace("mailto:jevans@oculyze.de?subject=Re-Order%20-%20", "")
		#Trim tail from "&" symbol
		head,sep,tail = linkName.partition('&')
		trimLink = head
		# Save as filename
		img.save(head+" QR Code")


## and images, PIL side by side maybe?


		





