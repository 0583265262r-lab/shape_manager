'''
The main file(main.py) manages the user interface(CLI)
and connects the user to the ShapeManager
'''



from shape_manager import *
from logger import get_logger


logger = get_logger(__name__)
shape_manager=ShapeManager()

def handel_add_shape():
    ''' Receives form type and parameters from the user, and passes them to management '''
    logger.info(" Main: add shape process initiated")
    shape_arg = {}
    user_choice = {"1":"circle","2":"square","3":"rectangle"}
    print("1.circle\n"
          "2.square\n"
          "3.rectangle")
    choice_shape=input("enter your choice: ")
    if choice_shape in user_choice:
        shape_type=user_choice[choice_shape]
        shape_arg[shape_type]={}
        for arg in shape_manager.SHAPE_CLS[shape_type]["filed"]:
            try:
                parameter = int(input(f"please enter {arg}: "))
                if parameter <= 0:
                    logger.warning(f"Main: Invalid input {parameter} for {arg}")
                    print("parameter cannot be 0 or negative.")
                    return
                shape_arg[shape_type][arg]=parameter
            except ValueError:
                logger.error("Main: User entered non-integer value")
                print("Error: please enter a valid number")
                return
        else:
            shape_manager.create_shape(shape_arg)
            logger.info(f"Main: Successfully added {shape_type}")
    else:
        logger.warning("Invalid shape choice")
        print("invalid choice")
    
    


def handel_update():
    ''' Updating an existing shape by ID'''
    logger.info("Main: Update process initiated")
    try:
        input_shape_id = int(input("please enter ID: "))
        shape_id=str(input_shape_id)
        if shape_id not in shape_manager.data:
            print("ID not found")
            return
        current_type= shape_manager.data[shape_id]["type"]
        shape_arg = {current_type : {}}
        for arg in shape_manager.SHAPE_CLS[current_type]["filed"]:
            try:
                parameter = int(input(f"please enter {arg}: "))
                shape_arg[current_type][arg]=parameter
            except ValueError:
                logger.error("Main: User entered non-integer value")
                print("Error: please enter a valid number")
                return
        else:
            shape_manager.update_shape(shape_id,shape_arg)
            logger.info(f"Main: Shape {shape_id} update")
            print(f"The update {shape_id} was successful.")
    except Exception as e:
        logger.error(f"Main: Update failed: {e}")
        print(f"Update failed")
    

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
                handel_add_shape()
            case "2":
                shape_manager.get_all_shapes()
            case "3":
                handel_update()
            case "4":
                delete()
            case "5":
                print("goodby")
                break
            case _:
                print(" please choose between 1-5")

        
if __name__ == "__main__":
    main()              





    

        



        
        

    


