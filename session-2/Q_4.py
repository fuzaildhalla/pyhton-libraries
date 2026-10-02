""".
Suppose you have a NumPy array of product prices from Flipkart. Use broadcasting to apply a 10% discount to all prices and print the new array.<br><br><em><strong>Constraint:</strong> Do not use any loops.</em>"""
import numpy as np
flipkart_product_prices = np.arange(500,1000,100)
discount = flipkart_product_prices * 10/100
print(flipkart_product_prices - discount)
