import matplotlib.pyplot as plt
import csv
import pandas as pd
import numpy as np

# do everything with standard Python libraries
data = []
data_pd = []
def prep_data():
    with open('full_data.csv') as csvfile:
        reader = csv.reader(csvfile)
        for row in reader:
            data.append(row)
        header=data[0]
        print(header)
        data.pop(0)
    data_pd=pd.DataFrame(data, columns=header)
    data_pd["age"] = data_pd["age"].replace("NA", 0).astype('int') # data type int for "age"
    data_pd["year"] = data_pd["year"].replace("NA", 0).astype('int')  # data type int for "age"
    return data_pd

def get_numbers(data_pd):

    # Get numbers from article
    # 1. suicides
    perc_intent=data_pd[['intent','sex','age']].groupby(['intent']).count().apply(lambda x: 100*x/ x.sum())
    #print(round(perc_intent,2))

    # 2. men in suicide category
    data_pd_intent=data_pd[data_pd["intent"] == "Suicide"]
    perc_intent_sex=data_pd_intent[['intent', 'sex', 'age']].groupby(['sex']).count().apply(lambda x: 100 * x / x.sum())
    #print(round(perc_intent_sex,2))

    # 3. pecentage of men aged 45 or older in suicides
    perc_intent_sex_age=data_pd_intent[data_pd_intent["age"] >= 45].count() / data_pd_intent.count()
    #print(round(perc_suicide_sex_age[0],2))

    # 4. total homicides / year
    data_pd_homicide=data_pd[data_pd["intent"] == "Homicide"]
    sum_intent = data_pd_homicide[['intent', 'age','year']].groupby(['year']).sum() # TODO I get other numbers
    #print(sum_intent)

    # TODO where is victim data?

    #perc_men_suicide = data_pd_suicide[['intent', 'sex', 'age']].groupby(['sex']).count().apply(lambda x: 100 * x / x.sum())  # get all intents in percent


data_pd=prep_data()
get_numbers(data_pd)