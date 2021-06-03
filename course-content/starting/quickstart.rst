================
Quick Start
================

If you're impatient and just want to get going, follow these instructions.

1.  Download and run the Python installer for your computer from `Anaconda.com <https://www.anaconda.com/distribution>`_.
    Install for the current user only, which does not require administrator permissions.
    If you installed anaconda previously, you usually don't need to re-install it, but
    you may want to update conda to be sure you're running the latest version.  To do
    so, open "Anaconda Prompt" (Windows) or the Terminal (Linux/MacOS) and enter:

    .. code-block:: console

        conda update -n base -c defaults conda

    If this update command does not work (probably because you first installed anaconda
    a long long time ago), you may want to consider uninstalling it and starting fresh.
    If you don't know how, consider talking to your I.T. department about how to update
    conda successfully.

2.  Open "Anaconda Prompt" (Windows) or the Terminal (Linux/MacOS) and enter this command to
    set up a working environment to use with this tutorial:

    .. code-block:: console

        conda env create camsys/tt

    If you had previously installed this "tt" environment and you want to update to the
    latest version, replace "create" with "update", but otherwise the process is the same.

3.  Open "Anaconda Prompt" (Windows) or the Terminal (Linux/MacOS) and enter these two commands
    to start up *Jupyter Notebook*:

    .. code-block:: console

        conda activate tt
        jupyter notebook

    Alternatively, if you prefer the *JupyterLab* interface:
	
    .. code-block:: console

        conda activate tt
        jupyter lab


Only *Step 3* is required for subsequent sessions on the same computer.

What's the difference between *Jupyter Notebook* and *JupyterLab*?  Both provide a
web-based interactive environment for Python (and a few other languages, but mostly
Python).  The *Notebook* has more limited capabilities, tightly focused on using
one notebook at a time.  *JupyterLab* has a more modular approach, where you can open
several notebooks or other related files as tabs in the same window. It offers more
of an IDE-like experience, but may be a little slower to work with, especially if
you create large notebooks with a lot of interactive components.


Troubleshooting
---------------

**I got `ModuleNotFoundError` when trying to import the `transportation_tutorials` package.**

The quick start instructions above will sometimes fail to install the transportation_tutorials
package correctly.  If you get this error, you can try re-installing the module using `pip`:

.. code-block:: console

    conda activate tt
    pip install transportation_tutorials

This re-install procedure should only need to be done once to download and install the files
in the `tt` conda environment, and then you'll have the files you need in the future.

**I got `CondaValueError: prefix already exists` when running `conda env create camsys/tt`.**

If you already have an environment named "tt" (i.e. because you installed this tutorial in the
past once before) then you won't be able to use the command `conda env create camsys/tt`.  In
this case you have two options.

To delete the "tt" environment and start over, run:

.. code-block:: console

    conda env remove -n tt

You'll probably need to confirm this action at the prompt, and then try installing again
following the normal instructions above.  Alternatively, you can update the "tt"
environment in place by running:

.. code-block:: console

    conda env update camsys/tt

This is an easy path if it works cleaning, but if you have any trouble updating
the environment in place, you will almost certainly find it easier to start over
(which is not very hard) rather than to try to fix the broken conda environment.

**I didn't get an environment named "tt" when running `conda env create camsys/tt`.**

By default, the conda environment creation tool looks first for a YAML file in the current
directory named "environment.yml", and if this file exists it will be used to create the new
environment instead of downloading the environment definition from the cloud.  To avoid this,
use the `conda env create camsys/tt` command in a directory that does not contain a file
with this name.

**I got an error complaining that 'osmnx' has no attribute 'gdf_from_place'.**

This error indicates that one or more packages in your environment are out-of-date,
possibly because you installed some of the tools for this tutorial some time ago.
Try updating your working environment by running:

.. code-block:: console

    conda env update camsys/tt

