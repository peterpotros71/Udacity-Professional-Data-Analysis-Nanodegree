import time
import pandas as pd
import numpy as np

CITY_DATA = { 'chicago': 'chicago.csv',
              'new york city': 'new_york_city.csv',
              'washington': 'washington.csv' }

def get_filters():
    """
    Asks user to specify a city, month, and day to analyze.

    Returns:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    """
    print('Hello! Let\'s explore some US bikeshare data!')
    # TO DO: get user input for city (chicago, new york city, washington). HINT: Use a while loop to handle invalid inputs
    city = input("would you like to see data for chicago, new york city or washington? please type out one city name from the three cities       \n")
    while city.lower() not in ['chicago', 'new york city', 'washington']:
        city = input("please type out the correct city name\n")
        
    # TO DO: get user input for month (all, january, february, ... , june)
    month = input("which month? january, february, ... ,june or all? please type out the full month name\n")
    while month.lower() not in ["january", "february", "march", "april", "may", "june", "all"]:
        month = input("please type out the correct month name\n")
     
    # TO DO: get user input for day of week (all, monday, tuesday, ... sunday)
    day = input("which day? monday, tuesday, ... ,sunday or all? please type out the full day name\n")
    while day.lower() not in ["monday", "tuesday", "wednesday", "thursday", "friday", "saturday", "sunday", "all"]:
        day = input("please type out the correct day name\n")
        
        
    print('-'*40)
    return city.lower(), month.lower(), day.lower()


def load_data(city, month, day):
    """
    Loads data for the specified city and filters by month and day if applicable.

    Args:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    Returns:
        df - Pandas DataFrame containing city data filtered by month and day
    """
    # load data file into a dataframe
    df = pd.read_csv(CITY_DATA[city])
    
    # convert the Start Time column to datetime
    df['Start Time'] = pd.to_datetime(df['Start Time'])
    
    # extract month from the Start Time column to create a month column
    df['month'] = df['Start Time'].dt.month
    
    # extract day_of_week from the Start Time column to create a day_of_week column
    df['day_of_week'] = df['Start Time'].dt.weekday_name
    
    if month != 'all':
        months = ['january', 'february', 'march', 'april', 'may', 'june']
        month = months.index(month) + 1
        df = df[df['month'] == month]
    
    if day != 'all':
        df = df[df['day_of_week'] == day.title()]

    return df


def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    # TO DO: display the most common month
    most_common_month = df['month'].mode()[0]
    count_month = 0
    for month in df['month']:
        if month == most_common_month:
            count_month += 1
    print("most common month:{} ,count:{}".format(most_common_month, count_month))
    
    # TO DO: display the most common day of week
    most_common_day_of_week = df['day_of_week'].mode()[0]
    count_day_of_week = 0
    for day in df['day_of_week']:
        if day == most_common_day_of_week:
            count_day_of_week += 1
    print("most common day of week:{} ,count:{}".format(most_common_day_of_week, count_day_of_week))
    
    # TO DO: display the most common start hour
    df['hour'] = df['Start Time'].dt.hour
    most_common_start_hour = df['hour'].mode()[0]
    count_start_hour = 0
    for hour in df['hour']:
        if hour == most_common_start_hour:
            count_start_hour += 1
    print("most common start hour:{}, count:{}".format(most_common_start_hour, count_start_hour))
    
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # TO DO: display most commonly used start station
    most_commonly_used_start_station = df['Start Station'].mode()[0]
    count_start_station= 0
    for start_station in df['Start Station']:
        if start_station == most_commonly_used_start_station:
            count_start_station += 1
    print("most commonly used start station:{} ,count:{}".format(most_commonly_used_start_station, count_start_station))
    

    # TO DO: display most commonly used end station
    most_commonly_used_end_station = df['End Station'].mode()[0]
    count_end_station= 0
    for end_station in df['End Station']:
        if end_station == most_commonly_used_end_station:
            count_end_station += 1
    print("most commonly used end station:{} ,count:{}".format(most_commonly_used_end_station, count_end_station))      


    # TO DO: display most frequent combination of start station and end station trip


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # TO DO: display total travel time
    total_travel_time = sum(df['Trip Duration'])
    print("total travel time:{}".format(total_travel_time))


    # TO DO: display mean travel time
    mean_travel_time = df['Trip Duration'].mean()
    print("mean travel time:{}".format(mean_travel_time))


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_stats(df, city):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # TO DO: Display counts of user types
    user_types = df['User Type'].value_counts()
    print(user_types)


    if city == "washington":
        print("there arn\'t information about Gender and Year of Birth in washington city")
    else:    
        # TO DO: Display counts of gender
        user_genders = df['Gender'].value_counts()
        print(user_genders)


        # TO DO: Display earliest, most recent, and most common year of birth
        earliest = df['Birth Year'].min()
        recent = df['Birth Year'].max()      
        most_common = df['Birth Year'].mode()[0]
        print("earliest year of birth:{}, recent year of birth:{}, most common year of birth:{}".format(earliest, recent, most_common)) 


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)
    
    
def display_data(city, num_of_raws):
    #print(df.head())
    print(pd.read_csv(CITY_DATA[city]).iloc[num_of_raws-5:num_of_raws])
    

def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)

        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df, city)
        
        num_of_raws = 5
        if input('\ndo you want to see raw data? Enter yes or no.\n').lower() == 'yes':
            display_data(city, num_of_raws)
            num_of_raws += 5
            while input('\ndo you want to see more 5 lines of raw data? Enter yes or no.\n').lower() == 'yes':        
                display_data(city, num_of_raws)
                num_of_raws += 5
            

        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break


if __name__ == "__main__":
	main()
