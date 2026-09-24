# 🎫 Fast Ticket Booker

A simple command-line ticket booking system built in Python. Book tickets for **Bus, Train, Car, or Van**, choose your travel class, get an instant price breakdown (with a special discount on train tickets), and keep a saved history of all your bookings.

## ✨ Features

- Book tickets for **4 vehicle types**: Bus, Train, Car, Van
- **3 travel classes** for every vehicle: Economy, Business, Sleeper
- **5% automatic discount** on all train ticket classes
- **Unique Ticket ID** generated for every booking
- Collects **travel date, time, and number of passengers**
- Calculates **total price** based on passengers and class
- Generates a clean, **formatted receipt** for every booking
- Saves every booking to both a **`.txt` file** and a **`.json` file**
- **Booking history** — view all past bookings anytime
- Full **input validation** — invalid choices are rejected and re-asked
- Menu-driven — book a ticket, view history, or exit

## 📁 Project Structure

```
fast-ticket-booker/
│
├── main.py            # Entry point — menu loop (Book / View History / Exit)
├── booking.py          # User input collection + validation (vehicle, route, date/time, passengers, class)
├── pricing.py          # Price lookup, train discount, and total price calculation
├── ticket.py            # Ticket ID generation + formatted receipt builder
├── storage.py           # Saves bookings to .txt/.json, and loads booking history
│
├── data/
│   └── prices.py        # Base prices for every vehicle and class
│
├── tickets/              # Auto-created — stores tickets.txt and tickets.json
│
└── README.md
```

## ⚙️ How It Works

1. Run `main.py`
2. Choose an option from the menu:
   - **1. Book Ticket** — walks you through vehicle, route, date/time, passengers, and class selection, shows prices (with train discount), then asks for confirmation before saving
   - **2. View Booking History** — displays every ticket booked so far, pulled from the saved JSON file
   - **3. Exit** — closes the program
3. On confirming a booking, a receipt is printed, and the details are saved to `tickets/tickets.txt` and `tickets/tickets.json`

## 💰 Pricing Logic

- Each vehicle (Bus, Train, Car, Van) has its own base price per class (Economy, Business, Sleeper)
- **Train tickets get an automatic 5% discount** on top of the base price, for every class
- Final price = (discounted or base price) × number of passengers

## 🖥️ Running the Project

```bash
python main.py
```

No external libraries required — built entirely with Python's standard library (`json`, `uuid`, `datetime`, `os`).

## 🛠️ Built With

- Python 3
- Standard library modules: `json`, `uuid`, `datetime`, `os`

## 👤 Author

**Muhammad Shanzail** ([@dev_shanzail](https://github.com/shanzailarif012-jpg)) Python Mini Projects series.