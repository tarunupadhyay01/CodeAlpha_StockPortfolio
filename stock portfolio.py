def portfolio_tracker():
    portfolio = {}

    print("Stock Portfolio Tracker")
    print("Type 'done' to finish.")

    while True:
        stock = input("Enter stock name: ")

        if stock.lower() == "done":
            break

        quantity = int(input("Enter quantity: "))
        price = float(input("Enter price per stock: "))

        portfolio[stock] = quantity * price

    total = 0

    print("\nPortfolio:")

    for stock, value in portfolio.items():
        print(stock, ":", value)
        total += value

    print("Total Investment:", total)


portfolio_tracker()