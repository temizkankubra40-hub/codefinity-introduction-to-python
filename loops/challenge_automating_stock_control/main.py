# Initialize the inventory dictionary with stock details
inventory = {
    "Bread": [30, 50, 10, False],   # [current stock, min stock, restock qty, on sale]
    "Eggs": [120, 200, 40, False],
    "Milk": [60, 100, 20, False],
    "Apples": [15, 50, 15, False]
}

discount_threshold = 100

print("Processing started")

for item in inventory:
    print(f"Processing {item}")
    current_stock, min_stock, restock_amount, on_sale = inventory[item]
    # Restock until at or above minimum
    while current_stock < min_stock:
        current_stock += restock_amount
    inventory[item][0] = current_stock
    # Apply discount flag if above threshold
    if current_stock > discount_threshold and not on_sale:
        inventory[item][3] = True

print("Processing completed")