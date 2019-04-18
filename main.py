from Interpreter import Interpreter


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
