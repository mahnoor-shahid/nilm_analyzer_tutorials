
def check_house_availability(house, collection):
    """

    """
    try:
        if house in collection:
            return True

        else:
            print(f"House number = {house} does not exist in the provided dataset.")
            return False

    except Exception as e:
        print("Error occured in check_house_availability method due to ", e)