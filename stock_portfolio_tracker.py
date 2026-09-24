stock_prices = {
    "AAPL": 180,
    "TSLA": 250,
    "GOOGL": 150,
    "MSFT": 400,
    "AMZN": 180
}

total_investment = 0

print("===== Stock Portfolio Tracker =====")
print("Available stocks:", ", ".join(stock_prices.keys()))

while True:
    stock = input("\nEnter stock name (or 'done' to finish): ").upper()

    if stock == "DONE":
        break

    if stock not in stock_prices:
        print("Stock not available.")
        continue

    try:
        quantity = int(input("Enter quantity: "))

        if quantity <= 0:
            print("Quantity must be greater than 0.")
            continue

        value = stock_prices[stock] * quantity
        total_investment += value

        print(f"{stock}: {quantity} shares = ${value}")

    except ValueError:
        print("Please enter a valid quantity.")

print("\n===== Portfolio Summary =====")
print(f"Total Investment Value: ${total_investment}")