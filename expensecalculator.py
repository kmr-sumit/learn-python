# calculate total expenses for purchasing products
x=int(input("enter the number of products: " ))
price=0
for n in range(x):
    prod_1 = input("enter the price of product ?")
    quantity_1 = input("enter the quantity of product ?")
    price = price + float(prod_1) * float(quantity_1)

print("your final payment is ",price)


