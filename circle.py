from shape import *
from logger import get_logger
logger=get_logger("circle")
class Circle(Shape):
    def __init__(self, type, shape_id,radius):
        super().__init__(type, shape_id)
        self.radius = radius
        
    def get_area(self):
        logger.info(f"calculating area")
        return str((self.radius ** 2) * 3.14)
    
    def get_perimeter(self):
        logger.info(f"calculating perimeter")
        return str((self.radius * 2) * 3.14)
    def to_dict(self):
        logger.info(f"creating dictionary")
        return {str(self.shape_id):{"radius":str(self.radius),
                                    "area":self.get_area(),
                                    "perimeter":self.get_perimeter()}}




