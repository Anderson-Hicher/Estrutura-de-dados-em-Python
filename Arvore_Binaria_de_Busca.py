"""Arvore Binária de Busca"""
'''
@author: andersonhicher
@email: hicherhp6@gmail.com
@date: 16-07-2020
@version: 0.1.0
'''
class Node:

    def __init__(self, label):
        self.label = label
        self.left = None
        self.right = None

    def getLabel(self):
        return self.label

    def setLabel(self, label):
        self.label = label

    def getLeft(self):
        return self.left

    def setLeft(self, left):
        self.left = left

    def getRight(self):
        return self.right

    def setRight(self, right):
        self.right = right


class BinarySearchTree:

    def __init__(self):
        self.root = None

    def insert(self, label):

        # Cria um novo nó.
        node = Node(label)

        # Se for o primeiro item da arvori binária, será inserido na
        # raiz da arvore binária.
        if self.empty():
            self.root = node

        # Se não for o primeiro item da arvore binária, para adicionar
        # um item devemos percorre-la.
        else:
            dad_node = None
            curr_node = self.root

            while True:

                if curr_node is not None:

                    dad_node = curr_node

                    # Verifica se vai para a esquerda ou a direita
                    if node.getLabel() == curr_node.getLabel():
                        break
                    elif node.getLabel() < curr_node.getLabel():
                        # Vai para a esquerda.
                        curr_node = curr_node.getLeft()
                    else:
                        # Vai para a direita.
                        curr_node = curr_node.getRight()

                else:

                    # Se o curr_node for igual a None eu ja posso
                    # inserir o node em seu local.

                    if node.getLabel() < dad_node.getLabel():
                        dad_node.setLeft(node)
                    else:
                        dad_node.setRight(node)
                    break
    def empty(self):
        if self.root is None:
            return True
        return False

    # Mostra em pré-ordem (raiz-esq-dir)
    def show(self, curr_node):

        if curr_node is not None:
            print("{}".format(curr_node.getLabel()), end=' ')
            self.show(curr_node.getLeft())
            self.show(curr_node.getRight())
    def getRoot(self):
        return self.root

t = BinarySearchTree()
t.insert(8)
t.insert(3)
t.insert(1)
t.insert(6)
t.insert(4)
t.insert(7)
t.insert(10)
t.insert(6)
t.insert(14)
t.insert(13)
t.show(t.getRoot())
