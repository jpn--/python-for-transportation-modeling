
import platform
import os
import time

def creation_date(path_to_file):
	"""
	Get the file creation date.

	Try to get the date that a file was created, falling back to when it was
	last modified if that isn't possible.

	See http://stackoverflow.com/a/39501288/1709587 for explanation.
	"""
	if platform.system() == 'Windows':
		return os.path.getctime(path_to_file)
	else:
		stat = os.stat(path_to_file)
		try:
			return stat.st_birthtime
		except AttributeError:
			# We're probably on Linux. No easy way to get creation dates here,
			# so we'll settle for when its content was last modified.
			return stat.st_mtime

def append_date_to_filename(filename, epoch):
	"""
	Append a date to a filename

	Parameters
	----------
	filename : Path-like
		The original filename to modify.

	epoch : Number
		The number of seconds since the beginning of 1970.

	Returns
	-------
	str
	"""
	from datetime import datetime
	strftime = datetime.fromtimestamp(epoch).strftime('%Y-%m-%d-%H%M')
	basename, extension = os.path.splitext(filename)
	return f"{basename:s}.{strftime:s}{extension:s}"


