class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None

    def insert(self, newNode):
        #If head is none, the node we add will become head
        if self.head is None:
            self.head=newNode
        else:
        #Else we will traverse the node and whenever the node becomes none we will insert the node
            lastNode = self.head
            while True:
                if lastNode.next is None:
                    break
                lastNode= lastNode.next
            lastNode.next = newNode

    def printlist(self):
        current_node = self.head
        while True:
            if current_node is None:
                break
            print(current_node.data)
            current_node = current_node.next



firstNode = Node('John')
linkedList = LinkedList()
linkedList.insert(firstNode)
secondNode = Node('megha')
linkedList.insert(secondNode)
thirdNode = Node('neha')
linkedList.insert(thirdNode)
linkedList.printlist()
