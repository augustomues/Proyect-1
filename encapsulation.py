import pandas as pd
import numpy as np
import datetime as dt
import matplotlib.pyplot as plt
import seaborn as sns


def df_import_clean(df):
    """
        Description: Function created to clean the shark dataframe extracted from Kaggle: https://www.kaggle.com/datasets/teajay/global-shark-attacks
        Input: Location path of the dataframe
        Return: Shark DataFrame cleaned    
    """
    original = pd.read_csv(df)
    original.drop(columns=['Unnamed: 22', 'Unnamed: 23'], inplace=True)
    original.dropna(axis=0, how='all', inplace=True)
    original.drop(['pdf', 'Name', 'href formula', 'href', 'Case Number.1', 'Case Number.2', 'original order'], axis=1, inplace=True)
    original.drop('Case Number', axis=1, inplace=True) 
    original.dropna(axis=0, subset=['Year'], inplace=True)
    original['Year'] = original['Year'].apply(lambda x: int(x))
    original['Date'] = original['Date'].str.extract('(\d\d.\w\w\w.\d+)')
    original = original[original['Year'] != 0]
    return original

def time_of_day(x):
    """
        Description: From the column 'Time', this function calculate the moment of the day:
            Night: 0 to 5:59
            Morning: 6 to 11:59
            Afternoon: 12 to 17:59
            Evening: 18:00 to 23:59
        Input: string containing "hh:mm" 
        Return: It return the momento of the day (Night, Morning, Afternoon or Evening. If it cannot convert, it will return 'Unknown'  
    """
    if (x == 'Morning') or (x == 'Afternoon') or (x == 'Night'):
        return x
    else:
        try:
            if int(x[:2]) < 6:
                return 'Night'
            elif int(x[:2]) < 12:
                return 'Morning'
            elif int(x[:2]) < 18:
                return 'Afternoon'
            else:
                return 'Evening'
        except:
            return 'Unknown'
        
def decades_fun(x):
    """
        Description: It calculates the corresponding the decade of a passed year 
        Input: int
        Return: If int <1900, it return '<1900'. If it is between 1900 and 2020, will return the first year of the decade. E.g. 1992 -> 1990 
    """
    decades = dict()
    for i in range(1900, 2020, 10):
        decades[i] = list(range(i, i+10))
    for key, values in decades.items():
        if x in values:
            return key
    return '<1900'

def to_datetime(x: str):
    
    """
    Convert a date string in the format of '%d-%b-%Y' to a new string with the format of '%d-%b'.
    
    Args:
    x (str): a date string in the format of '%d-%b-%Y'
    
    Returns:
    A new string with the format of '%d-%b', representing the day and month of the input date string.
    If the input is not a valid date string, returns either the original input if it's not a TypeError, or 0 if it's a ValueError.
    """
    
    try:
        # convert the input string to a datetime object
        x = dt.datetime.strptime(x, '%d-%b-%Y')
        
        # convert the datetime object to a string with the desired format
        return dt.datetime.strftime(x, '%d-%b')
    
    except TypeError:
        # if the input is not a string, return the original input
        return x
    
    except ValueError:
        # if the input is not a valid date string, return 0
        return 0
    
def season(x):

    """
    Returns the seasason of the passed Year (from a DataFrame), as long as the country correspond to either USA, AUSTRALIA or SOUTHAFRICA

    Args:
    x (DataFrame): a DataFram containing the columns 'day_month' and 'Country'

    Returns:
    A new string that could be Summer, Autumn, Spring, Winter or Unkown (if the day_month passed is to on the %d-%b format)
    """
    if x['Country'] == 'USA':
        try:
            if (dt.datetime.strptime(x['day_month'], '%d-%b') > dt.datetime(year=1900, month=6, day=20)) & (dt.datetime.strptime(x['day_month'], '%d-%b') < dt.datetime(year=1900, month=9, day=21)):
                return 'Summer'
            elif (dt.datetime.strptime(x['day_month'], '%d-%b') > dt.datetime(year=1900, month=9, day=20)) & (dt.datetime.strptime(x['day_month'], '%d-%b') < dt.datetime(year=1900, month=12, day=21)):
                return 'Autumn'
            elif (dt.datetime.strptime(x['day_month'], '%d-%b') > dt.datetime(year=1900, month=3, day=20)) & (dt.datetime.strptime(x['day_month'], '%d-%b') < dt.datetime(year=1900, month=6, day=21)):
                return 'Spring'
            else:
                return 'Winter'
        except:
            return 'Unknown'
    elif (x['Country'] == 'AUSTRALIA') or (x['Country'] == 'SOUTHAFRICA'):
        try:
            if (dt.datetime.strptime(x['day_month'], '%d-%b') > dt.datetime(year=1900, month=6, day=20)) & (dt.datetime.strptime(x['day_month'], '%d-%b') < dt.datetime(year=1900, month=9, day=21)):
                return 'Winter'
            elif (dt.datetime.strptime(x['day_month'], '%d-%b') > dt.datetime(year=1900, month=9, day=20)) & (dt.datetime.strptime(x['day_month'], '%d-%b') < dt.datetime(year=1900, month=12, day=21)):
                return 'Spring'
            elif (dt.datetime.strptime(x['day_month'], '%d-%b') > dt.datetime(year=1900, month=3, day=20)) & (dt.datetime.strptime(x['day_month'], '%d-%b') < dt.datetime(year=1900, month=6, day=21)):
                return 'Autumn'
            else:
                return 'Summer'
        except:
           return 'Unknown'
    else:
        return 'Unknown'  
    
def location(x: str) -> str:

    """
    Returns a cleaned and formatted version of the input string based on a predefined list of locations.
    
    Args:
    x (str): the input string to be cleaned and formatted
    
    Returns:
    If the input string contains any of the predefined locations, returns that location capitalized.
    If the input string does not contain any of the predefined locations, returns 'Other'.
    """
    
    # Define a list of locations to look for in the input string
    locations = ['volusia', 'vrevard', 'palm', 'charleston', 'thursday', 'duval', 'martin']
    
    # Loop through the locations and check if the input string contains any of them
    for i in locations:
        if str(x).lower().find(i) >= 0:
            # If the input string contains a predefined location, return that location capitalized
            return i.capitalize()
    
    # If the input string does not contain any of the predefined locations, return 'Other'
    return 'Other'

def further_clean(df):
    """
    
    Returns a DataFrame that was further cleaned. It add the columns
    
    Args:
    df (DataFrame): the input is DataFrame related to sharks attacked, located on Kaggle.

    Returns: It returns a new DataFrame containing new columns such as Moment of Day, decades, day_month, etc.
    It also remove rows from before 1900 (decades != '<1900') and only keep rows where Fatal column was 'Y' or 'N'
    """
    df['Moment of Day'] = df['Time'].apply(lambda x: time_of_day(x))
    df['decades'] = df['Year'].apply(lambda x: decades_fun(x)) 
    df['day_month'] = df['Date'].apply(lambda x: to_datetime(x))
    df['season'] = df.apply(lambda x: season(x), axis=1)
    df['Location2'] = df['Location'].apply(lambda x: location(x))
    df = df[df['decades'] != '<1900']
    df = df[(df['Fatal (Y/N)'] == 'Y') | (df['Fatal (Y/N)'] == 'N')]
    df['GSAF?'] = df['Investigator or Source'].str.extract('(GSAF)')
    return df

def vis1(df):
    fig = plt.figure(figsize=(10,8))
    sns.countplot(x=df['decades'], data=df, palette='magma')
    plt.ylabel('Count of Incidents', fontsize = 16)
    plt.title('Shark Attacks Evolution', fontsize=18)
    plt.xlabel('Decades', fontsize = 16)
    fig.savefig('Images/1. Shark Attacks Evolution.png')

def vis2(df):
    fig = plt.figure(figsize=(20,8))
    sns.countplot(data=df, x=df['decades'], hue='Fatal (Y/N)', palette='magma')
    plt.ylabel('Count of Incidents', fontsize = 16)
    plt.title('Shark Attacks Ev per Fatality', fontsize=18)
    plt.xlabel('Decades', fontsize = 16)
    fig.savefig('Images/2. Shark Attack Ev. per Fatality.png')

def top_countries(df):
    top_countries = df.groupby(by='Country').agg({'Country': 'count'})
    top_countries.rename(columns = {'Country': 'Sum_Country'}, inplace=True)
    top_countries = top_countries.sort_values(by='Sum_Country', ascending=False)
    top_countries[:10].sum()/top_countries.sum() #Considering the top 3 countries, I'm already covering almost 70% of datab
    df_top_countries = df[df['Country'].isin(list(top_countries[:10].index))]
    return df_top_countries, top_countries

def vis3(df_top_countries, top_countries):
    fig = plt.figure(figsize=(10,8))
    sns.countplot(data=df_top_countries[(df_top_countries['decades'] == '2000') | (df_top_countries['decades'] == '2010')], y=df_top_countries['Country'], order=list(top_countries[:10].index), palette='magma')
    plt.ylabel('Top10 Countries', fontsize = 16)
    plt.title('Total Shark Attacks in last 2 decades for top10 Countries', fontsize=18)
    plt.xlabel('Count of shark attacks', fontsize = 16)
    plt.xticks(rotation=0, fontsize=14)
    fig.savefig('Images/3. Top10 Countries with most shark attacks (2020-2020).png')

def vis4(top_countries, df):
    fig, axs = plt.subplots(nrows=1, ncols=4, figsize=(30,10))
    fig.suptitle('Shark Attacks Ev. per Fatality per Countries')
    j=0
    for i in list(top_countries[:3].index):
        sub = sns.histplot(data=df[df['Country'] == i], x=df['decades'], hue='Fatal (Y/N)',palette='magma', ax=axs[j], multiple='stack', bins=12)
        sub.set(title=i)
        j += 1
    (sns.histplot(data=df[(df['Country'] != 'AUSTRALIA') & (df['Country'] != 'USA') & (df['Country'] != 'SOUTHAFRICA')], x=df['decades'], ax=axs[3], palette='magma', hue='Fatal (Y/N)', multiple='stack', bins=12)).set(title='OTHERS')
    fig.savefig('Images/4. Shark Attacks Ev. per Fatality per Top Countries.png')

def vis5(df):
    fig = plt.figure(figsize=(10,8))
    sns.countplot(data=df[(df['GSAF?'] == 'GSAF') & ((df['Country'] != 'USA') | (df['Country'] != 'AUSTRALIA'))], x='decades', palette='magma')
    plt.title('Shark Attacks reports evolution done by "GSAF"', fontsize=18)
    plt.ylabel('Shark Attacks count', fontsize=16)
    plt.xlabel('Decades', fontsize=16)
    plt.xticks(fontsize=14)
    plt.yticks(fontsize=14)
    fig.savefig('Images/5. Shark Attacks reports Ev. done by GSAF.png')

def vis6(df):
    usa_aus = df[((df['Country'] == 'USA') | (df['Country'] == 'AUSTRALIA')) & (df['Fatal (Y/N)'] == 'N')]
    fig = plt.figure(figsize=(15,8)) 
    sns.countplot(data=usa_aus[usa_aus['GSAF?'] == 'GSAF'], x='decades', hue='Country', palette='magma')
    plt.title('Shark Attacks reports evolution done by "GSAF" on USA and AUSTRALIA', fontsize=18)
    plt.ylabel('Shark Attacks count', fontsize=16)
    plt.xlabel('Decades', fontsize=16)
    plt.xticks(fontsize=14)
    plt.yticks(fontsize=14)
    fig.savefig('Images/6. Shark Attacks reports Ev. done by GSAF in USA and AUS.png')

def vis7(df, top_countries):
    fig = plt.figure(figsize=(10,8))
    sns.countplot(data=df[(df['Country'].isin(list(top_countries[:3].index))) & (df['Moment of Day'] != 'Unkown')], x='Country', hue='Moment of Day')
    plt.title('Shark Attacks in top 3 countries per Moment of Day', fontsize=18)
    plt.ylabel('Shark Attacks count', fontsize=16)
    plt.xlabel('Countries', fontsize=16)
    fig.savefig('Images/7. Shark Attacks in top 3 countries per Moment of Day.png')

def vis8(df):
    usa_aus = df[((df['Country'] == 'USA') | (df['Country'] == 'AUSTRALIA')) & (df['Fatal (Y/N)'] == 'N')]
    fig, axs = plt.subplots(nrows=1, ncols=2, figsize=(30,10))
    hues = ['Unkown', 'Night', 'Morning', 'Afternoon', 'Evening']
    (sns.countplot(data=usa_aus[usa_aus['Country'] == 'USA'], x='decades', hue='Moment of Day', hue_order=hues, ax=axs[0])).set(title='USA')
    axs[0].legend(loc='upper left')
    (sns.countplot(data=usa_aus[usa_aus['Country'] == 'AUSTRALIA'], x='decades', hue='Moment of Day', hue_order=hues, ax=axs[1])).set(title='AUSTRALIA')
    axs[1].legend(loc='upper left')
    fig.savefig('Images/8. Shark Attack Ev. per moment of Day.png');

def vis9(df):
    usa_aus = df[((df['Country'] == 'USA') | (df['Country'] == 'AUSTRALIA')) & (df['Fatal (Y/N)'] == 'N')]
    usa_aus_seasons = usa_aus[usa_aus['season'] != 'Unknown']
    fig, axs = plt.subplots(nrows=1, ncols=2,figsize=(30,10))
    hues=['Spring', 'Winter', 'Autumn', 'Summer']
    sns.countplot(data=usa_aus_seasons[usa_aus_seasons['Country'] != 'USA'], x='decades', hue='season', hue_order=hues, ax=axs[0]).set(title='USA')
    sns.countplot(data=usa_aus_seasons[usa_aus_seasons['Country'] != 'AUSTRALIA'], x='decades', hue='season', hue_order=hues, ax=axs[1]).set(title='AUSTRALIA')
    axs[0].legend(loc='upper left')
    axs[1].legend(loc='upper left')
    fig.savefig('Images/9. Shark Attack evolution per Season.png')

def vis10(df):
    fig = plt.figure(figsize=(10,8))
    usa_aus = df[((df['Country'] == 'USA') | (df['Country'] == 'AUSTRALIA')) & (df['Fatal (Y/N)'] == 'N')] 
    sns.countplot(data=usa_aus, x='decades', hue='Country', palette='magma', edgecolor='white')
    plt.title('Shark Attacks evolution in USA and AUSTRALIA per country', fontsize=18)
    plt.ylabel('Shark Attacks count', fontsize=16)
    plt.xlabel('Decades', fontsize=16)
    plt.legend(loc='upper left')
    fig.savefig('Images/10. Shark Attacks evolution in USA and AUSTRALIA.png');

def vis11(df):
    usa_aus = df[((df['Country'] == 'USA') | (df['Country'] == 'AUSTRALIA')) & (df['Fatal (Y/N)'] == 'N')] 
    fig = plt.figure(figsize=(20,8)) 
    sns.countplot(x='decades', data=usa_aus[usa_aus['Country'] == 'USA'], hue='Location2', edgecolor='white')
    plt.title('Shark Attacks evolution in USA per Location', fontsize=18)
    plt.ylabel('Shark Attacks count', fontsize=16)
    plt.xlabel('Decades', fontsize=16)
    plt.legend(loc='upper left')
    fig.savefig('Images/11. Skark Attacks in USA per Location.png')