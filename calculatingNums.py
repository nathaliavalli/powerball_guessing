import csv
# main.py
from scraping import powerball_numbers_scrapping  # Function that scrapes data and saves it

def probability_groups():

    # Initialize counters
    total_numbers = 0
    numbers_1_to_10 = 0
    numbers_11_to_20 = 0
    numbers_21_to_30 = 0
    numbers_31_to_40 = 0
    numbers_41_to_50 = 0
    numbers_51_to_60 = 0

    # Read the CSV file
    with open('powerball_numbers.csv', 'r') as file:
        reader = csv.reader(file)
        next(reader)  # Skip header
        for row in reader:
            # Each row contains a string of numbers separated by commas, split it into individual numbers
            numbers = [int(num) for num in row[0].split(', ')]
            
            # Update total count of numbers
            total_numbers += len(numbers)
            
            # Count how many numbers 
            numbers_1_to_10 += sum(1 for num in numbers if 1 <= num <= 10)
            numbers_11_to_20 += sum(1 for num in numbers if 11 <= num <= 20)
            numbers_21_to_30 += sum(1 for num in numbers if 21 <= num <= 30)
            numbers_31_to_40 += sum(1 for num in numbers if 31 <= num <= 40)
            numbers_41_to_50 += sum(1 for num in numbers if 41 <= num <= 50)
            numbers_51_to_60 += sum(1 for num in numbers if 51 <= num <= 60)

    # Calculate probability
    probability_1_10 = numbers_1_to_10 / total_numbers if total_numbers > 0 else 0
    probability_11_20 = numbers_11_to_20 / total_numbers if total_numbers > 0 else 0
    probability_21_30 = numbers_21_to_30 / total_numbers if total_numbers > 0 else 0
    probability_31_40 = numbers_31_to_40 / total_numbers if total_numbers > 0 else 0
    probability_41_50 = numbers_41_to_50 / total_numbers if total_numbers > 0 else 0
    probability_51_60 = numbers_51_to_60 / total_numbers if total_numbers > 0 else 0


    print(f"Total numbers drawn: {total_numbers}")
    print(f"Occurrences of numbers between 1 and 10: {numbers_1_to_10}")
    print(f"Probability of drawing a number from 1 to 10: {probability_1_10:.4f}\n")

    print(f"Occurrences of numbers between 11 and 20: {numbers_11_to_20}")
    print(f"Probability of drawing a number from 11 to 20: {probability_11_20:.4f}\n")

    print(f"Occurrences of numbers between 21 and 30: {numbers_21_to_30}")
    print(f"Probability of drawing a number from 21 to 30: {probability_21_30:.4f}\n")

    print(f"Occurrences of numbers between 31 and 40: {numbers_31_to_40}")
    print(f"Probability of drawing a number from 31 to 40: {probability_1_10:.4f}\n")

    print(f"Occurrences of numbers between 41 and 50: {numbers_41_to_50}")
    print(f"Probability of drawing a number from 41 to 50: {probability_41_50:.4f}\n")

    print(f"Occurrences of numbers between 51 and 60: {numbers_51_to_60}")
    print(f"Probability of drawing a number from 51 to 60: {probability_51_60:.4f}\n")