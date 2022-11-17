#!/usr/bin/env python
# coding: utf-8

# In[1]:


# 1. Write a Python program to convert kilometers to miles?

km = float(input("Enter the value: "))

miles = 0.621371
print('%0.3f km is equal to %0.3f miles' %(km,miles))


# In[5]:


# 2. Write a Python program to convert Celsius to Fahrenheit?

celsius = float(input("Enter the value in degree: "))
fahrenheit = (celsius * 1.8) + 32
print('%0.2f degree celcius is equal to %0.2f degree fahrenheit' %(celsius,fahrenheit))


# In[8]:


# 3. Write a Python program to display calendar?

import calendar
 
year = int(input("Enter the year: "))
month = int(input("Enter the month: "))

# display the calendar for a single year

print(calendar.calendar(year))

# display the calendar for a single month
print(calendar.month(year,month))


# In[5]:


# 4. Write a Python program to solve quadratic equation?

import cmath
a = float(input("Enter the value a: ")) 
b = float(input("Enter the value b: "))  
c = float(input("Enter the value c: "))  

disc = (b**2 - 4 *a*c)

x1 = (-b + cmath.sqrt(disc))/(2*a)
x2 = (-b - cmath.sqrt(disc))/(2*a)

if a==0:
    print("not a quadratic equation")

else:
    
    if disc<0:
        print("roots are imaginary and not real")
        print("solutions are {} and {}".format(x1,x2))

    elif disc==0:
        print("roots are real and equal")
        print("solutions are {} and {}".format(x1,x2))

    else:
        print("roots are real and distinct")
        print("solutions are {} and {}".format(x1,x2))
    
    


# In[6]:


# 5. Write a Python program to swap two variables without temp variable?

a = input("enter first variable: ")
b = input("enter second variable: ")

print("value before swapping: a: {} and b: {}".format(a,b))

a,b = b,a

print(("value after swapping: a: {} and b: {}".format(a,b)))


# In[ ]:




