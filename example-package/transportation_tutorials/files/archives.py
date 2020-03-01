
import os
import tempfile
import tarfile
import gzip
import shutil

temp_dir = tempfile.TemporaryDirectory()

def inflate_tar(tar_file, destination=None):
	"""
	Decompress and untar a .tar.gz file.

	Parameters
	----------
	tar_file : Path-like
		Source file.
	destination : Path-like, optional
		Destination directory.  If not given a temporary directory is used.

	Returns
	-------
	destination : Path-like
		The location where the tarball was inflated.
	names : list
		The name of files or directories that were created in the destination.
	"""
	tf = tarfile.open(name=tar_file, mode='r:*')
	if destination is None:
		destination = temp_dir.name
	tf.extractall(destination)
	return destination, tf.getnames()

def duplicate(sourcefile, destination=None):
	"""
	Copy and if needed decompress a file.

	Parameters
	----------
	sourcefile : Path-like
		Source file.
	destination : Path-like, optional
		Destination directory.  If not given a temporary directory is used.

	Returns
	-------
	destination : Path-like
		The location where the file was decompressed.
	name : str
		The name of the file that was created in the destination.
	"""
	source_dir, source_file = os.path.split(sourcefile)
	source_base, source_ext = os.path.splitext(source_file)

	if destination is None:
		destination = temp_dir.name

	if source_ext == '.gz':
		with gzip.open(sourcefile, 'rb') as f_in:
			with open(os.path.join(destination, source_base), 'wb') as f_out:
				shutil.copyfileobj(f_in, f_out)
		return destination, source_base
	else:
		with open(sourcefile, 'rb') as f_in:
			with open(os.path.join(destination, source_file), 'wb') as f_out:
				shutil.copyfileobj(f_in, f_out)
		return destination, source_file
