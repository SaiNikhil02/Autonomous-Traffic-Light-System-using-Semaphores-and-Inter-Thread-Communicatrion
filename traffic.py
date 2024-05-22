import threading
import time
import random

# Define the TrafficLight class
class TrafficLight:
    def __init__(self):
        self.green_light = threading.Semaphore(1)  # Initially green light for one direction
        self.red_light = threading.Semaphore(0)  # Initially red light for the other direction

    def switch_lights(self):
        self.green_light.acquire()
        self.red_light.release()

# Define the Intersection class
class Intersection:
    def __init__(self):
        self.north_south = TrafficLight()
        self.east_west = TrafficLight()

    def run_traffic_lights(self):
        while True:
            # North-South direction gets green light
            print("North-South Green Light")
            self.north_south.green_light.release()
            self.east_west.red_light.acquire()
            time.sleep(random.randint(5, 15))  # Adjust time based on traffic

            # Switch lights
            self.north_south.switch_lights()
            self.east_west.switch_lights()

            # East-West direction gets green light
            print("East-West Green Light")
            self.east_west.green_light.release()
            self.north_south.red_light.acquire()
            time.sleep(random.randint(5, 15))  # Adjust time based on traffic

            # Switch lights
            self.east_west.switch_lights()
            self.north_south.switch_lights()
class Vehicle(threading.Thread):
    def __init__(self, direction, intersection):
        threading.Thread.__init__(self)
        self.direction = direction
        self.intersection = intersection

    def run(self):
        if self.direction == "North-South":
            self.intersection.north_south.green_light.acquire()
            print(f"Vehicle passing through North-South direction")
            time.sleep(1)  # Simulate time taken to pass the intersection
            self.intersection.north_south.green_light.release()
        else:
            self.intersection.east_west.green_light.acquire()
            print(f"Vehicle passing through East-West direction")
            time.sleep(1)  # Simulate time taken to pass the intersection
            self.intersection.east_west.green_light.release()

def generate_vehicles(intersection):
    while True:
        direction = random.choice(["North-South", "East-West"])
        vehicle = Vehicle(direction, intersection)
        vehicle.start()
        time.sleep(random.randint(1, 5))  # Randomly generate vehicles
class DynamicTrafficLight(TrafficLight):
    def __init__(self):
        super().__init__()
        self.traffic_density = 0

    def update_traffic_density(self, density):
        self.traffic_density = density

    def dynamic_switch_lights(self):
        self.green_light.acquire()
        self.red_light.release()
        time.sleep(max(5, 15 - self.traffic_density))  # Adjust based on density

def dynamic_traffic_control(intersection):
    while True:
        # Simulate getting traffic density data
        north_south_density = random.randint(0, 10)
        east_west_density = random.randint(0, 10)
        intersection.north_south.update_traffic_density(north_south_density)
        intersection.east_west.update_traffic_density(east_west_density)

        # North-South direction gets green light
        print("North-South Green Light")
        intersection.north_south.green_light.release()
        intersection.east_west.red_light.acquire()
        time.sleep(max(5, 15 - north_south_density))  # Adjust based on density

        # Switch lights
        intersection.north_south.dynamic_switch_lights()
        intersection.east_west.dynamic_switch_lights()

        # East-West direction gets green light
        print("East-West Green Light")
        intersection.east_west.green_light.release()
        intersection.north_south.red_light.acquire()
        time.sleep(max(5, 15 - east_west_density))  # Adjust based on density

        # Switch lights
        intersection.east_west.dynamic_switch_lights()
        intersection.north_south.dynamic_switch_lights()
if __name__ == "__main__":
    intersection = Intersection()
    traffic_light_thread = threading.Thread(target=intersection.run_traffic_lights)
    vehicle_generation_thread = threading.Thread(target=generate_vehicles, args=(intersection,))
    dynamic_control_thread = threading.Thread(target=dynamic_traffic_control, args=(intersection,))

    traffic_light_thread.start()
    vehicle_generation_thread.start()
    dynamic_control_thread.start()

    traffic_light_thread.join()
    vehicle_generation_thread.join()
    dynamic_control_thread.join()

