# TuneTube

A music sharing forum developed for ITSC 3155 Software Engineering

## Setup

### Install dependencies

```bash
python -m venv venv
source venv/bin/activate
pip install -r requirements.txt
```

### Setup git hooks

**Note:** This is only needed if you'll be committing code

```bash
pre-commit install
```

## Management

### Tests

```bash
pytest
```

### Formatting

**Note:** Git hooks need to be set up for this to work

```bash
pre-commit run --all-files
```

### Running

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
