#!/usr/bin/env python
# coding: utf-8

# # PYTHON  - EDA

# In[1]:


import pandas as pd
import numpy as np


# In[2]:


import matplotlib.pyplot as plt
import seaborn as sns
sns.set()


# In[3]:


data=pd.read_csv("C:/Users/anees/OneDrive/Desktop/ENTRI DSML/data set/myexcel - myexcel.csv.csv")
data


# In[4]:


data.isnull().sum()


# In[5]:


x = data['Salary'].mean()
data['Salary'].fillna(x,inplace = True)
data


# In[6]:


data.drop_duplicates(inplace = True)
data


# In[7]:


data.dropna ( inplace = True)


# In[8]:


data.isnull().sum()


# In[9]:


data['Height'] = np.random.uniform(150,180,size = len(data))


# In[10]:


data


# # How Many Are There In Each Team and Precentage splitting with respect to the total employees.

# In[11]:


data['Team'].value_counts()


# # Precentage splitting with respect to the total employees:

# In[12]:


data['Team'].value_counts()/len(data)*100


# # Segregate employees based on their positions within the company. 
# 

# In[13]:


employees = data.groupby('Position')['Name'].apply(list)
for Position, Names in employees.items():
    print(f"employees in {Position} position:")
    for name in Names:
     print(name)
    print("\n")
    


# # Find from which age group most of the employees belong to.

# In[14]:


data['Age Group'] = data['Age'].apply(lambda age:'20-25' if 20 <= age <= 25 else ('26-30' if 26 <= age <= 30 else ('31-35' if 31 <= age <= 35 else '36 and above')))

data


# In[15]:


data['Age Group'].value_counts()


# # Find out under which team and position, spending in terms of salary is high.

# In[16]:


spending_salary = data.groupby(['Team','Position'])['Salary'].sum()
spending_salary.idxmax()


# # Find if there is any correlation between age and salary , represent it visually.
# 

# In[17]:


correlation = data['Salary'].corr(data['Age'])


# In[18]:


print("THE CORRELATION BETWEEN Salary AND Age IS:",correlation)


# In[19]:


sns.scatterplot(x="Age" ,y= "Salary",data= data)
plt.ylabel("Salary")
plt.xlabel("Age")
plt.title("correlation b/w Salary and Age")
plt.show()


# In[ ]:





# ## Data Insights
# 
# 1. **Distribution of Employees Across Each Team:**
#    - The team with the highest number of employees is [Team Name] which comprises [Percentage]% of the total workforce.
# 
# 2. **Segregation of Employees Based on Their Positions:**
#    - The most common position within the company is [Position], accounting for [Number] employees.
# 
# 3. **Predominant Age Group Among Employees:**
#    - The predominant age group is [Age Group], making up [Percentage]% of the workforce.
# 
# 4. **Team and Position with the Highest Salary Expenditure:**
#    - The team with the highest salary expenditure is [Team Name] with a total expenditure of [Amount].
#    - The position with the highest salary expenditure is [Position] with a total expenditure of [Amount].
# 
# 5. **Correlation Between Age and Salary:**
#    - The correlation between age and salary is [Correlation Value], indicating [nature of correlation (e.g., weak, strong, positive, negative)] relationship between age and salary.
# 

# In[ ]:




