actual_cost = float(input("Please enter the actual product price: "))
sale_amount = float(input("Please enter the sales amount:  "))

if (sale_amount > actual_cost):
    amount = sale_amount - actual_cost
    print("total profit = {0}".format(sale_amount - actual_cost))
else:
    print("no PROFIT!!!")