[]
["Isabel"]
["Isabel", "Mulan"]
["Isabel", "Mulan", 255]
["Isabel", "Mulan", 255, ["Pucca", "Percy"]]

fruits = []
fruits
fruits.append("Kiwi")
fruits.append("Berry")
fruits.append("Melon")
fruits
fruits.sort() # Para ordernar la lista
fruits.pop() # Elimina el último elemento
fruits.insert(0, "Apple") # Ingresa en la posición 0 el elemento Apple
fruits.insert(1, "Strawberry")
fruits.pop(1) # Elimina de acuerdo al indice pasado como parámetro
fruits.remove("Apple") # Elimina por elemento pasado como parámetro
# fruits.remove("Dragon Fruit") # Si se intenta eliminar un elemento que no existe, se generá error.

def pyramid_sum(lower, upper, margin=0):
    blanks = " " * margin
    print(blanks, lower, upper)
    if lower > upper:
            print(blanks, 0)
            return 0
    else:
            result = lower + pyramid_sum(lower + 1, upper, margin +4)
            print(blanks, result)
            return result
    
pyramid_sum(1,4)
