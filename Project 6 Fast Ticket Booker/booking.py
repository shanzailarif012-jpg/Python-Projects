# Generic Validation Function
def get_valid_input(prompt, valid_options):

    while True:
        user_input = input(prompt)
        # prompt = input(user_input)
        user_input = user_input.strip().lower()

        if user_input in valid_options:
            return user_input
        
        else:
            print("Invalid Options. Try Again")


# Vehicle Selection Function
def get_vehicle():
    
    valid_vehicles = ["bus" , "train" , "car" , "van"]
    prompt = "Choose Vehicle (bus/train/car/van):"

    vehicle = get_valid_input(prompt, valid_vehicles)

    return vehicle



# Route Input Function
def get_route():

    while True:
        source = input("Enter Source City: ")
        destination = input("Enter Destination City: ")


        source = source.strip()
        destination = destination.strip()

        if source == "" or destination == "":
            print("Source/Destination Cannt be Empty")
            continue

        if source.lower() == destination.lower():
            print("Source and Destination cannot be Same")
            continue

        break

    return source, destination



# travel date aur time lene ke liye 
from datetime import datetime 

def get_datetime():
    while True:
        date_str = input("Enter Travel Date (DD-MM-YYYY): ")

        try:
            parsed_date = datetime.strptime(date_str, "%d-%m-%Y")
            break

        except ValueError:
            print("invalid date format. Try again")
        
    while True:
        time_str = input("Enter Travel time (HH:MM, 24-hour): ")

        try:
            parsed_time = datetime.strptime(time_str, "%H:%M")
            break

        except ValueError:
            print("invalid time format. try again")
        
    return date_str, time_str



# passengers ki number poochna
def get_passenger_count():

    while True:
        count_str = input("Enter Number of Passenger: ")

        try:
            count = int(count_str)

            if count <= 0:
                print("Passeneger count must be greater than 0.")
                continue

            return count
        
        except ValueError:
            print("Please enter a valid number")




# Economy/Business/Sleeper choose karna, 
# price bhi sath show karna (train pe discount ke sath)
from data.prices import prices

def get_travel_class(vehicle):
    valid_classes = ["economy", "business", "sleeper"]

    print("Available Classes for", vehicle, ":")

    for class_name in valid_classes:
        base_price = prices[vehicle][class_name]

        if vehicle == "train":
            discounted_price = base_price - (base_price * 0.05)
            print(class_name, "- Rs.", base_price, "(Train Discount Price: Rs.", discounted_price, ")")

        else:
            print(class_name, "- Rs.", base_price)

        
    prompt = "Choose your class (economy/business/sleeper): "
    travel_class = get_valid_input(prompt, valid_classes)

    return travel_class
        
'''IMPORT prices FROM data.prices module

FUNCTION get_travel_class(vehicle):

    SET valid_classes = ["economy", "business", "sleeper"]

    PRINT "Available Classes for", vehicle, ":"

    FOR EACH class_name IN valid_classes DO
        SET base_price = prices[vehicle][class_name]

        IF vehicle == "train" THEN
            SET discounted_price = base_price - (base_price * 0.05)
            PRINT class_name, "- Rs.", base_price, "(Train Discount Price: Rs.", discounted_price, ")"
        ELSE
            PRINT class_name, "- Rs.", base_price
        END IF
    END FOR

    SET prompt = "Choose your class (economy/business/sleeper): "
    SET travel_class = CALL get_valid_input(prompt, valid_classes)

    RETURN travel_class

END FUNCTION'''