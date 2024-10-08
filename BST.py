#Binary Tree
#every node has at most 2 child nodes
#Binary Search Tree
#similar to binary tree but each element has some sort of order

class BinarySearchTreeNode:
    def __init__(self, data=None):
        self.data = data
        self.left = None
        self.right = None
        
    def add_child(self, data):
        if data == self.data:
            return
        
        if data < self.data:
            #add data in left subtree
            if self.left:
                self.left.add_child(data)
            else:
                self.left = BinarySearchTreeNode(data)
        else:
            #add data in right subtree
            if self.right:
                self.right.add_child(data)
            else:
                self.right = BinarySearchTreeNode(data)
    
    def in_order_traveral(self):
        elements = []
        
        #visit left tree
        if self.left:
            elements += self.left.in_order_traveral() #element[1]
            
            #[] = [] + self.left.left.data == 1
            # [] = [] + [1]
            # [1]
            
            #print(elements, "left")
                
        #visit base node
        elements.append(self.data)
        #print(elements, "base")
        #visit right tree
        if self.right:
            elements += self.right.in_order_traveral()
            #print(elements, "right")
        return elements
    #root=5
   #a=4    b
 #c=2   d
 
#BST = BinarySearchTreeNode(5)
#BST.add_child(4)
#BST.add_child(2)

#print(BST.data)
#print(BST.left.data)
#print(BST.left.left.data)

    def search(self, val):
        if self.data == val:
            return True

        if val < self.data:
            #val might be in left subtree
            if self.left:
                return self.left.search(val)
            else:
                return False
            
        if val > self.data: 
            #val might be in right subtree
            if self.right:
                return self.right.search(val)
            else:
                return False
    
    def find_max(self):
        if self.right is None:
            return self.data
         
        return self.right.find_max()
        
    def find_min(self):
        if self.left is None:
            return self.data
            
        return self.left.find_min()
        
    def delete(self, val):
        if val < self.data:
            if self.left:
                self.left = self.left.delete(val)
            else:
                return None
                
        elif val > self.data:
            if self.right:
                self.right = self.right.delete(val)
            else:
                return None
                
        else:
            if self.left is None and self.right is None:
                return None
            
            if self.left is None:
                return self.right
                
            if self.right is None:
                return self.right
                
            min_val = self.right.find_min()
            self.data = min_val
            self.right = self.right.delete(min_val)
        
        return self

def build_tree(elements):
    root = BinarySearchTreeNode(elements[0])
    
    for i in range(1,len(elements)):
        root.add_child(elements[i])
    
    return root

if __name__ == "__main__":
    numbers = [17,4,1,20,9,23,18,34]
    #BST = BinarySearchTreeNode(numbers[0])
    #numbers.pop(0)
    #for data in numbers:
        #BST.add_child(data)
    numbers_tree = build_tree(numbers)
    print(numbers_tree.in_order_traveral())
    #elem = [2]
    #elem2 = [1,2]
    #elem += elem2
    #print(elem)
    print(numbers_tree.search(4))
    print("After deleting 20 ", numbers_tree.delete(20).in_order_traveral())
    print("After deleting 20 ", numbers_tree.delete(9).in_order_traveral())
    #testing random stuff
    #https://stackoverflow.com/questions/4806911/how-are-strings-compared
    #print("a" is "b")
    #print("a" > "b")
    #alphabet = ['g','e','f','a','b','c','d']
    #ord_alphabet = []
    #for char in alphabet:
    #    ord_alphabet.append(ord(char))
    #print(ord_alphabet)
    #print(alphabet.sort())
    #print(alphabet)
    #ord_alphabet = []
    #for char in alphabet:
    #    ord_alphabet.append(ord(char))
    #print(ord_alphabet)
    #print(97//len(alphabet))