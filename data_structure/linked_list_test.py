"""The LinkedList code from before is provided below.
Add three functions to the LinkedList.
"get_position" returns the element at a certain position.
The "insert" function will add an element to a particular
spot in the list.
"delete" will delete the first element with that
particular value.
Then, use "Test Run" and "Submit" to run the test cases
at the bottom."""


class Element(object):
    def __init__(self, value):
        self.value = value
        self.next = None


class LinkedList(object):
    def __init__(self, head=None):
        self.head = head

    def append(self, new_element):
        current = self.head
        if self.head:
            while current.next:
                current = current.next
            current.next = new_element
        else:
            self.head = new_element

    def get_position(self, position):
        """Get an element from a particular position.
        Assume the first position is "1".
        Return "None" if position is not in the list."""
        if self.head:
            current = self.head
            current_pos = 1
            while current_pos < position:
                if not current.next:
                    return None
                current = current.next
                current_pos += 1
            return current
        return None

    def insert(self, new_element, position):
        """Insert a new node at the given position.
        Assume the first position is "1".
        Inserting at position 3 means between
        the 2nd and 3rd elements."""
        if self.head:
            current = self.head
            pos = 1
            while pos < position - 1:
                current = current.next
                pos += 1
            new_element.next = current.next
            current.next = new_element
        else:
            self.head = new_element

    def delete(self, value):
        """Delete the first node with a given value."""
        current = self.head
        if current.value == value:
            if current.next:
                self.head = current.next
            else:
                self.head = None
        while current.next.value != value:
            if not current.next.next:
                return
            current = current.next
        else:
            if current.next.next:
                current = current.next.next
            else:
                current.next = None

    def print_all(self):
        current = self.head
        while current.next:
            print("Blah ", current.value)
            current = current.next
        print("Blah", current.value)


# Test cases
# Set up some Elements
e1 = Element(1)
e2 = Element(2)
e3 = Element(3)
e4 = Element(4)

# Start setting up a LinkedList
ll = LinkedList(e1)
ll.append(e2)
ll.append(e3)
ll.print_all()

# Test get_position
# Should print 3
print(ll.head.next.next.value)
# Should also print 3
print(ll.get_position(3).value)

# Test insert
ll.insert(e4, 3)
# Should print 4 now
print(ll.get_position(3).value)

# Test delete
ll.delete(1)
# Should print 2 now
print(ll.get_position(1).value)
# Should print 4 now
print(ll.get_position(2).value)
# Should print 3 now
print(ll.get_position(3).value)