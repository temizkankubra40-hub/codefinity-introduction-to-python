def apply_discount(prices):
    # 1) Copy the list so the original stays unchanged
    prices_copy = prices.copy()
    # 2) Loop by index and apply 10% off when price > $2.00
    for i in range(len(prices_copy)):
        if prices_copy[i] > 2.00:
            prices_copy[i] *= 0.90
    # 3) Return after the loop finishes
    return prices_copy

product_prices = [1.50, 2.50, 3.00, 0.99, 2.30]
updated_prices = apply_discount(product_prices)

# 4) Print without embedding the dollar sign in front of the list
print(f"Updated product prices: {updated_prices}")