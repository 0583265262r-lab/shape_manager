from shape import *
from logger import get_logger
logger=get_logger(__name__)

class Square(Shape):
    ''' מחלקה המייצגת ריבוע'''
    def __init__(self, type, shape_id,side):
        super().__init__(type, shape_id)
        self.side = side
    
    def get_area(self):
        ''' calculate area of square'''
        logger.info(f"Square {self.shape_id}: calculating area")

        return str(self.side ** 2)
    
    def get_perimeter(self):
        ''' calculate perimeter of square'''
        logger.info(f"Square {self.shape_id}: calculating perimeter")
        return str(self.side * 4)
    
    def to_dict(self):
        ''' converting square details to a dictionary'''
        logger.info(f"Square {self.shape_id}: creating dictionary")
        return {str(self.shape_id):{"type":self.type,"side":str(self.side),
                                    "area":self.get_area(),
                                    "perimeter":self.get_perimeter(),
                                    }}



if __name__ == "__main__":
    shape_manager=Square("square",2,4)
    print(shape_manager.to_dict())
    
