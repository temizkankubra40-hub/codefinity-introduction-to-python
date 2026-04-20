produce = ["Tomatoes", "Lettuce"]
dairy = ["Milk", "Cheese"]

groceries = [produce, dairy]

for section in groceries:
    print(section)
    for item in section:
        print(f"Item name: {item}")
    