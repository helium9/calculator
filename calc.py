# +, *, **, -, /, trig
import random

pi = 3.14159265359

def fac(x):
    if x==0:
        return 1
    else:
        fac_value = x
        while x != 1:
            x-=1
            fac_value*=x
        return fac_value

def sin(x):
    neg = False
    if x<0: #support for negative entries
        neg = True
        x*=(-1)
    x = x%(2*pi) #bringing the input closer to 0 as the Maclaurin series will have less error around 0.
    expression = 0
    for iter in range(20):
        expression = expression + ((-1)**iter)*(x**(2*iter + 1))/fac(2*iter + 1)
    if neg == True:
        return -(expression)
    else:
        return expression

def cos(x):
    if x<0: #support for negative entries
        x*=(-1)
    expression = 0
    x = x%(2*pi) #bringing the input closer to 0 as the Maclaurin series will have less error around 0.
    for iter in range(20):
        expression = expression + ((-1)**iter)*(x**(2*iter))/fac(2*iter)
    return expression

def tan(x):
    return sin(x)/cos(x)

def max_freq(x): #returns highest occuring elem in a list
    set_soln = set(x)
    list_set = list(set_soln)
    freq = 0
    elem = 0
    for item in list_set:
        count = x.count(item)
        if count>freq:
            freq = count
            elem = item
    return elem

def arcsin(x): #using Newton–Raphson method for finding root of y = x0(input) and sin(x).
    var_list = []
    for iter in range(10):    #running the algorithm a few times to eliminate wrong roots due to divergence.
        var = random.uniform(-pi/2, pi/2)
        #print(var)

        def next(x, x0):
            return (x - (sin(x) - x0)/cos(x))

        for iter in range(1, 75):
            var_next = next(var, x)
            var = var_next
        var_list.append(var)
    out = max_freq(var_list) #taking in the highest occuring root (presumably correct)
    return out

def arccos(x): #using Newton–Raphson method for finding root of y = x0(input) and sin(x).
    var_list = []
    for iter in range(10): #running the algorithm a few times to eliminate wrong roots due to divergence.
        var = random.uniform(0, pi)
        #print(var)

        def next(x, x0):
            return (x + (cos(x) - x0)/sin(x))

        for iter in range(1, 75):
            var_next = next(var, x)
            var = var_next
        var_list.append(var)
    out = max_freq(var_list) #taking in the highest occuring root (presumably correct)
    return out

def arctan(x): #works only till three decimal points
    val = arcsin(x/((1+x**2)**(1/2)))
    return val

print("\nCALCULATOR\n")
interface = "0. Exit\n1. Add '+'\n2. Subtract '-'\n3. Multiply 'x'\n4. Divide '/'\n5. Exponentiation '^'\n6. Factorial '!'\n7. sin()\n8. cos()\n9. tan()\n10. arcsin()\n11. arccos()\n12. arctan()"
print(interface)


expr = input('Enter expression (with spaces between each operation) \n or \nEnter numbers one by one (by pressing enter after each number and operation): ')

split_expr = expr.split(' ')

Op_req = True
if ' ' not in expr: #Check for single interface mode or complete expression
    while True:
        if Op_req is True:
            print(interface)

            val = input('Enter operation: ')

            if val == '' or int(val) == 0:
                break
            
            if int(val) == 1:
                split_expr.append('+')
            elif int(val) == 2:
                split_expr.append('-')
            elif int(val) == 3:
                split_expr.append('x')
            elif int(val) == 4:
                split_expr.append('/')
            elif int(val) == 5:
                split_expr.append('^')
            elif int(val) == 6:
                split_expr.append('!')
            elif int(val) == 7:
                repl = 'sin(' + split_expr[len(split_expr) - 1] + ')'
                split_expr[len(split_expr) - 1] = repl
            elif int(val) == 8:
                repl = 'cos(' + split_expr[len(split_expr) - 1] + ')'
                split_expr[len(split_expr) - 1] = repl
            elif int(val) == 9:
                repl = 'tan(' + split_expr[len(split_expr) - 1] + ')'
                split_expr[len(split_expr) - 1] = repl
            elif int(val) == 10:
                repl = 'arcsin(' + split_expr[len(split_expr) - 1] + ')'
                split_expr[len(split_expr) - 1] = repl
            elif int(val) == 11:
                repl = 'arccos(' + split_expr[len(split_expr) - 1] + ')'
                split_expr[len(split_expr) - 1] = repl
            elif int(val) == 12:
                repl = 'arctan(' + split_expr[len(split_expr) - 1] + ')'
                split_expr[len(split_expr) - 1] = repl


            if int(val) < 6: #binary
                Op_req = False
            if int(val) >= 6: #unary
                pass

        elif Op_req is False:
            val = input("Enter number: ")
            if val == '':
                del split_expr[len(split_expr) - 1]
                break
            split_expr.append(val)
            Op_req = True
        
        #print(split_expr)
        print('The expression entered is: \'' + str(''.join(split_expr)) + '\'')
print('The expression is: \'' + str(''.join(split_expr)) + '\'')


#fixing string for evaluation
while 'x' in split_expr:
    split_expr[split_expr.index('x')] = '*'
while 'X' in split_expr:
    split_expr[split_expr.index('X')] = '*'
while '\\' in split_expr:
    split_expr[split_expr.index('\\')] = '/'
while '^' in split_expr:
    split_expr[split_expr.index('^')] = '**'
while '!' in split_expr:
    repl = str(fac(int(split_expr[split_expr.index('!') - 1])))
    split_expr[split_expr.index('!') - 1] = repl
    del split_expr[split_expr.index('!')] #Wherever pre eval processing is done, make sure the output is string.


#print(split_expr)
print('The output is: ' + str(eval(''.join(split_expr))))