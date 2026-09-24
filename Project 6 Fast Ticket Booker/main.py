# yahan sab functions ko sequence me call karenge,
# confirmation logic lagayenge, aur poora flow chalayenge

print("\t\t\t\t\t\t\t\t\t\t\tDeveloped by: Dev_Shanzail") # Developer Msg

from booking import get_vehicle, get_route, get_datetime, get_passenger_count, get_travel_class
from ticket import generate_ticket_id, build_receipt
from storage import save_to_txt, save_to_json, load_history
from pricing import get_base_price, apply_discount, calculate_total

def book_ticket():

    print("Welcome To Fast Ticket Booker")
    print("Your one-stop solution for booking bus, train, car, and van tickets.")

    vehicle = get_vehicle()
    source, destination = get_route()
    date_str, time_str = get_datetime()
    passengers = get_passenger_count()
    tarvel_class = get_travel_class(vehicle)

    base_price = get_base_price(vehicle, tarvel_class)
    final_price = apply_discount(vehicle, base_price)
    total_price = calculate_total(final_price, passengers)

    ticket_id = generate_ticket_id()

    details_dict = {
        "ticket_id" : ticket_id,
        "vehicle" : vehicle,
        "class" : tarvel_class,
        "source" : source,
        "destination" : destination,
        "date" : date_str,
        "time" : time_str,
        "passengers" : passengers,
        "price_per_ticket" : final_price,
        "total_price" : total_price

    }

    receipt = build_receipt(details_dict)
    print()
    print(receipt)

    confirm = input("Confirm booking? (yes/no): ")

    if confirm.lower() == "yes":
        save_to_txt(receipt)
        save_to_json(details_dict)
        print("Booking Successful!")
    else:
        print("Booking Cancelled")

def view_history():
    history = load_history()

    if history == []:
        print("No booking found yet.")
        return
    
    for ticket in history:
        print("Ticket ID:", ticket["ticket_id"])
        print("Vehicle:", ticket["vehicle"], "| Class:", ticket["class"])
        print("From:", ticket["source"], "To:", ticket["destination"])
        print("Date:", ticket["date"], "Time:", ticket["time"])
        print("Passengers:", ticket["passengers"], "| Total: Rs.", ticket["total_price"])
        print("-----------------------------")

    

def main():
    while True:
        print("1. Book Ticket")
        print("2. View Booking History")
        print("3. Exit")

        choice =input("Enter Your Choice: ")

        if choice == "1":
            book_ticket()
        elif choice == "2":
            view_history()
        elif choice == "3":
            print("Thank you for using Fast Ticket Booker!")
            break
        else:
            print("Invalid choice. Try again.")


main()