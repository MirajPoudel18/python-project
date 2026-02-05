#Vehicle Rental System using python class


class vehicle:
    def __init__(self, vehicle_id, brand, model, year, daily_rate):
        self.vehicle_id = vehicle_id
        self.brand = brand
        self.model = model
        self.year = year
        self.daily_rate = daily_rate
        self.is_available = True
        self.current_renter = None

class car(vehicle):
    def __init__(self, vehicle_id, brand, model, year, daily_rate, num_seats, trunk_capacity):
        super().__init__(vehicle_id, brand, model, year, daily_rate)
        self.num_seats = num_seats
        self.trunk_capacity = trunk_capacity
        self.vehicletype = "car"

class bike(vehicle):
    def __init__(self, vehicle_id, brand, model, year, daily_rate, engine_capacity, has_sidecar):
        super().__init__(vehicle_id, brand, model, year, daily_rate)
        self.engine_capacity = engine_capacity
        self.has_sidecar = has_sidecar
        self.vehicletype = "bike"

class bus(vehicle):
    def __init__(self, vehicle_id, brand, model, year, daily_rate, num_seats, trunk_capacity):
        super().__init__(vehicle_id, brand, model, year, daily_rate)
        self.num_seats = num_seats
        self.trunk_capacity = trunk_capacity
        self.vehicletype = "bus"

class customer:
    def __init__(self, customer_id, name, email, phone):  
        self.customer_id = customer_id
        self.name = name
        self.email = email
        self.phone = phone
        self.rental_history = []

class rental_info:
    def __init__(self):
        self.vehicle = []
        self.customer = []
        self.active_rental = []
    
    def add_vehicle(self, vehicle):
        self.vehicle.append(vehicle) 
    
    def register_customer(self, customer):
        self.customer.append(customer)
    
    def rent_vehicle(self, customer, vehicle, days):
        if vehicle.is_available:
            vehicle.is_available = False
            vehicle.current_renter = customer
            total_cost = vehicle.daily_rate * days

            rental_record = {
                "customer": customer,
                "vehicle": vehicle,
                "days": days,
                "total_cost": total_cost
            }
            self.active_rental.append(rental_record)
            customer.rental_history.append(rental_record)
            return f"Rental successful! Total: ${total_cost}"
        else:
            return "Vehicle not available"
    
    def return_vehicle(self, vehicle):
        vehicle.is_available = True
        vehicle.current_renter = None
        self.active_rental = [r for r in self.active_rental if r['vehicle'] != vehicle]  # ✅ Fixed

# Create rental system
rental_shop = rental_info()
car1 = car("0034", "bmw", "m3", 2022, 10, 2, 10)
bike1 = bike("098", "yamma", "32", 2021, 15, 70, False)
bus1 = bus("098", "tesla", "43", 2014, 20, 40, 20)

rental_shop.add_vehicle(car1)
rental_shop.add_vehicle(bike1)
rental_shop.add_vehicle(bus1)

# Register customer
customer1 = customer("CU001", "John Doe", "john@email.com", "555-1234")
rental_shop.register_customer(customer1)

# Rent a vehicle
print(rental_shop.rent_vehicle(customer1, car1, 3))

# Try to rent same vehicle (should fail)
print(rental_shop.rent_vehicle(customer1, car1, 2))

# Return vehicle
rental_shop.return_vehicle(car1)