import skia
import contextlib
import numpy as np
import shutil
import argparse
import io

def pixelToEscape(b,g,r,a):
	'''
	Convert color to escape sequences
	https://docs.microsoft.com/en-us/windows/console/console-virtual-terminal-sequences#extended-colors
	'''
	return "\x1b[38;2;{};{};{}m\x1b[48;2;{};{};{}m9".format(r,g,b,r,g,b)

def print_image(data = b'',scale=1.0,fit_to='h'):
	if not data:
		parser = argparse.ArgumentParser(description='''
		CLI tool to show images in terminal using Skia to load the images.Uses skia-python to read images and resize to fit 
		the terminal window.
		''')
		parser.add_argument('file',type=argparse.FileType("rb"),default='-',help='Path to image file to display')
		parser.add_argument('--scale',type=float,default=1.0,
		help='Amount of scale to be applied,image is still reduced to terminal width')
		parser.add_argument('--fit_to',default='h',choices=['w','h'],
		help='Fit to width (w) or height (h) of the terminal window (does not upscale)')

		args = parser.parse_args()

		if isinstance(args.file,io.BufferedReader):
			data = args.file.read()
		else:
			data = args.file.buffer.read()
		args.file.close()
		fit_to = args.fit_to
		scale = args.scale

	skImage = skia.Image.DecodeToRaster(data)

	w = skImage.width()
	h = skImage.height()
	tw = shutil.get_terminal_size().columns
	th = shutil.get_terminal_size().lines

	newWidth = int(w * scale)
	newHeight = int(h * scale)

	if fit_to == 'w':
		aspectRatio = h/w

		if w > tw:
			newWidth = int(tw * scale)
			newHeight = int(newWidth * aspectRatio)
	else:
		aspectRatio = w/h

		if h > th:
			newHeight = int(th * scale)
			newWidth = int(newHeight * aspectRatio)



	array = np.zeros((newWidth, newHeight, 4), dtype=np.uint8)
	newImage = skImage.resize(newWidth, newHeight)
	array = newImage.toarray()
	pixelArray = []

	for ix,iy in np.ndindex(newHeight, newWidth):
		if iy == newWidth - 1:
			pixelArray.append('\x1b[m\r\n')
		else:
			pixelArray.append(pixelToEscape(*array[ix][iy]))

	print(''.join(pixelArray))

if __name__ == '__main__':
	print_image()
