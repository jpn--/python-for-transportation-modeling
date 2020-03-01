
import os
import time
import shutil

from .timing import creation_date, append_date_to_filename

def filename_split(filename):
	pathlocation, basefile = os.path.split(filename)
	basefile_list = basefile.split(".")
	if len(basefile_list) > 1:
		basename = ".".join(basefile_list[:-1])
		extension = "." + basefile_list[-1]
	else:
		basename = basefile_list[0]
		extension = ""
	return (pathlocation, basename, extension)


def filename_fuse(pathlocation, basename, extension):
	x = os.path.join(pathlocation, basename)
	if extension != "": x += "." + extension
	return x


def next_filename(
		filename,
		format="{basename:s}.{number:03d}{extension:s}",
		suffix=None,
		plus=0,
		allow_natural=False,
		demand_natural=False,
):
	"""Finds the next file name in this stack that does not yet exist.

	Parameters
	----------
	filename : str or None
		The base file name to use for this stack.  New files would have a number
		appended after the basename but before the dot extension.  For example,
		if the filename is "/tmp/boo.txt", the first file created will be named
		"/tmp/boo.001.txt".  If None, then a temporary file is created instead.


	Other Parameters
	----------------
	suffix : str, optional
		If given, use this file extension instead of any extension given in the filename
		argument.  The usual use case for this parameter is when filename is None,
		and a temporary file of a particular kind is desired.
	format : str, optional
		If given, use this format string to generate new stack file names in a
		different format.
	plus : int, optional
		If given, increase the returned filenumber by this amount more than what
		is needed to generate a new file.  This can be useful with pytables, which can
		create pseudo-files that don't appear on disk but should all have unique names.
	allow_natural : bool
		If true, this function will return the unedited	`filename` parameter
		if that file does not already exist. Otherwise will always have a
		number appended to the name.
	demand_natural : bool
		If true, this function will just throw a FileExistsError instead of spooling
		if the file already exists.

	"""
	if filename is not None:
		filename = os.path.expanduser(filename)
	if demand_natural and os.path.exists(filename):
		raise FileExistsError(filename)
	if allow_natural and not os.path.exists(filename):
		return filename
	pathlocation, basename, extension = filename_split(filename)
	if suffix is not None:
		extension = "." + suffix
	fn = lambda n: os.path.join(pathlocation, format.format(basename=basename, extension=extension, number=n))
	n = 1
	while os.path.exists(fn(n)):
		n += 1
	return fn(n + plus)


def archive_existing_file(
		filename,
		archive_path=None,
		tag='now',
):
	"""
	Archive a file.

	Parameters
	----------
	filename : Path-like
		Source file.
	archive_path : Path-like, optional
		Destination for the archival copy.  If not given, the file name is modified
		in-place and the file is not moved.
	tag : {'now', 'creation'}, default 'now'
		Appends a tag to the existing file based on the current time, or
		the time that the file being archived was created.

	"""

	if tag=='now':
		epoch = time.time()
	elif tag=='creation':
		epoch = creation_date(filename)
	else:
		raise ValueError('supported tags are [now, creation]')

	if archive_path is None:
		archive_path = os.path.dirname(filename)

	filebasename = os.path.basename(filename)

	if not os.path.exists(filename):
		raise FileNotFoundError(filename)

	if not os.path.exists(archive_path):
		os.makedirs(archive_path)

	# send existing file to archive
	new_name = next_filename(
		append_date_to_filename(os.path.join(archive_path, filebasename), epoch),
		allow_natural=True
	)
	shutil.move(filename, new_name)


