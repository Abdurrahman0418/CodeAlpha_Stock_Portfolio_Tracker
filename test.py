stock_prices = {
    "AAPL": 150.25,
    "GOOGL": 2750.50,
    "F3A": 299.00,
    "AMZN": 3400.75,
    "TSLA": 720.10
}

print("Stock Prices:")
for stock, price in stock_prices.items():
    print(f"{stock}: ${price:}")

total_investment = 0
user_stocks = {}

while True:
    stock_name = input("\nEnter stock symbol to invest in (or 'done' to finish): ").upper()
    if stock_name == 'DONE':
        break

    if stock_name not in stock_prices:
        print("Stock not found. Please try again.")
        continue

    try:
        quantity = int(input(f"Enter quantity of {stock_name}: "))
    except ValueError:
        print("Invalid quantity. Please enter a number.")
        continue

    investment = stock_prices[stock_name] * quantity
    user_stocks[stock_name] = investment
    total_investment += investment

print("\n======= Investment Summary =======")
for stock, value in user_stocks.items():
    print(f"{stock}: ${value:}")
print(f"\n Total Investment: ${total_investment:}")

save_option = input("\nDo you want to save results to a file? (yes/no): ").lower()

if save_option == "yes":
    with open("stock_portfolio.txt", "w") as file:
        file.write("===== Stock Investment Summary =====\n")
        for stock, value in user_stocks.items():
            file.write(f"{stock}: ${value}\n")
        file.write(f"\nTotal Investment Value: ${total_investment}\n")
    print("✅ Results saved to 'stock_investment.txt'")
else:
    print("✅ Program finished without saving.")