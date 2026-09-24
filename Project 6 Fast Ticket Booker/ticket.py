# Unique Ticket ID generate hogi aur formatted receipt banega. 

import uuid 

def generate_ticket_id():
    random_part = uuid.uuid4().hex[0:5].upper()
    ticket_id = "FTB-" + random_part
    return ticket_id


def build_receipt(details_dict):
    receipt = ""
    receipt += "===== Fast Ticket Booker - Receipt =====\n"
    receipt += "Ticket ID: " + details_dict["ticket_id"] + "\n"
    receipt += "Vehicle: " + details_dict["vehicle"] + "\n"
    receipt += "Class: " + details_dict["class"] + "\n"
    receipt += "From: " + details_dict["source"] + " To: " + details_dict["destination"] + "\n"
    receipt += "Date: " + details_dict["date"] + " Time: " + details_dict["time"] + "\n"
    receipt += "Passengers: " + str(details_dict["passengers"]) + "\n"
    receipt += "Price per Ticket: Rs. " + str(details_dict["price_per_ticket"]) + "\n"
    receipt += "Total Price: Rs. " + str(details_dict["total_price"]) + "\n"
    receipt += "=========================================\n"
    return receipt
