import unittest


class Product:
    def __init__(self, name, price_per_unit, amount, description, category):
        self.name = name
        self.price_per_unit = price_per_unit
        self.amount = amount
        self.description = description
        self.category = category

    def __str__(self):
        return f' - {self.name:<15} - {self.amount:<10} - {self.price_per_unit:<12.2f} COP - {self.category:<15} - {self.description}'

    def total_price(self):
        return self.price_per_unit * self.amount

    def calcula_precio(self, cantidad):
        return self.price_per_unit * cantidad

    def inventario_precio(self):
        return self.total_price()


def get_product(num_product, name, price_per_unit, amount, description, category):
    return Product(name, price_per_unit, amount, description, category)

def show_summary(products):
    summary = []
    for product in products:
        summary.append(str(product))
    return summary

def show_category_summary(products):
    categories = {}
    for product in products:
        if product.category not in categories:
            categories[product.category] = 0
        categories[product.category] += product.total_price()
    summary = []
    for category, total_price in categories.items():
        summary.append(f'Category: {category:<15} - Total Price: {total_price:.2f} COP')
    return summary


# Test cases using unittest
class TestProduct(unittest.TestCase):

    def test_calcula_precio(self):
        # Proves that calcul_precio give us the total price
        product = Product("Producto A", 100, 10, "Descripción A", "Electrónica")
        self.assertEqual(product.calcula_precio(5), 500.00)
        self.assertEqual(product.calcula_precio(1), 100.00)
        self.assertEqual(product.calcula_precio(0), 0.00)

    def test_inventario_precio(self):
        # Proves that inventario_precio is giving the price over inventary
        product = Product("Producto A", 100, 10, "Descripción A", "Electrónica")
        self.assertEqual(product.inventario_precio(), 1000.00)

    def test_total_price(self):
        # Give us the total price ammount
        product = Product("Producto B", 200, 5, "Descripción B", "Muebles")
        self.assertEqual(product.total_price(), 1000.00)

    def test_show_summary(self):
        # Proves that show sumary is working fine
        product1 = Product("Producto A", 100, 10, "Descripción A", "Electrónica")
        product2 = Product("Producto B", 200, 5, "Descripción B", "Muebles")
        products = [product1, product2]
        summary = show_summary(products)
        

        self.assertEqual(len(summary), 2)
        self.assertIn("Producto A", summary[0]) 
        self.assertIn("Producto B", summary[1])

    def test_show_category_summary(self):
        # The sumary per category
        product1 = Product("Producto A", 100, 10, "Descripción A", "Electrónica")
        product2 = Product("Producto B", 200, 5, "Descripción B", "Muebles")
        product3 = Product("Producto C", 150, 3, "Descripción C", "Electrónica")
        products = [product1, product2, product3]
        category_summary = show_category_summary(products)

        # This proves that the category has two products
        self.assertEqual(len(category_summary), 2)
        self.assertIn("Electrónica", category_summary[0])
        self.assertIn("Muebles", category_summary[1])
        
        # The price of each category is correct
        self.assertIn("Total Price: 1500.00", category_summary[0])  
        self.assertIn("Total Price: 1000.00", category_summary[1]) 


# lauch code
if __name__ == '__main__':
    unittest.main()
