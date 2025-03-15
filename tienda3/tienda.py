"""
Practica1: Hacer un programa que maneje un inventario
de una tienda que devuelva el nombre del producto, cantidad y precio.

Por medio del siguiente programa lograremos
hacer un programa que nos ayude a identificar
el tipo de producto que tenemos en una tienda,
su precio y cantidad.

Autor: Daniel Gustavo Montañez Hurtado
<dgmontanezh@academia.usbbog.edu.co>
Fecha: 2025-02-25
"""

# we define the class product and int is the constructure of the class


class Product:
    def __init__(self, name, price_per_unit, amount, description, category):
        self.name = name
        self.price_per_unit = price_per_unit
        self.amount = amount
        self.description = description
        self.category = category

    # STR allows us to print in columns
    def __str__(self):
        return f' - {self.name:<15} - {self.amount:<10} - {self.price_per_unit:<12.2f} COP - {self.category:<15} - {self.description}'

    # This quotes the united price times the amount of it
    def total_price(self):
        return self.price_per_unit * self.amount

    # Returns the total price for an specific product
    def calcula_precio(self, cantidad):
        return self.price_per_unit * cantidad

    # Retunrs the total value of the inventary
    def inventario_precio(self):
        return self.total_price()


def get_product(num_product):
    name = input(f'Product {num_product}, what is the product name?')
    price_per_unit = float(input(f'What is the price of {name}?'))
    # Ensure valid input for amount
    while True:
        try:
            amount = int(input(f'How many {name} do we have?'))
            if amount < 0:
                print("Amount cannot be negative. Please enter a valid number.")
            else:
                break
        except ValueError:
            print("Invalid input. Please enter a valid number for amount.")

    description = input(f'Please describe {name}: ')
    category = input(f'What is the category name for {name}? ')
    return Product(name, price_per_unit, amount, description, category)


# show us the sumarry of the products
def show_summary(products):
    print("\nSummary:")
    print(f"{'Product':<15}{'Amount':<10}{'Price per unit':<20}{'Category':<20}{'Description'}")
    for product in products:
        print(product)


# This rejoin aall the product, sumaries them while print the toral price per product
def show_category_summary(products):
    categories = {}
    for product in products:
        if product.category not in categories:
            categories[product.category] = 0
        categories[product.category] += product.total_price()


    print("\nCategory summary:")
    for category, total_price in categories.items():
        print(f'Category: {category:<15} - Total Price: {total_price:.2f} COP')


def main():
    num_products = int(input("How many products would you like to enter? "))
    products = []
    for i in range(1, num_products + 1):
        product = get_product(i)
        products.append(product)

    # Show all product
    show_summary(products)

    # Get the price per unit times 5
    print("\nPrice for 5 units of each product:")
    for product in products:
        print(f'{product.name}: {product.calcula_precio(5):.2f} COP')

    # Show category sumary
    show_category_summary(products)

if __name__ == "__main__":
    main()
