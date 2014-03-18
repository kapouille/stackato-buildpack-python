stackato-buildpack-python
=========================

This is a simple but functional buildpack for (Active)Python meant to be used
with Stackato v3 or higher.

This is a variant of the basic buildpack provided by ActiveState.

To use this buildpack, you can:

* structure your application like a python package, and provide a ``setup.py``.
  This will be straightforwardly invoked and the application's package will
  be available globally within the docker container.  ``pip`` will be used to
  install the requirements associated to the application's package
* specify your Python dependencies in one, or both, of
  the following files. Note that those dependencies will be also processed
  if you have structured your application as a python package.
  - ``requirements.txt``: ``pip`` will be used to install these. Optional ``pip``
    parameters can be specified by providing a ``$PIP_OPTS`` environment
    variable in the stackato manifest file.
  - ``requirements.pypm``: ``pypm`` will be used to install these. Optional ``pypm``
    parameters can be specified by providing a ``$PYPM_OPTS`` environment
    variable in the stackato manifest file.

Selecting an alternate runtime
------------------------------

By default, Python 2.7 will be used unless the ``$PYTHON_VERSION`` environment
variable is set in the stackato manifest file.

Alternatively, a ``runtime.txt`` file can be bundled with the application,
with the following content::

    Python-<python_version>

Currently supported versions are 2.7 and 3.3.

Python wheels support and caching
---------------------------------

By default, the buildpack will use the default stackato cache directory to cache downloaded
packages and generated wheels.
An alternative location can be provided by defining the ``$PYTHON_CACHE_DIR`` environment
variable.

.. warning::

    As of version 3.0.x, stackato appears to discard the cache entirely on each staging
    attempt. This greatly diminishes the value of this mechanism.

    One way to remedy this problem is to define a custom stackato filesystem to be used for
    this caching.

    The following stackato manifest outlines how this could be done:

    .. code-block:: yaml

       name: myapp
       instances: 1
       buildpack: https://github.com/kapouille/stackato-buildpack-python.git
       services:
          python-install-cache:
            type: filesystem
       stackato:
          env:
            PYTHON_CACHE_DIR:
              default: $STACKATO_FILESYSTEM_PYTHON_INSTALL_CACHE

When ``pip`` is used for install (in all cases apart from when providing a
``requirements.pypm`` file), the buildpack will generate and cache
`python wheels <http://wheel.readthedocs.org/>`_ for all required packages. This means
that packages that need long compilation times should be instantly installed on
subsequent deployments, provided the cache wasn't cleared.
