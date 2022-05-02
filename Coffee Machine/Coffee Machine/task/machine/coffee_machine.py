import string


class Espresso:
    id = 1
    water = 250
    coffee = 16
    price = 4


class Latte:
    id = 2
    water = 350
    milk = 75
    coffee = 20
    price = 7


class Capuchino:
    id = 3
    water = 200
    milk = 100
    coffee = 12
    price = 6


class MaquinaCafe:
    water = 400
    milk = 540
    coffee = 120
    cups = 9
    money = 550
    espresso = 1
    latte = 2
    cappuccino = 3
    action_buy = "buy"
    action_fill = "fill"
    action_take = "take"

    coffee_espresso = Espresso()
    coffee_latte = Latte()
    coffee_capuchino = Capuchino()

    def __init__(self):
        pass

    try:
        @staticmethod
        def fx_exc_tpl(self):
            pass
    except TypeError:
        pass
    except Exception as e:
        print(str(e))
    else:
        pass
    finally:
        pass

    try:
        @staticmethod
        def insufficient_ingredient(ingredient):
            print(f"Sorry, not enough {ingredient}!")
    except TypeError:
        pass
    except Exception as e:
        print(str(e))
    else:
        pass
    finally:
        pass

    try:
        @staticmethod
        def availability(coffee_type):
            if coffee_machine.cups >= 1:
                if coffee_type == 1:
                    if coffee_machine.water >= coffee_machine.coffee_espresso.water and \
                            coffee_machine.coffee >= coffee_machine.coffee_espresso.coffee:
                        return True
                    else:
                        if coffee_machine.water < coffee_machine.coffee_espresso.water:
                            coffee_machine.insufficient_ingredient("water")

                        if coffee_machine.coffee < coffee_machine.coffee_espresso.coffee:
                            coffee_machine.insufficient_ingredient("coffee")

                        return False
                elif coffee_type == 2:
                    if coffee_machine.water >= coffee_machine.coffee_latte.water and \
                            coffee_machine.coffee >= coffee_machine.coffee_latte.coffee and \
                            coffee_machine.milk >= coffee_machine.coffee_latte.milk:
                        return True
                    else:
                        if coffee_machine.water < coffee_machine.coffee_latte.water:
                            coffee_machine.insufficient_ingredient("water")

                        if coffee_machine.coffee < coffee_machine.coffee_latte.coffee:
                            coffee_machine.insufficient_ingredient("coffee")

                        if coffee_machine.milk < coffee_machine.coffee_latte.milk:
                            coffee_machine.insufficient_ingredient("milk")

                        return False

                elif coffee_type == 3:
                    if coffee_machine.water >= coffee_machine.coffee_capuchino.water and \
                            coffee_machine.coffee >= coffee_machine.coffee_capuchino.coffee and \
                            coffee_machine.milk >= coffee_machine.coffee_capuchino.milk:
                        return True
                    else:
                        if coffee_machine.water < coffee_machine.coffee_capuchino.water:
                            coffee_machine.insufficient_ingredient("water")

                        if coffee_machine.coffee >= coffee_machine.coffee_capuchino.coffee:
                            coffee_machine.insufficient_ingredient("coffee")

                        if coffee_machine.milk >= coffee_machine.coffee_capuchino.milk:
                            coffee_machine.insufficient_ingredient("milk")

                        return False
                else:
                    return False
            else:
                coffee_machine.insufficient_ingredient("cups")
                return False
    except TypeError:
        pass
    except Exception as e:
        print(str(e))
    else:
        pass
    finally:
        pass

    try:
        @staticmethod
        def take():
            print(f"I gave you ${MaquinaCafe.money}")
            MaquinaCafe.money -= MaquinaCafe.money
            return

    except TypeError:
        pass
    except Exception as e:
        print(str(e))
    else:
        pass
    finally:
        pass

    try:
        @staticmethod
        def fill():
            water = int(input("Write how many ml of water you want to add:\n"))
            milk = int(input("Write how many ml of milk you want to add:\n"))
            coffee = int(input("Write how many grams of coffee beans you want to add:\n"))
            cups = int(input("Write how many disposable coffee cups you want to add:\n"))

            MaquinaCafe.water += water
            MaquinaCafe.milk += milk
            MaquinaCafe.coffee += coffee
            MaquinaCafe.cups += cups

    except TypeError:
        pass
    except Exception as e:
        print(str(e))
    else:
        pass
    finally:
        pass

    try:
        @staticmethod
        def sale(self):
            option = input("What do you want to buy? 1 - espresso, 2 - latte, 3 - cappuccino, back - to main menu::\n")
            if option in string.digits:
                option = int(option)
            if coffee_machine.availability(option):
                if option == MaquinaCafe.coffee_espresso.id:
                    MaquinaCafe.water -= MaquinaCafe.coffee_espresso.water
                    MaquinaCafe.coffee -= MaquinaCafe.coffee_espresso.coffee
                    MaquinaCafe.money += MaquinaCafe.coffee_espresso.price
                elif option == MaquinaCafe.coffee_latte.id:
                    MaquinaCafe.water -= MaquinaCafe.coffee_latte.water
                    MaquinaCafe.milk -= MaquinaCafe.coffee_latte.milk
                    MaquinaCafe.coffee -= MaquinaCafe.coffee_latte.coffee
                    MaquinaCafe.money += MaquinaCafe.coffee_latte.price
                elif str(option) == "back":
                    coffee_machine.action()
                else:
                    MaquinaCafe.water -= MaquinaCafe.coffee_capuchino.water
                    MaquinaCafe.milk -= MaquinaCafe.coffee_capuchino.milk
                    MaquinaCafe.coffee -= MaquinaCafe.coffee_capuchino.coffee
                    MaquinaCafe.money += MaquinaCafe.coffee_capuchino.price

                MaquinaCafe.cups -= 1
                print("I have enough resources, making you a coffee!")
            # else:
            #     print("NO enough resources, making you a coffee!")
    except TypeError:
        pass
    except Exception as e:
        print(str(e))
    else:
        pass
    finally:
        pass

    try:
        @staticmethod
        def status():
            print(f"The coffee machine has:\n"
                  f"{MaquinaCafe.water} of water\n"
                  f"{MaquinaCafe.milk} of milk\n"
                  f"{MaquinaCafe.coffee} of coffee beans\n"
                  f"{MaquinaCafe.cups} of disposable cups\n"
                  f"${MaquinaCafe.money} of money")
            return
    except Exception as e:
        print(str(e))
    else:
        pass

    try:
        @staticmethod
        def action():
            action = input("Write action(buy, fill, take, remaining, exit):\n")
            if action == MaquinaCafe.action_buy:
                print()
                coffee_machine.sale(self=None)
            elif action == MaquinaCafe.action_fill:
                print()
                coffee_machine.fill()
            elif action == "remaining":
                print()
                coffee_machine.status()
            elif action == "exit":
                quit()
            else:
                coffee_machine.take()

            print()
            coffee_machine.action()
            # coffee_machine.status(self=None)
            return
    except TypeError:
        pass
    except Exception as e:
        print(str(e))
    else:
        pass
    finally:
        pass


if __name__ == '__main__':
    coffee_machine = MaquinaCafe()
    coffee_machine.action()
