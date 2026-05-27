from shape import *
from logger import get_logger
logger=get_logger("Rectangle")
class Rectangle(Shape):
    def __init__(self, type, shape_id,width,height):
        super().__init__(type, shape_id)
        self.width = width
        self.height = height
    def get_area(self):
        logger.info(f"calculating area")
        return str(self.width * self.height)
    
    def get_perimeter(self):
        logger.info(f"calculating perimeter")
        return str((self.width ** 2) + (self.height ** 2))
    def to_dict(self):
        logger.info(f"creating dictionary")
        return {str(self.shape_id):{"width":str(self.width),
                                    "height":str(self.width),
                                    "area":self.get_area(),
                                    "perimeter":self.get_perimeter()
                                    }}


r1=Rectangle("Rectangle",1,3,4)
print(r1.to_dict())        



