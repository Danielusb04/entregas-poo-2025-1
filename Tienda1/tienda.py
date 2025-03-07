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
    def __init__(self, name, price_per_unit, amount, description, category):
        # we creat the class and the init constructure get the values
        self.name = name
        self.price_per_unit = price_per_unit
        self.amount = amount
        self.description = description
        self.category = category

    def __str__(self):  # it rerund a lash with the name, ammount and price
        return f' - {self.name:<10} - {self.amount:<12} - {self.price_per_unit:<10} cop - {self.category:<10} - {self.description}'

    def total_price(self):
        return self.price_per_unit * self.amount


# here is where we reuqest to the user the information
def get_product(num_product):
    name = input(f'Product {num_product}, what is the product name?')
    price_per_unit = float(input(f'What is the price of {name}? '))
    amount = int(input(f'How many {name} do we have? '))
    description = input((f'pleasde describe {name}'))
    category = input(f'What is the category name for {name}?')
    return Product(name, price_per_unit, amount, description, category)


def show_summary(products):
    print("\nSummary:")
    print(f"{'Product':<10}{'amount':<12}{'price per unit':<20}{'category':<20}{'description'}")
    for product in products:
        print(product)
    # show summary helps us to creat the table


def show_category_summary(products):
    categories = {}
    for product in products:
        if product.category not in categories:
            categories[product.category] = 0
        categories[product.category] += product.total_price()

    print("\nCategory summary:")
    for category, total_price in categories.items():
        print(f'category: {category} - total price: {total_price:.2f} cop')


def main():
    num_products = int(input("How many products would you like to enter?"))
    products = []
    for i in range(1, num_products + 1):
        product = get_product(i)
        products.append(product)
    # with the main i create a blank list where data would be save

    show_summary(products)
    show_category_summary(products)


# excute this code
if __name__ == "__main__":
    main()
