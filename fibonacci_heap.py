class Heap(object):
    """
    Une heap est une structure de données sous forme d'arbre.
    https://en.wikipedia.org/wiki/Heap_(data_structure)
    """

    def insert(self, value: int) -> None:
        """
        Ajoute une valeur dans l'arbre
        """
        pass

    def find_min(self) -> int:
        """
        Retourne la valeur minimum dans l'arbre
        """
        pass

    def delete_min(self) -> int:
        """
        Supprime et retourne la valeur minimum dans l'arbre
        """
        pass

    def decrease_key(self, current_value: int, new_value: int) -> None:
        """
        Modify une valeur dans l'arbre
        """
        pass

    def merge(self, fibonnaci_heap: object) -> None:
        """
        Fusionne deux arbres
        """
        pass


class Node:

    def __init__(self, value):
        self.value = value
        self.child = self.left = self.right = self.parent = None


class LinkedList:

    def __init__(self):
        self.tail = None
        self.head = None


class FibonacciHeap(Heap):
    """
    Une fibonnaci heap est un arbre permettant de stocker et trier des donnés efficacement
    https://en.wikipedia.org/wiki/Fibonacci_heap
    L'implémentation est décrite en anglais : https://en.wikipedia.org/wiki/Fibonacci_heap#Implementation_of_operations
    et en français : https://fr.wikipedia.org/wiki/Tas_de_Fibonacci#Implémentation_des_opérations
    """

    def __init__(self, min: Node = None):
        self.min = 1000000
        self.root_list = LinkedList() 
        
    def insert(self, value: int) -> None:
        """
        Ajoute une valeur dans l'arbre
        """
        node = Node(value)

        if self.min > node.value:
            self.min = node.value
            return

        if self.root_list.head == None:
            self.root_list.head = node
            node.left = None
            return

        if not self.root_list:
            node.left = self.root_list.tail
            self.root_list.tail.right = self.root_list.tail = self.min = node
            return

        pass

    def find_min(self) -> int:
        """
        Retourne la valeur minimum dans l'arbre
        """
        return self.min

    def delete_min(self) -> int:
        """
        Supprime et retourne la valeur minimum dans l'arbre
        """
        pass

    def merge(self, fibonnaci_heap: Heap) -> None:
        """
        Fusionne deux arbres
        """
        self.root_list.tail.right = fibonnaci_heap.root_list.head.left
        self.root_list.tail = fibonnaci_heap.root_list.tail
        #if self.min > fibonnaci_heap.min
        #   self.min = fibonnaci_heap.min
        
        pass 
    
#heap = FibonacciHeap(min)
#heap.insert(3)
#heap.insert(5)
#heap.insert(2)
#print(heap.min)
