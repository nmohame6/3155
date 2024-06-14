recipes = {
    "small": {
        "ingredients": {
            "bread": 2,  ## slice
            "ham": 4,  ## slice
            "cheese": 4,  ## ounces
        },
        "cost": 1.75,
    },
    "medium": {
        "ingredients": {
            "bread": 4,  ## slice
            "ham": 6,  ## slice
            "cheese": 8,  ## ounces
        },
        "cost": 3.25,
    },
    "large": {
        "ingredients": {
            "bread": 6,  ## slice
            "ham": 8,  ## slice
            "cheese": 12,  ## ounces
        },
        "cost": 5.5,
    }
}

resources = {
    "bread": 12,  ## slice
    "ham": 18,  ## slice
    "cheese": 24,  ## ounces
}


### Complete functions ###

class SandwichMachine:

    def __init__(self, machine_resources):
        self.machine_resources = machine_resources

    def check_resources(self, ingredients):
        if (self.machine_resources["bread"] >= ingredients["bread"] and self.machine_resources["ham"] >= ingredients[
            "ham"] and self.machine_resources["cheese"] >= ingredients["cheese"]):
            return True
        else:
            if (self.machine_resources["bread"] < ingredients["bread"]):
                print("Sorry, we don't have enough bread")
            if (self.machine_resources["ham"] < ingredients["ham"]):
                print("Sorry, we don't have enough ham")
            if (self.machine_resources["cheese"] < ingredients["cheese"]):
                print("Sorry, we don't have enough cheese")
            return False

    def process_coins(self):
        """Returns the total calculated from coins inserted.
           Hint: include input() function here, e.g. input("how many quarters?: ")"""
        dollars = input("How many dollars?: ")
        half_dollars = input("How many half dollars?: ")
        quarters = input("How many quarters?: ")
        dimes = input("How many dimes?: ")
        total = float(dollars) + float(half_dollars) * 0.5 + float(quarters) * 0.25 + float(dimes) * 0.1
        return total

    def transaction_result(self, coins, cost):
        if coins >= cost:
            change = coins - cost
            print(f"We're preparing your" ,sandwich_type , "sandwich! Your change is: $" , change)
            return True
        else:
            print("Sorry, that's not enough money, come back and try your order With more money or a smaller sandwich")
            return False

    def make_sandwich(self, sandwich_size, order_ingredients):
        """Deduct the required ingredients from the resources.
                   Hint: no output"""
        for item in order_ingredients:
            self.machine_resources[item] -= order_ingredients[item]


### Make an instance of SandwichMachine class and write the rest of the codes ###

sandwichMachine = SandwichMachine(resources)
insertedCoins = 0
costOfSammy = 0
change = 0

sandwich_type = input("What would you like? (small, medium, large, off, report): ")
while (sandwich_type != "off"):
    if (sandwich_type == "report"):
        print("Bread: ", resources["bread"])
        print("Ham: ", resources["ham"])
        print("Cheese: ", resources["cheese"])
    elif (sandwich_type == "small" or sandwich_type == "medium" or sandwich_type == "large"):
        if sandwichMachine.check_resources(recipes[sandwich_type]["ingredients"]):
            insertedCoins = sandwichMachine.process_coins()
            costOfSammy = recipes[sandwich_type]["cost"]
            if sandwichMachine.transaction_result(insertedCoins, costOfSammy):
                sandwichMachine.make_sandwich(sandwich_type, recipes[sandwich_type]["ingredients"])
                print("Your", sandwich_type, "sandwich is ready")
    sandwich_type = input("What would you like? (small, medium, large, off, report): ")

