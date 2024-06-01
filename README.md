# Income Tax Calculation Application

This application calculates income tax based on the user's income, company type, and eligibility for Young Entrepreneur Support. It uses Streamlit to provide a user-friendly web interface.

## Features

- Supports both monthly and yearly income inputs
- Calculates taxes for different company types: Individual, Limited Company, Anonymous Company, Limited Partnership
- Includes Young Entrepreneur Support option for tax exemptions
- Interactive and easy-to-use interface

## How to Run the Application

### Prerequisites

- Python 3.7 or higher
- Streamlit library

### Installation

1. Clone this repository or download the `app.py` file.

    ```bash
    git clone https://github.com/ysfzkn/income-tax-calculation.git
    cd income-tax-calculation
    ```

2. Install the required Python packages.

    ```bash
    pip install streamlit
    ```

### Running the Application

Run the following command in your terminal:

    ```bash
    streamlit run app.py
    ```

This will start the Streamlit server and open the application in your default web browser.

### Customization

You can customize the application by editing the `app.py` file. Adjust the tax brackets, rates, and other parameters as needed.

### Application Overview

- The application takes user inputs for income type (monthly or yearly), income amount, company type, and Young Entrepreneur Support eligibility.
- It converts monthly income to yearly if needed.
- Based on the company type, it sets the appropriate tax brackets and rates.
- It calculates the total tax payable based on the user's income and displays the result.

## License

This project is licensed under the MIT License.
