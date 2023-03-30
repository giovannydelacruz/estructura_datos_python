from node import Node

class SinglyLinkedList:
    def __init__(self):
        self.tail = None # tail es el primer objeto ingresado, que termina quedando en la cola
        self.size = 0

    def append(self, data):
        node = Node(data)
        if self.tail == None: # Puede ser que no tengamos nodos
            self.tail = node
        else: # o puede ser que tengamos.
            current = self.tail

            while current.next:
                current = current.next
            current.next = node
        
        self.size +=1
    
    def size(self):
        return str(self.size)
    
    def iter(self):
        current = self.tail
        while current:
            value = current.data
            current = current.next
            yield value # Yield genera valores y los podemos utilizar pero no son necesarios guardar.
        
    def delete(self, data):
        current = self.tail
        previous = self.tail

        while current:
            if current.data == data:
                if current == self.tail:
                    self.tail = current.next
                else:
                    previous.next = current.next
                    self.size -=1
                    return current.data
            previous = current
            current = current.next
        
    def search(self, data):
        for node in self.iter():
            if data == node:
                print(f"Data {data} found!")

    def clear(self):
        self.tail = None
        self.head = None
        self.size = 0

# from linked_list import SinglyLinkedList

# while current:
#     print(current.data)
#     current = current.next

# from array import Array
# arreglo = Array(3)
# arreglo.__setitem__(0,2)
# arreglo.__setitem__(1,4)
# arreglo.__setitem__(2,6)
# arreglo.__str__()

# datos = SinglyLinkedList()

# for i in arreglo:
#     datos.append(i)

# current = datos.tail
# current.data

# while current:
#     print(current.data)
#     current = current.next