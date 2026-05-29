from shape import *
from logger import get_logger
logger=get_logger(__name__)
class Circle(Shape):
    ''' מחלקה המייצגת מעגל'''
    def __init__(self, type, shape_id,radius):
        super().__init__(type, shape_id)
        self.radius = radius
        
    def get_area(self):
        ''' calculate area of circle'''
        logger.info(f"Circle {self.shape_id}: calculating area")
        return str((self.radius ** 2) * 3.14)
    
    def get_perimeter(self):
        '''calculate area of circle'''
        logger.info(f"Circle {self.shape_id}: calculating perimeter")
        return str((self.radius * 2) * 3.14)
    
    def to_dict(self):
        ''' converting circle details to a dictionary'''
        logger.info(f"Circle {self.shape_id}: creating dictionary")
        return {str(self.shape_id):{"type":self.type,
                                    "radius":str(self.radius),
                                    "area":self.get_area(),
                                    "perimeter":self.get_perimeter()}}



if __name__ == "__main__":
    c1=Circle("circle",3,3)
    print(c1.to_dict())
    




