import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns

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

