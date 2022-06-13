from deliverysys.csv_reader import get_list_from_csv


def get_addresses():
    addresses_and_distances = get_list_from_csv('WGUPS Distance Table.csv')

    addresses = []

    # Read only the first entry from each row; rest of row contains unnecessary distance data
    for row in addresses_and_distances:
        entry = str(row[0])

        addresses.append(entry)

    return addresses


def get_address_index(address):
    for i, s in enumerate(get_addresses()):
        if address in s:
            return i
    return -1
