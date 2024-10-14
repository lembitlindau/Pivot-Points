import requests
import matplotlib.pyplot as plt
import datetime

# Exante API URL ja autentimise andmed
API_URL = "https://api.exante.eu/your-endpoint"
API_KEY = "167f6829-aa61-4a4f-8c34-750f3e3a6548"


# 1. Funktsioon instrumentide nimekirja saamiseks
def get_instruments():
    headers = {'Authorization': f'Bearer {API_KEY}'}
    response = requests.get(f"{API_URL}/instruments", headers=headers)
    return response.json()


# 2. Funktsioon hindade saamiseks
def get_prices(instrument_id):
    headers = {'Authorization': f'Bearer {API_KEY}'}
    yesterday = (datetime.datetime.now() - datetime.timedelta(days=1)).strftime('%Y-%m-%d')
    params = {'date': yesterday}
    response = requests.get(f"{API_URL}/instruments/{instrument_id}/prices", headers=headers, params=params)
    return response.json()


# 3. Funktsioon Pivoti tasemete arvutamiseks
def calculate_pivot(high, low, close):
    pivot = (high + low + close) / 3
    r1 = 2 * pivot - low
    s1 = 2 * pivot - high
    r2 = pivot + (high - low)
    s2 = pivot - (high - low)
    return pivot, r1, s1, r2, s2


# 4. Funktsioon graafiku joonistamiseks
def plot_pivot_levels(instrument_name, pivot, r1, s1, r2, s2):
    plt.figure(figsize=(10, 6))
    plt.axhline(pivot, color='blue', label='Pivot')
    plt.axhline(r1, color='green', label='Resistance 1')
    plt.axhline(s1, color='red', label='Support 1')
    plt.axhline(r2, color='green', linestyle='--', label='Resistance 2')
    plt.axhline(s2, color='red', linestyle='--', label='Support 2')
    plt.title(f'Pivot Levels for {instrument_name}')
    plt.legend()
    plt.show()


# 5. Põhiprotsess instrumentide töötlemiseks ja graafiku loomiseks
def main():
    instruments = get_instruments()
    for instrument in instruments:
        instrument_id = instrument['id']
        instrument_name = instrument['name']
        prices = get_prices(instrument_id)
        high = prices['high']
        low = prices['low']
        close = prices['close']

        pivot, r1, s1, r2, s2 = calculate_pivot(high, low, close)
        plot_pivot_levels(instrument_name, pivot, r1, s1, r2, s2)


if __name__ == "__main__":
    main()
