from shape import *
from circle import *
from square import *
from rectangle import *
from logger import get_logger
import json
logger=get_logger(__name__)
FILE_NAME = "shapes.json"
class ShapeManager:
    ''' Manages the creation, saving, and deletion of shapes in the system'''
    SHAPE_CLS = {"circle":{"cls":Circle,"filed":["radius"]},
                 "square":{"cls":Square,"filed":["side"]},
                 "rectangle":{"cls":Rectangle,"filed":["width","height"]}
                }
    
    
    def __init__(self):
        self.logger = logger
        self.data = self.load_from_json(FILE_NAME)
        
    
    def create_shape(self,shape):
        ''' Creating a new shape and adding it to the file '''
        self.logger.info("Manager : creating new shape")
        shape_name=next(iter(shape))
        new_shape=self.SHAPE_CLS[shape_name]["cls"](shape_name,self.get_id(),**shape[shape_name])
        dict_of_new_shape = new_shape.to_dict()
        if self.data is None:
            self.data = {}
        self.data = self.data | dict_of_new_shape
        self.save_to_json(FILE_NAME)
        
        
    
    def get_all_shapes(self):
        ''' Displays all shapes present in the file '''
        print (self.data)
        
        
    
    def update_shape(self, shape_id, new_data):
        ''' Update shape by ID '''
        self.logger.info(f"Manager : updating shape {shape_id} ")
        # shapes=self.load_from_json(FILE_NAME)
        current_shape = self.data[shape_id]
        shape_update = self.SHAPE_CLS[current_shape["type"]]["cls"](current_shape["type"],int(shape_id) - 1,**new_data[current_shape["type"]])
        the_updated_shape=shape_update.to_dict()
        self.data = self.data | the_updated_shape
        self.save_to_json(FILE_NAME)

    def delete_shape(self, shape_id):
        ''' Deleting a shape from the system '''
        if str(shape_id) in self.data:
            del self.data[str(shape_id)]
            self.save_to_json(FILE_NAME)
            self.logger.info(f"Manager :deleted shape {shape_id}")
        else:
            self.logger.warning(f"Manager : shape {shape_id} not found")
            print("the ID not found")

    def save_to_json(self,filename):
        ''' Saving data to a file '''
        try:
            with open(filename,"w") as f:
               json.dump(self.data,f, indent=4)
        except Exception as e:
            self.logger.error(f"Manager :; save error {e}")
            print(f"file not exist {e}")
    
    def load_from_json(self,filename):
        ''' Loading data from a file '''
        try:
            with open(filename,"r") as f:
                return json.load(f)
        except:
            self.logger.info("Manager : the was empty")
            return None
            
   
    def get_id(self):
        ''' Getting ID next in line '''
        if self.data:
            return int(max(self.data,key=int))
        return 0

        

        
if __name__ == "__main__":
    c1 = ShapeManager()
    print(c1.get_id())

        
        

        
        


  

