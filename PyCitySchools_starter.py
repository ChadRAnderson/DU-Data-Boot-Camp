#!/usr/bin/env python
# coding: utf-8

# # PyCity Schools Analysis
# 
# * As a whole, schools with higher budgets, did not yield better test results. By contrast, schools with higher spending per student actually (\$645-675) underperformed compared to schools with smaller budgets (<\$585 per student).
# 
# * As a whole, smaller and medium sized schools dramatically out-performed large sized schools on passing math performances (89-91% passing vs 67%).
# 
# * As a whole, charter schools out-performed the public district schools across all metrics. However, more analysis will be required to glean if the effect is due to school practices or the fact that charter schools tend to serve smaller student populations per school. 
# ---

# ### Note
# * Instructions have been included for each segment. You do not have to follow them exactly, but they are included to help you think through the steps.

# In[2]:


# Dependencies and Setup
import pandas as pd
import numpy as np

# File to Load (Remember to Change These)
school_data_to_load = "Resources/schools_complete.csv"
student_data_to_load = "Resources/students_complete.csv"

# Read School and Student Data File and store into Pandas Data Frames
school_data = pd.read_csv(school_data_to_load)
student_data = pd.read_csv(student_data_to_load)

# Combine the data into a single dataset
complete_df = pd.merge(student_data, school_data, how="left", on=["school_name", "school_name"])


# ## District Summary
# 
# * Calculate the total number of schools
# 
# * Calculate the total number of students
# 
# * Calculate the total budget
# 
# * Calculate the average math score 
# 
# * Calculate the average reading score
# 
# * Calculate the overall passing rate (overall average score), i.e. (avg. math score + avg. reading score)/2
# 
# * Calculate the percentage of students with a passing math score (70 or greater)
# 
# * Calculate the percentage of students with a passing reading score (70 or greater)
# 
# * Create a dataframe to hold the above results
# 
# * Optional: give the displayed data cleaner formatting

# In[48]:


# complete_df.columns Index(['Student ID', 'student_name', 'gender', 'grade', 'school_name',
#        'reading_score', 'math_score', 'School ID', 'type', 'size', 'budget'],
#       dtype='object')

# complete_df.dtypes
# Student ID        int64
# student_name     object
# gender           object
# grade            object
# school_name      object
# reading_score     int64
# math_score        int64
# School ID         int64
# type             object
# size              int64
# budget            int64
# dtype: object

# Calculate the total number of schools
total_schools = complete_df['school_name'].nunique()
print(total_schools)

# Optional: give the displayed data cleaner formattingschool_data_complete.head()


# In[102]:


# Calculate the total number of students
complete_df = complete_df.rename(columns={"Student ID": "Student_ID"})
complete_df

total_students = complete_df["Student_ID"].nunique()
print(total_students)


# In[68]:


# # Calculate the total budget
# total_budget = complete_df['budget'].sum()
# print(total_budget)
# total_budget
# total_budget = complete_df.budget.sum()
# print(total_budget)
# budget_total = complete_df['budget'].sum()
# print(budget_total)

# budget_count = complete_df.groupby('budget').sum
# budget_count
totalBudget = school_data["budget"].sum()
totalBudget


# In[98]:


# Calculate the average math score
avg_math = complete_df['math_score'].mean()
avg_math # print(avg_math)


# In[30]:


# Calculate the average reading score
avg_reading = complete_df['reading_score'].mean()
print(avg_reading) 


# In[94]:


# Calculate the overall passing rate (overall average score), i.e. (avg. math score + avg. reading score)/2
combo_scores = avg_reading + avg_math
passing_rate = combo_scores / 2
print(passing_rate)
80.43160582078121
# df['Result'] = df['Column A']/df['Column B']  df.add(other_df, fill_value=0)
# passing_rate = (avg_math + avg_reading) / 2
# print(passing_rate)


# In[93]:


# Calculate the percentage of students with a passing math score (70 or greater)
passing_math = (((complete_df[(complete_df['math_score'] >= 70)].count()['Student_ID']) / total_students) * 100)
print(passing_math)
# percentReadingPass = (((student_data["reading_score"] > 70).sum()/student_data["reading_score"].count())*100)
# print(percentReadingPass)


# In[39]:


passing_reading = (((complete_df[(complete_df['reading_score'] >= 70)].count()['Student_ID']) / total_students) * 100) 
print(passing_reading)
# Calculate the percentage of students with a passing reading score (70 or greater)


# In[97]:


summary_df = pd.DataFrame({"Total Schools":[total_schools],
                               "Total Students":[total_students],
                               "Total Budget" : [totalBudget],
                               "Average Math Score":[avg_math],
                               "Average Reading Score":[avg_reading],
                               "% Passing Math":[passing_math],
                               "% Passing Reading": [passing_reading],
                               "% Overall Passing Rate":[passing_rate]})
summary_df


# ## School Summary

# In[ ]:





# In[65]:


# School Name
# Total Students
per_school_counts = complete_df['school_name'].value_counts()
per_school_counts


# In[56]:


# School Type
school_types = school_data.set_index(['school_name'])['type']
school_types


# In[57]:


# Total School Budget
per_school_budget = school_data.groupby(['school_name']).mean()['budget']
per_school_budget


# In[58]:


# Per Student Budget
per_capita_budget = per_school_budget / per_school_counts
per_capita_budget


# In[71]:


# Average Math Score
per_school_math = complete_df.groupby(['school_name']).mean()['math_score']
per_school_math


# * Create an overview table that summarizes key metrics about each school, including:
#   * School Name
#   * School Type
#   * Total Students
#   * Total School Budget
#   * Per Student Budget
#   * Average Math Score
#   * Average Reading Score
#   * % Passing Math
#   * % Passing Reading
#   * Overall Passing Rate (Average of the above two)
#   
# * Create a dataframe to hold the above results

# In[73]:


# Average reading Score
per_school_reading = complete_df.groupby(['school_name']).mean()['reading_score']
per_school_reading


# In[137]:


avg_math_sum = student_data.groupby(['school_name'])['math_score', 'reading_score'].mean().reset_index()
df_school_sum = school_data.merge(avg_math_sum, on='school_name', how="outer")
pass_math_sum=complete_df[(complete_df['reading_score'] >= 70)].groupby(["school_name"])['math_score'].count().reset_index()
pass_reading_sum=complete_df[(complete_df['math_score'] >= 70)].groupby(["school_name"])['reading_score'].count().reset_index()
pass_math_sum

df_school_sum = df_school_sum.merge(pass_math_sum, on='school_name', how="outer")
df_school_sum = df_school_sum.merge(pass_reading_sum, on='school_name', how="outer")

df_school_sum['% Passing Math']=df_school_sum['math_score_y']/df_school_sum['size']*100
df_school_sum['% Passing Reading']=df_school_sum['reading_score_y']/df_school_sum['size']*100
df_school_sum['% Overall Passing Rate']=((df_school_sum['reading_score_y']+df_school_sum['reading_score_y'])/2)/df_school_sum['size']*100# math_pass = student_data[student_data["math_score"]>70].groupby(["school_name"], as_index=False)

df_school_sum


# In[ ]:





# In[ ]:





# In[138]:





# ## Top Performing Schools (By Passing Rate)

# * Sort and display the top five schools in overall passing rate

# In[146]:


top_schools = df_school_sum.sort_values(['% Overall Passing Rate'], ascending=False)
top_schools.head()


# ## Bottom Performing Schools (By Passing Rate)

# * Sort and display the five worst-performing schools

# In[145]:


bottom_schools = df_school_sum.sort_values(['% Overall Passing Rate'], ascending=True)
bottom_schools.head()


# ## Math Scores by Grade

# * Create a table that lists the average Reading Score for students of each grade level (9th, 10th, 11th, 12th) at each school.
# 
#   * Create a pandas series for each grade. Hint: use a conditional statement.
#   
#   * Group each series by school
#   
#   * Combine the series into a dataframe
#   
#   * Optional: give the displayed data cleaner formatting

# In[153]:


ninth_grade = complete_df[(complete_df["grade"] == "9th")]
tenth_grade = complete_df[(complete_df["grade"] == "10th")]
eleventh_grade = complete_df[(complete_df["grade"] == "11th")]
twelfth_grade = complete_df[(complete_df["grade"] == "12th")]

ninth_graders_scores = ninth_grade.groupby(["school_name"]).mean()["math_score"]
tenth_graders_scores = tenth_grade.groupby(["school_name"]).mean()["math_score"]
eleventh_graders_scores = eleventh_grade.groupby(["school_name"]).mean()["math_score"]
twelfth_graders_scores = twelfth_grade.groupby(["school_name"]).mean()["math_score"]


scores_by_grade_df = pd.DataFrame({"9th": ninth_graders_scores,
                                "10th":tenth_graders_scores,
                                "11th":eleventh_graders_scores,
                                "12th":twelfth_graders_scores,})



scores_by_grade_df.index.name = None

scores_by_grade_df = scores_by_grade_df [["9th", "10th", "11th", "12th"]]


scores_by_grade_df


# ## Reading Score by Grade 

# * Perform the same operations as above for reading scores

# In[161]:


ninth_graders = complete_df[(complete_df["grade"] == "9th")]
tenth_graders = complete_df[(complete_df["grade"] == "10th")]
eleventh_graders = complete_df[(complete_df["grade"] == "11th")]
twelfth_graders = complete_df[(complete_df["grade"] == "12th")]

ninth_graders_scores = ninth_graders.groupby(["school_name"]).mean()["reading_score"]
tenth_graders_scores = tenth_graders.groupby(["school_name"]).mean()["reading_score"]
eleventh_graders_scores = eleventh_graders.groupby(["school_name"]).mean()["reading_score"]
twelfth_graders_scores = twelfth_graders.groupby(["school_name"]).mean()["reading_score"]


scores_by_grade_df = pd.DataFrame({"9th": ninth_graders_scores,
                                "10th":tenth_graders_scores,
                                "11th":eleventh_graders_scores,
                                "12th":twelfth_graders_scores})

scores_by_grade_df.index.name = None

scores_by_grade_df = scores_by_grade_df [["9th", "10th", "11th", "12th"]]
scores_by_grade_df


# ## Scores by School Spending

# * Create a table that breaks down school performances based on average Spending Ranges (Per Student). Use 4 reasonable bins to group school spending. Include in the table each of the following:
#   * Average Math Score
#   * Average Reading Score
#   * % Passing Math
#   * % Passing Reading
#   * Overall Passing Rate (Average of the above two)

# In[17]:


# Sample bins. Feel free to create your own bins.
spending_bins = [0, 585, 615, 645, 675]
group_names = ["<$585", "$585-615", "$615-645", "$645-675"]


# In[18]:





# ## Scores by School Size

# * Perform the same operations as above, based on school size.

# In[ ]:


# Sample bins. Feel free to create your own bins.
size_bins = [0, 1000, 2000, 5000]
group_names = ["Small (<1000)", "Medium (1000-2000)", "Large (2000-5000)"]


# In[162]:


school_data_complete_bin = complete_df.copy()
school_data_complete_bin.head()


# ## Scores by School Type

# * Perform the same operations as above, based on school type.

# In[20]:





# In[ ]:




