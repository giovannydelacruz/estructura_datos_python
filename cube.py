from array import Array

class Cube():
    def __init__(self, rows, columns, depth, fill_value=None):
        self.data = Array(rows)
        for row in range(rows):
            self.data[row] = Array(columns)
            for col in range(columns):
                self.data[row][col] = Array(depth, fill_value)

    def get_height(self):
        return len(self.data)
    
    def get_widht(self):
        return len(self.data[0])
    
    def get_depth(self):
        return len(self.data[0][0])
    
    def __getitem__(self, index):
        return self.data[index]
    
    def __str__(self):
        result = ""
        for row in range(self.get_height()):
            for col in range(self.get_widht()):
                for dep in range(self.get_depth()):
                    result += str(self.data[row][col][dep])+" "
                result += "\n"
        return str(result)