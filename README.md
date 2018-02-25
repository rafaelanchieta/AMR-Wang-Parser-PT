# CAMR Parser adapted to Portuguese

CARM is a transition-based, tree-to-graph parser for the Abstract Meaning Representation of a sentence.
For more details, visit https://github.com/c-amr/camr

## Trained Models

To download the trained models, run the following script
```
./download.sh
```

## Dependencies
- PALAVRAS Parser (http://visl.sdu.dk/constraint_grammar.html)
- NLTK (http://www.nltk.org/)

## Parsing with Pre-Trained Model (Little Prince)

The input data format for parsing should be raw document with one sentence per line.

First, run preprocessing
```
python3 wang_preprocessing.py -f <input_sentence_file>
```
This will give you the tokenized sentences (.tok), POS tag and name entity (.prp), and dependency structure (.charniak.parse.dep)

Then, run the parser

```
python amr_parsing.py -m parse --model <model_file> <input_sentence_file> 2>log/error.log
```
This will give you the parsed AMR file (.parsed) in the same directory as your input sentence file.
