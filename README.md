# Notes CLI tool 

A simple python tool for creating .md notes for various use cases. 

Main use case is daily notes, where the note templates contain specific frontmatter

https://github.com/alanionita/pkm-cli-tool/actions/workflows/python_package_flow.yml/badge.svg

## Install

### Pre-requisite

- [ ] miniconda, see [Installing on Linux](https://conda.io/projects/conda/en/stable/user-guide/install/linux.html) or other guides

### Create a conda environment for this project

Run: `conda env create --file=environment.yaml`

### Locally install the app

Run: `pip install --editable .`


## Usage

### Pre-requisite

Activate Conda environment

Run: ``conda activate pkm-cli`` 

### Start app

Run: `pkmcli`

Will return help text for the registered commands


## Testing

```
pytest

```

To return any output from the functions 

```
pytest -s

```

To output coverage reports

```
pytest --cov=pkmcli tests/

```