def order(item):
    print(f"Place an order: your order is {item}")

#fish => 4
#total = (base_price + 5) * 1.15
def calculate_total(item):
    base_price = 25.5
    VAT = 0.15
    total_price = (base_price + len(item))*1.15
    return total_price

def get_order():
    print("preparing order")
    return("order ready")

myfood = input("what would you like?")
order(myfood)
print (get_order())
order_total = calculate_total(myfood)

print(f"your order costs: R{order_total:.2f}")

    