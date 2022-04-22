# Review Summarization

## Author
Nick Buker

## Project Description
This repo represents the humble beginnings of an exploration of text summarization algorithms. Extractive algorithms identify key phrases or sentences through use of statistical or deep learning methods.

## Requirements
- Project created using Python 3.9.12
- Required Python packages and versions can be found in the `requirements.txt` file
- Pytest used as testing framework
- All *.py files formatted using the [black code formatter](https://github.com/psf/black).

## Project Structure
### Tree
```
├── README.md
├── __init__.py
├── data/
├── notebooks/
│   ├── 00_eda_and_data_prep.ipynb
│   ├── 01_summarization.ipynb
│   └── __init__.py
├── requirements.txt
├── src/
│   ├── __init__.py
│   └── utils.py
└── test/
    ├── __init__.py
    └── test_utils.py
```
### Desciptions
- `data/` - Directory to house reviews data
- `notebooks/` - Directory to house notebooks
    - `00_eda_and_data_prep.ipynb` - Exploratory data analysis of review data
    - `01_summarization.ipynb` - Key sentence extraction via TextRank algorithm using BM25 similarity
- `requirements.txt` - Python packages and versions required to run this project
- `src/` - Directory housing additional Python scripts
    - `utils.py` - Python helper functions
- `test/` - Directory housing tests
    - `test_utils.py` - Tests for functions in `utils.py`
