================
Starting Jupyter
================

A convenient interface for interactive use of Python for data analysis is
the Jupyter Notebook.  This data format combines code and output into
a portable package that is (relatively) easily sharable, and can provide
dynamic, real-time interactive output.

The most modern way to interact with a Jupyter notebook is using
`JupyterLab <https://jupyterlab.readthedocs.io/en/stable/>`_, which
provides a familiar interface, and allows you to open and edit multiple
notebooks simultaneously.
If it's not already installed in your base or working
environments, you can install it using conda:

.. code-block:: console

    conda install -c conda-forge jupyterlab

Then to start JupyterLab,

.. code-block:: console

    jupyter lab

JupyterLab will open automatically in your browser.  If you want to use a
particular environment to run JupyterLab, you can activate that environment
and run it in sequence like this:

.. code-block:: console

    conda activate tt
    jupyter lab
