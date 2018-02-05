#!/usr/bin/env python3

from pydub import AudioSegment
from sys import exit
import optparse
import os

def ConvertFile(infile, ext, outfile=None):
	
	if not os.path.isfile(infile):
		print('\n{} is an invalid path\n'.format(infile))
		exit(1)
	try:	
		audio = AudioSegment.from_file(infile)
		if outfile:
			outfile = outfile[:-3] + ext
			audio.export(outfile, format=ext)
		else:
			outfile = infile[:-3] + ext
			audio.export(outfile, format=ext)
		print('\n[*] Done!\tCreated File: {}\n'.format(outfile))
	except:
		print('\nAn Error Has Occured.')
		print('Check If Audio File is Not Corrupted and Extension is Valid\n')
		exit(1)

def main():
	parser = optparse.OptionParser(usage='usage %prog -f <Input File> -o <Output File=Input File> -e <Extension>')
	parser.add_option('-f', dest='input', type='string')
	parser.add_option('-o', dest='output', type='string')
	parser.add_option('-e', dest='ext', type='string')

	(options, args) = parser.parse_args()

	infile = options.input
	outfile = options.output
	ext = options.ext

	if None in [infile, ext]:
		print('\n{}\n'.format(parser.usage))
		exit(1)
	if outfile:
		ConvertFile(infile, ext=ext, outfile=outfile)
	else:
		ConvertFile(infile, ext=ext, outfile=infile)
if __name__ == '__main__':
	main()

