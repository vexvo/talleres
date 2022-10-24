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
                    choice_picked = input(Fore.GREEN + "What do you wish to do with the following SIMPLE LIST:\n        " + Fore.RED + "a. " + Fore.WHITE + "Añadir nodo\n        " + Fore.RED + "b. " + Fore.WHITE + "Eliminar nodo\n        " + Fore.RED + "c. " + Fore.WHITE + "Consultar valor contenido en el nodo\n        " + Fore.RED + "d. " + Fore.WHITE + "Modificar valor de nodo\n        " + Fore.RED + "e. " + Fore.WHITE + "Invertir toda la lista\n        " + Fore.RED + "f. " + Fore.WHITE + "[Validación Especial 2] Modificar valor al invertir y raiz cuadrada de cada nodo\n        " + Fore.RED + "g. " + Fore.WHITE + "Salir (cancela la ejecución del programa)\n")
                    if choice_picked == 'a':
                        # agregar nodo
                        s_value = int(input("Value of node:\n"))
                        if single_linked_list.repeated_value(s_value):
                                print(Fore.RED + 'This value is already in the list,')
                        else:
                            s_add_node = int(input("           1. Al inicio\n           2. Al final\n           3. En una posición específica\n"))
                            if s_add_node == 1:
                                single_linked_list.appbegin(s_value)
                            elif s_add_node == 2:
                                single_linked_list.append(s_value)
                            elif s_add_node == 3:
                                s_value_pos = int(input("Position of the node:\n"))
                                single_linked_list.insert(s_value_pos, s_value)

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
                        s_pos_v = int(input("Position of the node who's value you wish to get:\n"))
                        print(single_linked_list.get_node_value(s_pos_v))

                    elif choice_picked == 'd':
                        # modificar valor nodo
                        s_pos_s = int(input("Position of the node who's value you wish to set:\n"))
                        s_pos_sv = int(input("Value you wish to set to this node:\n"))
                        single_linked_list.set_node_value(s_pos_s, s_pos_sv)

                    elif choice_picked == 'e':
                        # invertir toda la lista
                        single_linked_list.reverse()

                    elif choice_picked == 'f':
                        # validación especial - 6 - modificar para que se invierta la lista y cada uno de los nodos se les saque la raiz
                        single_linked_list.sqr_reverse()
                    
                    elif choice_picked == 'g':
                        # salir de programa
                        program_active = False
                        break
                    print(Fore.YELLOW)
                    single_linked_list.print_values()
                    print("\n")
                except:
                    print("Expected a numerical value")
        if list_picked == 'b':
            while True:
                try:
                    d_choice_picked = input(Fore.GREEN + "What do you wish to do with the following DOUBLE LIST:\n        " + Fore.RED + "a. " + Fore.WHITE + "Añadir nodo\n        " + Fore.RED + "b. " + Fore.WHITE + "Eliminar nodo\n        " + Fore.RED + "c. " + Fore.WHITE + "Consultar valor contenido en el nodo\n        " + Fore.RED + "d. " + Fore.WHITE + "Modificar valor de nodo\n        " + Fore.RED + "e. " + Fore.WHITE + "Invertir toda la lista\n        " + Fore.RED + "f. " + Fore.WHITE + "[Validación Especial 1] Modificar valor al cuadrado del anterior\n        " + Fore.RED + "g. " + Fore.WHITE + "[Validación Especial 2] Modificar valor al invertir y raiz cuadrada de cada nodo\n        " + Fore.RED + "h. " + Fore.WHITE + "Salir (cancela la ejecución del programa)\n")
                    if d_choice_picked == 'a':
                        # agregar nodo
                        d_value = int(input("Value of node:\n"))
                        if double_linked_list.repeated_value(d_value):
                                print(Fore.RED + 'This value is already in the list,')
                        else:
                            d_add_node = int(input("           1. Al inicio\n           2. Al final\n           3. En una posición específica\n"))
                            if d_add_node == 1:
                                double_linked_list.unshift_node(d_value)
                            elif d_add_node == 2:
                                double_linked_list.append_node(d_value)
                            elif d_add_node == 3:
                                d_value_pos = int(input("Position of the node:\n"))
                                double_linked_list.insert_node(d_value_pos, d_value)

                    elif d_choice_picked == 'b':
                        # eliminar nodo
                        d_delete_node = int(input("           1. Al inicio\n           2. Al final\n           3. En una posición específica\n"))
                        if d_delete_node == 1:
                            double_linked_list.shift_node()
                        if d_delete_node == 2:
                            double_linked_list.pop_node()
                        if d_delete_node == 3:
                            d_pos = int(input("Position of the node you wish to delete:\n"))
                            double_linked_list.remove_node(d_pos)

                    elif d_choice_picked == 'c':
                        # consultar valor nodo
                        d_pos_v = int(input("Position of the node who's value you wish to get:\n"))
                        print(double_linked_list.get_node_value(d_pos_v))

                    elif d_choice_picked == 'd':
                        # modificar valor nodo
                        d_pos_s = int(input("Position of the node who's value you wish to set:\n"))
                        d_pos_sv = int(input("Value you wish to set to this node:\n"))
                        double_linked_list.set_node_value(d_pos_s, d_pos_sv)

                    elif d_choice_picked == 'e':
                        # invertir toda la lista
                        double_linked_list.reverse()

                    elif d_choice_picked == 'f':
                        # validación especial - 5 - modificar para que nodo sea el cuadrado del anterior
                        double_linked_list.print_list()
                        d_index = int(input("Index of the position of the node you wish to modify\n"))
                        cuad_ant = double_linked_list.cuadrado_anterior(d_index)
                        double_linked_list.set_node_value(d_index, cuad_ant)                        
                        
                    elif d_choice_picked == 'g':
                        # validación especial - 6 - modificar para que se invierta la lista y cada uno de los nodos se les saque la raiz
                        double_linked_list.sqr_reverse()

                    elif d_choice_picked == 'h':
                        # salir de programa
                        program_active = False
                        break
                    print(Fore.YELLOW)
                    double_linked_list.print_list()
                    print("\n")
                except:
                    print("Expected a numerical value")
        if list_picked == 'c':
            program_active = False
            break
        break
    except:
        print("expected a letter either a, b or c")

