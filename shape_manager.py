from shape import *
from circle import *
from square import *
from rectangle import *
# from logger import get_logger
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
    
    
    def __init__(self, logger):
        self.logger = logger
        # self.shapes = []
        self.data = self.load_from_json(FILE_NAME)
        
    
    def create_shape(self,shape):
        self.logger.info("created")
        shape_name=next(iter(shape))
        c1=self.SHAPE_CLS[shape_name]["cls"](shape_name,self.get_id(),**shape[shape_name])
        x = c1.to_dict()
        if self.data is None:
            self.data = {}

        self.data = self.data | x
        self.save_to_json(FILE_NAME)
        
        
    
    def get_all_shapes(self):
    
        print (self.data)
        
        
    
    def update_shape(self, shape_id, new_data):
        logger.info("b")
        shapes=self.load_from_json(FILE_NAME)
        current_shape = shapes[shape_id]
        print(current_shape)
        print(self.SHAPE_CLS[current_shape["type"]]["cls"])
        c1 = self.SHAPE_CLS[current_shape["type"]]["cls"](int(shape_id) - 1,current_shape["type"],**new_data[current_shape["type"]])
        x=c1.to_dict()
        self.data = self.data | x
        self.save_to_json(FILE_NAME)


        

        logger.info("c")
        


        
    
    def delete_shape(self, shape_id):
        if str(shape_id) in self.data:
            del self.data[str(shape_id)]
            self.save_to_json(FILE_NAME)
        else:
            print("the ID not found")

    
        

        
    
    def save_to_json(self,filename):
        logger.info("jfhdh")
        try:
            with open(filename,"w") as f:
               json.dump(self.data,f, indent=4)
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
   
    def get_id(self):

        if self.data:
            return int(max(self.data,key=int))
        return 0

        

        
if __name__ == "__main__":
    c1 = ShapeManager()
    print(c1.get_id())

        
        

        
        


  

