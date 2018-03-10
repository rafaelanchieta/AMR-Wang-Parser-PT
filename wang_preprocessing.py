# -*- coding: utf-8 -*-

import argparse
import os
import re
import string
import sys

from nltk import word_tokenize
from util import run_palavras,run_lxparser,run_corenlp,run_nlpnet

class W_Preprocessing(object):
    """
    Creates preprocessing files for CAMR Parser
    """

    def __init__(self, amr_file):
        self.name = os.path.abspath(amr_file)
        self.amr = open(amr_file, 'r')
        self.regex_snt = r'# ::snt (.+)'

    def create_token_sentence(self, train):
        print('Creating tokenized sentences')
        sentences_file = open(self.name + '.tok', 'w')
        for snt in self.amr.readlines():
            if train:
                match = re.match(self.regex_snt, snt)
                if match:
                    tr = str.maketrans("", "", string.punctuation)
                    s = match.group(1).translate(tr)
                    sentences_file.write(' '.join(word_tokenize(s)))
                    sentences_file.write('\n')
            else:
                tr = str.maketrans("", "", string.punctuation)
                s = snt.translate(tr)
                sentences_file.write(' '.join(word_tokenize(s)))
                sentences_file.write('\n')
        print('Done!!')
        sentences_file.close()

    def create_prp_sentence(self):
        print('Preprocessing sentences')
        sentence_file = open(self.name+'.tok', 'r')
        prp_file = open(self.name+'.prp', 'w')
        cont_line = 0
        prp_file.write('----------------------------------------')
        prp_file.write('\n')
        
        for line in sentence_file.readlines():
            size = 0
            prp_file.write(line)
            prp_file.write('\n')
            prp_file.write('Sentence #')
            prp_file.write(str(cont_line+1))
            prp_file.write(' (')
            prp_file.write(str(len(word_tokenize(line))))
            prp_file.write(' tokens):')
            prp_file.write('\n')
            prp_file.write(line)
            tags = run_nlpnet.call_nlpnet(line)
            for word, tag in tags:
                prp_file.write('[Text=')
                prp_file.write(word)
                prp_file.write(' CharacterOffsetBegin=')
                prp_file.write(str(size))
                prp_file.write(' CharacterOffsetEnd=')
                size += len(word)
                prp_file.write(str(size))
                prp_file.write(' PartOfSpeech=')
                prp_file.write(tag)
                lemma = run_palavras.call_palavras(word)
                print('Lemma: ', lemma)
                prp_file.write(' Lemma=')
                prp_file.write(lemma)
                prp_file.write(' NamedEntityTag=O]')
                prp_file.write('\n')
                size += 1
            prp_file.write('NLP> NLP> ----------------------------------------')
            prp_file.write('\n')
            cont_line += 1
        print('Done!!!')
        prp_file.close()

    def create_charniak(self):
        print('Charniak parser')
        tok_name = self.name+'.tok'
        #sentence_file = open(tok_name, 'r')
        charniak_file = open(tok_name+'.charniak.parse', 'w')
        constituents = run_lxparser.call_lxparser(tok_name)
        for c in constituents:
            charniak_file.write(c)
        print('Done')
        charniak_file.close()

    def create_charniak_dep(self):
        print('Dependency parser')
        tok_name = self.name + '.tok'
        sentence_file = open(tok_name, 'r')
        charniak_file = open(tok_name + '.charniak.parse.dep', 'a')
        for line in sentence_file.readlines():
            charniak_file.write(run_corenlp.call_corenlp(line))
        print('Done!!')
        charniak_file.close()

    def creat_tok(self):
        new_amr = open(self.name+'.amr.tok', 'w')
        flag = False
        for line in self.amr.readlines():
            match = re.match(self.regex_snt, line)
            new_amr.write(line)
            #new_amr.write('\n')
            if match:
                flag = True
            if flag:
                new_amr.write('# ::tok ')
                new_amr.write(match.group(1))
                new_amr.write('\n')
                flag = False

if __name__ == '__main__':
    argparser = argparse.ArgumentParser(description='Preprocessing CAMR')
    argparser.add_argument('-f', '--file', help='Input file', required=True)
    argparser.add_argument('-t', '--train', choices=['train'], help='Create files for training')
    try:
        args = argparser.parse_args()
    except:
        argparser.error('Invalid arguments')
        sys.exit()
    p = W_Preprocessing(args.file)

    train = False
    if args.mode == 'train':
        train = True


    #p = W_Preprocessing('files/dev.txt')
    p.create_token_sentence(train)
    p.create_prp_sentence()
    p.create_charniak()
    p.create_charniak_dep()
    if args.mode == 'train':
        p.creat_tok()