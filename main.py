class Vehicle:
    def __init__(self, vin, make, model, daily_rate):
        self.vin = vin
        self.make = make
        self.model = model
        self.daily_rate = daily_rate
        self.available = True

    def start_rental(self):
        if self.available:
            self.available = False
            return True
        return False

    def end_rental(self):
        self.available = True
        return True

    def __str__(self):
        status = "Available" if self.available else "Not Available"
        return f"{self.make} {self.model} (VIN: {self.vin}) - {status}"


class Car(Vehicle):
    def __init__(self, vin, make, model, daily_rate, passenger_capacity):
        super().__init__(vin, make, model, daily_rate)
        self.passenger_capacity = passenger_capacity

    def __str__(self):
        return f"Car: {super().__str__()} - Seats {self.passenger_capacity}"


class Motorcycle(Vehicle):
    def __init__(self, vin, make, model, daily_rate, engine_size):
        super().__init__(vin, make, model, daily_rate)
        self.engine_size = engine_size

    def __str__(self):
        return f"Motorcycle: {super().__str__()} - {self.engine_size}cc"


class Rental:
    def __init__(self, rental_id, vehicle, customer_name, days):
        self.rental_id = rental_id
        self.vehicle = vehicle
        self.customer_name = customer_name
        self.days = days
        self.is_active = True

    def calculate_cost(self):
        return self.vehicle.daily_rate * self.days

    def end_rental(self):
        if not self.is_active:
            return False
        self.is_active = False
        self.vehicle.end_rental()
        return True

    def __str__(self):
        status = "Active" if self.is_active else "Completed"
        return f"Rental {self.rental_id}: {self.vehicle.make} {self.vehicle.model} for {self.customer_name} - {status}"


class RentalAgency:
    def __init__(self, name):
        self.name = name
        self.vehicles = {}
        self.rentals = {}
        self.next_rental_id = 1

    def add_vehicle(self, vehicle):
        self.vehicles[vehicle.vin] = vehicle
        return True

    def rent_vehicle(self, vin, customer_name, days):
        if vin not in self.vehicles:
            return None

        vehicle = self.vehicles[vin]
        if not vehicle.available:
            return None

        rental_id = f"R{self.next_rental_id}"
        self.next_rental_id += 1

        rental = Rental(rental_id, vehicle, customer_name, days)
        vehicle.start_rental()
        self.rentals[rental_id] = rental

        return rental_id

    def return_vehicle(self, rental_id):
        if rental_id not in self.rentals:
            return False

        rental = self.rentals[rental_id]
        if not rental.is_active:
            return False

        return rental.end_rental()

    def available_vehicles(self):
        return [v for v in self.vehicles.values() if v.available]