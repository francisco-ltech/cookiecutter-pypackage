# cookiecutter-pypackage
A python package template generated with cookiecutter.

![Tests](https://github.com/francisco-ltech/cookiecutter-pypackage/actions/workflows/tests.yml/badge.svg)

## Install

Install cookiecutter package

```
$ pip install -U cookiecutter
```

Generate a Python package project

```
$ cookiecutter gh:francisco-ltech/cookiecutter-pypackage
```

## Packages
- [pytest](https://docs.pytest.org/en/7.0.x/) for running tests
- [mypy](http://mypy-lang.org/) for checking typings
- [flake8](https://flake8.pycqa.org/en/latest/) for linting and checking code style
- [tox](https://tox.wiki/) for running tests in various isolated environments

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


## Not Exactly What You Want?

Don't worry, you have options:

### Similar Cookiecutter Templates

-   [audreyfeldroy/cookiecutter-pypackage](https://github.com/audreyfeldroy/cookiecutter-pypackage): Cookiecutter template for a Python package.

### Fork This / Create Your Own

If you have differences in your preferred setup, I encourage you to fork
this to create your own version. Or create your own; it doesn't strictly
have to be a fork.

-   Once you have your own version working, add it to the Similar
    Cookiecutter Templates list above with a brief description.
-   It's up to you whether or not to rename your fork/own version. Do
    whatever you think sounds good.

### Or Submit a Pull Request

I also accept pull requests on this, if they're small, atomic, and if
they make my own packaging experience better.