import sys


def multiply(arg1, arg2):
    return arg1 * arg2


def add(arg1, arg2):
    return arg1 + arg2


''' 
An example of Add function to support an arbitrary number of arguments
def add2(expression):
    result = 0
    for arg in expression[1:]:
        result += int(arg)
    return result
'''

'''
An example of exponent function type
def exponent(arg1, arg2):
    return arg1**arg2
'''


def sexp_calculator(expression):
    if expression[0] == 'multiply':  # check for type of function, 'multiply'
        return multiply(int(expression[1]), int(expression[2]))

    elif expression[0] == 'add':  # check for type of function, 'add'
        return add(int(expression[1]), int(expression[2]))


''' An example of Add function to support an arbitrary number of arguments 
    elif expression[0] == 'add':  # check for type of function, 'add'
        return add2(expression)
'''

'''
    More function types can be defined and added here!
    An example of exponent function type
    elif expression[0] == 'exponent':
        return exponent(int(expression[1]), int(expression[2]))
'''


class SExpression:
    def __init__(self, inp_sexp):
        self.inp_sexp = inp_sexp

    def parser(self):
        while '(' in self.inp_sexp:
            # find the first ')' and '(' according to that --> the innermost and left most expression
            right_bound = self.inp_sexp.find(')')
            left_bound = self.inp_sexp[:right_bound].rfind('(')

            # split the innermost expresion base on the single space, " ", between function arguments
            sub_expression = self.inp_sexp[left_bound + 1:right_bound].split(" ")

            # calculate sub expression value
            sub_expression = sexp_calculator(sub_expression)

            # replace sub expression with the calculated value
            self.inp_sexp = self.inp_sexp[:left_bound] + str(sub_expression) + self.inp_sexp[right_bound + 1:]

        return self.inp_sexp


if __name__ == '__main__':
    print(SExpression(sys.argv[1]).parser())
