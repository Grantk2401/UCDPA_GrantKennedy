import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns
import functions as fs
import numpy as np

general = pd.read_csv("general_data.csv")
survey = pd.read_csv("employee_survey_data.csv")

fs.allinfo()

#data cleaning
print(general.isnull().sum())
print(survey.isnull().sum())

general.fillna(0,inplace= True)
survey.fillna(0,inplace= True)

print(general.isnull().any())
print(survey.isnull().any())

#sorting
general_years = general.sort_values("YearsAtCompany", ascending= False)
survey_satisfaction = survey.sort_values("JobSatisfaction", ascending= False)

print(general_years)
print(survey_satisfaction)

#looping iterrows
for lab, row in general_years.iterrows():
    print("EmployeeID:", lab, "- ", row["YearsAtCompany"])

#merging dataframes
merged_data = pd.merge(general_years, survey_satisfaction, on="EmployeeID")
print(merged_data.info)

merged_satisfaction = merged_data.sort_values("JobSatisfaction", ascending= False)

#using numpy
average_satisfaction = np.mean(merged_satisfaction["JobSatisfaction"])
average_age = np.mean(merged_satisfaction["Age"])
average_years = np.mean(merged_satisfaction["YearsAtCompany"])
average_distance = np.mean(merged_satisfaction["DistanceFromHome"])

print(average_satisfaction, average_age, average_years, average_distance)

#creating a list
satisfaction = 2.71
age = 37
years = 7
distance = 9.19

averages = [satisfaction, age, years, distance]

print(averages)

averages = ["Job satisfaction:", satisfaction, "Age:", age, "Years at company:", years, "Distance from home in miles:",
            distance]

print(averages)

#visulize

#displot showing job satisfaction by gender
sns.set_theme(style="darkgrid")
sns.displot(
    merged_satisfaction, x="JobSatisfaction", col= "Gender",
)
plt.show()

#catplot showing job satisfaction by department and job level
sns.catplot(
    data=merged_satisfaction, kind="bar",
    x="Department", y= "JobSatisfaction", hue= "JobLevel",
    ci="sd", palette="dark", alpha=.6, height=6,
)
plt.show()

#Pie chart to show job satisfaction scores in %'s
print(merged_satisfaction["JobSatisfaction"].value_counts())
labels = '0', '1', '2', '3', '4'
sizes = [20, 840, 860, 1323, 1367]

fig1, ax1 = plt.subplots()
ax1.pie(sizes, labels=labels, autopct='%1.1f%%',
        shadow=True, startangle=90)
ax1.axis('equal')
plt.title("Job satisfaction score %'s")

plt.show()

#Bar chart showing averages
average_dict = {"Satisfaction":2.71, "Age":37, "Years at company":7, "Dist from home in KM":9.19}
category = list(average_dict.keys())
value = list(average_dict.values())

fig = plt.figure(figsize= (10, 5))

plt.bar(category,value, color = "maroon", width= 0.4)

plt.xlabel("Categories")
plt.ylabel("Average figure")
plt.title("The average figure for multiple categories")
plt.show()