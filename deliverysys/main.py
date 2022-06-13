# Tyler Astle, Student ID: 002187769
from obj.package import get_package_hashmap
from obj.package import print_all_package_details
from obj.truck import Truck
from delivery_controller import DeliveryController
from datetime import time


class Main:
    # Initialize trucks
    truck1 = Truck("1")
    truck2 = Truck("2")
    truck3 = Truck("3")
    trucks = [truck1, truck2, truck3]

    # Initialize packages hashmap
    packages = get_package_hashmap()

    # Initialize delivery controller
    controller = DeliveryController()

    # Load first 2 trucks with packages: 3rd will be loaded once package #9 address is corrected
    truck1.load_packages(packages)
    truck2.load_packages(packages)
    package9_address_corrected = False

    # Take user input, and run program until user exits
    while True:
        input_string = input(
            'Current time is ' + str(controller.clock.time()) +
            '. Enter an integer to advance time by that many minutes, and view package status. '
            'Or, type Exit: ')

        if input_string == "Exit":
            exit(1)

        # Number of minutes to advance time
        amt_minutes = int(input_string)

        # Advance time in increments of one minute, until the specified number of minutes has elapsed
        controller.skip_to_time(amt_minutes, trucks)

        # Once 10:20AM is reached, correct package #9 address and load truck 3
        if (controller.clock.time() >= time(10, 20)) & (package9_address_corrected == False):
            packages.search(9).address = "410 S State St"
            packages.search(9).zip = "84111"

            truck3.load_packages(packages)

            package9_address_corrected = True

            print("Loading truck 3")

        # Display all info for all packages
        print_all_package_details(packages)

        # Display truck mileage
        for truck in trucks:
            print("Truck " + str(truck.id) + " mileage: " + str(round(truck.mileage, 1)))

        print("Total mileage: " + str(round(truck1.mileage + truck2.mileage + truck3.mileage, 1)))
