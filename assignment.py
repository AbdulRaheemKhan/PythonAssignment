
# coding: utf-8

# # ASSIGNMENT 

# <h3> 1 : Declare and initialize a variable name total_marks with a value 500</h3>
# 

# In[4]:


total_marks = 500


# <h3> 2 : Declare and initialize 5 variables name maths , english , urdu , physics and chemisrty with different integer values</h3>

# In[3]:


maths = 100
english = 100
urdu = 75
physics = 100
chemistry = 70


# <h3>3 : Calculate the obtained marks And assign the value In variable name obtained_marks</h3>

# In[7]:


obtained_marks = 445


# <h3>4 : Calculate percentage and assign the value in variable name percentage</h3>

# In[8]:


percentage = (445/500)*100
print(percentage)


# <h3>5 : Declare and initialize an empty variable name grade </h3>

# In[16]:


grade 
print(grade)


# <h3>6 : assign a vlue to grade by checking the following conditions:: </h3>
# <h3>if % is greater then and equal to 90 and less then 100 grade is A+ </h3>
# <h3>if % is greater then and equal to 80 and less then 90 grade is A </h3>
# <h3>if % is greater then and equal to 70 and less then 80 grade is B </h3>
# <h3>if % is greater then and equal to 60 and less then 70 grade is C </h3>
# <h3>if % is less than 60 grade is FAIL </h3>
# 

# In[30]:


if percentage>= 90 and percentage <100:
    grade = "A+"
if percentage>= 80 and percentage <90:
    grade = "A"
if percentage>= 70 and percentage <80:
    grade = "B"
if percentage>= 60 and percentage <70:
    grade = "C"
if percentage<60:
    grade = "FAIL"


# <h3>7 : Print grade percentage and obtained marks</h3>

# In[31]:


print(grade)
print(percentage)
print(obtained_marks)

