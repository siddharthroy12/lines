#!/usr/bin/env python3

from os import listdir
from os.path import isfile, join
import argparse

# Options
path_to_search = './'
ignore_empty_lines = True
verbose = False
filesnames_to_ingore = []

def parse_cmd_args():
	global path_to_search
	global ignore_empty_lines
	global filesnames_to_ingore
	global verbose

	parser = argparse.ArgumentParser(
		prog='lines',
		usage='%(prog)s [options]',
		description='Count the lines of code in a project folder'
	)

	parser.add_argument('-p',
    	metavar='path',
    	type=str,
		default='./',
    	help='the path to the project folder')

	parser.add_argument('-e',
		action='store_true',
    	help='Count empty lines',
		required=False
	)

	parser.add_argument('-i',
		metavar='Files',
		nargs='*',
		action='store',
    	help='Files to ignore',
		default='',
		required=False
	)

	parser.add_argument('-v',
    	'--verbose',
    	action='store_true',
    	help='Show files that are counted')

	args = parser.parse_args()

	path_to_search = args.p

	if args.e:
		ignore_empty_lines = False

	if args.verbose:
		verbose = True
        

	for filesname in args.i:
		filesnames_to_ingore.append(filesname)

def count_lines_in_file(file: str) -> int:
	lines = 0

	try:
		with open(file) as f:
			for line in f:
				# Skip the empty lines
				if line.strip() == '' and ignore_empty_lines:
					continue
				lines += 1
	except UnicodeDecodeError: # If file is not text file
		return 0
	
	if verbose:
		print(file, f" [{lines}]")

	return lines

def count_lines_in_dir(dir: str) -> int:
	files = []

	for file_or_folder in listdir(dir):
		if isfile(join(dir, file_or_folder)) and not (file_or_folder in filesnames_to_ingore):
			files.append(join(dir, file_or_folder))

	lines = 0
	
	for file in files:
		lines += count_lines_in_file(file)

	return lines

# Count lines in the files in dir (Recursive)
def count_lines_recursive(dir: str):
	total_lines = count_lines_in_dir(dir)
	
	folders = []

	for file_or_folder in listdir(dir):
		if not isfile(join(dir, file_or_folder)):
			if file_or_folder[0] != '.': # Ignore hidden folders
				folders.append(file_or_folder)

	for folder in folders:
		total_lines += count_lines_recursive(join(dir, folder))

	return total_lines


if __name__ == "__main__":
	parse_cmd_args()

	print("Lines: ", count_lines_recursive(path_to_search))
