
def check_house_availability(arg_name, arg_value, collection):
    """

    """
    try:
        if arg_value in collection:
            return True
        
        elif arg_value == None:
            print(f"NoneTypeError: Argument value provided is 'None'")
            return False
        
        elif isinstance(arg_value, str):
            print(f"TypeError: String not accepted. Expected value of datatype <class 'int'>")
            return False

        else:
            print(f"{arg_name} = {arg_value} does not exist in the provided dataset.")
            return False

    except Exception as e:
        print("Error occured in check_availability method due to ", e)
        

def check_correct_datatype(arg_name, arg_value, target_datatype):
    """

    """
    try:
        if isinstance(arg_value, target_datatype):
            return True
        
        elif arg_value == None:
            print(f"NoneTypeError: Argument '{arg_name}' cannot be 'None' and it accepts datatype {target_datatype})")
            return False

        else:
            print(f"TypeError: Argument '{arg_name}' accepts datatype {target_datatype}")
            return False

    except Exception as e:
        print("Error occured in check_correct_datatype method due to ", e)

        
def check_list_validations(arg_name, arg_value, member_datatype):
    """

    """
    try:
        if check_correct_datatype(arg_name, arg_value, list):
            if len(arg_value)!=0:
                return True
            else:
                print(f"Error: Empty list. Please specify some values using the argument '{arg_name}' <class 'list'>: ({member_datatype})")
                return False
        else:
            return False

    except Exception as e:
        print("Error occured in check_correct_datatype method due to ", e)