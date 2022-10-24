from array import array
from locale import currency


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
        print(f'Lista actual: {array_dll}\nCantidad de nodos: {self.length}')

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
            self.head = new_node
            self.tail = new_node
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

    # 8. Retorna un nodo necesario de la lista
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

    # 9. Retorna el valor del nodo solicitado
    def get_node_value(self, index):
        node = self.get_node(index)
        if node != None: return node.value
        else: print('Index fuera de rango')

    # 9. Cambia el valor del nodo solicitado 
    def set_node_value(self, index, value):
        search_node = self.get_node(index)
        if search_node != None:
            search_node.value = value
        else:
            print('Index fuera de rango')

    ### video functions


    # 10. Inserta un nodo con un valor dado en una posicion dada de la lista
    # video
    def insert_node(self, index, value):
        if index < 0 or index > self.length:
            return
        if index == 0:
            self.unshift_node(value)
        elif index == self.length:
            self.append_node(value)
        else:
            prev = self.get_node(index-1)
            next = prev.next
            new_node = self.Node(value)
            prev.next = new_node
            new_node.prev = prev
            new_node.next = next
            next.prev = new_node
            self.length += 1

    # 11. Elimina el nodo en la posición indicada de la lista
    # video
    def remove_node(self, index):
        if index < 0 or index > self.length-1:
            return
        if index == 0:
            self.shift_node()
        elif index == self.length-1:
            self.pop_node()
        else:
            temp = self.get_node(index)
            next = temp.next
            prev = temp.prev
            #Asignaciones de enlace
            prev.next = next
            next.prev = prev
            self.length -= 1

    # 12. Invierte la lista
    # video
    def reverse(self):
        if self.length <= 1:
            return
        for i in range(self.length):
            current = self.head
            self.insert_node(self.length-i, current.value)
            self.shift_node()

    # 13. revisa se un valor esta repetido en la lista
    # video
    def repeated_value(self, value):
        current = self.head
        flag = False
        while current != None:
            if current.value == value:
                flag = True
                return flag
            current = current.next
        return flag

    # 14. saca el cuadrado del indice anterior al dado
    # video
    def cuadrado_anterior(self, index):
        if index == 0:
            self.head.value = 0
            return
        current_node, c = self.head, 0
        while c < index:
            current_node = current_node.next
            c += 1
        prev = self.get_node(index-1)
        current_node.value = prev.value ** 2
        return current_node.value

    # 15. Invierte la lista y le saca la raiz a cada una 
    # video
    def sqr_reverse(self):
        if self.length <= 1:
            current_node = self.head
            if current_node != None:
                current_node.value = round(current_node.value ** (1/2), 2)
            return
        for i in range(self.length):
            current_node = self.head
            current_node.value = round(current_node.value ** (1/2), 2)
            self.append_node(current_node.value)
            self.shift_node()
        self.reverse()