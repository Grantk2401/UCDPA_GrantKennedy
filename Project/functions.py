import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns
import numpy as np

general = pd.read_csv("general_data.csv")
survey = pd.read_csv("employee_survey_data.csv")

def allinfo():
    print(general.info(), general.head(10), general.shape, general.describe())
    print(survey.info(), survey.head(10), survey.shape, survey.describe())

def importgeneral(filename):
    general = pd.read_csv("general_data.csv")
    print(general.head(10))
    print(general.index)
    print(general.info)

def importsurvey(filename):
    survey = pd.read_csv("employee_survey_data.csv")
    print(survey.head(10))
    print(survey.index)
    print(survey.info)

def runaverages():
    average_satisfaction = np.mean(merged_satisfaction["JobSatisfaction"])
    average_age = np.mean(merged_satisfaction["Age"])
    average_years = np.mean(merged_satisfaction["YearsAtCompany"])
    average_distance = np.mean(merged_satisfaction["DistanceFromHome"])

    print(average_satisfaction, average_age, average_years, average_distance)

def addfiles():
    general = pd.read_csv("general_data.csv")
    survey = pd.read_csv("employee_survey_data.csv")

    # data cleaning
    print(general.isnull().sum())
    print(survey.isnull().sum())

    general.fillna(0, inplace=True)
    survey.fillna(0, inplace=True)

    print(general.isnull().any())
    print(survey.isnull().any())

    # sorting
    general_years = general.sort_values("YearsAtCompany", ascending=False)
    survey_satisfaction = survey.sort_values("JobSatisfaction", ascending=False)

    print(general_years)
    print(survey_satisfaction)

    # looping iterrows
    for lab, row in general_years.iterrows():
        print("EmployeeID:", lab, "- ", row["YearsAtCompany"])

    # merging dataframes
    merged_data = pd.merge(general_years, survey_satisfaction, on="EmployeeID")
    print(merged_data.info)

    merged_satisfaction = merged_data.sort_values("JobSatisfaction", ascending=False)
    print(merged_satisfaction)
