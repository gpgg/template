# My Template for Deep Learning

## Usage

```
poetry update
```

## Tools

- pyenv: python version management.

use pyenv to set the python version:

```python
pyenv local 3.8.10
```

- poetry: dependency management.

poetry config settings:

```python
virtualenvs.in-project = true # poetryの仮想環境をプロジェクトと同一フォルダに配置する
virtualenvs.prefer-active-python = true # Poetry will try to find the current python of your shell.
```

### Packages

- torch
- torchaudio
- torchvision
- torchtext
- jupyter

About formatting etc :

- black
- flake8
- isort

## Tested Platforms

- Windows 11 Pro
- MacBook Pro M1 Pro

[reference1](https://qiita.com/MasashiSD/items/a8ddc0b039a5b112b109)

[reference2](https://hippocampus-garden.com/jupyter_poetry_pipenv/)
