# Fast Ticket Booker - Flask frontend
# Ye file apne project folder me main.py ke saath rakho aur chalao: python app.py

import os
from datetime import datetime

# storage.py "tickets/" relative path use karta hai, isliye project folder me hi kaam karo
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
os.chdir(BASE_DIR)

from flask import Flask, render_template, request, redirect, url_for, session, flash

from data.prices import prices
from pricing import apply_discount, calculate_total, get_base_price
from ticket import build_receipt, generate_ticket_id
from storage import load_history, save_to_json, save_to_txt

app = Flask(__name__)
app.secret_key = os.environ.get("SECRET_KEY", "fast-ticket-booker-dev-key")

VEHICLES = list(prices.keys())
CLASSES = ["economy", "business", "sleeper"]


@app.template_filter("money")
def money(value):
    value = float(value)
    if value.is_integer():
        return f"{value:,.0f}"
    return f"{value:,.2f}"


def price_table():
    # Form me live price dikhane ke liye: har vehicle/class ki base aur final price
    table = {}
    for vehicle in VEHICLES:
        table[vehicle] = {}
        for travel_class in CLASSES:
            base = get_base_price(vehicle, travel_class)
            table[vehicle][travel_class] = {
                "base": base,
                "final": apply_discount(vehicle, base),
            }
    return table


def validate_booking(form):
    """CLI (booking.py) wale hi rules: errors list aur cleaned data return karta hai."""
    errors = []

    vehicle = form.get("vehicle", "").strip().lower()
    if vehicle not in VEHICLES:
        errors.append("Choose a vehicle: bus, train, car or van.")

    travel_class = form.get("travel_class", "").strip().lower()
    if travel_class not in CLASSES:
        errors.append("Choose a class: economy, business or sleeper.")

    source = form.get("source", "").strip()
    destination = form.get("destination", "").strip()
    if source == "" or destination == "":
        errors.append("Source and destination cannot be empty.")
    elif source.lower() == destination.lower():
        errors.append("Source and destination cannot be the same.")

    date_str = ""
    try:
        parsed_date = datetime.strptime(form.get("date", "").strip(), "%Y-%m-%d")
        date_str = parsed_date.strftime("%d-%m-%Y")  # DD-MM-YYYY, jaise CLI me
    except ValueError:
        errors.append("Enter a valid travel date.")

    time_str = ""
    try:
        parsed_time = datetime.strptime(form.get("time", "").strip(), "%H:%M")
        time_str = parsed_time.strftime("%H:%M")
    except ValueError:
        errors.append("Enter a valid travel time.")

    passengers = 0
    try:
        passengers = int(form.get("passengers", "").strip())
        if passengers <= 0:
            errors.append("Passenger count must be greater than 0.")
    except ValueError:
        errors.append("Enter a valid number of passengers.")

    cleaned = {
        "vehicle": vehicle,
        "travel_class": travel_class,
        "source": source,
        "destination": destination,
        "date_str": date_str,
        "time_str": time_str,
        "passengers": passengers,
    }
    return errors, cleaned


@app.route("/")
def index():
    return render_template("index.html", form={}, errors=[], price_table=price_table())


@app.route("/review", methods=["GET", "POST"])
def review():
    if request.method == "GET":
        return redirect(url_for("index"))

    errors, data = validate_booking(request.form)
    if errors:
        return render_template(
            "index.html", form=request.form, errors=errors, price_table=price_table()
        )

    # Wahi pricing functions jo CLI me use hote hain
    base_price = get_base_price(data["vehicle"], data["travel_class"])
    final_price = apply_discount(data["vehicle"], base_price)
    total_price = calculate_total(final_price, data["passengers"])

    details = {
        "ticket_id": generate_ticket_id(),
        "vehicle": data["vehicle"],
        "class": data["travel_class"],
        "source": data["source"],
        "destination": data["destination"],
        "date": data["date_str"],
        "time": data["time_str"],
        "passengers": data["passengers"],
        "price_per_ticket": final_price,
        "total_price": total_price,
    }

    # Confirm hone tak details session me rehti hain, save sirf confirm par hoga
    session["pending"] = details
    return render_template("review.html", t=details, discounted=(final_price != base_price), base_price=base_price)


@app.route("/confirm", methods=["POST"])
def confirm():
    details = session.get("pending")
    if not details:
        flash("Your booking session expired. Please start again.")
        return redirect(url_for("index"))

    if request.form.get("action") == "yes":
        save_to_txt(build_receipt(details))
        save_to_json(details)
        session.pop("pending", None)
        return render_template("success.html", t=details)

    session.pop("pending", None)
    flash("Booking cancelled.")
    return redirect(url_for("index"))


@app.route("/history")
def history():
    tickets = list(reversed(load_history()))  # nayi booking sabse upar
    return render_template("history.html", tickets=tickets)


if __name__ == "__main__":
    app.run(debug=True)
