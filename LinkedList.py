"""Lista ligada."""
'''
@author: andersonhicher
@email: hicherhp6@gmail.com
@date: 16-07-2020
'''


class Node:
    """Abstração da classe nó."""

    def __init__(self, label):
        """Construtor da classe Node.

        Atributos
        ----------
        label:
            Recebe o item a ser mantido.
        next:
            Recebe o link para o próximo nó.

        Métodos
        ----------
        getLabel:
            Retorna o conteúdo de label.
        setLabel:
            Insere o conteúdo de label.
        getNext:
            Retorna o link do próximo nó.
        setNext:
            Insere um link para o próximo nó
        """
        self.label = label
        self.next = None

    def getLabel(self):
        """Captura label.

        Retorna o conteúdo de label.

        Parametros
        ----------
        Este método não recebe parâmetros.

        Retorno
        ----------
        label : object
        """
        return self.label

    def setLabel(self, label):
        """Altera label.

        Altera o conteúdo de label.

        Parametros
        ----------
        label : object

        Retorno
        ----------
        Este método não tem retorno.
        """
        self.label = label

    def getNext(self):
        """Captura next.

        Retorna o conteúdo de next.

        Parametros
        ----------
        Este método não recebe parâmetros.

        Retorno
        ----------
        next : object
        """
        return self.next

    def setNext(self, next):
        """Altera next.

        Altera o conteúdo de next.

        Parametros
        ----------
        next : object

        Retorno
        ----------
        Este método não tem retorno.
        """
        self.next = next


class LinkedList:
    """Abstração da classe Lista Ligada."""

    def __init__(self):
        """Construtor da classe LinkedList.

        Atributos
        ----------
        first:
            Armazena informações do primeiro itém da lista.
        last:
            Armazena informações do ultimo item da lista.
        len_list:
            Armazena o comprimento da lista.

        Métodos
        ----------
        push:
            Insere um item na lista por meio de um index.
        pop:
            Remove um item da lista por meio de um index.
        empty:
            Verifica e retorna se a lista contém algúm item.
        length:
            Retorna o comprimento atual da lista
        show:
            Imprime o conteúdo de lista.
        """
        self.first = None
        self.last = None
        self.len_list = 0

    def push(self, label, index):
        """Insere na lista.

        Insere o conteúdo em lista posicionando-o no local
        determinado pelo index.

        Parametros
        ----------
        label : object
        index : integer

        Retorno
        ----------
        Este método não tem retorno.
        """
        if index >= 0:

            # Cria o novo nó
            node = Node(label)

            # Verifica se a lista está vazia
            if self.empty():
                self.first = node
                self.last = node
            else:

                if index == 0:
                    # Inserção no inicio
                    node.setNext(self.first)
                    self.first = node

                elif index >= self.len_list:
                    # Inserção no final
                    self.last.setNext(node)
                    self.last = node

                else:
                    # Inserção no meio:
                    prev_node = self.first
                    curr_node = self.first.getNext()
                    curr_index = 1

                    # Percorremos a lista e buscamos o index do nó
                    while curr_index is not None:

                        if curr_index == index:
                            # Setamos o curr_node como o próximo do nó
                            node.setNext(curr_node)
                            # Seta o node atual como o próximo do prev_node
                            prev_node.setNext(node)
                            break
                        prev_node = curr_node
                        curr_node = curr_node.getNext()
                        curr_index += 1
                    # Atualiza o tamanho da lista
            self.len_list += 1

    def pop(self, index):
        """Remove da lista.

        Remove o conteúdo de lista referênciado pelo index.

        Parametros
        ----------
        index : integer

        Retorno
        ----------
        Este método não tem retorno.
        """
        if not self.empty() and index >= 0 and index < self.len_list:

            flag_remove = False

            # Verifica se a lista possui apenas um elemento
            if self.first.getNext() is None:
                # Possui apenas um elemento,
                # portanto removemos este elemento
                self.first = None
                self.last = None
                flag_remove = True

            # A lista possui mais de um elemento mas o index
            # pertence ao primeiro elemento da lista:
            elif index == 0:
                self.first = self.first.getNext()
                flag_remove = True

            # Se o index a ser removido não for o primeiro
            # index da lista, percorremos a lista em busca do
            # index desejado.
            else:

                prev_node = self.first
                curr_node = self.first.getNext()
                curr_index = 1

                # Percorrendo a lista
                while curr_node is not None:

                    # Verificamos se o index buscado é igual ao
                    # index encontrado
                    if curr_index == index:
                        # Remove o node atual da lista
                        prev_node.setNext(curr_node.getNext())
                        curr_node.setNext(None)
                        flag_remove = True
                        break

                    prev_node = curr_node
                    curr_node = curr_node.getNext()
                    curr_index += 1

            if flag_remove:
                # Atualiza o tamanho da lista
                self.len_list -= 1

    def empty(self):
        """Verifica conteúdo.

        Verifica se há conteúdo em lista.

        Parametros
        ----------
        Este método não tem parâmetros

        Retorno
        ----------
        boolean
            Se há conteúdo em lista retornará False
            senão retornará True.
        """
        if self.first is None:
            return True
        return False

    def length(self):
        """Comprimento da lista.

        Retorna o comprimento da lista.

        Parametros
        ----------
        Este método não tem parâmetros

        Retorno
        ----------
        len_list : integer
        """
        return self.len_list

    def show(self):
        """Imprime lista.

        Imprime o conteúdo de lista na tela por meio do
        print.

        Parametros
        ----------
        Este método não tem parâmetros

        Retorno
        ----------
        Este método não tem retorno.
        """
        curr_node = self.first

        while curr_node is not None:
            print(curr_node.getLabel(), end=' ')
            curr_node = curr_node.getNext()
        print(' ')


lista = LinkedList()

# teste de inserção
lista.push('Anderson', 0)
lista.push('Junior', 1)
lista.show()
lista.push('Ptolomeu', 2)
lista.show()
lista.push('Yankee', 0)
lista.show()
lista.push('Catarina', 2)
lista.show()
lista.push('lilica', 4)
lista.show()
print('Tamanho da lista: {}'.format(lista.length()))

# Teste de remoção

lista.pop(0)
lista.show()
lista.pop(3)
lista.show()
print('Tamanho da lista: {}'.format(lista.length()))
