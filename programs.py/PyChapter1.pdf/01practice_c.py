'''This program is used to print all the files in the respective folder
since os module is present in python it doesn't show any error,but if i enter
any other word instead of os it shows"module not found"error'''
#feel free to try(u can replace any other word instead of os)
import os
'''below statement is used to print names of all the files in this
particular folder(the folder where the terminal is running),
 you can uncomment it! '''
print(os.listdir())