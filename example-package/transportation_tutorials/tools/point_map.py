
# Code based on an original given in
# https://github.com/agaidus/census_data_extraction/blob/master/census_mapper.py

import geopandas as gpd
import pandas as pd
from shapely.geometry import Point
from numpy.random import RandomState, uniform


def generate_random_points_in_polygon(poly, num_points, seed=None):
	"""
	Create a list of randomly generated points within a polygon.

	Parameters
	----------
	poly : Polygon
	num_points : int
		The number of random points to create within the polygon
	seed : int, optional
		A random seed

	Returns
	-------
	List
	"""
	min_x, min_y, max_x, max_y = poly.bounds
	points = []
	i = 0
	while len(points) < num_points:
		s = RandomState(seed + i) if seed else RandomState(seed)
		random_point = Point([s.uniform(min_x, max_x), s.uniform(min_y, max_y)])
		if random_point.within(poly):
			points.append(random_point)
		i += 1
	return points


def generate_points_in_areas(gdf, values, points_per_unit=1, seed=None):
	"""
	Create a GeoSeries of random points in polygons.

	Parameters
	----------
	gdf : GeoDataFrame
		The areas in which to create points
	values : str or Series
		The [possibly scaled] number of points to create in each area
	points_per_unit : numeric, optional
		The rate to scale the values in point generation.
	seed : int, optional
		A random seed

	Returns
	-------
	GeoSeries
	"""
	geometry = gdf.geometry
	if isinstance(values, str) and values in gdf.columns:
		values = gdf[values]
	new_values = (values / points_per_unit).astype(int)
	g = gpd.GeoDataFrame(data={'vals': new_values}, geometry=geometry)
	a = g.apply(lambda row: tuple(generate_random_points_in_polygon(row['geometry'], row['vals'], seed)), 1)
	b = gpd.GeoSeries(a.apply(pd.Series).stack(), crs=geometry.crs)
	b.name = 'geometry'
	return b

