class Interpreter:
    def __init__(self):
        self.stack = []

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

    def run_code(self, what_to_execute):
        instructions = what_to_execute['instructions']
        numbers = what_to_execute['numbers']

        for each_step in instructions:
            instruction, argument = each_step
            if instruction == 'LOAD_VALUE':
                number = numbers[argument]
                self.LOAD_VALUE(number)
            elif instruction == 'PRINT_ANSWER':
                self.PRINT_ANSWER()
            elif instruction == 'ADD_TWO_VALUES':
                self.ADD_TWO_VALUES()


instructions = {
    'instructions': [
        ['LOAD_VALUE', 0],
        ['LOAD_VALUE', 1],
        ['ADD_TWO_VALUES', None],
        ['PRINT_ANSWER', None],
    ],
    'numbers': [2, 3]
}

i = Interpreter()
i.run_code(instructions)
