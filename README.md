Currency Converter

This is a real-time currency converter application built using Python's tkinter library for the GUI, requests for making API calls, and matplotlib for plotting charts. It allows users to convert an amount from one currency to another, fetch exchange rates data, reset the input fields, and plot exchange rate charts over time.
Features

    Convert an amount from one currency to another: Users can enter an amount in the input field and select the currencies for conversion using the dropdown menus for "From Currency" and "To Currency". Clicking the "Convert" button will fetch the current exchange rates from the Open Exchange Rates API, calculate the converted amount, and display it in the result label.

    Reset the input fields: Users can click the "Reset" button to clear the input fields for amount and currency selection.

    Plot exchange rate charts: Users can click the "Plot Chart" button to fetch historical exchange rate data from the Open Exchange Rates API, plot a chart of exchange rates over time using matplotlib, and display it in a new window. The chart shows the exchange rates of various currencies against the base currency over time.

How to Use

    Install Dependencies: Make sure you have Python 3 installed on your system. You need to install the following libraries if they are not already installed:
        tkinter: pip install tkinter
        requests: pip install requests
        matplotlib: pip install matplotlib

    Run the Application: Execute the code in a Python environment, and the currency converter application window will open.

    Convert Currency: Enter the amount in the "Amount" input field, select the "From Currency" and "To Currency" from the dropdown menus, and click the "Convert" button. The converted amount will be displayed in the result label.

    Reset Input Fields: Click the "Reset" button to clear the input fields for amount and currency selection.

    Plot Exchange Rate Chart: Click the "Plot Chart" button to fetch historical exchange rate data, plot a chart of exchange rates over time using matplotlib, and display it in a new window.

    Close the Application: Click the close button (X) on the application window to close the application.

Note: The exchange rates are fetched from the Open Exchange Rates API, which requires an app_id. The app_id used in the code is a free trial app_id with limited functionality. You may need to sign up for an API key from the Open Exchange Rates website (https://openexchangerates.org/) and replace the app_id in the API_BASE_URL variable in the code for full functionality.

 You can now use the currency converter application to convert currency amounts and plot exchange rate charts over time.

by umer





