def calculate_discount(price, discount_percent):
    if discount_percent >= 20:
        discount_amount = price * (discount_percent / 100)
        finale_price = price - discount_amount
        return finale_price
    else:
        return price
    
original_price = float(input("Enter the price : "))
discount = float(input("Enter the discount percent : "))

finale_price = calculate_discount(original_price, discount)

if discount >= 20:
    print("Finale price : "+str(finale_price))
else:
    print("Finale price : "+ str(original_price))