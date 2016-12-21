from bicycles import *

"""Create bike instances, bike shop instance, and customer instances."""
if __name__=="__main__":

    bikes = []
    for bike in inventory:
        inventory[bike][0] = Bicycle(bike, inventory[bike][1],inventory[bike][2])
        bikes.append(inventory[bike][0])

    shop_instance = BikeShop("Dave's World of Bikes", 0.20)

    customers = []
    for customer in demand_curve:
        demand_curve[customer][0] = Customer(customer, demand_curve[customer][1])
        customers.append(demand_curve[customer][0])

    for customer in customers:
        print("\nCustomer Name: %s\nCustomer Budget: %d\n" % (customer.customer_name, customer.budget))
        for bike in bikes:
            if bike.cost * (1 + shop_instance.margin) <= customer.budget:
                print("Bike Model: %s, Price: %d" % (bike.model, bike.cost * (1 + shop_instance.margin)))

    print("\nInitial Inventory: ")
    print(inventory.keys())

    for customer in customers:
        for bike in bikes:
            if bike.cost * (1 + shop_instance.margin) <= customer.budget:
            customer.buy_bike(bike)
    shop_instance.sell_bike(bike1)
    del inventory[0]
    print("\n%s purchased: %s, Price paid: %.2f, Budget Remaining: %.2f" % (customer1.customer_name,
                                                                            bike1.model,
                                                                            bike1.cost * (1 + shop_instance.margin),
                                                                            customer1.budget))

    customer2.buy_bike(bike2)
    shop_instance.sell_bike(bike2)
    del inventory[1]
    print("\n%s purchased: %s, Price paid: %.2f, Budget Remaining: %.2f" % (customer2.customer_name,
                                                                            bike2.model,
                                                                            bike2.cost * (1 + shop_instance.margin),
                                                                            customer2.budget))

    customer3.buy_bike(bike4)
    shop_instance.sell_bike(bike4)
    del inventory[3]
    print("\n%s purchased: %s, Price paid: %.2f, Budget Remaining: %.2f" % (customer3.customer_name,
                                                                            bike4.model,
                                                                            bike4.cost * (1 + shop_instance.margin),
                                                                            customer3.budget))

    print("\nRemaining Inventory: ")
    for x in range(0,len(inventory)):
        print(inventory[x][0])

    print("\nShop: %s, Total Profit: %.2f" % (shop_instance.shop_name, shop_instance.profit))