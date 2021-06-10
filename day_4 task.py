#!/usr/bin/env python
# coding: utf-8

# In[5]:


#CLASS AND OBJECT IN PYTHON
#Almost everything in Python is an object, with its properties and methods.
#A Class is like an object constructor, or a "blueprint" for creating objects.

#To create a class, use the keyword class:   
#To create object we can use the class named MyClass to create objects:
 
class MyClass:
  x = 5

p1 = MyClass()
print(p1.x)


# In[7]:


class Person:
  def __init__(self, name, age):
    self.name = name
    self.age = age

p1 = Person("Aman", 22)

print(p1.name)
print(p1.age)


# In[8]:


class Person:
  def __init__(self, name, age):
    self.name = name
    self.age = age

  def myfunc(self):
    print("Hello my name is " + self.name)

p1 = Person("Aman", 36)
p1.myfunc()


# In[9]:


class Dog:
    attr1 = "mammal"
    attr2 = "dog"
 
    # A sample method 
    def fun(self):
        print("I'm a", self.attr1)
        print("I'm a", self.attr2)

Rodger = Dog()

print(Rodger.attr1)
Rodger.fun()


# In[14]:


# Class for Dog
class Dog:
    
    animal = 'dog'            
   
    def __init__(self, breed, color):
        
        self.breed = breed
        self.color = color       
    
# Objects of Dog class
Rodger = Dog("Pug", "brown")
Pearl = Dog("Bulldog", "black")
 
print('Rodger details:')  
print('Rodger is a', Rodger.animal)
print('Breed: ', Rodger.breed)
print('Color: ', Rodger.color)
 
print('\nPearl details:')  
print('Pearl is a', Pearl.animal)
print('Breed: ', Pearl.breed)
print('Color: ', Pearl.color)
 


# In[15]:


#closure in python
#A Closure is a function object that remembers values in enclosing scopes even if they are not present in memory. 


# In[18]:


# Python program to illustrate
# closures
def outerFunction(text):
    text = text
 
    def innerFunction():
        print(text)
 
    # Note we are returning function
    # WITHOUT parenthesis
    return innerFunction 
 
if __name__ == '__main__':
    myFunction = outerFunction('Hey! I am from internity' )
    myFunction()


# In[22]:


def make_multiplier_of(n):
    def multiplier(x):
        return x * n
    return multiplier

times3 = make_multiplier_of(3)

times5 = make_multiplier_of(5)

print(times3(9))

print(times5(3))

print(times5(times3(2)))


# In[23]:


#DECORETORS IN PYTHON
#A decorator is a function that takes a function as its only parameter and returns a function. 
#This is helpful to “wrap” functionality with the same code over and over again.
#Treating the functions as objects.
def say(text): 
    return text.upper() 
  
print(say('Hello')) 
  
yell = say 
  
print(yell('Hello')) 


# In[28]:


#Passing the function as argument
def shout(text): 
    return text.upper() 
  
def whisper(text): 
    return text.lower() 
  
def greet(func): 
    
    greeting = func("""Hi, I am from internity.""") 
    print (greeting) 
  
greet(shout) 
greet(whisper) 
  


# In[29]:


#Returning functions from another functions.
def create_adder(x): 
    def adder(y): 
        return x+y 
  
    return adder 
  
add_15 = create_adder(15) 
  
print(add_15(10))


# In[30]:


#DESCRIPTORS
#Python descriptors are created to manage the attributes of different classes which use the object as reference. 
#In descriptors we used three different methods that are __getters__(), __setters__(), and __delete__(). 
#If any of those methods are defined for an object, it can be termed as a descriptor. 
#1.# how to invoke descriptor
  
def __getattribute__(self, key):
    v = object.__getattribute__(self, key)
    if hasattr(v, '__get__'):
        return v.__get__(None, self)
    return v


# In[35]:


class Descriptor(object):
  
    def __init__(self, name =''):
        self.name = name
  
    def __get__(self, obj, objtype):
        return "{}for{}".format(self.name, self.name)
  
    def __set__(self, obj, name):
        if isinstance(name, str):
            self.name = name
        else:
            raise TypeError("Name should be string")
          
class ABC(object):
    name = Descriptor()
    
g = ABC()
g.name = "SUN"
print(g.name)


# In[36]:


#PROPERTIES
#Python property() function
#The main purpose of Property() function is to create property of a class.


# In[37]:


#Syntax: property(fget, fset, fdel, doc)

#Parameters:
#fget() – used to get the value of attribute
#fset() – used to set the value of attribute
#fdel() – used to delete the attribute value
#doc() – string that contains the documentation (docstring) for the attribute

#Return: Returns a property attribute from the given getter, setter and deleter


# In[38]:


class Alphabet:
    def __init__(self, value):
        self._value = value
          
    # getting the values
    def getValue(self):
        print('Getting value')
        return self._value
          
    # setting the values
    def setValue(self, value):
        print('Setting value to ' + value)
        self._value = value
          
    # deleting the values
    def delValue(self):
        print('Deleting value')
        del self._value
      
    value = property(getValue, setValue, delValue, )
  
# passing the value
x = Alphabet('SunforSun')
print(x.value)
  
x.value = 'ABC'
  
del x.value


# In[ ]:




