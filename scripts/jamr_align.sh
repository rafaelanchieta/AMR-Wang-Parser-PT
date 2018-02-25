#!/bin/bash

#JAMR_HOME="/home/j/llc/cwang24/Tools/jamr"
JAMR_HOME="/home/rafael/Documentos/Doutorado/jamr-Semeval-2016"

#### Config ####
${JAMR_HOME}/scripts/config.sh

#### Align the tokenized amr file ####

echo "### Aligning $1 ###"
# input should be tokenized AMR file, which has :tok tag in the comments
${JAMR_HOME}/run Aligner -v 0 < $1 > $1.aligned