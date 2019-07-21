# Small talk benchmark dashboard

This repository is used to display some small talk benchmark.

[**Click here to see the app!**](https://dash-text-mining-dashboard.herokuapp.com/)

## Index

1.  [References](#references)
1.  [Dependencies](#dependencies)
1.  [Installation](#installation)
1.  [Launch App](#launch-app)

## References

- [_Build a Complex Reporting Dashboard using Dash and Plotly_](https://github.com/davidcomfort/dash_sample_dashboard) by @davidcomfort
- [_Small talk data_](https://github.com/rahul051296/small-talk-rasa-stack) from @rahul051296

## Dependencies

- [anaconda](https://www.anaconda.com/distribution/)

## Installation

Install a conda environment:

```bash
conda create -n smalltalk anaconda python=3.7.2
conda activate smalltalk
pip install -r ./requirements.txt
```

_N.B.:_ The `requirements.txt` file has been generated with the following command lines:

```bash
conda create -n smalltalk anaconda python=3.7.2
conda activate smalltalk
pip install black dash dash_auth flake8 gunicorn pandas swifter
pip freeze > requirements.txt
```

## Launch App

The app can be launched by activating the Python environment and launching the `index.py` file in the `smalltalk` folder in command line:

```bash
conda activate smalltalk
python index.py
```

The app is then running on `http://127.0.0.1:8050/`.
