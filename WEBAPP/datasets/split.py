import csv
import sys
import random
import collections

maxInt = sys.maxsize

while True:
    # decrease the maxInt value by factor 10
    # as long as the OverflowError occurs.
    try:
        csv.field_size_limit(maxInt)
        break
    except OverflowError:
        maxInt = int(maxInt/10)


def extract_rows(input_file, output_file_1, output_file_2, num_rows, target_column_index):
    with open(input_file, 'r', newline='', encoding='utf-8') as file:
        reader = csv.reader(file)
        header = next(reader)  # Read and store the header

        data = list(reader)  # Read all rows into a list
        random.shuffle(data)  # Shuffle the list

        data_1 = data[:num_rows]  # First num_rows for training
        data_2 = data[num_rows:]  # Remaining rows

        # Count the number of 1s and 0s in the target column of the training data
        counter = collections.Counter(row[target_column_index] for row in data_1)
        print(f"In the trimmed dataset: {counter}")

    with open(output_file_1, 'w', newline='', encoding='utf-8') as file:
        writer = csv.writer(file)
        writer.writerow(header)
        writer.writerows(data_1)

    with open(output_file_2, 'w', newline='', encoding='utf-8') as file:
        writer = csv.writer(file)
        writer.writerow(header)
        writer.writerows(data_2)


# Usage example
input_file = 'WELFake_Dataset.csv'
output_file_1 = 'trimmed-WEL.csv'
output_file_2 = 'remaining-WEL.csv'
num_rows = 3000
target_column_index = -1  # change it to the number of column where the labels are located

extract_rows(input_file, output_file_1, output_file_2, num_rows, target_column_index)