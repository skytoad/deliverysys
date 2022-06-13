from deliverysys.csv_reader import get_list_from_csv


def get_distances():
    addresses_and_distances = get_list_from_csv('WGUPS Distance Table.csv')

    distances = []

    # Ignore first two entries in each row, which contain unnecessary address data
    for row in addresses_and_distances:
        distances.append(row[2:])

    return distances
