"""Bicycle market model. (1) Set up bike inventory and customer lists including 6 bikes and 3 customers.
   Bike inventory includes name, bike weight in lbs, and cost in dollars for each bike.
   Customer demand curve is defined by the name and bicycle budget for each customer. (2) Establish classes
   for bicycles, bike shops, and customers.
   """

inventory = {"Beater":[bike1, 8, 100],
             "Fixie": [bike2, 7, 300],
             "Mountain": [bike3, 6, 500],
             "Single Speed":[bike4, 5, 700],
             "Road": [bike5, 4, 900],
             "Downhill": [bike6, 2, 1100],
             }

demand_curve = {"beginner":[customer1, 200],
                "Commuter": [customer2, 500],
                "Weekend Warrior": [customer3, 1000],
                }

class Bicycle(object):
    """Bike class includes model name, weight, and cost to produce parameters.
       """
    def __init__(self, model, weight, cost):
        self.model = model
        self.weight = weight
        self.cost = cost

    def display_bike(self, bike):
        return "Model: %s: \nWeight: %d \nCost: %d" % (inventory[bike][0], inventory[bike][1],
        inventory[bike][2])



class BikeShop(object):
    """Bike shop class includes name and margin parameters. The class will also initiate a total profit
       variable to be incremented after each sale by a profit method.
       """
    profit = 0

    def __init__(self, shop_name, margin):
        self.shop_name = shop_name
        self.margin = margin
        self.inventory = inventory

    def sell_bike(self, bike):
        self.profit += self.margin * inventory[bike][2]
        del inventory[bike]
        return self.profit, inventory


class Customer(object):
    """Customer class includes name and budget parameters. This class will also include methods for determining
       the bikes that fall within the customers' budgets after factoring in the store's markup. It will also
       include a methog for purchasing bikes.
       """
    def __init__(self, customer_name, budget):
        self.customer_name = customer_name
        self.budget = budget

    def buy_bike(self, bike, shop_name):
        price = inventory[bike][2] * (1 + BikeShop.margin)
        if inventory[bike][2] * price <= self.budget:
            self.budget -= price
            return self.budget