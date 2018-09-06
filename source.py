import random

class Game:
    min_range = 0
    max_range = 100
    operations = ['+', '-', '*', '/']

    system_solution = ""
    user_solution = ""

    applause = ['Great!', 'You are awsome', 'Good Kidoo', 'Wow!!']

    def get_operand(self):
        return random.randint(self.min_range, self.max_range)
    
    def get_operator(self):
        return random.choice(self.operations)
    
    def calculate(self, operand_1, operand_2, operation):
        calculator = {
            '+': operand_1 + operand_2,
            '-': operand_1 - operand_2,
            '*': operand_1 * operand_2,
            '/': operand_1 / operand_2
        }

        return calculator.get(operation)

def generate_question(game):
    op1 = game.get_operand()
    op2 = game.get_operand()
    operation = game.get_operator()

    print("What is "+str(op1)+operation+str(op2))
    game.system_solution = str(game.calculate(op1, op2, operation))
    game.user_solution = input("Your answer:")

def start_game():
    game = Game()
    
    generate_question(game)

    while(True):
        if game.system_solution == game.user_solution:
            print(random.choice(game.applause))
            generate_question(game)
        else:
            print("You loose")
            print("Correct answer is: "+game.system_solution)
            return  #Game ends


if __name__ == '__main__':
    print("Let's play")
    start_game()