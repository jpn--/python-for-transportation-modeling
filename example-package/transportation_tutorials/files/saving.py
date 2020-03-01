
from .opening import open_file_writer

import os
import gzip
import hashlib
try:
	import cloudpickle as pickle
except ImportError:
	import pickle




def save(
		obj,
		filename,
		overwrite=False,
		archive_dir='./archive/',
		compress=True,
):
	"""
	Save an object to a file.

	Parameters
	----------

	obj : Any
		An object to be saved.  Must be pickle-able (using cloudpickle if
		available, otherwise regular pickle).

	filename : Path-like
		This is either a text or byte string giving the name (and the path
		if the file isn't in the current working directory) of the file to
		be written to.

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

	"""

	with open_file_writer(filename, overwrite=overwrite, archive_dir=archive_dir, binary=True) as f:
		if compress:
			f.write(gzip.compress(pickle.dumps(obj)))
		else:
			f.write(pickle.dumps(obj))

def load(filename):
	"""
	Load an object from a file.

	Parameters
	----------

	filename : Path-like
		This is either a text or byte string giving the name (and the path
		if the file isn't in the current working directory) of the file to
		be written to.

	Returns
	-------
	object
	"""
	if not os.path.isfile(filename):
		raise FileNotFoundError(filename)
	content = None
	with open(filename, 'rb') as f:
		content = f.read()

	try:
		content = gzip.decompress(content)
	except:
		pass

	return pickle.loads(content)


def cache(filename, function, *args, **kwargs):
	"""
	Cache a function's return value to a file.

	This is not a smart cache: if the named cache file exists, it is loaded
	and the given arguments are ignored.

	Parameters
	----------
	filename : Path-like
		This is either a text or byte string giving the name (and the path
		if the file isn't in the current working directory) of the file to
		be used.
	function : Callable
		A function
	*args, **kwargs : Any
		Arguments to the function if the result is not cached.

	Returns
	-------
	object
	"""
	if os.path.isfile(filename):
		return load(filename)
	else:
		obj = function(*args, **kwargs)
		save(obj, filename, overwrite=False)
		return obj

def auto_cache(cache_dir, function, *args, **kwargs):
	"""
	Cache a function's return value to a file.

	This is slightly smarter cache: if the named cache file exists, it is loaded
	and the given arguments are ignored.

	Parameters
	----------
	cache_dir : Path-like
		This is either a text or byte string giving the name (and the path
		if the file isn't in the current working directory) of the directory to
		be used to store cache files.
	function : Callable
		A function
	*args, **kwargs : Any
		Arguments to the function if the result is not cached.

	Returns
	-------
	object
	"""
	h = hashlib.sha224(pickle.dumps((args, kwargs))).hexdigest()
	cachefile = os.path.join(cache_dir, f"{h}.gzpk")
	return cache(cachefile, function, *args, **kwargs)

def cached(function, cache_dir):
	"""
	A function wrapper that implements an auto_cache.

	Parameters
	----------
	function : Callable
		A function
	cache_dir : Path-like
		This is either a text or byte string giving the name (and the path
		if the file isn't in the current working directory) of the directory to
		be used to store cache files.

	Returns
	-------
	function : Callable
	"""
	return lambda *args, **kwargs: auto_cache(cache_dir, function, *args, **kwargs)


def save_vars(*args, directory=None):
	"""
	Save variables from the main namespace.

	Parameters
	----------
	*args : Collection[str]
		The names of variables in the main namespace to save.
	directory : Path-like, optional
		The directory in which to save the files.  The default is
		the current cache_dir in the parent package.
	"""
	if directory is None:
		from .. import memory
		directory = memory.location
	if directory is None:
		raise ValueError("no directory")
	os.makedirs(os.path.join(directory, '_locals'), exist_ok=True)
	import __main__
	for a in args:
		obj = getattr(__main__, a)
		save(obj, os.path.join(directory, '_locals', f'{a}.gzpk'), overwrite=True)

def load_vars(*args, directory=None):
	"""
	Load variables into the main namespace.

	Parameters
	----------
	*args : Collection[str]
		The names of variables in the main namespace to save.
	directory : Path-like, optional
		The directory in which to save the files.  The default is
		the current cache_dir in the parent package.
	"""
	if directory is None:
		from .. import memory
		directory = memory.location
	if directory is None:
		raise ValueError("no directory")
	import __main__
	for a in args:
		obj = load(os.path.join(directory, '_locals', f'{a}.gzpk'))
		setattr(__main__, a, obj)
