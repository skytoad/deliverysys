from datetime import datetime
from datetime import timedelta


class DeliveryController:

    def __init__(self):
        self.clock = datetime(2021,1,15,8,0,0,0)

    # Increment time
    # O(n)
    def advance_time(self, amt_minutes, trucks):
        # Advance clock by provided number of minutes
        self.clock += timedelta(minutes=amt_minutes)

        print(self.clock.time())

        # Track which trucks are currently active (have drivers and have left the hub)
        active_trucks = [trucks[0]]

        # If it is past 9:05, add second truck to active fleet
        if self.clock.time() > self.clock.time().replace(hour=9, minute=5):
            active_trucks.append(trucks[1])

        # If it is past 10:20, add third truck to active fleet, and remove first truck
        if self.clock.time() > self.clock.time().replace(hour=10, minute=20):
            active_trucks.append(trucks[2])
            active_trucks.remove(trucks[0])

        # Run delivery simulation for each truck
        for truck in active_trucks:
            if len(truck.route) > 0:

                # Increase mileage to reflect elapsed time
                truck.mileage += float(amt_minutes) * 0.3

                # Read delivery information from route
                next_delivery = truck.route[0]
                next_package = next_delivery[0]
                mileage_at_next_delivery = next_delivery[1]

                # If truck has traveled far enough, deliver next package on route
                if truck.mileage >= mileage_at_next_delivery:
                    print("Delivering package, ID: " + str(next_package.id))
                    truck.deliver(next_package, self.clock.time())

        return True

    # Execute advance_time() with increment of 1 minute, and repeat x times
    # O(n)
    def skip_to_time(self, amt_minutes, trucks):
        for i in range(0, amt_minutes):
            self.advance_time(1, trucks)

        return
