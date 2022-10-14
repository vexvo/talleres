from re import search


class SingleLinkedList:

    ''' Creación de la clase anidada en SingleLinkedList '''
    class Node:
        def __init__(self, value):
            self.value = value
            self.next = None
    
    ''' Metodo inicializador de la clase SingleLinkesList '''
    def __init__(self):
        self.head = None
        self.tail = None
        self.length = 0

    ''' Método que imprime el contenido de la lista simplemente enlazada '''
    def print_values(self):
        print_sll = []
        current_node = self.head
        while current_node != None:
            print_sll.append(current_node.value)
            current_node = current_node.next
        print(f'Lista actual: {print_sll}\nCantidad de nodos: {self.length}')

    ''' Método que agrega un nodo nuevo al final de la lista '''
    def append(self, value):
        new_node = self.Node(value)
        if self.length == 0:
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            self.tail = new_node
        self.length += 1

    ''' Método que elimina el ultimo nodo de la lista '''
    def pop(self):
        if self.length == 1:
            self.head = None
            self.tail = None
        else:
            current_node = self.head
            for i in range(self.length - 2):
                current_node = current_node.next
            current_node.next = None
            self.tail = current_node
        self.length -= 1

    ''' Método que agrega un nodo nuevo al inicio de la lista '''
    def appbegin(self, value):
        new_node = self.Node(value)
        if self.length == 0:
            self.head = new_node
            self.tail = new_node
        else:
            new_node.next = self.head
            self.head = new_node
        self.length += 1
    
    ''' Método que elimina el primer nodo de la lista '''
    def shift(self):
        if self.length > 0:
            remove_node = self.head
            self.head = remove_node.next
            remove_node.next = None
            self.length -= 1

    ''' Método que elimina el nodo en la posición indicada de la lista'''
    def remove(self, index):
        if self.length > 0 and index < self.length:
            if index == 0:
                self.shift()
            elif index == self.length - 1:
                self.pop()
            else:
                remove_node = self.get_node(index)
                previous_node = self.get_node(index -1)
                previous_node.next = remove_node.next
                remove_node.next = None
        else:
            print('Index fuera de rango')

    ''' Método que retorna el nodo en la posición indicada de la lista'''
    def get_node(self, index):
        if index < 0 or index >= self.length:
            return None
        if index == self.length - 1:
            return self.tail
        
        current_node = self.head
        counter = 0
        while index != counter:
            current_node = current_node.next
            counter += 1
        return current_node

    ''' Método que retorna el valor del nodo en la posición indicada de la lista'''
    def get_node_value(self, index):
        node = self.get_node(index)
        if node != None: return node.value
        else: print('Index fuera de rango')

    ''' Método que settea el valor del nodo en la posición indicada de la lista'''
    def set_node_value(self, index, value):
        search_node = self.get_node(index)
        if search_node != None:
            search_node.value = value
        else:
            print('Index fuera de rango') 
            
    ''' Método que inserta un valor en la posición dada'''
    def insert(self, index, value):
        if self.length > 0 and index < self.length:
            if index == 0:
                self.appbegin(value)
            elif index == self.length:
                self.append(value)
            else:
                new_node = self.Node(value)
                new_node.next = self.get_node(index)
                previous_node = self.get_node(index - 1)
                previous_node.next =  new_node
                self.length += 1
        else:
           print('Index fuera de rango')

    ''' Método que hace que se invierta la lista'''
    def reverse(self):
        for i in range(0, self.length - 1):
            self.insert(i, self.tail.value)
            self.pop()