class Rectangle:
    def __init__(self,ancho,altura):
        self.width=ancho
        self.height=altura

    def __repr__(self):
        return "Rectangle(width={}, height={})".format(self.width, self.height)

    def set_width(self,x):
        self.width=x

    def set_height(self,x):
        self.height=x
    
    def get_area(self):
        area= self.width * self.height
        return area
    
    def get_perimeter(self):
        perimeter=(2*self.width)+(2*self.height)
        return perimeter
    
    def get_diagonal(self):
        diagonal=(self.width**2 + self.height**2)**0.5
        return diagonal
    
    def get_picture(self):
        figura=""
        if self.width>50 or self.height>50:
            print("Too big for picture.")
        else:
            for x in range(self.height):
                for c in range(self.width):
                    figura+="*"
                figura+="\n"
        return figura

class Square(Rectangle):
    def __init__(self,L):
        self.width=self.height=L
    
    def __repr__(self):
        return "Square (Side={})".format(self.lado)
    
    def set_side(self,x):
        self.width=self.height=x

