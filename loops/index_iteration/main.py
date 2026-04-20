prices = [29.99, 45.50, 12.75, 38.20]
discounts = [10, 20, 15, 5]

for i in range(len(prices)):
    # apply the discount: price * (1 - discount_fraction)
    prices[i] = prices[i] * (1 - discounts[i] / 100)
    print(f"Updated price for item {i}: ${prices[i]:.2f}")