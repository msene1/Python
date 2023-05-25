from car import Car
from motorcycle import Motorcycle
from bus import Bus
from electric_scooter import ElectricScooter
from bicycle import Bicycle

vehicles = []

def add_vehicle():
    vehicle_type = input("Enter vehicle type (car/motorcycle/bus/scooter/bicycle): ")
    brand = input("Enter brand: ")
    model = input("Enter model: ")
    year = input("Enter year: ")
    color = input("Enter color: ")
    num_vignette_critair = input("Enter Crit'Air Vignette number: ")

    if vehicle_type == "car":
        vehicle = Car(brand, model, year, color, num_vignette_critair)
    elif vehicle_type == "motorcycle":
        vehicle = Motorcycle(brand, model, year, color, num_vignette_critair)
    elif vehicle_type == "bus":
        vehicle = Bus(brand, model, year, color, num_vignette_critair)
    elif vehicle_type == "scooter":
        vehicle = ElectricScooter(brand, model, year, color, num_vignette_critair)
    elif vehicle_type == "bicycle":
        vehicle = Bicycle(brand, model, year, color, num_vignette_critair)
    else:
        print("Invalid vehicle type.")
        return

    vehicles.append(vehicle)
    print("Vehicle added successfully.")

def remove_vehicle():
    if len(vehicles) == 0:
        print("No vehicles to remove.")
        return

    print("Select a vehicle to remove:")
    for index, vehicle in enumerate(vehicles):
        print(f"{index + 1}. {vehicle.get_brand()} {vehicle.get_model()}")

    choice = int(input("Enter vehicle number: "))
    if choice < 1 or choice > len(vehicles):
        print("Invalid vehicle number.")
        return

    removed_vehicle = vehicles.pop(choice - 1)
    print(f"Removed {removed_vehicle.get_brand()} {removed_vehicle.get_model()} successfully.")

def modify_vehicle():
    if len(vehicles) == 0:
        print("No vehicles to modify.")
        return

    print("Select a vehicle to modify:")
    for index, vehicle in enumerate(vehicles):
        print(f"{index + 1}. {vehicle.get_brand()} {vehicle.get_model()}")

    choice = int(input("Enter vehicle number: "))
    if choice < 1 or choice > len(vehicles):
        print("Invalid vehicle number.")
        return

    vehicle = vehicles[choice - 1]
    brand = input("Enter brand (press Enter to skip): ")
    if brand:
        vehicle.brand = brand

    model = input("Enter model (press Enter to skip): ")
    if model:
        vehicle.model = model

    year = input("Enter year (press Enter to skip): ")
    if year:
        vehicle.year = year

    color = input("Enter color (press Enter to skip): ")
    if color:
        vehicle.color = color

    num_vignette_critair = input("Enter Crit'Air Vignette number (press Enter to skip): ")
    if num_vignette_critair:
        vehicle.num_vignette_critair = num_vignette_critair

    print(f"Modified {vehicle.get_brand()} {vehicle.get_model()} successfully.")

def display_statistics():
    print("==== Vehicle Statistics ====")
    print(f"Total Vehicles: {len(vehicles)}")
    print(f"Total Cars: {Car.car_count}")
    print(f"Total Motorcycles: {Motorcycle.motorcycle_count}")
    print(f"Total Buses: {Bus.bus_count}")
    print(f"Total Electric Scooters: {ElectricScooter.scooter_count}")
    print(f"Total Bicycles: {Bicycle.bicycle_count}")

    color = input("Enter color to get count (press Enter to skip): ")
    if color:
        color_count = sum(1 for vehicle in vehicles if vehicle.get_color().lower() == color.lower())
        print(f"Total {color.capitalize()} Vehicles: {color_count}")

    vignette_critair = input("Enter Crit'Air Vignette number to get count (press Enter to skip): ")
    if vignette_critair:
        vignette_count = sum(1 for vehicle in vehicles if vehicle.get_num_vignette_critair().lower() == vignette_critair.lower())
        print(f"Total Vehicles with Crit'Air Vignette {vignette_critair}: {vignette_count}")

def display_menu():
    print("==== Vehicle Management System ====")
    print("1. Add Vehicle")
    print("2. Remove Vehicle")
    print("3. Modify Vehicle")
    print("4. Display Statistics")
    print("5. Quit")

def main():
    while True:
        display_menu()
        choice = input("Enter your choice: ")

        if choice == "1":
            add_vehicle()
        elif choice == "2":
            remove_vehicle()
        elif choice == "3":
            modify_vehicle()
        elif choice == "4":
            display_statistics()
        elif choice == "5":
            break
        else:
            print("Invalid choice. Please try again.")

    print("Exiting Vehicle Management System.")


if __name__ == "__main__":
    main()
