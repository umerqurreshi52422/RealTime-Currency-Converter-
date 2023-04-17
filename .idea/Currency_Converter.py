import tkinter as tk
import requests
import matplotlib.pyplot as plt
import matplotlib.dates as mdates
from datetime import datetime, timedelta

# Define the base URL for the API
API_BASE_URL = "https://openexchangerates.org/api/latest.json?app_id=9113b78c9c1f47ae856e6f4dfb51a04c"

# List to store exchange rates data
exchange_rates = []


# Function to handle currency conversion
def convert_currency():
    # Get user input
    amount = float(amount_entry.get())
    from_currency = str(from_currency_var.get())
    to_currency = str(to_currency_var.get())

    # Fetch data from API
    response = requests.get(API_BASE_URL)
    data = response.json()

    # Extract converted amount from API response
    converted_amount = data["rates"][from_currency]
    amt = data["rates"][to_currency]
    print(converted_amount)
    print(amt)
    # Update result label
    result_label.config(text=f"Converted Amount: {(amt / converted_amount) * amount}")


# Function to reset the application
def reset():
    # Clear input fields and result label
    amount_entry.delete(0, tk.END)
    from_currency_var.set("")
    to_currency_var.set("")
    result_label.config(text="")




# Function to fetch exchange rates data
def fetch_exchange_rates():
    global exchange_rates  # Make sure to use the global exchange_rates list

    # Fetch data from API
    response = requests.get(API_BASE_URL)
    data = response.json()

    # Extract exchange rates data from API response
    rates = data["rates"]
    base_currency = data["base"]

    # Loop through the rates dictionary and append data to exchange_rates list
    for currency, rate in rates.items():
        exchange_rates.append((currency, rate))

    # Sort the exchange_rates list by currency code
    exchange_rates.sort(key=lambda x: x[0])

# Call the fetch_exchange_rates() function before plotting the chart
fetch_exchange_rates()

# Function to plot chart
def plot_chart():
    # Call the fetch_exchange_rates() function before plotting the chart to update the exchange_rates list
    fetch_exchange_rates()


def plot_chart():
    # Clear existing plot
    plt.clf()

    # Extract data for x and y axes
    dates = [item[0] for item in exchange_rates]
    rates = [item[1] for item in exchange_rates]

    # Create a figure and axis
    fig, ax = plt.subplots(figsize=(10, 6))

    # Plot the data
    ax.plot(dates, rates)

    # Set labels and title
    ax.set_xlabel("Date")
    ax.set_ylabel("Exchange Rate")
    ax.set_title("Exchange Rate Over Time")

    # Format x-axis ticks as dates
    ax.xaxis.set_major_formatter(mdates.DateFormatter('%Y-%m-%d'))
    ax.xaxis.set_major_locator(mdates.DayLocator(interval=7))

    # Rotate x-axis labels for better readability
    plt.xticks(rotation=45)

    # Display the chart
    plt.show()




# Create main window
root = tk.Tk()
root.title("Currency Converter")
root.geometry("500x500")
root.configure(bg="#3d6466")

# Create input fields
label = tk.Label(root, text="Real-Time Currency Converter", font=("Arial", 22), bg="PeachPuff2")
label.pack()
amount_label = tk.Label(root, text="Amount:", font=("Arial", 18))
amount_label.place(x=210, y=90)
amount_entry = tk.Entry(root, font=("Arial", 15))
amount_entry.place(x=140, y=120)

from_currency_label = tk.Label(root, text="From Currency:", font=("Arial", 14))
from_currency_label.place(x=185, y=160)
from_currency_var = tk.StringVar(root)
from_currency_var.set("Select")
from_currency_dropdown = tk.OptionMenu(root, from_currency_var, "USD", "EUR", "GBP", "JPY", "CAD", "PKR")
from_currency_dropdown.config(width=5)
from_currency_dropdown.place(x=220, y=190)

to_currency_label = tk.Label(root, text="To  Currency:", font=("Arial", 14))
to_currency_label.place(x=190, y=230)
to_currency_var = tk.StringVar(root)
to_currency_var.set("Select")
to_currency_dropdown = tk.OptionMenu(root, to_currency_var, "USD", "EUR", "GBP", "JPY", "CAD", "PKR")
to_currency_dropdown.config(width=5)
to_currency_dropdown.place(x=220, y=260)

# Create buttons
convert_button = tk.Button(root, text="Convert", font=("Arial", 18), bg="orange red", command=convert_currency)
convert_button.place(x=200, y=300)

reset_button = tk.Button(root, text="Reset", font=("Arial", 14), bg="orange red", command=reset)
reset_button.place(x=320, y=420)

# Create a button for plotting
plot_button = tk.Button(root, text="Plot Chart", font=("Arial", 14), bg="orange red", command=plot_chart)
plot_button.place(x=120, y=420)

# Create result label
result_label = tk.Label(root, text="",font=("Arial",16),bg="Gray50")
result_label.place(x=140, y=360)

# Start GUI event loop
root.mainloop()