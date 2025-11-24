class Stack:
    def __init__(self):
        self.items = []

    def push(self, item):
        self.items.append(item)
        print(f"{item} pushed to stack")

    def pop(self):
        if not self.items:
            print("Stack is empty! Cannot pop.")
        else:
            print(f"Popped item: {self.items.pop()}")

    def peek(self):
        if not self.items:
            print("Stack is empty! Cannot peek.")
        else:
            print(f"Top item: {self.items[-1]}")

    def display(self):
        print("Stack contents:", self.items)


stack = Stack()

while True:
    print("\n--- Stack Menu ---")
    print("1. Push")
    print("2. Pop")
    print("3. Peek")
    print("4. Display Stack")
    print("5. Exit")

    choice = input("Enter your choice: ")

    if choice == '1':
        item = input("Enter value to push: ")
        stack.push(item)
    elif choice == '2':
        stack.pop()
    elif choice == '3':
        stack.peek()
    elif choice == '4':
        stack.display()
    elif choice == '5':
        print("Exiting… Thank you!")
        break
    else:
        print("Invalid choice! Please try again.")
