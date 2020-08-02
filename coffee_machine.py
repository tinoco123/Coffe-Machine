class CoffeMachine:
    money = 550
    water = 400
    milk = 540
    coffe_beans = 120
    disposable_cups = 9

    def main(self):
        while True:
            action = self.input_text("Write action (buy, fill, take, remaining, exit):")
            if action == "exit":
                break
            elif action == "remaining":
                self.machine_state()
            elif action == "buy":
                self.buy()
            elif action == "fill":
                self.fill()
            elif action == "take":
                self.take()

    def buy(self):
        item = self.input_text("What do you want to buy? 1 - espresso, 2 - latte, 3 - cappuccino, back - to main menu:")
        if item == "back":
            return
        elif int(item) == 1:
            self.buy_espreesso()
        elif int(item) == 2:
            self.buy_latte()
        elif int(item) == 3:
            self.buy_cappucino()

    def machine_state(self):
        print("The coffe machine has:\n"
              f"{CoffeMachine.water} of water\n"
              f"{CoffeMachine.milk} of milk\n"
              f"{CoffeMachine.coffe_beans} of coffe beans\n"
              f"{CoffeMachine.disposable_cups} of disposable cups\n"
              f"${CoffeMachine.money} of money\n")

    def fill(self):
        CoffeMachine.water += int(self.input_text("Write how many ml of water do you want to add:"))
        CoffeMachine.milk += int(self.input_text("Write how many ml of milk do you want to add:"))
        CoffeMachine.coffe_beans += int(self.input_text("Write how many grams of coffee beans do you want to add:"))
        CoffeMachine.disposable_cups += int(self.input_text("Write how many disposable cups of coffee do you want to add:"))

    def take(self):
        print(f"I gave you ${CoffeMachine.money}")
        CoffeMachine.money = 0

    def validate(self, water_need, coffe_beans_need, milk_need, coffe_type):
        if coffe_type == "espresso":
            if CoffeMachine.water // water_need >= 1 and CoffeMachine.coffe_beans // coffe_beans_need >= 1:
                return "I have enough resources, making you a coffee!", True
            elif CoffeMachine.water // water_need < 1:
                return "Sorry, not enough water!", False
            elif CoffeMachine.coffe_beans // coffe_beans_need < 1:
                return "Sorry, not enough coffe beans!", False
        else:
            if CoffeMachine.water // water_need >= 1 and CoffeMachine.coffe_beans // coffe_beans_need >= 1 and CoffeMachine.milk // milk_need >= 1:
                return "I have enough resources, making you a coffee!", True
            elif CoffeMachine.water // water_need < 1:
                return "Sorry, not enough water!", False
            elif CoffeMachine.coffe_beans // coffe_beans_need < 1:
                return "Sorry, not enough coffe beans!", False
            elif CoffeMachine.milk // milk_need < 1:
                return "Sorry, not enough milk!", False

    def buy_espreesso(self):
        can_do_coffe = self.validate(250, 16, 0, "espresso")
        if can_do_coffe[1]:
            print(can_do_coffe[0])
            CoffeMachine.water -= 250
            CoffeMachine.coffe_beans -= 16
            CoffeMachine.money += 4
            CoffeMachine.disposable_cups -= 1
        else:
            print(can_do_coffe[0])

    def buy_latte(self):
        can_do_coffe = self.validate(350, 20, 75, "latte")
        if can_do_coffe[1]:
            print(can_do_coffe[0])
            CoffeMachine.water -= 350
            CoffeMachine.milk -= 75
            CoffeMachine.coffe_beans -= 20
            CoffeMachine.disposable_cups -= 1
            CoffeMachine.money += 7
        else:
            print(can_do_coffe[0])

    def buy_cappucino(self):
        can_do_coffe = self.validate(200, 12, 100, "cappucino")
        if can_do_coffe[1]:
            print(can_do_coffe[0])
            CoffeMachine.water -= 200
            CoffeMachine.milk -= 100
            CoffeMachine.coffe_beans -= 12
            CoffeMachine.disposable_cups -= 1
            CoffeMachine.money += 6
        else:
            print(can_do_coffe[0])

    def input_text(self, text):
        text_input = input(text)
        return text_input


if __name__ == '__main__':
    coffe_machine = CoffeMachine()
    coffe_machine.main()