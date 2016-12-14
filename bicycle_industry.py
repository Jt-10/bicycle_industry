"""Basic model of a bicycle market. Establish classes for bicycles, bike shops, and customers.
   """

"""Set up bike inventory and customer tuples including 6 bikes and 3 customers. Bike inventory includes
   name, bike weight in lbs, and cost in $ parameters for each bike. Customer tuple includes name and
   budget for each customer. These can be referenced later in the model to streamline the initiation
   of bike and customer instances.
   """

inventory = (["Beater", 8, 100],
             ["Fixie", 7, 300],
             ["Mountain", 6, 500],
             ["Single Speed", 5, 700],
             ["Road", 4, 900],
             ["Downhill", 2, 1100],
             )

customer = (["Noob", 200],
            ["Commuter", 500],
            ["Weekend Warrior", 1000],
            )

"""Bike class includes model name, weight, and cost parameters.
   """
class Bicycle(object):
    def __init__(self, model, weight, cost):
        self.model = model
        self.weight = weight
        self.cost = cost

"""Bike shop class includes name, stock, and margin parameters. The class will also initiate a total profit
   value to be incremented for each sale by a profit method.
   """
class BikeShop(object):
    total_profit = 0

    def __init__(self, shop_name, stock, margin):
        self.shop_name = shop_name
        self.stock = stock
        self.margin = margin

    def profit(self, total_profit):
        print(total_profit)

"""Customer class includes name and budget parameter. This class will also include methods for defining
   the bikes within budget and purchasing bikes.
   """
class Customer(object):
    def __init__(self, customer_name, budget):
        self.customer_name = customer_name
        self.budget = budget

    def buy_bike(self):
        price = cost * margin
        own = []
        if price <= budget:
            own[].append(bikei)
            budget -= price
            return budget
            return stock



"""Create bike, bike shop, and customer instances.
   """
for i in range(0,6):
    bikei = Bicycle(inventory[i[0]],inventory[i[1]], inventory[i[2]])
    stock[i] = bikei

for i in range(0,3):
    customeri = Customer(customer[i[0]], customer[i[1]])

for i in range(0,3):
    print(custumeri + ": ")
    for i in range (0,6):
        if stock[i[2]] <= budget:
            customeri.buy()
            return


bike_shop = BikeShop("Bikes 'n Beans", stock, 0.2)







