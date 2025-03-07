import unittest
from io import StringIO
import sys


from tienda import Product, get_product, show_summary, show_category_summary

class TestProduct(unittest.TestCase):

    # Test to check the product creation
    def test_product_creation(self):
        product = Product("Apple", 2.5, 10, "Fresh red apples", "Fruits")
        self.assertEqual(product.name, "Apple")
        self.assertEqual(product.price_per_unit, 2.5)
        self.assertEqual(product.amount, 10)
        self.assertEqual(product.description, "Fresh red apples")
        self.assertEqual(product.category, "Fruits")

    # Test to check out the quote of the prodcut
    def test_total_price(self):
        product = Product("Apple", 2.5, 10, "Fresh red apples", "Fruits")
        self.assertEqual(product.total_price(), 25.0)

    # Test for the futnon show category
    def test_show_category_summary(self):
        # some product as example are created
        products = [
            Product("Apple", 2.5, 10, "Fresh red apples", "Fruits"),
            Product("Banana", 1.2, 20, "Yellow bananas", "Fruits"),
            Product("Carrot", 1.5, 5, "Fresh carrots", "Vegetables")
        ]
        
        captured_output = StringIO()
        sys.stdout = captured_output
        
        show_category_summary(products)
        
        # This if for chect the categories
        self.assertIn("Category: Fruits", captured_output.getvalue())
        self.assertIn("Category: Vegetables", captured_output.getvalue())
        self.assertIn("Total Price", captured_output.getvalue())
        
        sys.stdout = sys.__stdout__

    # Test for the summary
    def test_show_summary(self):
        # some examples
        products = [
            Product("Apple", 2.5, 10, "Fresh red apples", "Fruits"),
            Product("Banana", 1.2, 20, "Yellow bananas", "Fruits"),
            Product("Carrot", 1.5, 5, "Fresh carrots", "Vegetables")
        ]
        
        captured_output = StringIO()
        sys.stdout = captured_output
        
        show_summary(products)
        
        # we get the retund for the products
        self.assertIn("Apple", captured_output.getvalue())
        self.assertIn("Banana", captured_output.getvalue())
        self.assertIn("Carrot", captured_output.getvalue())
        self.assertIn("2.5", captured_output.getvalue())  # This verify that the information apperar
        
        # get the reply
        sys.stdout = sys.__stdout__

if __name__ == '__main__':
    unittest.main()
