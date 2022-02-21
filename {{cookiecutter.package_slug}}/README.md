# cookiecutter-pypackage
A python package template generated with cookiecutter.

![Tests](https://github.com/francisco-ltech/cookiecutter-pypackage/actions/workflows/tests.yml/badge.svg)

## Packages
- [pytest](https://docs.pytest.org/en/7.0.x/) for running tests
- [mypy](http://mypy-lang.org/) for checking typings
- [flake8](https://flake8.pycqa.org/en/latest/) for linting and checking code style
- [tox](https://tox.wiki/) for running tests in various isolated environments

### Pytest features
| Name                     | Description                                                                                                          |
|--------------------------|----------------------------------------------------------------------------------------------------------------------|
| @pytest.mark.parametrize | Allows to feed different test cases in the form of arguments to a single test function.                              |
| @pytest.mark.skip        | Allows to skip (not run) a test for a justified reason, e.g.: feature not yet supported.                             |
| @pytest.mark.xfail       | Allows to ignore a failing test to not fail the build and don't count as a failure.                                  |
| @pytest.fixture          | Allows to re-use code that will run on various test, fixtures should be place in conftest.py. E.g.: a db connection. |
| with pytest.raises       | Allows to test an exception outcome form the function under test.                                                    |

## Build tools

### Tox

[Tox](https://tox.wiki/) is a generic virtualenv management and test command line tool you can use for:
- Checking that your package installs correctly with different Python versions and interpreters.
- Running your tests in each of the environments, configuring your test tool of choice.
- Acting as a frontend to Continuous Integration servers, greatly reducing boilerplate and merging CI and shell-based testing.

Note: Tox will provision a configured environment from scratch, e.g.: will install all dependencies from fresh, run test, etc. This can take longer tha just testing on a local pre-configured environment.

It is **good practice** to run tox locally before git push to ensure build will succeed on your build server, e.g.: GitHub actions.

### GitHub Actions

- GitHub Action is configured to run Tox on commit action.
- The [test.yml](.github/workflows/tests.yml) file contains all the details of the GitHub workflow.
- Tox environments run on Ubuntu Linux and Windows operating systems.
- The result of the test check on GH is reflected on this README.md (see top of the page).


