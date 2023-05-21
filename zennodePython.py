catalog = {"product A": 20,
           "product B": 40,
           "product C": 50}

quantities ={}
for product in catalog.keys():
    quantity = int(input(f"Enter the quantity of the {product}:  "))
    quantities[product] = quantity

amount = 0
total_quantity = 0
for product, quantity in quantities.items():
    amount += catalog[product] * quantity

def discount(amount ,quantities):
    discount_amount = 0

    if amount > 200:
        discount_amount -= 10
    
    for product, quantity in quantities.items():
        if quantity > 10:
            discount_amount = max(discount_amount, 0.05 * (catalog[product] * quantity))

    total_quantity = sum(quantities.values())
    if total_quantity > 20:
        discount = 0.1 * amount
        amount -= discount

    if total_quantity > 30 and any(quantity > 15 for quantity in quantities.values()):
        for product, quantity in quantities.items():
            if quantity > 15:
                discount_amount = max(discount_amount, 0.5 * (catalog[product] * (quantity - 15)))

    return discount_amount
    
discount_amount = discount(amount, quantities)

subtotal = amount
shipping_fee = 5 * (total_quantity // 10)
gift_wrap_fee = sum(quantities.values())

total = subtotal - discount_amount + shipping_fee + gift_wrap_fee

for product, quantity in quantities.items():
    print(f"{product}: Quantity - {quantity}, Total Amount - {catalog[product] * quantity}")

print(f"\nSubtotal: {subtotal}")
print(f"Discount Amount: {discount_amount}")
print(f"Shipping Fee: {shipping_fee}")
print(f"Gift Wrap Fee: {gift_wrap_fee}")
print(f"Total: {total}")
