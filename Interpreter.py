class Interpreter:
    def __init__(self):
        self.stack = []
        self.enviroment = {}

    def STORE_NAME(self, name):
        value = self.stack.pop()
        self.enviroment[name] = value

    def LOAD_NAME(self, name):
        value = self.enviroment[name]
        self.stack.append(value)

    def LOAD_VALUE(self, number):
        self.stack.append(number)

    def PRINT_ANSWER(self):
        value = self.stack.pop()
        print(value)

    def ADD_TWO_VALUES(self):
        first = self.stack.pop()
        second = self.stack.pop()
        result = first + second
        self.stack.append(result)

    def parse_argument(self, instruction, argument, what_to_execute):
        """ Return the right arguments for each type of instruction """
        numbers = ['LOAD_VALUE']
        names = ['STORE_NAME', 'LOAD_NAME']

        if instruction in numbers:
            return what_to_execute['numbers'][argument]
        elif instruction in names:
            return what_to_execute['names'][argument]

    def run_code(self, what_to_execute):
        instructions = what_to_execute['instructions']

        for each_step in instructions:
            instruction, argument = each_step
            argument = self.parse_argument(
                instruction, argument, what_to_execute)
            if instruction == 'LOAD_VALUE':
                self.LOAD_VALUE(argument)
            elif instruction == 'PRINT_ANSWER':
                self.PRINT_ANSWER()
            elif instruction == 'ADD_TWO_VALUES':
                self.ADD_TWO_VALUES()
            elif instruction == 'STORE_NAME':
                self.STORE_NAME(argument)
            elif instruction == 'LOAD_NAME':
                self.LOAD_NAME(argument)
