from shape import *
from circle import *
from square import *
from rectangle import *
from logger import get_logger

class ShapeManager:
    SHAPE_CLS = {"circle":
                   {"cls":Circle,
                    "filed":["radius"]},
                    "square":
                   {"cls":Square,
                    "filed":["side"]},
                    "rectangle":
                   {"cls":Rectangle,
                    "filed":["width","height"]}
                    }
    
    
    def __init__(self):
        self.shapes = []
        self.load_from_json()
    
    def create_shape(self,shape):
        shape_name=next(iter(shape))
        c1=self.SHAPE_CLS[shape_name]["cls"](1,shape_name,**shape[shape_name])
        return c1.to_dict()
        
        
    
    def get_all_shapes(self):
        pass
    
    def update_shape(self, shape_id, new_data):
        pass
    
    def delete_shape(self, shape_id):
        pass
    
    def save_to_json(self):
        pass
    
    def load_from_json(self):
        
        pass

