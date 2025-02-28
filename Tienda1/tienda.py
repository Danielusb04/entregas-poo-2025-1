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


class Product:
    def __init__(self, name, price_per_unit, amount): # we creat the class and the init constructure get the values
        self.name = name
        self.price_per_unit = price_per_unit
        self.amount = amount

    def __str__(self):  # it rerund a lash with the name, ammount and price
        return f' - {self.name:<10} - {self.amount:<12} - {self.price_per_unit:<10} cop'


def get_product(num_product): # here is where we reuqest to the user the information
    name = input(f'Product {num_product}, what is the product name? ')
    price_per_unit = float(input(f'What is the price of {name}? '))
    amount = int(input(f'How many {name} do we have? '))
    return Product(name, price_per_unit, amount)


def show_summary(products): # show summary helps us to creat the table
    print("\nSummary:")
    print("Product       Amount       Price per unit")
    for product in products:
        print(product)


def main(): # with the main i create a blank list where data would be save
    products = []
    for i in range(1, 4):
        product = get_product(i)
        products.append(product)
    show_summary(products)


if __name__ == "__main__": #excute this code
    main()
