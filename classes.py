# class Phone:
#     def __init__(self, Name , Battery , Price , Ram): # constructor
#         self.Name = Name
#         self.Battery = Battery
#         self.Price = Price
#         self.Ram = Ram
#     def MobileData(self):   # creating a function
#         print("Mobile Name:" , self.Name) 
#         print("Battery :", self.Battery)
#         print("Price :", self.Price)       #  
#         print("Ram :", self.Ram)
#         print("---------------------")
        
# for resofMobile in range(4):    

#     resofMobile = Phone("Iphone" , "3600MAH" , "60,000","6gb Ram")
#     resofMobile.MobileData()  

# resofMobile = Phone("Vivo" , "3600MAH" , "30,000","12gb Ram")
# resofMobile.MobileData()    
        
#   ----------------------------------      
        
# class Harsha:
#     def __init__(self):
#         print("This is constructor method , it is called when we create object for class")
#     def normalMethod(self):
#         print("This is normel method , it cannot call Automatically")
        
# res = Harsha()   # creating object for Harsha Class
# res.normalMethod()  # printing method using object


# SINGLE INHERITANCE : One child class access propertics from one parent class

# class Parent:
#     def father(self):
#         print("This is a parent class")
        
# class Child(Parent):
#         def harsha(self):
#             print("This is a child class")      

# res = Child()
# res.harsha() 
# res.father() 

# MULTILEVEL INHERITANCE : grandfather-> father -> child 

# class grandfather:
#     def fun1(self):
#         print("This is grandfather class")   

# class father(grandfather):
#     def fun2(self):
#         print("This is father class")
        
# class child(father):
#     def fun3(self):
#         print("This is child class")               
        
# res = child()
# res.fun1()      
# res.fun2()      
# res.fun3() 

# HIERARCHIAL INHERITANCE : one parent class accessed by multiple child classes

# class Parent:
#     def fun1(self):
#         print("This is parent class")

# class child1:
#     def fun2(self):
#         print("This is child-1 class")
# class child2:
#     def fun3(self):
#         print("This is child-2 class")

# res1 = child1()
# res2 = child2()
# res2.fun3()
# res1.fun2()
#res2 = child2()

# MULTIPLE INHERITANCE : One Child access properties from multiple parent classes father , mother

# class Father:
#     def fun1(self):
#         print("This is father class")

# class Mother:
#     def fun2(self):
#         print("This is mother class")

# class Child(Father , Mother):
#     def fun3(self):
#         print("This is Child class")

# res = Child()
# res.fun1()
# res.fun2()
# res.fun3()


# SUPER KEYWORD : USED TO ACCESS PROPERTIES FROM PARENTS CLS TO CHILD CLS

# class Dad:
#     def __init__(self):
#         print("This is parent class")
        
#     def fun1(self):
#         print("iam from parent inside function")    
# class Child(Dad):
#     def __init__(self):
#         print("This is child class")
#         super().__init__() 
#     def fun2(self):
#         print("Iam from Child fun 2")    
# res = Child()

# POLYMORPHISM

# Method Overriding Example

# class Payment:
#     def pay(self):
#         print("This is Payment class")

# class phonePe(Payment):
#     def pay(self):
#         print("Payment done through Phonepe")
# class googlePay(Payment):
#     def pay(self):
#         print("Payment done through googlepay")
     
# res = [phonePe() , googlePay()]
# for i in res:
    # i.pay()   
          