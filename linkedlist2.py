class Node:
    def _init_(self, u):
        self.data = u
        self.nxt = None

class SLL:
    def _init_(self):
        self.head = None

    def display(self):
        t = self.head
        while t is not None:
            print(t.data, end="->")
            t = t.nxt
        print("None")

    def addback(self, x):
        if not self.head:
            self.head = Node(x)
            return
        t = self.head
        while t.nxt is not None:
            t = t.nxt
        t.nxt = Node(x)

    def addeven(self):
        t = self.head
        s = 0
        while t is not None:
            if t.data % 2 == 0:
                s += t.data
            t = t.nxt
        print(f"Sum of even elements: {s}")

    def linear(self, value):
        t = self.head
        while t is not None:
            if t.data == value:
                return True
            t = t.nxt
        return False

    def find_middle(self):
        slow = self.head
        fast = self.head
        
        while fast is not None and fast.nxt is not None:
            slow = slow.nxt
            fast = fast.nxt.nxt
        
        if slow is not None:
            print(f"Middle element: {slow.data}")
        else:
            print("The list is empty.")

    def check_length_even_odd(self):
        count = 0
        t = self.head
        while t is not None:
            count += 1
            t = t.nxt
        if count % 2 == 0:
            print("The length of the list is even.")
        else:
            print("The length of the list is odd.")



l1 = SLL()
l1.addback(10)
l1.addback(20)
l1.addback(40)
l1.addback(50)
l1.addback(60)
l1.addback(70)


print("Displaying list:")
l1.display()

print("Adding even numbers:")
l1.addeven()

print("Linear search for 30:")
print(l1.linear(30))  

print("Linear search for 100:")
print(l1.linear(100)) 

print("Finding middle number in the list:")
l1.find_middle()

print("Checking if the length of the list is even or odd:")
l1.check_length_even_odd()
