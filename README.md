## Setup virtual environment

1. Install pip: sudo apt-get install python-pip
2. Install virtual environment: pip install virtualenv
3. Create virtual environment: virtualenv venv
4. Activate virtual environment: source venv/bin/activate
5. Install project dependencies: pip install -r requirements.txt

### Run all tests

```
pytest
```

### Run tests matching given mark expression

```
pytest -m smoke
```

### Run tests by keyword expression
```
pytest -k TestApiDevices
```
