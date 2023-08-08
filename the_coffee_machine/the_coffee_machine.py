""" coffe machine """
import sys
import os
# from pprint import pprint
import decimal

class Machine:
    """ abstract drink machine """
    def __init__(self, resources, menu) -> None:
        self.resources = resources
        self.menu = menu
        self.profit = 0
        self.status = True

    @property
    def report(self):
        """ get report """
        resources = '\n'.join(str(ingredient) + ': ' + str(value)
                     for ingredient, value in self.resources.items())
        return '\n'.join((resources, f'profit: {self.profit} $'))

    def check_ingredients(self, drink_name: str) -> bool:
        """ check if there are enough ingredients for drink in machine are available """
        drink = self.menu[drink_name]
        return all(value <= self.resources.get(ingredient_name, 0)
                   for ingredient_name, value in drink['ingredients'].items())

    def consume_ingredients(self, drink_name: str):
        """ consume ingredients from machine to make Drink """
        drink = self.menu[drink_name]
        for ingredient_name, value in drink['ingredients'].items():
            self.resources[ingredient_name] -= value

    @staticmethod
    def get_money():
        """ receive payment from customer"""
        while True:
            try:
                money = decimal.Decimal(input('input money: '))
                if money >= 0:
                    return money
                print('You must input sum greater than 0 for order or equal 0 for cancelling')
                continue
            except (TypeError, ValueError, decimal.InvalidOperation):
                print('You must input sum greater than 0 for order or equal 0 for cancelling')
                continue

    def process_client(self, drink_name: str):
        """ processing client """
        # drink = coffee_machine.menu[drink_name]
        if self.check_ingredients(drink_name) is False:
            print('Not enough ingredients for ', drink_name)
            return False
        drink = self.menu[drink_name]
        drink_cost = decimal.Decimal(drink['cost'])
        while True:
            money = self.get_money()
            if money == 0: # order is cancelled
                return False
            if money < drink_cost: # money isn't enough
                print(f'You must input sum greater than {drink_cost} or equal')
                continue
            print('payment has been successfully completed')
            break
        if money > drink_cost:
            print('Get your change', money - drink_cost)
        self.consume_ingredients(drink_name)
        self.profit += drink_cost
        return True

def main():
    """ main function """
    resources = {"water": 300, "milk": 200, "coffee": 100,}
    # resources = {"water": 3000, "milk": 2000, "coffee": 1000,}
    menu = {
    'espresso': {"ingredients": {"water": 50, "coffee": 18, }, "cost": 1.5,},
    'latte': {"ingredients": {"water": 200, "milk": 150, "coffee": 24, }, "cost": 2.5, },
    'capuccino': {"ingredients": {"water": 250, "milk": 100, "coffee": 24,}, "cost": 3.0, },
    'romano': {"ingredients": {"water": 50, "coffee": 18, 'lemon': 10}, "cost": 5.0,} 
    }
    coffee_machine = Machine(resources, menu)
    while coffee_machine.status:
        # for admin: off, report
        drink_name = input('What would you like: espresso, latte, capuccino ? ')
        if drink_name == 'off':
            coffee_machine.status = None
        elif drink_name == 'report':
            print(coffee_machine.report)
        elif drink_name not in coffee_machine.menu:
            print('You can select espresso, latte, capuccino only')
        else:
            if coffee_machine.process_client(drink_name):
                print('Enjoy your', drink_name)

def test():
    """ testing """
    resources = {"water": 300, "milk": 200, "coffee": 100,}
    menu = {
    'espresso': {"ingredients": {"water": 50, "coffee": 18, }, "cost": 1.5,},
    'latte': {"ingredients": {"water": 200, "milk": 150, "coffee": 24, }, "cost": 2.5, },
    'capuccino': {"ingredients": {"water": 250, "milk": 100, "coffee": 24,}, "cost": 3.0, },
    'romano': {"ingredients": {"water": 50, "coffee": 18, 'lemon': 10}, "cost": 5.0,} 
    }
    coffee_machine = Machine(resources, menu)
    assert coffee_machine.check_ingredients('latte') is True
    assert coffee_machine.check_ingredients('espresso') is True
    assert coffee_machine.check_ingredients('capuccino') is True
    assert coffee_machine.check_ingredients('romano') is False

    coffee_machine.resources = {"water": 50, "coffee": 18, 'lemon': 10}
    assert coffee_machine.check_ingredients('romano') is True
    assert coffee_machine.check_ingredients('capuccino') is False
    assert coffee_machine.check_ingredients('latte') is False
    assert coffee_machine.check_ingredients('espresso') is True

if __name__ == "__main__":
    os.system('cls')
    print('-----------------------------------------------------------')
    main()
    # test()
    sys.exit()
