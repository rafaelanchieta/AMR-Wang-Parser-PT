#!/bin/bash

wget http://143.107.183.175:23580/models/model.zip
unzip model.zip
rm -f model.zip

wget http://143.107.183.175:23580/models/model_nlpnet.zip
unzip model_nlpnet.zip
rm -f model_nlpnet.zip

wget http://143.107.183.175:23580/models/model-pt/model-pt.m

wget http://143.107.183.175:23580/models/bllip-parser.zip
unzip bllip-parser.zip
rm -f bllip-parser.zip

wget http://143.107.183.175:23580/models/stanfordnlp.zip
unzip stanfordnlp.zip
rm -f stanfordnlp.zip

wget http://143.107.183.175:23580/models/stanford-corenlp-full-2017-06-09.zip
unzip stanford-corenlp-full-2017-06-09.zip
rm -f stanford-corenlp-full-2017-06-09.zip

wget http://143.107.183.175:23580/models/stanford-parser-2010-11-30.zip
unzip stanford-parser-2010-11-30.zip
rm -f stanford-parser-2010-11-30.zip