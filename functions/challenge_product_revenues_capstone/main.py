# Task 1: calculate the revenue list
def calculate_revenue(prices, quantities_sold):
    revenue = []
    for i in range(len(prices)):
        revenue.append(prices[i] * quantities_sold[i])
    return revenue

# Task 2: format and print sorted output
def formatted_output(revenue_per_product):
    for product, rev in sorted(revenue_per_product):
        print(f"{product} has total revenue of ${rev}")

# Given data
products = ["Bread", "Apples", "Oranges", "Bananas"]
prices = [0.50, 1.20, 2.50, 2.00]
quantities_sold = [150, 200, 100, 50]

# Task 3: compute revenues
revenue = calculate_revenue(prices, quantities_sold)

# Task 4: combine names with revenues
revenue_per_product = list(zip(products, revenue))

# Task 5: display
formatted_output(revenue_per_product)