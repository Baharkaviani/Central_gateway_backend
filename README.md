# Smart Meter Server

## installation

- install [pyenv](https://github.com/pyenv/pyenv)
- install [pyenv-virtualenv](https://github.com/pyenv/pyenv-virtualenv)
- install [poetry](https://github.com/sdispater/poetry)
- install python 3.10.7 via pyenv

```bash
pyenv install 3.10.7
```

- create virtualenv 

```bash
pyenv virtualenv 3.10.7 smart_meter_3.10.7
pyenv activate smart_meter_3.10.7
```
- set pyenv local version in the root folder

```bash
pyenv local smart_meter_3.10.7
```

- install dependencies

```bash
poetry install --no-dev
```