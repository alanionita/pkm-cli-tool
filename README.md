# Notes CLI tool 

A simple python tool for creating .md notes for various use cases. 

Main use case is daily notes, where the note templates contain specific frontmatter

## Install

### Pre-requisite

- [ ] miniconda, see [Installing on Linux](https://conda.io/projects/conda/en/stable/user-guide/install/linux.html) or other guides

### Create a conda environment for this project

Run: `conda env create --file=environment.yaml`


## Usage

### Pre-requisite

Activate Conda environment

Run: ``conda activate pkm-cli-tool`` 

### Start app

Run: `python3 main.py`

### Install

Run: `pip install --editable .`

### Testing

```
pytest

```

To return any output from the functions 

```
pytest -s

```