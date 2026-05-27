from shape_manager import *
s1=ShapeManager()

def add_shape():
    shape_arg = {}
    user_choice = {"1":"circle","2":"square","3":"rectangle"}
    print("1.circle\n"
          "2.square\n"
          "3.rectangle")
    choice_shape=input("enter your choice: ")
    if choice_shape in user_choice:
        shape_arg[user_choice[choice_shape]]={}
        for arg in s1.SHAPE_CLS[user_choice[choice_shape]]["filed"]:
            try:
                parameter = int(input(f"please enter {arg}: "))
                shape_arg[user_choice[choice_shape]][arg]=parameter
            except ValueError as e:
                print( f"int needed {e}")
    else:
        print("invalid input")
    s1.create_shape(shape_arg)
    # s1.get_all_shapes()    
add_shape()

# def updata():
#     logger.info("a")
#     shape_id = int(input("please enter ID: "))
    
    

#     s1.update_shape(shape_id,add_shape())
# updata()

    
        



        
        

    


