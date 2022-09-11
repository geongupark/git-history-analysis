![logo_long](https://user-images.githubusercontent.com/66377511/189514826-e83bf135-5dcd-4b86-82e9-2774bfda4dab.png)
***
![pypi](https://img.shields.io/badge/pypi-v0.1.0-blue/)
![Python](https://img.shields.io/badge/python-3.6+-blue)
![License](https://camo.githubusercontent.com/890acbdcb87868b382af9a4b1fac507b9659d9bf/68747470733a2f2f696d672e736869656c64732e696f2f62616467652f6c6963656e73652d4d49542d626c75652e737667)
[![Build](https://github.com/geongupark/git-log-analysis/workflows/unit-test/badge.svg)](https://github.com/geongupark/git-log-analysis/actions/workflows/unit_test.yml)
[![Documentation](https://img.shields.io/badge/ref-Documentation-blue)](https://geongupark.github.io/git-log-analysis/)
![lastcommit](https://img.shields.io/github/last-commit/geongupark/git-log-analysis)
* The `gitloganalysis` framework makes it easy to get and sort the git commit frequency by files.

# Features
* Easy to get the git commit frequency by files for a specific repository
* Can get the git commit frequency for a specific period
* Can see the git commit frequency using a histogram
* Use `gitloganalysis` package by command line or package import

# How to use

## 1) Install
```
pip install gitloganalysis
```

## 2) Usage
```
$ gitloganalysis -h
usage: gitloganalysis [-h] -r ROOT [-p HISTOGRAM] [-o OUTPUT] [-a AFTER] [-b BEFORE] [-e ALLOWEDEXT [ALLOWEDEXT ...]]

optional arguments:
  -h, --help            show this help message and exit
  -r ROOT, --root ROOT  Project root directory ex) -r ./
  -p HISTOGRAM, --histogram HISTOGRAM
                        Print histogram ex) -p False
  -o OUTPUT, --output OUTPUT
                        Output file(json) path ex) -o ./gla_output.json
  -a AFTER, --after AFTER
                        After ex) -a 2022-09-07
  -b BEFORE, --before BEFORE
                        Before ex) -b 2022-09-10
  -e ALLOWEDEXT [ALLOWEDEXT ...], --allowedext ALLOWEDEXT [ALLOWEDEXT ...]
                        Allowed extension ex) -e py java c cpp
```

# License
* Distributed under the terms of the MIT license, `gitloganalysis` is free and open source software.