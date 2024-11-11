

def merge(array, p, q, r, f):
    
    start, mid, end = p, q, r
    n_left = mid - start + 1
    n_right = end - mid
    left_array = [array[n] for n in range(start, mid + 1)]
    right_array = [array[n] for n in range(mid + 1, end + 1)]
    left_marker, right_marker = 0, 0
    target = start
    #print("Left array: {} \n Right array: {}\n left, right, target = {},{},{}".format(left_array, right_array,left_marker,right_marker,target))
    while left_marker < n_left and right_marker < n_right:
        if f(left_array[left_marker]) <= f(right_array[right_marker]):   #  <---- calling the function here to compare the elements
            array[target] = left_array[left_marker]
            left_marker += 1
        else:
            array[target] = right_array[right_marker]
            right_marker += 1
        target += 1
    while left_marker < n_left:
        array[target] = left_array[left_marker]
        left_marker += 1
        target += 1
    while right_marker < n_right:
        array[target] = right_array[right_marker]
        right_marker += 1
        target += 1


def mergesort_recursive(array, p, r, func):
    start, end = p, r
    if end - start > 0:
        mid = (start + end) //2
        mergesort_recursive(array, start, mid, func)
        mergesort_recursive(array, mid +1, end, func)
        merge(array, start, mid, end, func)

## mergesort
def mergesort(array, byfunc=None):
    if byfunc is None:
        byfunc = lambda x: x
    mergesort_recursive(array, 0, len(array) - 1, byfunc)

class Stack:
    def __init__(self) -> None:
        self.__items = []
        
    def push(self, item):
        self.__items.append(item)

    def pop(self):
        return self.__items.pop() if not self.is_empty else None

    def peek(self):
        return None if self.is_empty else self.__items[-1]

    @property
    def is_empty(self) -> bool:
        return self.__items == []

    @property
    def size(self):
        return len(self.__items)

    @property
    def items (self):
        return self.__items

class EvaluateExpression:
  # copy the other definitions
  # from the previous parts
  op = {'+': lambda x, y: x + y,
          '-': lambda x, y: x - y,
          '*': lambda x, y: x * y,
          '/': lambda x, y: x // y}
  valid_char = '0123456789+-*/() '
  def __init__(self, string=""):
    self.expression = string

  @property
  def expression(self):
    return self.expr

  @expression.setter
  def expression(self, new_expr):
    for char in new_expr:
      if char not in self.valid_char:
        self.expr = ""
        return
    self.expr = new_expr
  

  def insert_space(self):
    new_str = ""
    for char in self.expression:
      new_str += char if char not in "+-*/()" else ' ' + char + ' '
    return new_str
  
  def process_operator(self, operand_stack, operator_stack):
    operator = operator_stack.pop()
    right_op, left_op = operand_stack.pop(), operand_stack.pop()
    operand_stack.push(self.op[operator](left_op, right_op))
  

  def evaluate(self):
    operand_stack = Stack()
    operator_stack = Stack()
    expression = self.insert_space()
    tokens = expression.split()

    ##Phase 1
    for char in tokens:
      if char in "0123456789":
        operand_stack.push(int(char))
      elif char in "+-":
        while not operator_stack.is_empty and operator_stack.peek() != "(":
          self.process_operator(operand_stack, operator_stack)
        operator_stack.push(char)
      elif char in "*/":
        while not operator_stack.is_empty and operator_stack.peek() in "*/" and operator_stack.peek() != "(":
          self.process_operator(operand_stack, operator_stack)
        operator_stack.push(char)
      elif char == "(":
        operator_stack.push(char)
      elif char == ")":
        while operator_stack.peek() != "(":
          self.process_operator(operand_stack, operator_stack)
        operator_stack.pop()

      #print("checking char : ", char, operand_stack.items, operator_stack.items)

    ##Phase 2
    while not operator_stack.is_empty:
        self.process_operator(operand_stack, operator_stack)
    return operand_stack.pop()


def get_smallest_three(challenge):
  records = challenge.records
  times = [r for r in records]
  mergesort(times, lambda x: x.elapsed_time)
  return times[:3]





