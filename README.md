
---

# M-Pesa STK Integration with Python and Flask

This repository demonstrates how to integrate M-Pesa STK (Sim Tool Kit) payment functionality using Python and Flask. The application allows users to subscribe to different Wi-Fi plans and processes payments through the M-Pesa API. It also handles and logs transaction statuses and provides error handling.

## Features

- **Wi-Fi Subscription Plans**: Offers three different subscription plans with varying prices.
- **M-Pesa STK Push Integration**: Initiates payment requests to M-Pesa and handles responses.
- **Transaction Logging**: Logs transaction details for successful and failed transactions.
- **Error Handling**: Displays errors and success messages to users.
- **Responsive Design**: Frontend built with Tailwind CSS for a modern and responsive user experience.

## Prerequisites

- Python 3.6+
- Flask
- Requests library

## Installation

1. Clone the repository:
    ```sh
    git clone https://github.com/Griffins-Mbae/Mpesa-stk-python-flask.git
    cd Mpesa-stk-python-flask
    ```

2. Install the required Python packages:
    ```sh
    pip install -r requirements.txt
    ```

## Configuration

1. Update the M-Pesa credentials in `app.py`:
    ```python
    consumer_key = 'your_consumer_key'
    consumer_secret = 'your_consumer_secret'
    shortcode = 'your_shortcode'
    passkey = 'your_passkey'
    callback_url = 'your_callback_url'
    ```

2. Ensure your callback URL is accessible and correctly configured to handle M-Pesa callbacks.

## Usage

1. Run the Flask application:
    ```sh
    python app.py
    ```

2. Open your web browser and navigate to `http://127.0.0.1:5000/` to access the subscription page.

3. Enter your phone number and select a subscription plan to initiate the M-Pesa STK Push payment.

## File Structure

- `app.py`: Main Flask application file with routes and M-Pesa integration logic.
- `templates/`
  - `index.html`: Subscription plans page.
  - `callback.html`: Page to display transaction statuses.
- `static/`
  - `css/`: Tailwind CSS files.
  - `js/`: JavaScript files for frontend functionality.

## Endpoints

- `/`: Main page displaying subscription plans.
- `/subscribe`: Endpoint to handle subscription form submissions and initiate M-Pesa payments.
- `/mpesa/callback`: Endpoint to handle M-Pesa payment callbacks.

## License

This project is licensed under the MIT License.

## Acknowledgments

- [Safaricom Developers](https://developer.safaricom.co.ke) for M-Pesa API documentation and support.
- [Flask](https://flask.palletsprojects.com) for providing a simple and powerful web framework.
- [Tailwind CSS](https://tailwindcss.com) for modern and responsive design capabilities.

---

