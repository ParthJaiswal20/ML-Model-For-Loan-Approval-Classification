class Employee:
    startTime = "10am"
    endTIme = "6pm"

class Teachers(Employee):  # THIS IS HOW U DO INHERITANCE
    def __init__(self,subject):
        self.subject = subject

# MAKINF OF THE OBJECT  
t1 = Teachers("PYTHON")

# PRINTING FROM THE TEACHERS CLASS
print(t1.subject)
# PRINTING FROM THE TEACHER CLASS INHERITED PROPERTY FROM THE PARENT CLASS
print(t1.subject, t1.startTime , t1.endTIme)