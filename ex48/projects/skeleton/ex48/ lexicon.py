#!/usr/bin/env python
#coding=utf-8

import re

def convert_number(s):
    try:
        return int(s)
    except ValueError:
        return None


def scan(input_str):

    words = input_str.split(' ')

    pattern = re.compile(r'\d+')

    
    direction_list = ['north', 'south', 'west', 'east', 'down', 'up', 'left', 'right', 'back']
    verb_list = ['go', 'kill', 'stop', 'eat']
    stop_list = ['the', 'in', 'of', 'from', 'at', 'it']
    noun_list = ['door', 'bear', 'princess', 'cabinet']
    sentence_list = []

    for word in words:
        
        bool = pattern.match(word)
        if bool:
            sentence = ('number', convert_number(word))
            sentence_list.append(sentence)
        
        elif word in direction_list:
            sentence = ('direction', word)
            sentence_list.append(sentence)
        
        
        elif word in verb_list:
            sentence = ('verb', word)
            sentence_list.append(sentence)

        elif word in stop_list:
            sentence = ('stop', word)
            sentence_list.append(sentence)

        elif word in noun_list:
            sentence = ('noun', word)
            sentence_list.append(sentence)
        
        else:
            sentence = ('error', word)
            sentence_list.append(sentence)
    
    return sentence_list
