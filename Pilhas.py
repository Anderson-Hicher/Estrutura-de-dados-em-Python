#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Feb 25 23:04:41 2020

@author: andersonhicher
"""

class Stack:                                #Cria o objeto pilha
    def __init__(self):
        self.__stack = []                   #Mantemos a pilha encapsulada para evitar acessos indevidos a pilha
        self.__len_stack = 0                #Criamos uma variável para manter armazenado o tamanho da pilha
    
    def push(self, e):                      #Implementação do método push para adicionar itens à pilha
        self.__stack.append(e)
        self.__len_stack += 1
    
    def pop(self):                          #Implementação do método pop, para realizar a remoção de itens da pilha
        if not self.empty():                #Verifica se a pilha está vazia antes de realizar a remoção
            self.__stack.pop(self.__len_stack -1)
            self.__len_stack -=1
    
    def top(self):                          #Retorna o valor presente no topo da pilha
        if not self.empty():
            return self.__stack[-1]
        return None
    
    def empty(self):                        #método para verificar se a pilha está vazia
        if (self.__len_stack == 0):
            return True
        return False
        
    def lengh(self):
        return self.__len_stack             #Metodo para verificar o comprimento da pilha
    
    
s=Stack()                                   #Instanciando objeto Stack de nome 's'
s.push(3)                                   #Inserindo item a pilha
s.push(5)                                   #Inserindo item a pilha
s.push(2)                                   #Inserindo item a pilha
print(s.top())                              #Verificando item no topo da pilha
s.pop()                                     #Removendo item a pilha
print(s.top())                              #Verificando item no topo da pilha
