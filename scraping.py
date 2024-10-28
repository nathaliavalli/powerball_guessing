import csv  # Import csv for writing the file
from bs4 import BeautifulSoup 
import requests

def powerball_numbers_scrapping ():

    # Make a request to the webpage
    r = requests.get("https://api.scrapingdog.com/scrape?api_key=<671f84a60cf88d4aa9ab6f95>&url=https://www.powerball.com/previous-results?gc=powerball&sd=2023-01-02&ed=2023-12-302&dynamic=true").content


    # URL of the page
    url = "https://www.powerball.com/previous-results?gc=powerball&sd=2023-01-02&ed=2023-12-30"
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.75 Safari/537.36'
    }
    r = requests.get(url, headers=headers)
    soup = BeautifulSoup(r.content, 'html.parser')

    # Initialize list to store data
    data = []

    # Select all the main containers that hold the winning numbers
    draws = soup.find_all("div", class_="row row-cols-2 flex-column gap-3 h-100")
    for draw in draws:
        # Extract the winning numbers and sort them
        numbers = sorted(int(num.text.strip()) for num in draw.find_all("div", class_="item-powerball"))
        data.append(numbers)
        print(f"Sorted Winning Numbers: {numbers}")  # Debug print

    # Write data to CSV 
    with open('powerball_numbers.csv', 'w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(["Winning Numbers"])  # Single header for the numbers
        writer.writerows([[', '.join(map(str, row))] for row in data])  # Join sorted numbers in a single column

    print("Data written to powerball_numbers.csv")