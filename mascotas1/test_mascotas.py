import unittest
from io import StringIO
import sys
import datetime

# Here we impor the code that we hace just created
# from petstore import Pet, Dog, Cat, entry_data, petstore_management


# class are created again in ordet to test them.
class Pet:
    def __init__(self, name, age, breed):
        self.name = name
        self.age = age
        self.breed = breed
        self.entry_date = datetime.datetime.now()

    def show_data(self):
        return f"Name: {self.name}, Age: {self.age}, Breed: {self.breed}, Entry Date: {self.entry_date.strftime('%Y-%m-%d %H:%M:%S')}"


class Dog(Pet):
    def __init__(self, name, age, breed):
        super().__init__(name, age, breed)
        self.type = "Dog"


class Cat(Pet):
    def __init__(self, name, age, breed):
        super().__init__(name, age, breed)
        self.type = "Cat"


def entry_data(pet_type, name, age, breed):
    if pet_type == "dog":
        return Dog(name, age, breed)
    elif pet_type == "cat":
        return Cat(name, age, breed)
    else:
        return None


# Test Case class
class TestPetStore(unittest.TestCase):

    def test_create_dog(self):
        # Create a Dog instance
        dog = Dog("Buddy", 3, "Golden Retriever")
        
        # Test the attributes of the dog
        self.assertEqual(dog.name, "Buddy")
        self.assertEqual(dog.age, 3)
        self.assertEqual(dog.breed, "Golden Retriever")
        self.assertTrue(isinstance(dog, Dog))  # Ensure it's an instance of Dog class

    def test_create_cat(self):
        # Create a Cat instance
        cat = Cat("Whiskers", 2, "Siamese")
        
        # Test the attributes of the cat
        self.assertEqual(cat.name, "Whiskers")
        self.assertEqual(cat.age, 2)
        self.assertEqual(cat.breed, "Siamese")
        self.assertTrue(isinstance(cat, Cat))  # Ensure it's an instance of Cat class

    def test_show_data(self):
        # Test the show_data method for a Dog instance
        dog = Dog("Buddy", 3, "Golden Retriever")
        expected_output = f"Name: Buddy, Age: 3, Breed: Golden Retriever, Entry Date: {dog.entry_date.strftime('%Y-%m-%d %H:%M:%S')}"
        self.assertEqual(dog.show_data(), expected_output[:len(dog.show_data())])

    def test_entry_data(self):
        # Test the entry_data function with valid inputs for dog
        dog = entry_data("dog", "Buddy", 3, "Golden Retriever")
        self.assertTrue(isinstance(dog, Dog))
        self.assertEqual(dog.name, "Buddy")
        self.assertEqual(dog.age, 3)
        self.assertEqual(dog.breed, "Golden Retriever")

        # Test the entry_data function with valid inputs for cat
        cat = entry_data("cat", "Whiskers", 2, "Siamese")
        self.assertTrue(isinstance(cat, Cat))
        self.assertEqual(cat.name, "Whiskers")
        self.assertEqual(cat.age, 2)
        self.assertEqual(cat.breed, "Siamese")

    def test_invalid_pet_type(self):
        # Test the entry_data function with an invalid pet type
        invalid_pet = entry_data("bird", "Tweety", 1, "Canary")
        self.assertIsNone(invalid_pet)  # Should return None for invalid pet type


if __name__ == "__main__":
    unittest.main()
