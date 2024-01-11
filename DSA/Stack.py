class Stack:
    def __init__(self):
        self.item = []

    def isEmpty(self):
        return self.item == []
    
    def push(self, item):
        return self.item.insert(0, item)

    def pop(self):
        return self.item.pop(0)
    
    def peek(self):
        if len(self.item) == 0:
            raise Exception("peek() called on empty stack.")
        return self.item[0]
    
def revstring(string):
    mystack = Stack()
    for i in string:
        mystack.push(i)
    rev = ''
    while not mystack.isEmpty():
        rev = rev + mystack.pop()
    return rev
        
def parChecker(check):
    s = Stack()
    balance = True
    index = 0
    while index < len(check) and balance:
        symbol = check[index]
        if symbol in "([{":
            s.push(symbol)
        else:
            if s.isEmpty():
                balance = False
            else:
                top = s.pop()
                if not matches(top, symbol):
                    balance = False
        
        index += 1
    if balance and s.isEmpty():
        return True
    else:
        return False
def matches(opened, closed):
    opens = '([{'
    closes = ')]}'
    return opens.index(opened) == closes.index(closed)

def divide2by(num):
    remainderstack = Stack()
    binary_str = ''
    while num > 0:
        remainder = num % 2
        remainderstack.push(remainder)
        num = num // 2
    
    while not remainderstack.isEmpty():
        binary_str = binary_str + str(remainderstack.pop())
    
    return binary_str

def baseconverter(num, base):
    digits = '0123456789ABCDEF'
    remainderstack = Stack()
    binary_str = ''

    while num > 0:
        rem = num % base
        remainderstack.push(rem)
        num = num // 2

    while not remainderstack.isEmpty():
        binary_str = binary_str + digits[remainderstack.pop()]

    return binary_str

def infixToPostfix(input):
    prec = {}
    prec['*'] = 3
    prec['**'] = 4
    prec['/'] = 3
    prec['+'] = 2
    prec['-'] = 2
    prec['('] = 1
    opstack = Stack()
    output = []
    convert = input.split()
    for i in convert:
        if i in 'ABCDEFGHIJKLMNOPQRSTUVWXYZ' or i in '0123456789':
            output.append(i)
        elif i == '(':
            opstack.push(i)
        elif i == ')':
            top_val = opstack.pop()
            while top_val != '(':
                output.append(top_val)
                top_val = opstack.pop()
        else:
            while (not opstack.isEmpty()) and (prec[opstack.peek()] >= prec[i]):
                output.append(opstack.pop())
            opstack.push(i)

    while not opstack.isEmpty():
        output.append(opstack.pop())
    return " ".join(output)

def postfixEval(num):
    poststack = Stack()
    convert = num.split()
    for i in convert:
        if i in '01234567891017':
            poststack.push(int(i))
        else:
            first_val = poststack.pop()
            second_val = poststack.pop()
            total = calculation(i, first_val, second_val)
            poststack.push(total)
    return poststack.pop()

def calculation(symbol, first, second):
    if symbol == '*':
        return second * first
    elif symbol == '/':
        return second / first
    elif symbol == '+':
        return second + first
    elif symbol == '-':
        return second - first
    else:
        raise "Symbol is unknown"

s = Stack()
s.push("testing1")
s.push("testing2")
s.push("testing3")
# print("popping out this value : ", s.pop())
# print(s.peek())

# print("Reverse a string: ", revstring("hello"))

# print("parchecker: ", parChecker('[({})]'))

# print("Divided by: ", divide2by(42))

# print("base converter 1: ", baseconverter(25,2))
# print("base converter 2: ", baseconverter(25,16))

# print("Infix into postfix 1: ", infixToPostfix("A * B + C * D"))
# print("Infix into postfix 2: ", infixToPostfix("( A + B ) * C - ( D - E ) * ( F + G )"))
# print("Infix into postfix testing Q3: ", infixToPostfix("9 + 3 * 5 / ( 6 - 4 )"))
# print("Infix into postfix testing Q5: ", infixToPostfix("5 * 3 ** ( 4 - 2 )"))

# print("Postfix 1:", postfixEval('7 8 + 3 2 + /'))
# print("Postfix testing Q4", postfixEval('17 10 + 3 * 9 /'))
