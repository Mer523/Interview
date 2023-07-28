class Stack:

    def __init__(self):
        self.data = []

    def is_empty(self):
        if self.data:
            return True
        else:
            return False

    def push(self, el):
        self.data.append(el)

    def pop(self):
        return self.data.pop()

    def peek(self):
        return self.data[-1]

    def size(self):
        return len(self.data)



def check_balance(arr):
    corr_parenth = {'}': '{', ')': '(', ']': '['}
    if len(arr) % 2 != 0 or arr[0] in corr_parenth:
        print('Несбалансированно')
    else:
        stack = Stack()
        for el in arr:
            if el in corr_parenth.values():
                stack.push(el)
            elif stack.data and el in corr_parenth and stack.peek() == corr_parenth[el]:
                stack.pop()

        if not stack.is_empty():
            print('Сбалансированно')
        else:
            print('Несбалансированно')


if __name__ == '__main__':

    n1 = '(((([{}]))))'
    n4 = '[([])((([[[]]])))]{()}'
    n2 = '[([])((([[[]]])))]'
    n3 = '{{[()]}}'
    m1 = '}{}'
    m2 = '{{[(])]}}'
    m3 = '[[{())}]'
    m4 = '}{}{'


    check_balance(n1)
    check_balance(m2)