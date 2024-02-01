#Contains Linked list class and hashtable class for openhashing

# class to represent a single node in the hashtable
# data represents the value stored in the node and next is the value that links to the next node
class Node:
    def __init__(self, data, next):
        self.data = data
        self.next = next
        

#LinkedList init has two pointers head and tail 
# tail points to the Lists last node and head to it's first
# len indicates the lenth or the number of nodes in the list
class LinkedList:
    def __init__(self):
        self.tail = Node(None, None)
        self.head = Node(None, self.tail)
        self.len = 0
    
    


    # takes in one variable data which will be appended to the end of the linked list
    def append(self, data):
        # if list contains no values then the head node is updated from none to the appended value
        # in this case the tail and head point to the same node
        if (self.len == 0):
            newNode = Node(data, self.tail)    # creating a node The newnode will temporarilly have a link to the tail which points to none
            self.head = newNode                # pointing the head to that node
            
        # in case that the list contains aleady nodes only the tail pointer is updated
        else:
            
            newNode = Node(data, self.tail.next)
            self.tail.next = newNode
        
        self.tail = newNode
        self.tail.next = None
        self.len +=1 # length of list is updated
        return None
    # prints the values appended to the linked list
    def print(self):
        current = self.head
        while (current != None):
            
            if(current.next != None):
                print(current.data, end=" -> ")
            else:
                print(current.data, end="")
            current = current.next
        print()
        return None
    #searches the linked list for given value    
    def index(self, value):
        # if list contains no or only one node then traversing the list is avoided and function returns -1 if not found
        if(self.len == 0):
            return -1
        elif(self.len ==1 and self.head.data != value):
            
           
            return -1
        #traversing list to find value if found returns index of value found if not -1
        current = self.head
        count = 0
        index = -1
        while(current != None):
            if(current.data == value):
                
                index = count
                break
            else:
                current = current.next
            count += 1
        
        return index
    
    #deletes a node at the given index of list and modifies the pointers
    def delete(self, index):
        current = self.head
        previous = None
        count = 0
        while (current != None):
            if(index == count):
                # when the node to be deleted is not the first node of the list
                if(previous != None):
                    previous.next = current.next
                    if(current.next == None):
                        self.tail = previous    # tail points to the previous node
                    self.len -= 1
                # when the node is the first
                else:
                    self.head = self.head.next
                    self.len -= 1
                    if self.len == 0:   # when the list contained only the deleted node
                        self.tail = None
            previous = current    
            current = current.next
            count += 1
        return None

    

# Hash has M and T in init
# M is the size of the hashtable
# T is the table itself
class Hash:
    def __init__(self, M):
        self.M = M              
        self.T = [LinkedList() for _ in range(self.M)]  # Intializing table of empty linked lists

    # Method returns a hash for a string value by using the string folding function
    # based on the openDSA course material    
    def foldin(self, x):
        sum = 0
        mul = 1
        for i in range(len(x)):
            if(i%4 == 0):
                mul = 1
            else:
                mul = mul * 256
            sum += ord(x[i])*mul
        return abs(sum)%self.M

    # hashes the the given value x  and sends it to the linkedlist which is it at the hashed values index in the table
    # Strings and integers are hashed differently
    def insert(self, x):
        if(isinstance(x, int) == True):   # checks whether value x to be inserted is integer
           value = x % self.M          # hashing a integer by getting the remainder of the integer and the tablesize
           if(self.T[value].index(x) == -1): # checking that no duplicates are inserted by using the linked lists index function
               self.T[value].append(x)       # # using LinkedList method append to insert the value to the end of the list at the hashed index of the table
           return
        # when value to be inserted is string
        value = self.foldin(x)
        if(self.T[value].index(x) == -1):  # checking that no duplicates are inserted by using the linked lists index function
            self.T[value].append(x)        # using LinkedList method append to insert the value to the end of the list at the hashed index of the table
         
        return
        
    
    
    # deletes given value from table    
    def delete(self, x):
        if(isinstance(x, int) == True):  # checks whether x is integer
            value = x % self.M           # value is hashed value of x
            index = self.T[value].index(x) # finds index of the value x in the table
            self.T[value].delete(index)    # using LinkedList method delete to remove x
            return
        
        # when x is string
        value = self.foldin(x)
        index = self.T[value].index(x)
        self.T[value].delete(index)

        
    # return True when value x found and False when not found in the hashtable
    def search(self, x):
        found = True
        value = 0
        # hashing 
        if(isinstance(x, int) == True):
            value = x % self.M 
        else:    
            value = self.foldin(x) 
        # using the LinkedList method index to locate x in the list at the hashed index of the table    
        p = self.T[value].index(x)  
        # not found
        if(p == -1):
            
            found = False
        return found
        #self.T[value].
    
    # prints linked lists of hashtable and the index of the linked list¨
    # doesn't print empty lists
    def print(self):
        print("content of hashtable and index of content:")
        for i in range(self.M):
            if(self.T[i].len != 0):
                print("At index:[{}]:".format(i), end=" ")
                self.T[i].print()
            
        print("")

if __name__ == "__main__":
    table = Hash(3)


    table.insert(12)
    table.insert( 'hashtable')
    table.insert( 1234) 
    table.insert(4328989)
    table.insert('BM40A1500')
    table.insert( -12456)
    table.insert( 'aaaabbbbcccc')
    
    table.print()
    print("searching whether table contains following values:")
    print(table.search(-12456))    # -12456, 'hashtable', 1235
    print(table.search('hashtable'))
    print(table.search(1235))
    table.delete('BM40A1500')
    table.delete(1234)
    table.delete( 'aaaabbbbcccc')
    print("after deletation:")
    table.print()