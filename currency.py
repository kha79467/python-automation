import requests

API_KEY = 'fca_live_XYjS4vGgvetB6csNwKrZP3KR0vfrcpX5WZf6IfCg'
BASE_URL = f'https://api.freecurrencyapi.com/v1/latest?apikey={API_KEY}'
CURRENCIES = ["USD", "CAD", "EUR", "AUD", "CNY"]

def convert_currency(base):
    currencies = ",".join(CURRENCIES)
    url = f"{BASE_URL}&base_currency={base}&currencies={currencies}"
    try:
        response = requests.get(url)
        data = response.json()
        if "data" in data:
            return data["data"]
        else:
            print("Invalid currency or API error.")
            return None
    except Exception as e:
        print(f"Error fetching data: {e}")
        return None

while True:
    base = input("Enter the base currency (q for quit): ").upper()
    if base == "Q":
        break

    data = convert_currency(base)
    if not data:
        continue  # Skip the rest of the loop if data is None

    if base in data:
        del data[base]  # Only delete if the base currency exists in the data

    for ticker, value in data.items():
        print(f"{ticker}: {value}")





