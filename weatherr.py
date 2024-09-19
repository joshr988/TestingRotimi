import requests
from bs4 import BeautifulSoup

def get_weather_data():
    # URL for the 10-day weather forecast for Decatur, GA
    url = "https://weather.com/weather/tenday/l/Decatur+GA?canonicalCityId=220f2724230f044971ce6df02e859d0cd3d7733c626907c49dbb1e426cd54e5d"

    # Make the request to the website
    response = requests.get(url)

    # Check if the request was successful
    if response.status_code == 200:
        # Parse the HTML content using BeautifulSoup
        soup = BeautifulSoup(response.content, 'html.parser')

        # Extracting the 10-day forecast data
        try:
            days = soup.find_all('h2', class_='DetailsSummary--daypartName--1Mebr')
            dates = soup.find_all('span', class_='DetailsSummary--date--1Mebr')
            temperatures = soup.find_all('span', class_='DetailsSummary--tempValue--1K4ka')
            descriptions = soup.find_all('span', class_='DetailsSummary--extendedData--aaFeV')

            # Print the lengths of the lists to debug
            print(f"Found {len(days)} days, {len(dates)} dates, {len(temperatures)} temperatures, and {len(descriptions)} descriptions.")

            # Find the minimum length among the lists to avoid index errors
            forecast_length = min(len(days), len(dates), len(temperatures), len(descriptions))

            # Loop through the available days and print the weather data
            for i in range(forecast_length):
                day = days[i].text.strip()
                date = dates[i].text.strip()
                temp = temperatures[i].text.strip()
                desc = descriptions[i].text.strip()
                
                print(f"{day} ({date}): {temp}, {desc}")

        except AttributeError:
            print("Could not extract weather data. The website layout may have changed.")
    else:
        print(f"Failed to retrieve data. HTTP Status code: {response.status_code}")

if __name__ == "__main__":
    get_weather_data()


    stuff 