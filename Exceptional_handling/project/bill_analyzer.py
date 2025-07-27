def process_purchase_file():
    try:
        filename = input("Enter the file name (without .txt): ").strip() + ".txt"
        
        with open(filename, 'r') as file:
            lines = file.readlines()

        purchased_items = 0
        free_items = 0
        total_price = 0
        discount = 0

        for line in lines:
            line = line.strip()

            # Skip empty lines
            if not line:
                continue

            try:
                item, price = line.split()

                if price.lower() == "free":
                    free_items += 1
                elif item.lower() == "discount":
                    discount = int(price)
                else:
                    total_price += int(price)
                    purchased_items += 1

            except ValueError:
                # Skip malformed lines
                continue

        final_amount = total_price - discount

        print("\nNo of items purchased:", purchased_items)
        print("No of free items:", free_items)
        print("Amount to pay:", total_price)
        print("Discount given:", discount)
        print("Final amount paid:", final_amount)

    except FileNotFoundError:
        print("Error: File not found. Please check the file name.")
    except Exception as e:
        print("An unexpected error occurred:", e)

# Run the function
process_purchase_file()
