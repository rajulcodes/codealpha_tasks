import os

def get_stock_prices():
    """
    Returns a hardcoded dictionary of stock prices.
    In a real application, this would come from an API or database.
    """
    return {
        "AAPL": 180.00,  # Apple Inc.
        "MSFT": 420.50,  # Microsoft Corporation
        "GOOG": 175.25,  # Alphabet Inc. (Google)
        "AMZN": 190.75,  # Amazon.com Inc.
        "TSLA": 250.00,  # Tesla Inc.
        "NVDA": 1200.00, # NVIDIA Corporation
        "META": 495.00,  # Meta Platforms Inc.
    }

def get_user_portfolio(available_stocks):
    """
    Prompts the user to input stock names and quantities for their portfolio.
    Validates input against available stocks and ensures positive quantities.
    """
    portfolio = {}
    print("\nEnter your stock holdings. Type 'done' when finished.")
    
    while True:
        stock_name = input("Enter stock symbol (e.g., AAPL) or 'done': ").upper().strip()
        if stock_name == 'DONE':
            break
        
        if stock_name not in available_stocks:
            print(f"Error: '{stock_name}' is not a recognized stock symbol. Please try again.")
            print(f"Available stocks: {', '.join(available_stocks.keys())}")
            continue
        
        while True:
            try:
                quantity_str = input(f"Enter quantity for {stock_name}: ").strip()
                quantity = int(quantity_str)
                if quantity <= 0:
                    print("Quantity must be a positive whole number. Please try again.")
                else:
                    portfolio[stock_name] = portfolio.get(stock_name, 0) + quantity # Add to existing quantity if stock entered again
                    break
            except ValueError:
                print("Invalid quantity. Please enter a whole number (e.g., 10, 50).")
    return portfolio

def calculate_portfolio_value(portfolio, stock_prices):
    """
    Calculates the total investment value of the given portfolio.
    Returns a tuple: (total_value, list_of_individual_holdings_details).
    """
    total_value = 0.0
    holdings_details = []

    if not portfolio:
        return 0.0, []

    print("\n--- Your Portfolio Summary ---")
    for stock, quantity in portfolio.items():
        price = stock_prices.get(stock)
        if price is not None:
            holding_value = price * quantity
            total_value += holding_value
            holdings_details.append({
                "symbol": stock,
                "quantity": quantity,
                "price_per_share": price,
                "holding_value": holding_value
            })
            print(f"{stock}: {quantity} shares @ ${price:.2f}/share = ${holding_value:.2f}")
        else:
            # This case should ideally not be hit if input validation is strict
            print(f"Warning: Price for {stock} not found. Skipping calculation for this stock.")
    
    return total_value, holdings_details

def display_results(total_value, holdings_details):
    """
    Displays the total investment value and individual holdings in a formatted way.
    """
    if not holdings_details:
        print("\nYour portfolio is empty. No investment to display.")
        return

    print(f"\nTotal Investment Value: ${total_value:.2f}")

def save_results_to_file(total_value, holdings_details, file_type='txt'):
    """
    Saves the portfolio summary to a .txt or .csv file.
    """
    if not holdings_details:
        print("No portfolio data to save.")
        return

    filename = f"stock_portfolio_{file_type}.{file_type}"
    
    try:
        if file_type.lower() == 'txt':
            with open(filename, 'w') as f:
                f.write("--- Stock Portfolio Report ---\n")
                f.write(f"Date: {os.path.basename(__file__)}\n\n") # Using filename as a placeholder for date
                f.write("Individual Holdings:\n")
                for holding in holdings_details:
                    f.write(f"  {holding['symbol']}: {holding['quantity']} shares @ ${holding['price_per_share']:.2f}/share = ${holding['holding_value']:.2f}\n")
                f.write(f"\nTotal Investment Value: ${total_value:.2f}\n")
            print(f"\nPortfolio saved to {filename}")
        elif file_type.lower() == 'csv':
            with open(filename, 'w') as f:
                # Write CSV header
                f.write("Symbol,Quantity,Price Per Share,Holding Value\n")
                # Write individual holdings
                for holding in holdings_details:
                    f.write(f"{holding['symbol']},{holding['quantity']},{holding['price_per_share']:.2f},{holding['holding_value']:.2f}\n")
                # Add a row for total value (optional, but useful)
                f.write(f"\nTotal Investment Value,${total_value:.2f},,\n")
            print(f"\nPortfolio saved to {filename}")
        else:
            print("Unsupported file type. Please choose 'txt' or 'csv'.")
    except IOError as e:
        print(f"Error saving file: {e}")

def main():
    """
    Main function to run the stock portfolio tracker.
    """
    print("Welcome to the Simple Stock Portfolio Tracker! 📈")
    
    stock_prices = get_stock_prices()
    print("\n--- Available Stock Prices ---")
    for symbol, price in stock_prices.items():
        print(f"{symbol}: ${price:.2f}")

    portfolio = get_user_portfolio(stock_prices)
    
    total_value, holdings_details = calculate_portfolio_value(portfolio, stock_prices)
    
    display_results(total_value, holdings_details)

    if holdings_details: # Only ask to save if there's data
        while True:
            save_option = input("\nDo you want to save the portfolio report? (yes/no): ").lower().strip()
            if save_option == 'yes':
                file_format = input("Save as (txt/csv)? ").lower().strip()
                save_results_to_file(total_value, holdings_details, file_format)
                break
            elif save_option == 'no':
                print("Report not saved. Goodbye!")
                break
            else:
                print("Invalid input. Please enter 'yes' or 'no'.")

if __name__ == "__main__":
    main()

