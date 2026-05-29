from shape import *
from logger import get_logger
logger=get_logger(__name__)
class Rectangle(Shape):
    '''מחלקה המייצגת מלבן'''
    def __init__(self, type, shape_id,width,height):
        super().__init__(type, shape_id)
        self.width = width
        self.height = height
    
    def get_area(self):
        ''' calculate area of rectangle'''
        logger.info(f"Rectangle {self.shape_id}: calculating area")
        return str(self.width * self.height)
    
    def get_perimeter(self):
        ''' calculate perimeter of rectangle'''
        logger.info(f"Rectangle {self.shape_id}: calculating perimeter")
        return str((self.width * 2) + (self.height * 2))
    
    def to_dict(self):
        '''converting rectangle details to a dictionary '''
        logger.info(f"Rectangle {self.shape_id}: creating dictionary")
        return {str(self.shape_id):{"type":self.type,"width":str(self.width),
                                    "height":str(self.height),
                                    "area":self.get_area(),
                                    "perimeter":self.get_perimeter()
                                    }}


   
if __name__ == "__main__":
    r1=Rectangle("Rectangle",1,3,4)
    print(r1.to_dict())
         



