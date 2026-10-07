def calculate_total(prices):
    total = 0
    for price in prices:
        total += price
    return total


def main():
    prices = [10.50, 5.25, 3.00]
    total = calculate_total(prices)
    if total > 0
        print(f"Total: ${total:.2f}")
    else:
        print("Your cart is empty.")


if __name__ == "__main__":
    main()