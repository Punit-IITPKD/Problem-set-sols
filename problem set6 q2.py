class Node:

    def __init__(self,book_id,book_name,edition,height=0):
        self.book_id=book_id
        self.book_name=book_name
        self.edition=edition
        self.height=height
        self.left=None
        self.right=None
        self.parent=None

class Library_Management_system:

    def __init__(self,root=None):
        self.root=root

    def get_height(self,root):
        if root==None:
            return 0
        
        return root.height
    
    def get_balance(self,root):
        if root==None:
            return 0
        
        return self.get_height(root.left)-self.get_height(root.right)
    

    def right_rotate(self,root):
        y=root.left
        t2=y.right
        parent_node=root.parent

        y.right=root
        root.left=t2

        if t2:
            t2.parent=root

        root.parent=y
        y.parent=parent_node

        if parent_node:
            if parent_node.left==root:
                parent_node.left=y
            else:
                parent_node.right=y

        if parent_node==None:
            self.root=y

        return y
    
    def left_rotate(self,root):
        y=root.right
        parent_node=root.parent
        t2=y.left

        root.right=t2
        y.left=root

        if t2:
            t2.parent=y
        y.parent=parent_node
        root.parent=y

        if parent_node:
            if parent_node.left==root:
                parent_node.left=y
            else:
                parent_node.right=y
            
        if parent_node==None:
            self.root=y


    def insert(self,book_id,book_name,edition):

        new_node=Node(book_id,book_name,edition)

        if self.root==None:
            self.root=new_node
            return 
        
        temp=self.root
        while True:
            if book_id<temp.book_id:
                if temp.left:
                    temp=temp.left
                else:
                    temp.left=new_node
                    break
            
            else:
                if temp.right:
                    temp=temp.right
                else:
                    temp.right=new_node
                    break

        temp=new_node.parent

        while(temp!=None):

            temp.height=1+max(self.get_height(temp.left),self.get_height(temp.right))
            balance_factor=self.get_balance(temp)

            if balance_factor in [-1,0,1]:
                temp=temp.parent

            else:
                if balance_factor>1 and book_id<temp.left.book_id:
                    return self.right_rotate(temp)
                
                if balance_factor>1 and book_id>temp.left.book_id:
                    temp.left=self.left_rotate(temp.left)
                    return self.right_rotate(temp)
                
                if balance_factor<-1 and book_id>temp.right.book_id:
                    return self.left_rotate(temp)
                
                if balance_factor<-1 and book_id<temp.right.book_id:
                    temp.right=self.right_rotate(temp.right)
                    return self.left_rotate(temp)


    def search(self,book_id):
        temp=self.root

        while(temp!=None):
            if temp.book_id==book_id:
                return temp
            elif temp.book_id>book_id:
                temp=temp.left
            else:
                temp=temp.right
        
        return None
    
    def inorder(self,root):
        if root==None:
            return
        
        self.inorder(root.left)
        print(f"Book ID: {root.book_id}, Book Name: {root.book_name}, Edition: {root.edition}")
        self.inorder(root.right)

    def display(self):
        if self.root==None:
            return 
        
        print("Displaing all books..")
        self.inorder(self.root)

    def update(self,book_id,book_name=None,edition=None):
        node=self.search(book_id)

        if node==None:
            return False
        
        if node:
            if book_name!=None:
                node.book_name=book_name
            if edition!=None:
                node.edition=edition
        
        return True
    
    def delete(self,root,book_id):
        if root==None:
            return
        
        if book_id<root.book_id:
            root.left=self.delete(root.left,book_id)
        
        elif book_id>root.book_id:
            root.right=self.delete(root.right,book_id)
        
        else:
            
            if root.left==None:
                return root.right
            
            if root.right==None:
                return root.left
            
            else:
                temp=root.right
                while(temp.left!=None):
                    temp=temp.left

                temp.book_id,root.book_id=root.book_id,temp.book_id
                temp.book_name,root.book_name=root.book_name,temp.book_name
                temp.edition,root.edition=root.edition,temp.edition

                root.right=self.delete(root.right,root.book_id)
            
            
            root.height=1+max(self.get_height(root.left),self.get_height(root.right))
            balance_factor=(self.get_balance(root))

            if balance_factor>1 and self.get_balance(root.left)>=0:
                return self.right_rotate(root)
            
            if balance_factor>1 and self.get_balance(root.left)<0:
                root.left=self.left_rotate(root.left)
                return self.right_rotate(root)
            
            if balance_factor<-1 and self.get_balance(root.right)<=0:
                return self.left_rotate(root)
            
            if balance_factor<-1 and self.get_balance(root.right)>0:
                root.right=self.right_rotate(root.right)
                return self.left_rotate(root)

        return root



def run_library_tests():
    # Initialize library
    library = Library_Management_system()

    print("===== Test Case 1: Insert books =====")
    library.insert(10, "Physics", 1)
    library.insert(20, "Maths", 2)
    library.insert(5, "Chemistry", 1)
    library.insert(15, "Biology", 1)
    library.insert(25, "CS", 1)

    print("In-order traversal after insertions:")
    library.display()
    print("\n")

    print("===== Test Case 2: Insert causing rotations =====")
    library.insert(30, "Engg", 1)
    library.insert(40, "History", 1)
    library.insert(35, "Art", 1)
    library.display()
    print("\n")

    print("===== Test Case 3: Search books =====")
    print("Search for BID 15:")
    result = library.search(15)
    if result:
        print(f"Book ID: {result.book_id}, Name: {result.book_name}, Edition: {result.edition}")
    else:
        print("Book not found.")

    print("Search for BID 100 (non-existent):")
    result = library.search(100)
    if result:
        print(f"Book ID: {result.book_id}, Name: {result.book_name}, Edition: {result.edition}")
    else:
        print("Book not found.")
    print("\n")

    print("===== Test Case 4: Update book details =====")
    print("Update BID 20 → Advanced Maths, Edition 3")
    updated = library.update(20, book_name="Advanced Maths", edition=3)
    if updated:
        library.display()
    else:
        print("Book not found for update.")

    print("Update BID 50 → Unknown (non-existent)")
    updated = library.update(50, book_name="Unknown")
    if not updated:
        print("Book not found for update.")
    print("\n")

    print("===== Test Case 5: Delete books =====")
    print("Delete BID 5 (leaf node)")
    library.root = library.delete(library.root, 5)
    print("Delete BID 30 (node with one child)")
    library.root = library.delete(library.root, 30)
    print("Delete BID 20 (node with two children)")
    library.root = library.delete(library.root, 20)
    print("In-order traversal after deletions:")
    library.display()
    print("\n")


# Run all test cases
run_library_tests()
