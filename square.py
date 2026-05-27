from shape import *
from logger import get_logger
logger=get_logger("square")

class Square(Shape):
    def __init__(self, type, shape_id,side):
        super().__init__(type, shape_id)
        self.side = side
    def get_area(self):
        logger.info(f"calculating area")

        return str(self.side ** 2)
    
    def get_perimeter(self):
        logger.info(f"calculating perimeter")
        return str(self.side * 4)
    def to_dict(self):
        logger.info(f"creating dictionary")
        return {str(self.shape_id):{"side":str(self.side),
                                    "area":self.get_area(),
                                    "perimeter":self.get_perimeter(),
                                    }}


