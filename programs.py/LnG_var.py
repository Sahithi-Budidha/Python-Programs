#local var
'''def a():
    tag="internshala"
    print(tag)
    return
a()
print(tag)'''
#end

#Global var
'''age=7
def a():
    global age
    age=12
    print("age :",age)
    return
a()
print("the age outside the function :",age)'''
#end

#globals() keyword
'''alpha=1
beta=2
gamma=3

print(globals())'''
#end

#same var LnG var
age=7
def a():
    print("Global variable 'age' :",globals()['age'])

    #modifying the GLOBAL var INSIDE the fn.
    globals()['age']=27
    print("Global var 'age' after modifying INSIDE the fn :",globals()['age'])

    #creating a LOCAL variable, Inside the fn.
    age=19
    print("Local var 'age' :",age)
    return
a()
print("Checking GLOBAL var outsdie the fn:",age)
















