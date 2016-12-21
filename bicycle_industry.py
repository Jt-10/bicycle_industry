"""Bicycle market model. Establish classes for bicycles, bike shops, and customers. Set up
   bike inventory and customer lists including 6 bikes and 3 customers. Bike inventory includes
   name, bike weight in lbs, and cost in $ parameters for each bike. Customer tuple includes name and
   budget for each customer.
   """

inventory = [["Beater", 8, 100],
             ["Fixie", 7, 300],
             ["Mountain", 6, 500],
             ["Single Speed", 5, 700],
             ["Road", 4, 900],
             ["Downhill", 2, 1100],
             ]

demand_curve = [["Beginner", 200],
                ["Commuter", 500],
                ["Weekend Warrior", 1000],
                ]


class Bicycle(object):
    """Bike class includes model name, weight, and cost parameters.
       """
    def __init__(self, model, weight, cost):
        self.model = model
        self.weight = weight
        self.cost = cost

    def display_bike(self, bike):
        return "Model: %s: \nWeight: %d \nCost: %d" % (inventory[bike][0], inventory[bike][1],
        inventory[bike][2])



class BikeShop(object):
    """Bike shop class includes name, stock, and margin parameters. The class will also initiate a total profit
       value to be incremented for each sale by a profit method.
       """

    profit = 0

    def __init__(self, shop_name, margin):
        self.shop_name = shop_name
        self.margin = margin
        self.inventory = inventory

    def display_profit(self, profit):
        return "Total Profit: %s" % (profit)

    def sell_bike(self, bike):
        self.profit += (bike.cost * self.margin)
        if bike == bike1:
            del inventory[0]
        elif bike == bike2:
            del inventory[1]
        elif bike == bike3:
            del inventory[2]
        elif bike == bike4:
            del inventory[3]
        elif bike == bike5:
            del inventory[4]
        elif bike == bike6:
            del inventory[5]
        return self.profit, inventory


class Customer(object):
    """Customer class includes name and budget parameter. This class will also include methods for defining
       the bikes within customer's budget and purchasing bikes.
       """
    def __init__(self, customer_name, budget):
        self.customer_name = customer_name
        self.budget = budget

    def buy_bike(self, bike):
        price = bike.cost * (1 + shop_instance.margin)
        if price <= self.budget:
            self.budget -= price
            return self.budget


"""Create bike instances, bike shop instance, and customer instances."""
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

    customer1.buy_bike(bike1)
    shop_instance.sell_bike(bike1)
    print("\n%s purchased: %s, Price paid: %.2f, Budget Remaining: %.2f" % (customer1.customer_name,
                                                                            bike1.model,
                                                                            bike1.cost * (1 + shop_instance.margin),
                                                                            customer1.budget))
    customer2.buy_bike(bike2)
    shop_instance.sell_bike(bike2)
    print("\n%s purchased: %s, Price paid: %.2f, Budget Remaining: %.2f" % (customer2.customer_name,
                                                                            bike2.model,
                                                                            bike2.cost * (1 + shop_instance.margin),
                                                                            customer2.budget))

    customer3.buy_bike(bike4)
    shop_instance.sell_bike(bike4)
    print("\n%s purchased: %s, Price paid: %.2f, Budget Remaining: %.2f" % (customer3.customer_name,
                                                                            bike4.model,
                                                                            bike4.cost * (1 + shop_instance.margin),
                                                                            customer3.budget))

    print("\nRemaining Inventory: ")
    for x in range(0,len(inventory)):
        print(inventory[x][0])

    print("\nShop: %s, Total Profit: %.2f" % (shop_instance.shop_name, shop_instance.profit))














