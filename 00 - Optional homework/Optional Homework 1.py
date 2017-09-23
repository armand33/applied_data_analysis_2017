import matplotlib.pyplot as plt

# do everything with standard Python libraries
def nativeversion():
    import csv

    # Open CSV
    table=[]
    with open('full_data.csv') as csvfile:
        reader = csv.DictReader(csvfile)
        data=dict()
        for fname in reader.fieldnames:  #TODO rewrite code more elegant
            data[fname]=[] # initialize

        for row in reader:
            table.append(row)
            for fname in reader.fieldnames:
                data[fname].append(row[fname])
    print(table)

    # GET NUMBERS FROM ARTICLE
    # percentage suicide
    perc_suicide=data['intent'].count("Suicide") / len(data['intent'])*100 # percentage of suicides
    print("Percentage Suicides: " + repr(round(perc_suicide, 2)) + " %")

    # percentage male suicides

    print("Percentage Males in Suicides: " + repr(round(perc_suicide_male, 2)) + " %")




# do the same with a more sophisticated library
def pandaversion():
    import pandas

    # Load the data into a DataFrame
    data = pandas.read_csv('full_data.csv')

    ## Group by intent
    print(data.groupby('intent').sum())


    ## Group by intent, sex
    data_agg_intent_sex=data.groupby(['intent','sex']).count()
    #print(data_agg_intent_sex.groupby(level=0).apply(lambda x: 100*x/ x.sum()))



#nativeversion()
pandaversion()