"""Bicycle market model. (1) Set up bike inventory and customer lists including 6 bikes and 3 customers.
   Bike inventory includes name, bike weight in lbs, and cost in dollars for each bike.
   Customer demand curve is defined by the name and bicycle budget for each customer. (2) Establish classes
   for bicycles, bike shops, and customers.
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
        if bike.model == "Beater":
            del inventory[0]
        elif bike.model == "Fixie":
            del inventory[1]
        elif bike.model == "Mountain":
            del inventory[2]
        elif bike.model == "Single Speed":
            del inventory[3]
        elif bike.model == "Road":
            del inventory[4]
        elif bike.model == "Downhill":
            del inventory[5]
        return self.profit, inventory


class Customer(object):
    """Customer class includes name and budget parameter. This class will also include methods for defining
       the bikes within customer's budget and purchasing bikes.
       """
    def __init__(self, customer_name, budget):
        self.customer_name = customer_name
        self.budget = budget

    def buy_bike(self, bike, BikeShop):
        price = bike.cost * (1 + BikeShop.margin)
        if price <= self.budget:
            self.budget -= price
            return self.budget