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

    # 8. Retorna un nodo necesario de la lista
    def get_node(self, index):
        if index < 0 or index > self.len-1:
            return
        current_node, counter = self.head, 0
        while counter < index:
            current_node = current_node.next 
            counter += 1
        return current_node

    # 9. Retorna el valor del nodo solicitado
    def get_node_value(self, index):
        if index < 0 or index > self.len-1:
            return
        current_node, counter = self.head, 0
        while counter < index:
            current_node = current_node.next
            counter += 1
        return current_node.data

    # 9. Cambia el valor del nodo solicitado 
    def set_node_value(self, value, index):
        if index > self.len-1 or index < 0:
            return
        if index == 0:
            self.head.data = value
        elif index == self.len-1:
            self.tail.data = value
        else:
            to_rep = self.get_node(index)
            to_rep.data = value

    # 10. Inserta un nodo con un valor dado en una posicion dada de la lista
    def insert_node(self, index, value):
        if index < 0 or index > self.len:
            return
        if index == 0:
            self.unshift_node(value)
        elif index == self.len:
            self.append_node(value)
        else:
            prev = self.get_node(index-1)
            next = prev.next
            new_node = self.Node(value)
            prev.next = new_node
            new_node.prev = prev
            new_node.next = next
            next.prev = new_node
            self.len += 1

    # 11. Elimina el nodo en la posición indicada de la lista
    def remove_node(self, index):
        if index < 0 or index > self.len-1:
            return
        if index == 0:
            self.remove_head()
        elif index == self.len-1:
            self.pop()
        else:
            temp = self.get_node(index)
            next = temp.next
            prev = temp.prev
            #Asignaciones de enlace
            prev.next = next
            next.prev = prev
            self.len -= 1

    # 12. Invierte la lista
    def reverse(self):
        arr = []
        if self.len <= 1:
            current_node = self.head
            if current_node != None:
                arr.append(round(current_node.data ** (1/2), 2))
            return
        for i in range(self.len):
            current_node = self.head
            arr.insert(0, round(current_node.data ** (1/2), 2))
            self.insert_node(self.len-i, current_node.data)
            self.remove_head()
        print(arr, self.len)

    # 13. saca el cuadrado del indice anterior al dado
    def cuadrado_anterior(self, index):
        if index == 0:
            self.selected_structure.head.data = 0
            return
        current_node, c = self.selected_structure.head, 0
        while c < index:
            current_node = current_node.next
            c += 1
        prev = current_node.prev
        current_node.data = prev.data ** 2

    # 14. Invierte la lista y le saca la raiz a cada una 
    def sqr_reverse(self):
        if self.len <= 1:
            current_node = self.head
            if current_node != None:
                current_node.data = round(current_node.data ** (1/2), 2)
            return
        for i in range(self.len):
            current_node = self.head
            current_node.data = round(current_node.data ** (1/2), 2)
            self.insert_node(self.len-i, current_node.data)
            self.remove_head()