from shape_manager import *
from logger import get_logger
logger = get_logger(__name__)
shape_manager=ShapeManager(logger)

def add_shape():
    shape_arg = {}
    user_choice = {"1":"circle","2":"square","3":"rectangle"}
    print("1.circle\n"
          "2.square\n"
          "3.rectangle")
    choice_shape=input("enter your choice: ")
    if choice_shape in user_choice:
        shape_arg[user_choice[choice_shape]]={}
        for arg in shape_manager.SHAPE_CLS[user_choice[choice_shape]]["filed"]:
            try:
                parameter = int(input(f"please enter {arg}: "))
                if parameter <= 0:
                    logger.info("zero")
                    print("parameter cen not be 0")
                    break
                shape_arg[user_choice[choice_shape]][arg]=parameter
            except ValueError as e:
                print( f"int needed {e}")
                break
        else:
            shape_manager.create_shape(shape_arg)
    else:
        print("invalid input")
        logger.info("user input not in the options")
    
    


def update():
    logger.info("a")
    try:
        input_shape_id = int(input("please enter ID: "))
        shape_id=str(input_shape_id)
        shapes = shape_manager.load_from_json("shapes.json")
        current_shape = shapes[shape_id]
        shape_arg = {}
        shape_arg[current_shape["type"]]={}
        for arg in shape_manager.SHAPE_CLS[current_shape["type"]]["filed"]:
            try:
                parameter = int(input(f"please enter {arg}: "))
                shape_arg[current_shape["type"]][arg]=parameter
            except ValueError as e:
                print( f"int needed {e}")
                break
        else:
            shape_manager.update_shape(shape_id,shape_arg)
    except ValueError as e:
        print(f"invalid input {e}")
    

def delete():
    try:
        shape_id = int(input("please enter ID: "))
        shape_manager.delete_shape(shape_id)
    except ValueError as e:
        print(f"invalid input {e}")

    




def main():
    while True:
        print("=============\n")
        choice_from_user=input("1. Add shape: \n" \
                                "2. Show all shape\n" \
                                "3. Update shape\n" \
                                "4. Delete shape\n" \
                                "5. Exit\n" \
                                "")
        match choice_from_user:
            case "1":
                add_shape()
            case "2":
                shape_manager.get_all_shapes()
            case "3":
                update()
            case "4":
                delete()
            case "5":
                print("goodby")
                break
            case _:
                print(" please choose between 1-5")

        
if __name__ == "__main__":
    main()              





    

        



        
        

    


