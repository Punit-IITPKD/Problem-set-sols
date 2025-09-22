class Node:

    def __init__(self,student_id,student_name,CGPA,degree_program,year,semster,subjects_enrolled,height=0):
        self.student_id=student_id
        self.student_name=student_name
        self.CGPA=CGPA
        self.degree_program=degree_program
        self.year=year
        self.semster=semster
        self.subjects_enrolled=subjects_enrolled
        self.height=height
        self.left=None
        self.right=None
        self.parent=None


class Student_management_system:

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
    
    def total_count(self,root):
        if root==None:
            return 0
        
        left_count=self.total_count(root.left)
        right_count=self.total_count(root.right)
        return 1+left_count+right_count
    
    def total_count_by_degree(self,root,degree_program):
        if root==None:
            return 0
            
        left_count=self.total_count_by_degree(root.left,degree_program)
        right_count=self.total_count_by_degree(root.right,degree_program)
    
        if root.degree_program==degree_program:
            return 1+left_count+right_count
        else:
            return left_count+right_count


    def total_count_by_subjects(self,root,subject):
        if root==None:
            return 0
        
        left_count=self.total_count_by_subjects(root.left,subject)
        right_count=self.total_count_by_subjects(root.right,subject)

        if subject in root.subjects_enrolled:
            return 1+left_count+right_count
        else:
            return left_count+right_count
        
    def top_k_students(self,k):

        students=[]

        def traverse(root):
            if root==None:
                return
            
            traverse(root.left)
            students.append(root)
            traverse(root.right)
        
        traverse(self.root)

        students.sort(key=lambda x: x.CGPA,reverse=True)

        print(f"Top {k} students by CGPA:")
        for student in students[:k]:
            print(f"SID: {student.student_id}, Name: {student.student_name}, CGPA: {student.CGPA}, Subjects: {student.subjects_enrolled}")


    def top_k_students_by_degree(self,k,degree):
        students=[]

        def traverse(root):
            if root==None:
                return
            
            traverse(root.left)
            if root.degree_program==degree:
                students.append(root)
            traverse(root.right)

        traverse(self.root)

        students.sort(key=lambda x:x.CGPA,reverse=True)

        print(f"Top {k} students by CGPA in {degree}:")
        for i in students[:k]:
            print(f"SID: {i.student_id}, Name: {i.student_name}, CGPA: {i.CGPA}, Subjects: {i.subjects_enrolled}")


    def left_rotate(self,root):
        parent_node=root.parent
        y=root.right
        t2=y.left

        y.left=root
        root.right=t2

        if t2:
            t2.parent=root
        y.parent=parent_node
        root.parent=y

        if parent_node:
            if parent_node.right==root:
                parent_node.right=y
            else:
                parent_node.left=y
        
        if parent_node==None:
            self.root=y

        root.height=1+max(self.get_height(root.left),self.get_height(root.right))
        y.height=1+max(self.get_height(y.left),self.get_height(y.right))

        return y
    

    def right_rotate(self,root):
        y=root.left
        t2=y.right
        parent_node=root.parent

        root.left=t2
        y.right=root

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

        root.height=1+max(self.get_height(root.left),self.get_height(root.right))
        y.height=1+max(self.get_height(y.left),self.get_height(y.right))

        return y


    def insert(self,student_id,student_name,CGPA,degree_program,year,semster,subjects_enrolled):

        if self.root==None:
            new_node=Node(student_id,student_name,CGPA,degree_program,year,semster,subjects_enrolled)
            self.root=new_node
            return self.root
        
        temp=self.root
        while True:
            if student_id<temp.student_id:
                if temp.left:
                    temp=temp.left
                else:
                    new_node=Node(student_id,student_name,CGPA,degree_program,year,semster,subjects_enrolled)
                    temp.left=new_node
                    new_node.parent=temp
                    break
            
            else:
                if temp.right:
                    temp=temp.right
                else:
                    new_node=Node(student_id,student_name,CGPA,degree_program,year,semster,subjects_enrolled)
                    temp.right=new_node
                    new_node.parent=temp
                    break
        
        temp=new_node.parent

        while(temp!=None):

            temp.height=1+max(self.get_height(temp.left),self.get_height(temp.right))

            balance_factor=self.get_balance(temp)

            if balance_factor in [-1,0,1]:
                temp=temp.parent

            else:
                if balance_factor>1 and student_id<temp.left.student_id:
                    return self.right_rotate(temp)
                
                if balance_factor>1 and student_id>temp.left.student_id:
                    temp.left=self.left_rotate(temp.left)
                    return self.right_rotate(temp)
                
                if balance_factor<-1 and student_id>temp.right.student_id:
                    return self.left_rotate(temp)
                
                if balance_factor<-1 and student_id<temp.right.student_id:
                    temp.right=self.right_rotate(temp.right)
                    return self.left_rotate(temp)

    
    def search(self,student_id):

        temp=self.root
        while(temp!=None):

            if student_id==temp.student_id:
                return temp
            elif student_id<temp.student_id:
                temp=temp.left
            else:
                temp=temp.right
        
        return None
    

    def inorder(self,root):
        if root==None:
            return
        
        self.inorder(root.left)
        print(f"student name: {root.student_name}, student id: {root.student_id},cgpa: {root.CGPA}, degree program; {root.degree_program}, year: {root.year}, semester: {root.semster}, subjects enrolled: {root.subjects_enrolled}")
        self.inorder(root.right)


    def display(self):
        self.inorder(self.root)


    def update_student_details(self, student_id, cgpa=None, year=None, semester=None, subjects=None):
        node = self.search(student_id)
        if not node:
            return False  # student not found

        # Update only the fields provided
        if cgpa is not None:
            node.CGPA = cgpa
        if year is not None:
            node.year = year
        if semester is not None:
            node.semster = semester 
        if subjects is not None:
            node.subjects_enrolled = subjects

        return True  



    def delete(self,root,student_id):
        if root==None:
            return None

        if root.student_id>student_id:
            root.left=self.delete(root.left,student_id)
        
        elif root.student_id<student_id:
            root.right=self.delete(root.right,student_id)

        else:
            
            if root.left==None and root.right==None:
                return None

            elif root.left==None:
                return root.right
            
            elif root.right==None:
                return root.left
            else:
                temp=root.right
                while(temp.left!=None):
                    temp=temp.left

                root.student_id = temp.student_id
                root.student_name = temp.student_name
                root.CGPA = temp.CGPA
                root.degree_program = temp.degree_program
                root.year = temp.year
                root.semster = temp.semster
                root.subjects_enrolled = temp.subjects_enrolled

                root.right=self.delete(root.right,temp.student_id)
        
        root.height=1+max(self.get_height(root.left),self.get_height(root.right))

        balance_factor=self.get_balance(root)

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





# =============================
# Test Script for Student Management System
# =============================

# Assuming your Student_management_system class is already defined and imported

tree = Student_management_system()

# -----------------------------
# 1️⃣ Insert students
# -----------------------------
tree.insert(102, "Bob", 8.5, "B.Tech ME", 1, 2, ["Thermo", "Maths"])
tree.insert(101, "Alice", 9.1, "B.Tech CSE", 2, 4, ["DSA", "DBMS"])
tree.insert(103, "Charlie", 7.9, "B.Tech EE", 3, 6, ["Circuits", "Signals"])
tree.insert(104, "David", 9.3, "B.Tech CSE", 2, 4, ["AI", "ML"])
tree.insert(100, "Eve", 8.8, "B.Tech ME", 1, 2, ["Mechanics", "Maths"])

print("\n--- Students inserted ---")
tree.display()

# -----------------------------
# 2️⃣ Search students
# -----------------------------
print("\n--- Search Students ---")
s = tree.search(101)
print("Search SID 101:", s.student_name if s else "Not found")  # Alice
s = tree.search(200)
print("Search SID 200:", s.student_name if s else "Not found")  # Not found

# -----------------------------
# 3️⃣ Update student details
# -----------------------------
print("\n--- Update Student 102 ---")
tree.update_student_details(102, cgpa=9.0, year=2, semester=4, subjects=["Thermo", "Maths", "Robotics"])
s = tree.search(102)
print(s.student_name, s.CGPA, s.year, s.semster, s.subjects_enrolled)
# Expected: Bob 9.0 2 4 ['Thermo', 'Maths', 'Robotics']

# -----------------------------
# 4️⃣ Delete students
# -----------------------------
print("\n--- Delete Students ---")
# Delete leaf node
tree.delete(tree.root, 103)
# Delete node with one child
tree.delete(tree.root, 100)

print("\n--- Students after deletions ---")
tree.display()

# -----------------------------
# 5️⃣ Top k students by CGPA
# -----------------------------
print("\n--- Top 2 Students by CGPA (Sort) ---")
tree.top_k_students(2)

# -----------------------------
# 6️⃣ Top k students by Degree Program
# -----------------------------
print("\n--- Top Students in B.Tech CSE ---")
tree.top_k_students_by_degree(2,"B.Tech CSE")

# -----------------------------
# 7️⃣ Count total students
# -----------------------------
print("\nTotal students in system:", tree.total_count(tree.root))

# -----------------------------
# 8️⃣ Count by degree
# -----------------------------
print("Total students in B.Tech CSE:", tree.total_count_by_degree(tree.root,"B.Tech CSE"))
print("Total students in B.Tech ME:", tree.total_count_by_degree(tree.root,"B.Tech ME"))

# -----------------------------
# 9️⃣ Count by subject
# -----------------------------
print("Students enrolled in DSA:", tree.total_count_by_subjects(tree.root,"DSA"))
print("Students enrolled in ML:", tree.total_count_by_subjects(tree.root,"ML"))
print("Students enrolled in Maths:", tree.total_count_by_subjects(tree.root,"Maths"))
