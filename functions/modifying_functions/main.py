def apply_discount(price, discount=0.05):
    updated_price1 = price * (1 - discount)
    return updated_price1

def apply_tax(price, tax=0.07):
    updated_price2 = price * (1 + tax)
    return updated_price2

def calculate_total(price, discount=0.05, tax=0.07):
    discounted = apply_discount(price, discount)
    final_price = apply_tax(discounted, tax)
    return final_price

total_price_default = calculate_total(120)
print(f"Total cost with default discount and tax: ${total_price_default}")

total_price_custom = calculate_total(100, discount=0.10, tax=0.08)
print(f"Total cost with custom discount and tax: ${total_price_custom}")