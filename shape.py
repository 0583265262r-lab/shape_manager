

class Shape:
    
    def __init__(self,type, shape_id,logger=__name__):
        self.shape_id = shape_id
        self.type = type
        self.logger = logger
        self.shape_id += 1
    def get_area(self):
        pass
    def get_perimeter(self):
        pass
    def to_dict(self):
        pass

  