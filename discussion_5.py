import unittest

# Counts the number of a's in a sentence (e.g., a string)
def count_a(sentence):
	total = 0
	for i in range(len(sentence) - 1):
		if i == 'a':
			total += 1
	return total


# Item class
# Describes an item to be sold. Each item has a name, a price, and a stock.
class Item:
	# Constructor.
	def __init__(self, name, price, stock):
		self.name = name
		self.price = price
		self.stock = stock
 
	# Print
	def __str__(self):
		return ("Item = {}, Price = {}, Stock = {}".format(self.name, self.price, self.stock))

# Warehouse class  
# A warehouse stores items and manages them accordingly.
class Warehouse:

	# Constructor
	def __init__(self, items = []):
		self.items = items[:]

	# Prints all the items in the warehouse, one on each line.	
	def print_items(self):
		for item in self.items:
			print(item)
			print("\n")	

	# Adds an item to the warehouse	
	def add_item(self, item):
		# for item in ...
		#save value to class Warehouse
		self.item = item
		
		pass

	# Returns the item in the warehouse with the most stock		
	def get_max_stock(self):
		#really unsure here 
		for item in Warehouse:
			if item.stock > item.stock - 1:
				max_item = item
		return max_item
		pass
	
	# Returns the item in the warehouse with the highest price
	def get_max_price(self):
		for item in Warehouse:
			if item.price > item.price - 1:
				max_item = item
		return max_item
		
		pass	



# Tests
class TestAllMethods(unittest.TestCase):

	# SetUp -- we create a bunch of items for you to use in your tests.
	def setUp(self):
		self.item1 = Item("Beer", 6, 20)
		self.item2 = Item("Cider", 5, 25)
		self.item3 = Item("Water", 1, 100)
		self.item4 = Item("Fanta", 2, 60)
		self.item5 = Item("CocaCola", 3, 40)

	## Check to see whether count_a works
	def test_count_a(self):
		self.assertEqual(count_a("I like bananas"), 3, "Tested count_a on input 'I like bananas'")
		self.assertEqual(count_a("I like dogs"), 0, "Tested count_a on input 'I like dogs'")
		self.assertEqual(count_a(" "), 0, "Tested count_a on input ' '")
		self.assertEqual(count_a("A dog ate apples"), 3, "Tested count_a on input 'A dog at apples'")
		self.assertEqual(count_a("I like banana"), 3, "Tested count_a on input 'I like bananas'")
	 #wondering if the 'i' in the for statement is counting words with 'a' in them, not 'a's in each word
		pass


	## Check to see whether you can add an item to the warehouse
	def test_add_item(self):
		self.assertEqual(add_item(self, "thing"), "thing", "Tested add_item on input 'thing'")
		self.assertEqual(print_items(self, "thing"), "thing", "Tested add_item on input 'thing'")

		variable = self.item1
		
		pass
		#confused on best way to test this. should I use old school way of print testing or unittest?

	## Check to see whether warehouse correctly returns the item with the most stock
	def test_warehouse_max_stocks(self):
		#i'm so confused, i thought we were just testing here...i can't seem to find anything written for warehouse_max_stocks
		print(f"Testing warehouse_max_stocks([????]) should return ??? and returns {warehouse_max_stocks([???])}")
		self.assertEqual(warehouse_max_stock(5), stock, "Tested warehouse_max_price on input 'price'")

		#i don't fully understand what sort of unittest I need to do...need to go back and re read unittests
		pass


	# Check to see whether the warehouse correctly return the item with the highest price
	def test_warehouse_max_price(self):
		self.assertEqual(warehouse_max_price(5), price, "Tested warehouse_max_price on input 'price'")
		#still having trouble fully understanding what i'm testing


		pass
		

def main():
	unittest.main()

if __name__ == "__main__":
	main()