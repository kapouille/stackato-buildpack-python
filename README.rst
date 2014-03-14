stackato-buildpack-python
=========================

This is a simple but functional buildpack for (Active)Python meant to be used
with Stackato v3 or higher.

This is a variant of the basic buildpack provided by ActiveState.

To use this buildpack, you can either:

* structure your application like a python package, and provide a `setup.py`.
  This will be straightforwardly invoked and the application's package will
  be available globally within the docker container.
* specify your Python dependencies in one, or both, of
  the following files:

  - `requirements.txt`: `pip` will be used to install these. Optional `pip`
    parameters can be specified by providing a `$PIP_OPTS` environment
    variable in the stackato manifest file.

  - `requirements.pypm`: `pypm` will be used to install these. Optional `pypm`
    parameters can be specified by providing a `$PYPM_OPTS` environment
    variable in the stackato manifest file.

Selecting an alternate runtime
------------------------------

By default, Python 2.7 will be used unless the `$PYTHON_VERSION` environment
variable is set in the stackato manifest file.

Alternatively, a `runtime.txt` file can be bundled with the application,
with the following content::

    Python-<python_version>

Currently supported versions are 2.7 and 3.3.

Differences from Heroku buildpack
---------------------------------

* Lightweight (no virtualenv is created)
* Uses ActiveState python
