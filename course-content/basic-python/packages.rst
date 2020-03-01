

Python Packages
===============

Transportation analysis in Python relies heavily on external and 3rd party packages
to enable a complete set of vital functionality.  Multiple proprietary systems for
transportation planning offer varying levels of compatibility with, and dependency on,
Python and affiliated tools.  Outlined below are a selection of *free, open source* packages
that offer a great deal of important functionality.  Although the construction of
a complete transportation demand forecasting model system using only
these tools may not be possible without great effort, it is likely you will find
some of them useful for ancillary analysis tasks undertaken in Python.


Math and Statistical Analysis
-----------------------------

- `NumPy <https://docs.scipy.org/doc/numpy/user/>`_

  NumPy is the core library for basic array-based mathematical operations in Python.
  It is generally a dependency of most other mathematical analysis packages.

- `SciPy <https://docs.scipy.org/doc/scipy/reference/>`_

  SciPy (pronounced “Sigh Pie”) is open-source software for mathematics, science, and engineering.

- `Pandas <https://pandas.pydata.org>`_

  Pandas is an open source library providing high-performance, easy-to-use data structures
  and data analysis tools for the Python programming language.

- `statsmodels <https://www.statsmodels.org>`_

  Statsmodels is a Python module that provides classes and functions for the estimation of
  many different statistical models, as well as for conducting statistical tests, and statistical
  data exploration. An extensive list of result statistics are available for each estimator.

- `scikit-learn <https://scikit-learn.org>`_

  Scikit-learn includes simple and efficient machine learning tools for data mining and
  data analysis.  Note: While this package is *installed* using `conda install scikit-learn`,
  it is *imported* into python using `import sklearn`.

Data Visualization
------------------

- `Matplotlib <https://matplotlib.org>`_

  Matplotlib is a Python 2D plotting library which produces figures in a variety of hardcopy
  formats and interactive environments across platforms.

- `seaborn <https://seaborn.pydata.org/>`_

  Seaborn is a Python data visualization library based on matplotlib. It provides a high-level
  interface for drawing attractive and informative statistical graphics.


Data Management
---------------

- `pytables <https://www.pytables.org/>`_

  PyTables is a package for managing hierarchical datasets, using HDF5. It is designed to
  efficiently and easily cope with extremely large amounts of data.  It is designed to
  integrate well into Python, but it does not attempt to replicate all of the features in
  the HDF5 library.

- `h5py <https://www.pytables.org/>`_

  The h5py package is a Pythonic interface to the HDF5 binary data format, and it tries
  as much as possible to directly map as many features of the HDF5 library to NumPy as possible.

- `openmatrix <https://github.com/osPlanning/omx-python>`_

  The `open matrix file format <https://github.com/osPlanning/omx/wiki>`_ (or simply OMX) is
  based on the open-source file storage technology HDF5. OMX files can store multiple
  matrices in one file, can include multiple indexes/lookups, and can contain attributes
  (key/value pairs) for both matrices and indexes.


Discrete Choice Analysis
------------------------

- `Larch <https://larch.newman.me>`_

  Larch is a package for the estimation and application of logit-based discrete choice
  models. It is designed to integrate with NumPy and Pandas, and facilitate fast processing
  of linear models.  (If you want to estimate non-linear models, try Biogeme).
  Note: Larch is not available in the default conda package channel, and must be installed
  using `conda install larch -c jpn`.

- `Biogeme <https://biogeme.epfl.ch/>`_

  Biogeme is a open source Python package designed for the maximum likelihood estimation of
  parametric models in general, with a special emphasis on discrete choice models. It can
  handle a wider variety of functional forms than Larch, although the structure of inputs and
  outputs is less customizable.  Note: Biogeme is not currently available from conda, and must
  be installed using `pip install biogeme`.


Network Analysis
----------------

- `networkx <https://networkx.github.io/>`_

  NetworkX is a Python package for the creation, manipulation, and study of the structure,
  dynamics, and functions of complex networks.

- `OSMnx <https://osmnx.readthedocs.io/en/stable/>`_

  OSMnx is a Python package that lets you download spatial geometries and construct,
  project, visualize, and analyze street networks from OpenStreetMap’s APIs. Users can
  download and construct walkable, drivable, or bikable urban networks with a single line
  of Python code, and then easily analyze and visualize them.


Mapping and Geographic Analysis
-------------------------------

- `GeoPandas <http://geopandas.org/>`_

  GeoPandas is an open source project to make working with geospatial data in python easier.
  GeoPandas extends the datatypes used by pandas to allow spatial operations on geometric
  types. Geometric operations are performed by shapely.

- `Shapely <https://shapely.readthedocs.io/en/latest/>`_

  Shapely is a BSD-licensed Python package for manipulation and analysis of planar geometric
  objects. Shapely is not concerned with data formats or coordinate systems, but can be
  readily integrated with packages that are (e.g. GeoPandas).

- `Folium <https://python-visualization.github.io/folium/>`_

  Folium is a Python-based interface for generating for dynamic maps using
  `Leaflet <https://leafletjs.com>`_.

