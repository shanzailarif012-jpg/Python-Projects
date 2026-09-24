# hum price calculation aur train discount ka logic karein ge 

from data.prices import prices

def get_base_price(vehicle, travel_class):
    return prices[vehicle][travel_class]

def apply_discount(vehicle, price):
    if vehicle == "train":
        return price - (price * 0.05)
    
    else:
        return price
    
def calculate_total(price, passengers):
    return price * passengers
'''FROM data.prices IMPORT prices

FUNCTION get_base_price(vehicle, travel_class):
    RETURN prices[vehicle][travel_class]

FUNCTION apply_discount(vehicle, price):
    IF vehicle == "train" THEN
        RETURN price - (price * 0.05)
    ELSE
        RETURN price
    END IF

FUNCTION calculate_total(price, passengers):
    RETURN price * passengers'''