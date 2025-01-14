import random

class RandomizedSet:
    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.data = []  # Lista para almacenar los elementos
        self.idx_map = {}  # Diccionario para mapear valores a índices

    def insert(self, val):
        """
        Inserts a value to the set. Returns true if the set did not already contain the specified element.
        """
        if val in self.idx_map:
            return False  # El valor ya existe en el conjunto
        
        # Insertar el valor y actualizar el diccionario
        self.idx_map[val] = len(self.data)
        self.data.append(val)
        return True

    def remove(self, val):
        """
        Removes a value from the set. Returns true if the set contained the specified element.
        """
        if val not in self.idx_map:
            return False  # El valor no existe en el conjunto
        
        # Intercambiar el valor a eliminar con el último elemento en la lista
        last_val = self.data[-1]
        idx_to_remove = self.idx_map[val]
        
        self.data[idx_to_remove] = last_val
        self.idx_map[last_val] = idx_to_remove
        
        # Eliminar el último elemento de la lista y el valor del diccionario
        self.data.pop()
        del self.idx_map[val]
        return True

    def getRandom(self):
        """
        Get a random element from the set.
        """
        return random.choice(self.data)
