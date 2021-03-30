
import os
from ..files import inflate_tar, latest_matching, duplicate

this_directory = os.path.dirname(__file__)

loaded_data = {}

def data(name, file=None):
	global loaded_data
	if name not in loaded_data:
		rawfile = os.path.join(this_directory, name)
		tarfile = os.path.join(this_directory, f'{name}.tar.gz')
		csvfile = os.path.join(this_directory, f'{name}.csv.gz')
		dbffile = os.path.join(this_directory, f'{name}.dbf.gz')
		omxfile = os.path.join(this_directory, f'{name}.omx')
		xlsxfile = os.path.join(this_directory, f'{name}.xlsx')
		if os.path.isfile(tarfile):
			f, f_names = inflate_tar(tarfile)
			loaded_data[name] = os.path.join(f, f_names[0])
		elif os.path.isfile(csvfile):
			loaded_data[name] = csvfile
		elif os.path.isfile(dbffile):
			f, f_name = duplicate(dbffile)
			loaded_data[name] = os.path.join(f, f_name)
		elif os.path.isfile(omxfile):
			f, f_name = duplicate(omxfile)
			loaded_data[name] = os.path.join(f, f_name)
		elif os.path.isfile(xlsxfile):
			loaded_data[name] = xlsxfile
		elif os.path.isfile(rawfile):
			loaded_data[name] = rawfile
		else:
			raise FileNotFoundError(os.path.join(this_directory, f'{name}.*.gz'))
	if file is not None:
		return os.path.relpath(latest_matching(os.path.join(loaded_data[name], file)))
	return os.path.relpath(loaded_data[name])


def list_data():
	import glob
	files = []
	for i in glob.glob(os.path.join(this_directory, '*.tar.gz')):
		files.append(os.path.basename(i)[:-7])
	for i in glob.glob(os.path.join(this_directory, '*.csv.gz')):
		files.append(os.path.basename(i)[:-7])
	return files

def problematic():
	filename = data('THIS-FILE-IS-CORRUPT')
	import pandas
	# When there are various lines of code intervening,
	# you might not get to see the relevant problem in the traceback
	result = pandas.read_csv(filename)
	return result




# https://sites.google.com/site/serpm8reference/model-outputs/highway-networks-and-skims?authuser=0

