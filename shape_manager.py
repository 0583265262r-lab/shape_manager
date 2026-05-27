from shape import *
from circle import *
from square import *
from rectangle import *
from logger import get_logger
import json
FILE_NAME = "shapes.json"
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
        self.data = self.load_from_json(FILE_NAME)
        
    
    def create_shape(self,shape):
        logger.info("created")
        shape_name=next(iter(shape))
        c1=self.SHAPE_CLS[shape_name]["cls"](8,shape_name,**shape[shape_name])
        x = c1.to_dict()
        try:
            self.data = self.data | x
        except json.JSONDecodeError as e:
            print(f"{e}")
            self.data =x
        self.save_to_json(FILE_NAME)
        
    
    def get_all_shapes(self):
    
        print(self.data)
        
        
    
    def update_shape(self, shape_id, new_data):
        logger.info("b")
        shapes=self.load_from_json(FILE_NAME)
        self.delete_shape(shape_id)
        logger.info("c")
        self.create_shape(new_data)

        
    
    def delete_shape(self, shape_id):
        shapes=self.load_from_json(FILE_NAME)
        deleted_shape = shapes.pop(shape_id)
        return deleted_shape
    
        

        
    
    def save_to_json(self,filename):
        logger.info("jfhdh")
        try:
            with open(filename,"w") as f:
               json.dump(self.data,f)
        except FileNotFoundError as e:
            print(f"file not exist {e}")
        return
    
    def load_from_json(self,filename):
        try:
            with open(filename,"r") as f:
                file=json.load(f)
            return file
        except json.JSONDecodeError as e:
            print(f"the file is empty {e}")
            # with open(filename,"w") as f:
            #     file=json.load({})
            # return file
    
    def get_id():
        pass


        
        

        
        


  

