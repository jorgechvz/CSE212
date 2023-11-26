"""
CSE212 
(c) BYU-Idaho
04-Prove - Problem 2

It is a violation of BYU-Idaho Honor Code to post or share this code with others or 
to post it online.  Storage into a personal and private repository (e.g. private
GitHub repository, unshared Google Drive folder) is acceptable.
"""

class Priority_Queue:
    """
    This queue follows the same FIFO process except that higher priority
    nodes will be dequeued before lower priority nodes.  Nodes of the same
    priority will follow the same FIFO process.
    """

    class Node:
        """
        Each node is the queue will have both a value and a priority.
        """

        def __init__(self, value, priority):
            """
            Initialize a new node
            """
            self.value = value
            self.priority = priority

        def __str__(self):
            """
            Display a single node
            """
            return "{} (Pri:{})".format(self.value, self.priority)

    def __init__(self):
        """ 
        Initialize an empty priority queue
        """
        self.queue = []

    def enqueue(self, value, priority):
        """
        Add a new value to the queue with an associated priority.  The
        node is always added to the back of the queue irregardless of 
        the priority.
        """
        #new_node = Priority_Queue.Node(priority, value)  # Defect 1 - Change the order of parameters (priority, value) to (value, priority)
        new_node = Priority_Queue.Node(value, priority)
        self.queue.append(new_node)

    def dequeue(self):
        """
        Remove the next value from the queue based on the priority.  The 
        highest priority item will be removed.  In the case of multiple
        values with the same high priority, the one closest to the front
        (in traditional FIFO order) will be removed.  Priority values are
        interpreted as higher numbers have higher priority.  For example, 
        10 is a higher priority than 5.
        """
        if len(self.queue) == 0:  # Verify the queue is not empty
            # print("The queue is empty.")
            # return None                     # Defect 4 - Return should the error message
            return "The queue is empty."
        # Find the index of the item with the highest priority to remove
        high_pri_index = 0
        for index in range(1, len(self.queue)):
            # if self.queue[index].priority >= self.queue[high_pri_index].priority: 
            # Defect 3 - The if statement should use >
            if self.queue[index].priority > self.queue[high_pri_index].priority:
                high_pri_index = index
        # Remove and return the item with the highest priority
        value = self.queue[high_pri_index].value
        del self.queue[high_pri_index]      # Defect 2 - Should add method to remove from the queue: del self.queue[high_pri_index]  
        return value
        
    def __len__(self):
        """
        Support the len() function
        """
        return len(self.queue)

    def __str__(self):
        """ 
        Suppport the str() function to provide a string representation of the
        priority queue.  This is useful for debugging.  If you have a 
        Priority_Queue object called pq, then you run print(pq) to see the 
        contents.
        """
        result = "["
        for node in self.queue:
            result += str(node)  # This uses the __str__ from the Node class
            result += ", "
        result += "]"
        return result

# Test Cases

# Test 1
# Scenario: Create a queue with the following values and priority: Test 1 (5), Test 2 (10)
# Expected Result: Test 1 (Pri: 5), Test 2 (Pri 10)
print("Test 1")
pq = Priority_Queue()
pq.enqueue("Test 1", 5)
pq.enqueue("Test 2", 10)
print("Queue: ", pq)
print("Length: ", pq.__len__())

# Defect(s) Found: The order of parameters in display node is incorrect 

print("=================")

# Test 2
# Scenario: One element is dequeued from the priority queue.
# Expected Result: Test 1 (Pri: 5) 
#                  Removed value: Test 2
print("\nTest 2")
value = pq.dequeue()
print("Queue: ", pq)
print("Removed value: ", value)
# Defect(s) Found: There was no method to remove the element from self.queue[high_pri_index] after it was identified for removal. 

print("=================")

# Add more Test Cases As Needed Below
# Test 3
# Scenario: Two elements with the same priority are enqueued, and then one element is dequeued from the priority queue
# Expected Result: 
#                  Queue Before delete:  [Test 1 (Pri:5), Test 3 (Pri:5), Test 4 (Pri:7), Test 5 (Pri:10), Test 6 (Pri:10), ]
#                  Queue After delete:  [Test 1 (Pri:5), Test 3 (Pri:5), Test 4 (Pri:7), Test 6 (Pri:10), ]
#                  Removed value:  Test 5

print("\nTest 3")
pq.enqueue("Test 3", 5)
pq.enqueue("Test 4", 7)
pq.enqueue("Test 5", 10)
pq.enqueue("Test 6", 10)
print("Queue Before delete: ", pq)
value = pq.dequeue()
print("Queue After delete: ", pq)
print("Removed value: ", value)
# Defect(s) Found: When multiple elements had the same priority, the last element with the same priority was removed instead of the first one added.

print("=================")

#Test 4
#Scenario: Delete each node 
#Expected Result: Error message should be displayed
print("\nTest 4")
value = pq.dequeue()
value = pq.dequeue()
value = pq.dequeue()
value = pq.dequeue()
value = pq.dequeue()
print(value)
# Defect(s) Found: When attempting to print for an empty queue, it prints the error message and None
