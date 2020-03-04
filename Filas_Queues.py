#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Mar  4 15:13:58 2020

@author: andersonhicher
"""

'''
Desenvolvimento de fila (Queue) para estudos de estruturas de dados em liguagem python
'''
class Queue:
    '''
    Criação da classe Queue e seu construtor
    '''
    def __init__(self):
        self.__queue = []
        self.__len_queue = 0
    
    def push_queue(self, item):
        '''
        método push da classe queue
        '''
        self.__queue.append(item)
        self.__len_queue +=1
    
    def pop_queue(self):
        item = self.__queue[0]
        self.__queue.remove(0)
        self.__len_queue -= 1
        return item
    
    
    