"""
Practica1: Hacer un programa que maneje un inventario 
de una tienda que devuelva el nombre del 
producto cantidad y precio.

Por medio del siguient programa lograremos
hacer un programa que nos ayude a identificar
el tipo producto que tenemos en una tienda
su precio y catidad.

Autor: Daniel Gustavo Montañez Hurtado 
<dgmontanezh@academia.usbbog.edu.co>
Fecha: 2025-02-25
"""

class product:
    def __init__(self, name, price_per_unit, amount):
        self.name = name
        self.price_per_unit = price_per_unit
        self.amount = amount
        
    def __str__(self):
        return f"- {self.name:<10} - {self.price_per_unit:<12} - {self.amount:<10} cop -"

def get_product(num_product):
    name = input(f'product {num_product}, what is the product name')
    price_per_unit = float(input(f'which is the product price of {name}?'))
    amount = int(input(f'how much {name} do we have?'))
    
    return product(name, amount, price_per_unit)

def show_sumary(products):
    print("\nSumary:")
    print("product - amount - price_per_unit")
    for product in products:
        print(product)

def main():
    products = []
    
    
    for i in range (1, 4):
        product = get_product(i)
        products.append(product)
        
        show_sumary(products)
        
if __name__ == "__main__":
    main()

    
    