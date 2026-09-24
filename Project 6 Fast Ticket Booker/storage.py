# ticket details .txt aur .json dono me save honge, 
# aur booking history read karne ka function bhi banega

import json
import os

os.makedirs("tickets", exist_ok=True)

def save_to_txt(receipt_text):
    with open ("tickets/tickets.txt" , "a") as f:
        f.write(receipt_text)
        f.write("\n") 


def save_to_json(ticket_dict):
    try:
        with open ("tickets/tickets.json" , "r") as f:
            history = json.load(f)

    except FileNotFoundError:
        history = []

    history.append(ticket_dict)

    with open ("tickets/tickets.json" , "w") as f:
        json.dump(history, f, indent=4)



def load_history():
    try:
        with open("tickets/tickets.json" , "r") as f:
            history = json.load(f)
        return history
    
    except FileNotFoundError:
        return []

