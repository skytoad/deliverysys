from deliverysys.obj.distance import get_distances
from deliverysys.obj.address import get_address_index

class Truck:
    def __init__(self, id):
        self.id = id
        self.mileage = 0.0
        self.inventory = []
        self.route = []

    # Add single package to inventory:
    # O(1)
    def _load_package(self, package):
        self.inventory.append(package)

    # Given list of all packages, extract all individual packages marked with this Truck's id
    # O(n)
    def load_packages(self, packages):
        i = 1
        while i <= len(packages):

            # Identify Package in hashmap with matching id
            package = packages.search(i)

            # Compare Package id to Truck id
            if package.truck == self.id:
                package.status = "EN ROUTE"

                # Add to inventory
                self._load_package(package)

            i += 1

        # Apply our core algorithm to find a more efficient route between packages in inventory
        self.route = self.find_greedy_route()

    # Mark Package as delivered, and remove from this truck's route
    # O(1)
    def deliver(self, package, time):
        package.status = "DELIVERED " + str(time)

        self.route.pop(0)

        if len(self.route) == 0:
            distances = get_distances()

            last_stop_address_index = get_address_index(package.address)

            self.mileage += float(distances[0][last_stop_address_index])

            print("Returning to hub.")

    # Using inventory of this truck, create a more efficient route between each package
    # Time: O(n^2)
    # Space: O(n)
    def find_greedy_route(self):
        # Start with empty route
        route = []

        # Get package and distance data
        packages = self.inventory
        distances = get_distances()

        # Default starting address is HUB, index 0
        starting_address_index = 0

        # Track the total distance of the route
        totaldist = 0.0

        # Repeat once for each package in inventory
        for i in range(len(packages)):
            # Dummy value
            lowest_val = 50.0

            # Comparing each package in inventory, find shortest distance between starting address and package address
            for package in packages:

                # Get value from distances list
                dist = float(distances[get_address_index(package.address)][starting_address_index])

                # Compare to previous lowest value
                if dist < lowest_val:
                    # Select this package as primary candidate for next stop on route
                    package_to_add = package

                    # Update lowest_val to reflect new lowest distance
                    lowest_val = dist

            # Update total distance in route
            totaldist += lowest_val
            # After searching all packages, add selected package and distance info to route
            route.append([package_to_add, round(totaldist, 1)])

            # Remove selected package from candidate list
            packages.remove(package_to_add)

            # Next segment of route begins from selected package address
            starting_address_index = get_address_index(package_to_add.address)

            i += 1

        return route
