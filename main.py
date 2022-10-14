from colorama import *
init()
from dll import DoubleLinkedList
from sll import SingleLinkedList

double_linked_list = DoubleLinkedList()
single_linked_list = SingleLinkedList()

program_active = True
while program_active:
    try:
        list_picked = input(Fore.CYAN + "Please pick a letter a-c depending on your choice:" + Fore.CYAN + "\n  What type of list will you work with?\n     " + Fore.RED + "a. " + Fore.WHITE + "Listas simplemente enlazada\n     " + Fore.RED + "b. " + Fore.WHITE + "Listas doblemente enlazadas\n     " + Fore.RED + "c. " + Fore.WHITE + "Salir (cancela la ejecución del programa)\n")
        
        if list_picked == 'a':
            while True:
                try:
                    choice_picked = input(Fore.GREEN + "What do you wish to do with the following SIMPLE LIST:\n        " + Fore.RED + "a. " + Fore.WHITE + "Añadir nodo\n        " + Fore.RED + "b. " + Fore.WHITE + "Eliminar nodo\n        " + Fore.RED + "c. " + Fore.WHITE + "Consultar valor contenido en el nodo\n        " + Fore.RED + "d. " + Fore.WHITE + "Modificar valor de nodo\n        " + Fore.RED + "e. " + Fore.WHITE + "Invertir toda la lista\n        " + Fore.RED + "f. " + Fore.WHITE + "Validación especial\n        " + Fore.RED + "g. " + Fore.WHITE + "Salir (cancela la ejecución del programa)\n")
                    if choice_picked == 'a':
                        # agregar nodo
                        s_add_node = int(input("           1. Al inicio\n           2. Al final\n           3. En una posición específica\n"))
                        s_value = int(input("Value of node:\n"))
                        if s_add_node == 1:
                            single_linked_list.appbegin(s_value)
                        if s_add_node == 2:
                            single_linked_list.append(s_value)
                        if s_add_node == 3:
                            s_value_pos = int(input("Position of the node:\n"))
                            single_linked_list.insert(s_value, s_value_pos)

                    elif choice_picked == 'b':
                        # eliminar nodo
                        s_delete_node = int(input("           1. Al inicio\n           2. Al final\n           3. En una posición específica\n"))
                        if s_delete_node == 1:
                            single_linked_list.shift()
                        if s_delete_node == 2:
                            single_linked_list.pop()
                        if s_delete_node == 3:
                            s_pos = int(input("Position of the node you wish to delete:\n"))
                            single_linked_list.remove(s_pos)

                    elif choice_picked == 'c':
                        # consultar valor nodo
                        single_linked_list.get_node_value()

                    elif choice_picked == 'd':
                        # modificar valor nodo
                        single_linked_list.set_node_value()

                    elif choice_picked == 'e':
                        # invertir toda la lista
                        single_linked_list.reverse()

                    elif choice_picked == 'f':
                        # validación especial
                        print("validate 6") # TO DO
                    
                    elif choice_picked == 'g':
                        # salir de programa
                        program_active = False
                        break
                    single_linked_list.print_values()
                except:
                    print("Expected a numerical value")
        if list_picked == 'b':
            while True:
                try:
                    d_choice_picked = input(Fore.GREEN + "What do you wish to do with the following SIMPLE LIST:\n        " + Fore.RED + "a. " + Fore.WHITE + "Añadir nodo\n        " + Fore.RED + "b. " + Fore.WHITE + "Eliminar nodo\n        " + Fore.RED + "c. " + Fore.WHITE + "Consultar valor contenido en el nodo\n        " + Fore.RED + "d. " + Fore.WHITE + "Modificar valor de nodo\n        " + Fore.RED + "e. " + Fore.WHITE + "Invertir toda la lista\n        " + Fore.RED + "f. " + Fore.WHITE + "Validación especial\n        " + Fore.RED + "g. " + Fore.WHITE + "Salir (cancela la ejecución del programa)\n")
                    if d_choice_picked == 'a':
                        # agregar nodo
                        d_add_node = int(input("           1. Al inicio\n           2. Al final\n           3. En una posición específica\n"))
                        d_value = int(input("Value of node:\n"))
                        if d_add_node == 1:
                            double_linked_list.unshift_node(d_value)
                        if d_add_node == 2:
                            double_linked_list.append_node(d_value)
                        if d_add_node == 3:
                            d_value_pos = int(input("Position of the node:\n"))
                            #insert node in position # TO DO

                    elif d_choice_picked == 'b':
                        # eliminar nodo
                        d_delete_node = int(input("           1. Al inicio\n           2. Al final\n           3. En una posición específica\n"))
                        if d_delete_node == 1:
                            double_linked_list.shift_node()
                        if d_delete_node == 2:
                            double_linked_list.pop_node()
                        if d_delete_node == 3:
                            d_pos = int(input("Position of the node you wish to delete:\n"))
                            # delete node in position # TO DO

                    elif d_choice_picked == 'c':
                        # consultar valor nodo
                        double_linked_list.get_node_value() # TO DO

                    elif d_choice_picked == 'd':
                        # modificar valor nodo
                        double_linked_list.set_node_value() # TO DO

                    elif d_choice_picked == 'e':
                        # invertir toda la lista
                        double_linked_list.reverse() # TO DO

                    elif d_choice_picked == 'f':
                        # validación especial 
                        print("validate 5 & 6") # TO DO
                    
                    elif d_choice_picked == 'g':
                        # salir de programa
                        program_active = False
                        break
                    double_linked_list.print_list()
                except:
                    print("Expected a numerical value")
        if list_picked == 'c':
            program_active = False
            break
        break
    except:
        print("expected a letter either a, b or c")