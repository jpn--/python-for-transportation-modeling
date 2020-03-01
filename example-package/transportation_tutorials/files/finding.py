

import os
import sys
import glob
import time


def first_existing(*filenames, expanduser=True):
	"""
	Finds the first existing file among listed file names.

	Parameters
	----------
	filenames : tuple of Path-like
	expanduser : bool, default true
		Should each filename be passed through the `os.path.expanduser` function?

	Returns
	-------
	f : Path-like
		The first existing file in the list.

	Raises
	------
	FileNotFoundError
		If none of the listed file names exists

	"""
	for f in filenames:
		if expanduser:
			f = os.path.expanduser(f)
		if os.path.exists(f):
			return f
	raise FileNotFoundError('none of these files found:\n'+ '\n'.join(filenames) )

def all_existing(*filenames, expanduser=True, raise_if_none=True):
	"""
	Finds all existing files among listed file names.

	Parameters
	----------
	filenames : tuple of Path-like
	expanduser : bool, default True
		Should each filename be passed through the `os.path.expanduser` function?
	raise_if_none : bool, default True
		If none of `filenames` exists, raise an exception instead of returning an
		empty list

	Returns
	-------
	f : Path-like
		The first existing file in the list.

	Raises
	------
	FileNotFoundError
		If none of the listed file names exists

	"""
	result = []
	for f in filenames:
		if expanduser:
			f = os.path.expanduser(f)
		if os.path.exists(f):
			result.append(f)
	if raise_if_none and len(result)==0:
		raise FileNotFoundError('none of these files found:\n'+ '\n'.join(filenames) )
	return result


def _insensitive_glob(pattern):
	def either(c):
		return '[%s%s]' % (c.lower(), c.upper()) if c.isalpha() else c
	return ''.join(map(either, pattern))


def latest_matching(pattern, echo=False, case_insensitive=False, expanduser=True):
	"""Get the most recently modified file matching the glob pattern

	Parameters
	----------
	pattern : str
		A glob pattern to match on
	echo : bool, default False
		If true, print the last modified time for each matching file
	case_insensitive : bool, default False
		Tf true, the glob pattern will be modified to be case insensitive.
	expanduser : bool, default true
		Should each pattern be passed through the `os.path.expanduser` function?

	Returns
	-------
	str
		The filename of the most recently modified file matching the glob pattern

	"""
	if expanduser:
		pattern = os.path.expanduser(pattern)
	if case_insensitive:
		pattern = _insensitive_glob(pattern)
	files = glob.glob(pattern)
	propose = None
	propose_mtime = 0
	for file in files:
		(mode, ino, dev, nlink, uid, gid, size, atime, mtime, ctime) = os.stat(file)
		if echo:
			print (file,"last modified: %s" % time.ctime(mtime))
		if mtime > propose_mtime:
			propose_mtime = mtime
			propose = file
	return propose


def created_more_recently(filename0, filename1):
	"""
	Identify which of two files was created more recently.

	Parameters
	----------
	filename0, filename1 : Path-like

	Returns
	-------
	int
		0 if `filename0` was created more recently, otherwise 1

	"""
	(mode1, ino1, dev1, nlink1, uid1, gid1, size1, atime1, mtime1, ctime1) = os.stat(filename0)
	(mode2, ino2, dev2, nlink2, uid2, gid2, size2, atime2, mtime2, ctime2) = os.stat(filename1)
	if ctime1<ctime2:
		return 1
	if ctime1>=ctime2:
		return 0
