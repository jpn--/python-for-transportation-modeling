# -*- coding: utf-8 -*-

__version__ = '1.1.0'

import os
import appdirs
import osmnx as ox
import joblib
import requests
from .files import load_vars, save_vars, cached, inflate_tar, download_zipfile
from .data import data, list_data, problematic
from .tools.view_code import show_file
from . import mapping

cache_dir = None
memory = None


def set_cache_dir(location=None, compress=True, verbose=0, **kwargs):
	"""
	Set up a cache directory for use with the tutorials.

	Parameter
	---------
	cache_dir : Path-like or False, optional
		A path for the cache files.  Set to False to disable caching.
	"""
	global memory, cache_dir

	if location is None:
		location = appdirs.user_cache_dir('transportation_tutorials')

	if location is False:
		location = None

	memory = joblib.Memory(location, compress=compress, verbose=verbose, **kwargs)

	make_cache = (
		(ox, 'gdf_from_place'),
		(ox, 'geometries_from_place'),
		(ox, 'graph_from_bbox'),
		(requests, 'get'),
		(requests, 'post'),
	)

	for module, func_name in make_cache:
		try:
			func = getattr(module, f"_{func_name}_orig")
		except AttributeError:
			try:
				func = getattr(module, func_name)
			except:
				func = None
			else:
				setattr(module, f"_{func_name}_orig", func)
		if func is not None:
			setattr(module, func_name, memory.cache(func))


set_cache_dir()


