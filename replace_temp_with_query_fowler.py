
# Adapted from a Java code in the "Refactoring" book by Martin Fowler.
# Replace temp with query
# Code snippet. Not runnable.
quantity = 10
item_price = 5

def get_discount(base_price):
    if base_price > 1000: 
        return 0.95
    return 0.98
        
def get_price():
    base_price = quantity * item_price
    discount_factor = get_discount(base_price)
    return base_price * discount_factor

print(get_price())
