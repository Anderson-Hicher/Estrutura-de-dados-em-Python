#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Mar  4 15:13:58 2020

@author: andersonhicher
"""

'''
Desenvolvimento de fila (Queue) para estudos 
de estruturas de dados em liguagem python
'''
class Queue:
    '''
    Criação da classe Queue e seu construtor.
    '''
    def __init__(self):
        self.__queue = []
        self.__len_queue = 0
    
    def push_queue(self, item):
        '''
        Método push da classe queue
        Adiciona o item da fila e depois incrementa 
        o valor de comprimento da mesma.
        '''
        self.__queue.append(item)
        self.__len_queue +=1
    
    def use_item_from_queue(self):
        '''
        Retorna o item da fila e depois remove 
        a mesma da fila.
        '''
        if self.empty_queue() is True:
            '''
            Verifica se a fila está vazia 
            ou não antes de executar o 
            retorno e a remoção do primiro item da fila.
            Caso a fila esteja vazia, printa na tela que a
            mesma encontra-se vazia.
            '''
            item = self.__queue[0]
            self.__queue.pop(0)
            self.__len_queue -= 1
            return item
        return print('A fila está vazia!!')
    
    def pop_queue(self):
        '''
        Metodo pop da classe queue 
        deleta/remove o primeiro item
        da fila sem retornar o valor excluido.
        '''
        if self.empty_queue() is True:
            '''
            Verifica se a fila está vazia 
            ou não antes de executar a remoção 
            do primiro item da fila.
            Caso a fila esteja vazia, printa na tela que a
            mesma encontra-se vazia.
            '''
            self.__queue.pop(0)
            self.__len_queue -= 1
            return print('Item excluido com sucesso!!')
        return print('A fila está vazia!!')

    
    def empty_queue(self):
        '''
        Método para verificar se a fila está vazia ou não,
        caso esteja retorna um False, senão retorna um True
        '''
        if self.__len_queue == 0:
            return False
        return True
    
    def front_queue(self):
        '''
        Retorna o primeiro item da fila, ou seja, 
        retorna o próximo item da fila que será removido.
        '''
        return self.__queue[0]
    
    def size_queue(self):
        '''
        Retorna o comprimento da fila.
        '''
        return self.__len_queue
    
    
    
'''
Inicio dos testes da Estrutura de 
dados do tipo FIFO 'Fila' (Queue):
'''

#Isntanciando a Estrutura de Dados
fila = Queue()
#Adicionando ítens à fila
fila.push_queue('João')
fila.push_queue('José')
fila.push_queue('Maria')
#Verificando tamanho da fila
print('O tamanho da fila é: %d' % fila.size_queue())
#Retornando primeiro item da fila
print('O primeiro item da fila é: %s' % fila.front_queue())
#Deletando Item da fila
fila.pop_queue()
#Verificando tamanho da fila
print('O tamanho da fila é: %d' % fila.size_queue())
#Retornando primeiro item da fila
print('O primeiro item da fila é: %s' % fila.front_queue())
#Verificando tamanho da fila
print('O tamanho da fila é: %d' % fila.size_queue())
#Utilizando o primeiro item da fila
print('Utilizando o primeiro item da fila: %s' % fila.use_item_from_queue())
#Verificando tamanho da fila
print('O tamanho da fila é: %d' % fila.size_queue())
#Retornando primeiro item da fila
print('O primeiro item da fila é: %s' % fila.front_queue())    