def shopping_cart():
    cart = []  # List to store (item, price) tuples
    total_cost = 0.0

    print("🛒 Welcome to the Food Shopping Cart!")
    print("Enter the food item and price. Type 'exit' as the item name to finish.\n")

    while True:
        item = input("Enter food item (or type 'exit' to finish): ").strip()
        if item.lower() == 'exit':
            break

        try:
            price = float(input(f"Enter price for '{item}': R"))
            cart.append((item, price))
            total_cost += price
        except ValueError:
            print("❌ Invalid price. Please enter a number.\n")

    print("\n🧾 Shopping Cart Summary:")
    if cart:
        for i, (item, price) in enumerate(cart, start=1):
            print(f"{i}. {item} - R{price:.2f}")
        print(f"\n💰 Total Cost: R{total_cost:.2f}")
    else:
        print("Your cart is empty.")

# Run the shopping cart
shopping_cart()
