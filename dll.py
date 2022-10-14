from array import array


class DoubleLinkedList:
    
    class Node:
        # 1. Creamos el metodo inicializador de la clase
        def __init__(self, value):
            self.value = value
            self.next = None
            self.previous = None

    # 2. Creamos el metodo inicializador de la clase DoubleLinkedList
    def __init__(self):
        self.head = None
        self.tail = None
        self.length = 0

    # 3. Metodo que nos permita imprimir la lista
    def print_list(self):
        # array vacio que recibe el valor de cada nodo y lo almacena
        array_dll = []
        current_node = self.head
        while current_node is not None:
            array_dll.append(current_node.value)
            current_node = current_node.next
        return array_dll

    # 4. Insertamos un nodo al inicio de la lista 
    def unshift_node(self, value):
        new_node = self.Node(value)
        # validar si la lista esta vacía 
        if self.head == None and self.tail == None:
            self.head = new_node
            self.tail = new_node
        else:
            # el puntero previous va de derecha a izquierda
            self.head.previous = new_node
            # el puntero next va de izquierda a derecha
            new_node.next = self.head
            self.head = new_node
        self.length += 1
    
    # 5. Añadir nodo al final de la lista
    def append_node(self, value):
        new_node = self.Node(value)
        # validar si la lista esta vacia
        if self.head == None and self.tail == None:
            self.head = None
            self.tail = None
        else:
            self.tail.next = new_node
            new_node.previous = self.tail
            self.tail = new_node
        self.length += 1

    def shift_node(self):
        if self.length == 0:
            self.head = None
            self.tail = None
        elif self.head != None:
            remove_node = self.head
            self.head = remove_node.next
            remove_node.next = None
            self.length -= 1
            return print(remove_node.value)

    def pop_node(self):
        if self.length == 0:
            self.head = 0
            self.tail = 0
        else:
            remove_node = self.tail
            self.tail = remove_node.previous
            self.tail.next = None
            remove_node.previous = None
            self.length -= 1
            return print(remove_node.value)