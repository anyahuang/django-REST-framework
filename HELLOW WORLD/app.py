#!/usr/bin/env python3
#Task 1
x = int("234")
print(x)
x = float("43.12")
print(x)
x = complex(3+2j)
print(x)
x = str("Hello")
print(x)
x = bool(True)
print(x)

#Task 2
print("123 ","<class 'int'>", sep= "is type of " )
print("43.23 ","<class 'float'>", sep= "is type of ")
print("(4-1j) ","<class 'complex'>",sep = "is type of ")
print("How are you? ","<class 'str' >", sep="is type of" )
print("True ","<class 'bool' >", sep="is type of ")

#Task 3
print(isinstance(123,int))
print(isinstance(43.23,float))
print(isinstance(4-1j,bool))
print(isinstance("How are you",complex))
print(isinstance(True,str))

#Task 4

print("Is ""123" ,"int ? " ": True",sep= " an instance of ")
print("Is 43.23 an instance of bool?: ",isinstance(43.23,bool))
print("Is (4-1j) an instance of complex?: ",isinstance((4-1j),complex))
print("Is True an instance of bool?: ",isinstance(True,bool))
print("Is 'How are you?' an instance of float?: ",isinstance("How are you?",float))

# Task 5
#I use comments on all the tasts, and it's better to use # not """