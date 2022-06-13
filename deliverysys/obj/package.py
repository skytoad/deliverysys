from deliverysys.obj.hashmap import Hashmap
from deliverysys.csv_reader import get_list_from_csv

class Package:
    def __init__(self, id, address, city, zip, deadline, mass, truck, status):
        self.id = id
        self.address = address
        self.city = city
        self.zip = zip
        self.deadline = deadline
        self.mass = mass
        self.truck = truck
        self.status = status

    def get_details(self):
        return [self.id, self.address, self.city, self.zip, self.deadline, self.mass, self.truck, self.status]

    def __str__(self):
        return str(self.id)


def get_package_hashmap():
    # Get raw data from csv
    packages_raw = get_list_from_csv('WGUPS Package File.csv')

    # Initialize hashmap to hold all package data
    packages = Hashmap(len(packages_raw))

    # Read each attribute from each row
    for row in packages_raw:
        id = int(row[0])
        address = row[1]
        city = row[2]
        zip = row[4]
        deadline = row[5]
        mass = row[6]
        truck = row[7]
        status = "AT THE HUB"

        # Create Package that holds all data in attributes
        package = Package(id, address, city, zip, deadline, mass, truck, status)

        # Add new package to hashmap
        packages.insert(package.id, package)

    return packages

def print_all_package_details(packages):
    print("------------------------------PACKAGE DETAILS:------------------------------")
    i = 1

    while i <= 40:
        print(packages.search(i).get_details())

        i += 1

    print("----------------------------------------------------------------------------")
    return True