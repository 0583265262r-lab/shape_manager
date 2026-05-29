

class Shape:

    """
    מחלקת אב מייצגת צורה הנדסית כללית.
    """
    
    def __init__(self,type, shape_id,logger=__name__):
        '''
        אתחול צורה חדשה
           args:
                type (str): type of the shape
                shape_id (int): unique identifier
                logger: logger object for recording actions
        '''
        self.shape_id = shape_id
        self.type = type
        self.logger = logger
        self.shape_id += 1
    def get_area(self):
        '''calculate area '''

        pass
    def get_perimeter(self):
        ''' calculate perimeter'''
        pass
    def to_dict(self):
        '''converting shape details to a dictionary'''
        pass

  