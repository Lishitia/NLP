# NLP
# README for Edit Distance Calculation Scripts

This README document provides details on four Python scripts (`Q1.py`, `Q2.py`, `Q3.py`, `Q4.py`) each designed to solve specific problems related to string and sentence comparison using the concept of edit distance. Each script is tailored to handle different input formats and comparison levels (character or word).

## Q1.py: String Edit Distance

### Purpose
This script calculates the edit distance between two strings using a dynamic programming approach. The output includes the minimum cost of transforming one string into another and a possible alignment showing the edits.

### Input
Two strings directly provided to the function.

### Output
The minimum edit cost and a visual representation of the alignment between the two strings.

## Q2.py: Sentence Edit Distance

### Purpose
Extends `Q1.py` to handle sentences, comparing them on a word-by-word basis rather than character-by-character.

### Input
Two sentences directly provided to the function.

### Output
The minimum edit cost and a visual representation of the alignment between the two sentences.

## Q3.py: Batch Mode Word Edit Distance

### Purpose
This script computes the edit distances between pairs of words provided in a batch mode via an input file, storing the results in an output file.

### Input File
`word_corpus.txt` (Each row contains a word and a symbol 'R' or 'H', indicating a Reference or Hypothesis.)

### Output File
`word_edit_distance.txt` (Contains the reference, hypothesis, and their respective edit distance.)
## Q4.py: Batch Mode Sentence Edit Distance

### Purpose
Similar to `Q3.py` but adapted for sentences, this script calculates edit distances for pairs of sentences stored in an input file and outputs the results to a specified file.

### Input File
`sentence_corpus.txt` (Each row contains a sentence and a symbol 'R' or 'H', indicating a Reference or Hypothesis.)

### Output File
`sentence_edit_distance.txt` (Contains the reference, hypothesis, and their respective edit distance, assuming a constant number of hypotheses per reference.)

## Usage

To execute any of these scripts, ensure Python is installed on your machine and run the script corresponding to your task. For example, to run `Q1.py`, use:

```bash
python Q1.py
