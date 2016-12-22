"""Import classes and lists from Bicycles.py. Create bike instances, bike shop instance, and customer instances."""

from bicycles import Bicycle, BikeShop, Customer, inventory, demand_curve

if __name__=="__main__":

    bike1 = Bicycle(inventory[0][0], inventory[0][1], inventory[0][2])
    bike2 = Bicycle(inventory[1][0], inventory[1][1], inventory[1][2])
    bike3 = Bicycle(inventory[2][0], inventory[2][1], inventory[2][2])
    bike4 = Bicycle(inventory[3][0], inventory[3][1], inventory[3][2])
    bike5 = Bicycle(inventory[4][0], inventory[4][1], inventory[4][2])
    bike6 = Bicycle(inventory[5][0], inventory[5][1], inventory[5][2])

    bikes = [bike1, bike2, bike3, bike4, bike5, bike6]

    shop_instance = BikeShop("Dave's World of Bikes", 0.20)

    customer1 = Customer(demand_curve[0][0], demand_curve[0][1])
    customer2 = Customer(demand_curve[1][0], demand_curve[1][1])
    customer3 = Customer(demand_curve[2][0], demand_curve[2][1])

    customers = [customer1, customer2, customer3]

    for customer in customers:
        print("\nCustomer Name: %s\nCustomer Budget: %d\n" % (customer.customer_name, customer.budget))
        for bike in bikes:
            if bike.cost * (1 + shop_instance.margin) <= customer.budget:
                print("Bike Model: %s, Price: %d" % (bike.model, bike.cost * (1 + shop_instance.margin)))

    print("\nInitial Inventory: ")
    for x in range(0,6):
        print(inventory[x][0])

    customer1.buy_bike(bike1,shop_instance)
    shop_instance.sell_bike(bike1)
    print("\n%s purchased: %s, Price paid: %.2f, Budget Remaining: %.2f" % (customer1.customer_name,
                                                                            bike1.model,
                                                                            bike1.cost * (1 + shop_instance.margin),
                                                                            customer1.budget))
    customer2.buy_bike(bike2, shop_instance)
    shop_instance.sell_bike(bike2)
    print("\n%s purchased: %s, Price paid: %.2f, Budget Remaining: %.2f" % (customer2.customer_name,
                                                                            bike2.model,
                                                                            bike2.cost * (1 + shop_instance.margin),
                                                                            customer2.budget))

    customer3.buy_bike(bike4, shop_instance)
    shop_instance.sell_bike(bike4)
    print("\n%s purchased: %s, Price paid: %.2f, Budget Remaining: %.2f" % (customer3.customer_name,
                                                                            bike4.model,
                                                                            bike4.cost * (1 + shop_instance.margin),
                                                                            customer3.budget))

    print("\nRemaining Inventory: ")
    for x in range(0,len(inventory)):
        print(inventory[x][0])

    print("\nShop: %s, Total Profit: %.2f" % (shop_instance.shop_name, shop_instance.profit))