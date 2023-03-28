# TuneTube [![tests](https://github.com/PenguinSnail/tunetube/actions/workflows/tests.yml/badge.svg)](https://github.com/PenguinSnail/tunetube/actions/workflows/tests.yml)

A music sharing forum developed for ITSC 3155 Software Engineering

Visit TuneTube at [https://www.tunetube.online](https://www.tunetube.online)

## Setup

### Install dependencies

In order to run, a python virtual environment must be created, and dependencies must be installed via pip.
This can be done by executing the following commands:

```bash
python -m venv venv
source venv/bin/activate
pip install -r requirements.txt
```

### Setup git hooks

This repository is set up to be able to use git pre-commit hooks to automatically check and format code before committing.
To make use of this, the hooks must be installed:

```bash
pre-commit install
```

**Note:** This is only needed if you'll be committing code

## Management

### Tests

pytest is used for unit tests and end-to-end tests of the main python code:

```bash
pytest
```

### Formatting

Various style checkers and linters are set up to run through git hooks.
These include:

- [flake8](https://flake8.pycqa.org/): python style checking
- [black](https://black.readthedocs.io/): python code formatting
- [eslint](https://eslint.org/): javascript style checking and code formatting
- [prettier](https://prettier.io/): html and css style checking and formatting

These can also be triggered manually if needed:

```bash
pre-commit run --all-files
```

**Note:** Git hooks need to be set up for this to work

## Running

```bash
flask run
flask --debug run # run in debug mode
```

## Team Members

- Ethan Hurley [https://github.com/ethurley15](https://github.com/ethurley15)
- Aiden James [https://github.com/bubbybumble](https://github.com/bubbybumble)
- Tyler Jordan [https://github.com/tylerJordan223](https://github.com/tylerJordan223)
- Noah Piraino [https://github.com/PenguinSnail](https://github.com/PenguinSnail)
- Joe Sunshine [https://github.com/JoeSunshine2](https://github.com/JoeSunshine2)
- Franky Yang [https://github.com/frankyToast](https://github.com/frankyToast)
