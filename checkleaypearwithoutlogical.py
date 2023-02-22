price = float(input("Enter the price of the item: "))

if price > 10000:
    price = price - 0.05 * price
else:
    price = price - 0.02 * price
print(price)    
