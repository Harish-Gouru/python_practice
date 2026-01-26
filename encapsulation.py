class Marks:
    
    def __init__(self ,name, marks):
        self.__name = name
        self.__marks = marks
        
    def getName(self):
        return self.__name
    def getMarks(self):
        return self.__marks 
    
    def setMarks(self,marks):
        if 0 <= marks <= 100:
            self.__marks = marks
        else:
            print("invalid Marks!!")       
     
    
m1 = Marks("Physics", 89)
print(m1.getName())   
print(m1.getMarks())
print(m1.setMarks(95))
print("Updated marks :", m1.setMarks(95))
    
    
    
    
    
    
    