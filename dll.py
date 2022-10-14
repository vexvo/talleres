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

    # 6. Remover nodo al inicio de la lista
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

    # 7. Remover nodo al final de la lista
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

    # 8. Remover nodo en una posicion dada de la lista
    def remove_node(self, index):
        if self.length > 0 and index < self.length:
            if index == 0:
                self.shift_node()
            elif index == self.length - 1:
                self.pop_node()
            else:
                remove_node = self.get_node(index)
                previous_node = self.get_node(index -1)
                previous_node.next = remove_node.next
                remove_node.next = None
                remove_node = self.tail
                self.tail = remove_node.previous
                self.tail.next = None
                remove_node.previous = None
                self.length -= 1
                return print(remove_node.value)
        else:
            print('Index fuera de rango')

    # 9. Método que retorna el nodo en la posición indicada de la lista
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

    # Método que retorna el valor del nodo en la posición indicada de la lista
    def get_node_value(self, index):
        node = self.get_node(index)
        if node != None: return node.value
        else: print('Index fuera de rango')

    # Método que settea el valor del nodo en la posición indicada de la lista
    def set_node_value(self, index, value):
        search_node = self.get_node(index)
        if search_node != None:
            search_node.value = value
        else:
            print('Index fuera de rango') 