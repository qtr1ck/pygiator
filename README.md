# Pygiator

[![Streamlit App](https://static.streamlit.io/badges/streamlit_badge_black_white.svg)](https://share.streamlit.io/qtr1ck/pygiator/main)

## Overview

In the course "Scripting Languages" we have to develop a plagiarism finder for python scripts.
It must be developed in python and ultimately be available as a desktop or web application.
A logo is also required and the turtle module should be used for this.

## Requirements and Installation

To run **Pygiator** [Python 3.8 or higher](https://www.python.org/) must be installed.
Use the requirements.txt file to install the required modules.

```bash
pip install -r requirements.txt
```

## Run Pygiator

Open a CLI of your choice, go into the directory where the *streamlit_app.py* file is located and type:

```bash
streamlit run streamlit_app.py
```

A new tab will open in your default browser and the **Pygiator** application should be available there.

## Usage

### Select Files

When the app is running you can select two python files in the sidebar. The first file is usually the file to be checked and the second file the comparison file. As soon as you have selected both files, the result will be calculated and displayed.

### Result Visualization

In addition to the numerical result, a visual result is also displayed as a heatmap. On the left side you can see the blocks of the first file and on the right the blocks of the second file. In the sidebar you can find a slider where the similarity threshold can be changed, lines that are more similar are colored red.

### Swap Files

The selected files can be swapped at anytime by clicking the checkbox in the top left.
  

## Winnowing Similarity

As a second method to calculate the similarity of two python scripts the winnowing algorithm is available as well. Winnowing is using Hashing in combination with a Sliding-window to produce a fingerprint for each document. The similarity score is calculated using the [Jaccard similarity coefficient](https://en.wikipedia.org/wiki/Jaccard_index).  
  
In difference to our other calculation method, Winnowing is not able to deliver details about single Blocks, but only gives you a single result for similarity.  

For our implementation we made use of the paper [Winnowing: local algorithms for document fingerprinting](https://theory.stanford.edu/~aiken/publications/papers/sigmod03.pdf).
