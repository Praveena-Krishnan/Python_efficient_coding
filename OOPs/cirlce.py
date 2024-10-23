class circle:
    def __init__(self,rad):
        self.radius=rad
        
    def area(self):
        return 3.14 * (self.radius ** 2)
    
my_circle=circle(9)
print(my_circle.area())