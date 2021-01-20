# Pygiator

## Overview

In the course "Scripting Languages" we have to develop a plagiarism scanner for python scripts.
It must be developed in python and ultimately be available as a desktop or web application.
A logo is also required and the turtle module should be use for this.

## Requirements and Installation

To run **Pygiator** [Python 3.8](https://www.python.org/) or higher must be installed.
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

In progress.
