#Find Key with Maximum Value
#Given a dictionary of items and prices, print the item with the highest price.
items = {
    "laptop": 1200,
    "phone": 900,
    "headphones": 150,
    "monitor": 300,
    "keyboard": 100
}
maxPrice = items["laptop"]
for x in items:
   if maxPrice < items[x]:
       maxPrice = items[x]
print(f"the maximum price is: {maxPrice}")