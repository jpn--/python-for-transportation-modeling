

=====================
Managing Environments
=====================

When you use conda to install Python, by default a `base` environment is
created and packages are installed in that environment.  However, in general you should
almost never undertake project work in the `base` environment, especially if your
project involves installing any custom Python packages.  Instead,
you should create a new environment for each project, and install the
necessary packages and dependencies in that environment.  This will help
prevent software conflicts, and ensure that tools installed for one project
will not break another project.

.. note::

    The instructions below provide only the most basic steps to
    set up and use an environment.  Much more extensive documentation
    on :doc:`managing environments <conda:user-guide/tasks/manage-environments>`
    is available in the conda documentation
    itself.


Creating an Environment
-----------------------

From Scratch
~~~~~~~~~~~~

Use the terminal (MacOS/Linux) or an Anaconda Prompt (Windows) to create an environment:

.. code-block:: console

    conda create --name your_environment_name

Be sure to replace ``your_environment_name`` with a suitable
name for the environment to create.

When conda asks you to proceed, type "y" or just hit enter:

.. code-block:: console

    proceed ([y]/n)?

This creates the ``your_environment_name`` environment. By default,
this new environment uses the same version of Python that you are
currently using.  If you want a specific version of Python you can
request it explicitly:

.. code-block:: console

    conda create --name your_environment_name python=3.7

You can also create an environment with one or more specific packages
installed, by giving them as well:

.. code-block:: console

    conda create --name your_environment_name python=3.7 numpy pandas

Clearly, if you have a lot of packages to install, this can become a long
command, and a bit unwieldy to use.  Fortunately, you can instead just
describe the environment you want to create in a YAML file instead of
doing so on the command line.  To do so, you would get or create a YAML
file that looks something like this:

.. code-block:: yaml

    name: your_environment_name

    channels:
    - conda-forge
    - defaults

    dependencies:
    - python=3.7
    - pip
    - numpy>=1.15.4
    - pandas>=0.23.4
    - scipy>=1.1
    - scikit-learn>=0.20.1
    - networkx
    - pip:
      - specialty_package


And then create the environment using the file.

.. code-block:: console

    conda env create -f environment.yml

You may notice that the ``specialty_package`` in the environment.yml file
is installed using pip instead of conda.  This is
`strongly discouraged <https://www.anaconda.com/using-pip-in-a-conda-environment/>`_
if the package is also available from conda, but may be necessary to
install certain packages that are available only on PyPI.

From Anaconda Cloud
~~~~~~~~~~~~~~~~~~~

In addition to creating environments from a file on your local file system,
you can also create environments using remote definitions available on
`anaconda.org <https://www.anaconda.org>`_.  For example, an environment
specifically set up for this transportation tutorial ('tt' for short) can
be installed using the command:

.. code-block:: console

    conda env create camsys/tt

.. note::

    If you installed the "Miniconda" version of the anaconda package, you
    may need to install or update the *conda* and *anaconda-client* packages
    before the remote environment installation will work:

    .. code-block:: console

        conda install -n base -c defaults conda anaconda-client

Changing What is in an Environment
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

The set of packages in any existing environment can be changed after
creating an environment, using the *conda install* command.
For example, to add the latest *scikit-learn* package to the *tt* environment,

.. code-block:: console

    conda install scikit-learn -n tt

You can also install multiple packages at one time, by just listing them as well.

.. code-block:: console

    conda install scikit-learn scikit-image -n tt

The *-t* flag names the environment into which to install the package(s). If this
is omitted, the packages will be installed into the currently active
environment.  You can also install packages in the currently active environment
using *pip*, although like in the original environment definition, it is
recommended to install using conda if possible.  It is also recommended to install
as much as possible in the original definition and creation of the environment.
Adding packages later usually works, but sometimes it can break functionality
of previously installed packages (usually by changing some dependency).  Conda
does as best it can to prevent these problems, but inter-package dependencies
are complicated to manage.


Using an Environment
--------------------

When using the terminal (MacOS/Linux) or an Anaconda Prompt (Windows), the
current environment name will be shown as part of the prompt:

.. code-block:: batch

    (base) C:\Users\cfinley>


.. code-block:: shell-session

    (base) Computer:~ cfinley$

By default, when opening a new terminal the environment is set as the
``base`` environment, although this is typically not where you want to
be if you have followed the advice above.  Instead, to switch environments
use the ``conda activate`` command:

.. code-block:: batch

    (base) C:\Users\cfinley> conda activate your_environment_name
    (your_environment_name) C:\Users\cfinley>

.. code-block:: shell-session

    (base) Computer:~ cfinley$ conda activate your_environment_name
    (your_environment_name) Computer:~ cfinley$

