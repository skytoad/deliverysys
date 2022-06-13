import csv
from deliverysys.obj.hashmap import Hashmap


def get_list_from_csv(filename):
    # Access csv file from data directory
    with open('deliverysys/data/' + filename) as csvfile:
        csv_reader = csv.reader(csvfile)

        # Empty list to hold csv results
        csv_list = []

        # Read each row and add to list
        for row in csv_reader:
            csv_list.append(row)

        return csv_list
