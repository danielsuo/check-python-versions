Changelog
=========

0.13.1 (unreleased)
-------------------

- Nothing changed yet.


0.13.0 (2019-10-15)
-------------------

- Support Python 3.8.

- Stop adding ``dist: xenial`` to .travis.yml as that is now the default.


0.12.1 (2019-05-02)
-------------------

- Improvements in Python version updating:

  - preserve comma style in python_requires lines
  - no longer upgrade 'pypy' to 'pypy2.7-6.0.0' and 'pypy3' to 'pypy3.5-6.0.0'
    because xenial now has 'pypy' and 'pypy3' available


0.12.0 (2019-04-18)
-------------------

- Ignore unreleased Python versions (3.8 at the moment).

- Allow half-open ranges like ``--expect 3.5-``.

- Add experimental support for updating supported Python versions in
  setup.py, tox.ini, .travis.yml, appveyor.yml and .manylinux-install.sh:

  - command-line options --add and --drop to add and/or drop specific versions

  - command-line option --update to explicitly enumerate all supported versions

  - all changes are shown as diffs with confirmation before applying

  - command-line option --diff to show the diffs and exit without any prompting

  - command-line option --dry-run to re-run the parser and checker on in-memory
    copies of updated files, to see if the update would succeed

  - command-line option --only to limit the checks/update to some of the
    supported files


0.11.0 (2019-02-13)
-------------------

- Implement a full PEP-440 parser for python_requires.


0.10.0 (2018-12-11)
-------------------

- Do not consider "X.Y-dev" in .travis.yml as support for Python X.Y.
- Print warnings to stderr, not stdout.
- Add a test suite.
- Fix a lot of minor buglets.


0.9.2 (2018-12-03)
------------------

- Strip trailing spaces from classifiers.


0.9.1 (2018-11-30)
------------------

- Parse TOXENV in appveyor.yml.


0.9.0 (2018-11-19)
------------------

- Handle syntax errors while parsing setup.py.
- Handle 'Programming Language :: Python :: {N} :: Only" classifiers.
- New option: --skip-non-packages.


0.8.0 (2018-11-16)
------------------

- First public release.
