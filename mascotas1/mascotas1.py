import datetime

# Base class Pet and its constructor


class Pet:

    def __init__(self, name, age, breed):
        self.name = name
        self.age = age
        self.breed = breed
        self.entry_date = datetime.datetime.now()

    def show_data(self):
        # Displays the pet's information
        return (f"Name: {self.name}, Age: {self.age}, Breed: {self.breed}, "
                f"Entry Date: {self.entry_date.strftime('%Y-%m-%d %H:%M:%S')}")


# Derived classes from Pet (Inheritance)
class Dog(Pet):
    def __init__(self, name, age, breed):
        super().__init__(name, age, breed)
        self.type = "Dog"


class Cat(Pet):

    def __init__(self, name, age, breed):
        super().__init__(name, age, breed)
        self.type = "Cat"


# Function to enter the pet's data
def entry_data():

    pet_type = input("Please enter the type of pet (dog/cat): ").strip().lower()
    name = input("Please enter the pet's name: ")
    age = int(input("Please enter the pet's age: "))
    breed = input("Please enter the pet's breed: ")

# Checking the pet type
    if pet_type == "dog":
        return Dog(name, age, breed)
    elif pet_type == "cat":
        return Cat(name, age, breed)

    else:
        print("Invalid pet type.")
        return None


# Main function to manage the veterinary store
def petstore_management():

    pets = []

    while True:
        print("\n1. Enter pet:")
        print("2. Show all registered pets:")
        print("3. Exit:")
        option = input("Select an option: ")

        if option == "1":
            pet = entry_data()
            if pet:
                pets.append(pet)
                print(f"{pet.name} has been successfully added!")
            else:
                print("No pet was added.")
        elif option == "2":
            if pets:  # Check if the pets list is not empty
                print("\nSummary of registered pets:")
                for pet in pets:
                    print(pet.show_data())
            else:
                print("No pets have been registered yet.")

        elif option == "3":
            print("Thank you for using our pet service.")
            break
        else:
            print("Invalid choice, please try again.")
# Initializing the program


petstore_management()
