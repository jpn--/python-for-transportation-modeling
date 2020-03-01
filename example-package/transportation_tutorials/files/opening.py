
import os

from .spooling import archive_existing_file, next_filename

def open_file_writer(
		file,
		overwrite=False,
		archive_dir='./archive/',
		binary=False,
		**kwargs,
):
	"""
	Open file and return a stream.  Raise IOError upon failure.

	Parameters
	----------

	file : Path-like
		This is either a text or byte string giving the name (and the path
		if the file isn't in the current working directory) of the file to
		be opened.

	overwrite : {True, False, 'spool', 'archive'}, default False
		Indicates what to do with an existing file at the same location.
		True will simply overwrite the existing file.
		False will raise a `FileExistsError`.
		'archive' will rename and/or move the existing file so that it
		will not be overwritten.
		'spool' will add a number to the filename of the file to be
		created, so that it will not overwrite the existing file.

	archive_dir : Path-like
		Gives the location to move existing files when overwrite is set to
		'archive'. If given as a relative path, this is relative to the
		dirname of `file`, not relative to the current working directory.
		Has no effect for other overwrite settings.

	binary : bool, default False
		Open the file in binary mode.  This is equivalent to calling `open`
		with a mode parameter of 'b'. Otherwise, the mode parameter is set to 't'
		for text mode.

	"""
	if os.path.exists(file):
		if overwrite == False:
			raise FileExistsError(file)
		elif overwrite == 'archive':
			filedirname, filebasename = os.path.split(file)
			if os.path.isabs(archive_dir):
				# archive path is absolute
				archive_path = archive_dir
			else:
				# archive path is relative
				archive_path = os.path.normpath(os.path.join(filedirname, archive_dir))
			archive_existing_file(file, archive_path, tag='creation')
		elif overwrite == 'spool':
			file = next_filename(file)

	return open(file, mode='wb' if binary else 'wt', **kwargs)