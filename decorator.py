#decarators => A decorator is same as function but in decarator the parameters as well as return value is function
#usecase => Write a function to add two number which passes as a arguments
def add_decor(func):
    def add_new(num1,num2):
        if(type(num1)==type(num2)):
            return func(num1,num2)
        else:
            return func(str(num1),str(num2))
    return add_new
@add_decor #my decorator
def add(num1,num2):
    return num1+num2
print(add('Python',3))  #to avoid error lie value error such that we are using decarator to add more functionality


#given student marks declare whether student is pass or fail average>40 and each subject >5
""" def find_pf(func):
    def check(m):
        ans=[ele for ele in m if ele>35]
        if(len(ans)==len(m)):
            avg_marks=sum(m)/len(m)
            return "Pass with percentage::",avg_marks
        else:
            return "fail"
    return check
@find_pf
def pass_fail(marks):
    return 
print(pass_fail([60,50,70,70,80])) """


print("Modified decorator file in remote resporatory")
