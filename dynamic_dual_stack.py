class DynamicDualStack:
    def __init__(self, n=10):
        if n <= 0:
            n = 1
        self.array = [None] * n
        self.stack_sizes = [0, 0]
        self.initial_capacity = n
        self.array_capacity = n

    def __copy__(self):
        new_stack = DynamicDualStack(self.array_capacity)
        new_stack.stack_sizes = self.stack_sizes.copy()
        new_stack.array[:self.stack_sizes[0]] = self.array[:self.stack_sizes[0]]
        new_stack.array[-self.stack_sizes[1] :] = self.array[-self.stack_sizes[1]:]
        return new_stack

    def top(self, m):
        if m not in [0, 1]:
            raise ValueError("Invalid stack identifier")
        if self.empty(m):
            raise IndexError("Stack is empty")
        if m == 0:
            return self.array[self.stack_sizes[0] - 1]
        else:
            return self.array[-self.stack_sizes[1]]

    def size(self, m):
        if m not in [0, 1]:
            raise ValueError("Invalid stack identifier")
        return self.stack_sizes[m]

    def empty(self, m):
        if m not in [0, 1]:
            raise ValueError("Invalid stack identifier")
        return self.stack_sizes[m] == 0

    def capacity(self):
        return self.array_capacity

    def push(self, m, item):
        if m not in [0, 1]:
            raise ValueError("Invalid stack identifier")
        if self.stack_sizes[0] + self.stack_sizes[1] == self.array_capacity:
            self._resize(2 * self.array_capacity)
        if m == 0:
            self.array[self.stack_sizes[0]] = item
            self.stack_sizes[0] += 1
        else:
            self.array[-self.stack_sizes[1] - 1] = item
            self.stack_sizes[1] += 1

    def pop(self, m):
        if m not in [0, 1]:
            raise ValueError("Invalid stack identifier")
        if self.empty(m):
            raise IndexError("Stack is empty")
        if m == 0:
            item = self.array[self.stack_sizes[0] - 1]
            self.stack_sizes[0] -= 1
        else:
            item = self.array[-self.stack_sizes[1]]
            self.stack_sizes[1] -= 1
        if self.stack_sizes[0] + self.stack_sizes[1] <= self.array_capacity // 4 and self.array_capacity // 2 >= self.initial_capacity:
            self._resize(self.array_capacity // 2)
        return item

    def clear(self):
        self.stack_sizes = [0, 0]
        if self.array_capacity != self.initial_capacity:
            self._resize(self.initial_capacity)

    def _resize(self, new_capacity):
        print("Resize applied: new capacity =", new_capacity)
        new_array = [None] * new_capacity
        new_array[:self.stack_sizes[0]] = self.array[:self.stack_sizes[0]]
        new_array[-self.stack_sizes[1]:] = self.array[-self.stack_sizes[1]:]
        self.array = new_array
        self.array_capacity = new_capacity

    def swap(self, other):
        self.array, other.array = other.array, self.array
        self.stack_sizes, other.stack_sizes = other.stack_sizes, self.stack_sizes
        self.initial_capacity, other.initial_capacity = other.initial_capacity, self.initial_capacity
        self.array_capacity, other.array_capacity = other.array_capacity, self.array_capacity


# Example usage of the DynamicDualStack class
# Example usage of the DynamicDualStack class
stack1 = DynamicDualStack()  # Create a new instance of DynamicDualStack

stack1.push(0, 10)  # Push 10 onto the first stack
stack1.push(1, 20)  # Push 20 onto the second stack
stack1.push(0, 30)  # Push 30 onto the first stack
stack1.push(1, 40)  # Push 40 onto the second stack

print(stack1.pop(0))  # Output: 30 (Pop the top element from the first stack)
print(stack1.pop(1))  # Output: 40 (Pop the top element from the second stack)

print(stack1.top(0))  # Output: 10 (Get the top element from the first stack)
print(stack1.top(1))  # Output: 20 (Get the top element from the second stack)

print(stack1.size(0))  # Output: 1 (Get the size of the first stack)
print(stack1.size(1))  # Output: 1 (Get the size of the second stack)

print(stack1.empty(0))  # Output: False (Check if the first stack is empty)
print(stack1.empty(1))  # Output: False (Check if the second stack is empty)

# Output: Current capacity (Get the current capacity of the array)
print(stack1.capacity())

stack1.push(0, 50)  # Push 50 onto the first stack of stack1 (trigger resize)
stack1.push(1, 60)  # Push 60 onto the second stack of stack1 (trigger resize)
stack1.push(0, 89)
stack1.push(1, 90)
stack1.push(0, 50)  # Push 50 onto the first stack of stack1 (trigger resize)
stack1.push(1, 60)  # Push 60 onto the second stack of stack1 (trigger resize)

stack1.push(1, 60)
stack1.push(0, 50)  # Push 50 onto the first stack of stack1 (trigger resize)
stack1.push(1, 60)  # Push 60 onto the second stack of stack1 (trigger resize)
stack1.push(0, 89)
stack1.push(1, 90)
stack1.push(0, 50)  # Push 50 onto the first stack of stack1 (trigger resize)
stack1.push(1, 60)  # Push 60 onto the second stack of stack1 (trigger resize)

stack1.push(1, 60)

print("After resize:")
# Output: New capacity (Get the updated capacity of the array)
print(stack1.capacity())

stack1.push(0, 70)  # Push 70 onto the first stack of stack1 (no resize)


stack2 = DynamicDualStack()  # Create another instance of DynamicDualStack

stack2.push(0, 80)  # Push 80 onto the first stack of stack2
stack2.push(1, 90)  # Push 90 onto the second stack of stack2

print("Before swap:")
# Output: 70 (Get the top element from the first stack of stack1)
print(stack1.top(0))
# Output: None (Get the top element from the second stack of stack1)
print(stack1.top(1))
# Output: 80 (Get the top element from the first stack of stack2)
print(stack2.top(0))
# Output: 90 (Get the top element from the second stack of stack2)
print(stack2.top(1))

stack1.swap(stack2)  # Swap the member variables of stack1 with stack2

print("After swap:")
# Output: 80 (Get the top element from the first stack of stack1)
print(stack1.top(0))
# Output: 90 (Get the top element from the second stack of stack1)
print(stack1.top(1))
# Output: 70 (Get the top element from the first stack of stack2)
print(stack2.top(0))
# Output: None (Get the top element from the second stack of stack2)
print(stack2.top(1))

stack1.clear()  # Clear the stacks (trigger resize)
print("After clear:")
# Output: Initial capacity (Get the capacity after clear)
print(stack1.capacity())
