class Array:
    def __init__(self, capacity, fill_value=None): # Su capacidad siempre es definida desde un principio y no podrá ser cambiada.
        self.items = list()
        for i in range(capacity):
            self.items.append(fill_value)

    def __len__(self):
        return len(self.items)
    
    def __str__(self):
        return str(self.items)
    
    def __iter__(self):
        return iter(self.items)
    
    def __getitem__(self, index):
        return self.items[index]
    
    def __setitem__(self, index, new_item):
        self.items[index] = new_item

# Operaciones dentro de la Terminal.

# menu = Array(5)
# menu.__len__()
# menu.__str__()
# menu.__getitem__(2)
# menu.__setitem__(2,100)
# menu.__getitem__(2)

    # if __name__ == '__main__':
    #     arreglo = Array(3)
    #     # Ubicación en memoria
    #     print(arreglo) #<__main__.Array object at 0x0000020954591FA0>
        
    #     # Me retorna los espacios vacíos del array, los hoyos de para las plantas.
    #     print(arreglo.items) #[None, None, None]
        

    #     # Para llenar los datos debo usar .items o lista vacía,
    #     # para poder acceder a los elementos del arreglo.
    #     # Aquí evidencio como se llenan los datos.
    #     # [1, None, None]
    #     # [1, 2, None]
    #     # [1, 2, 3]
    # for i in range(0, len(arreglo.items)):
    #     arreglo.items[i] = i + 1
    #     print(arreglo.items)



    # # Usando los métodos que creamos para el arreglo.
    # length = arreglo.items.__len__()
    # print("El arreglo tiene como largo : "+ str(length))

    # # Retorno un str
    # strings = arreglo.items.__str__()
    # print(type(strings))

    # # Creo un Objeto lista iterador y lo recorro con next
    # iterador = arreglo.items.__iter__()
    # print(iterador)
    # print(next(iterador))

    # # Consigo el elemnto en la posición 1
    # consigo_elemento = arreglo.items.__getitem__(1)
    # print(consigo_elemento)

    # # Ingreso un elemento específicado.
    # arreglo.items.__setitem__(1,"Arreglo terminado!")
    # print(arreglo.items) 