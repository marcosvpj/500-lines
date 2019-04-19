from Interpreter import Interpreter


instructions = {
    'instructions': [
        ['LOAD_VALUE', 0],
        ['STORE_NAME', 0],
        ['LOAD_VALUE', 1],
        ['STORE_NAME', 1],
        ['LOAD_NAME', 0],
        ['LOAD_NAME', 1],
        ['ADD_TWO_VALUES', None],
        ['PRINT_ANSWER', None],
    ],
    'numbers': [2, 3],
    'names': ['a', 'b'],
}

i = Interpreter()
i.run_code(instructions)
