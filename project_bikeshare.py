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
    
    #Valid values for cities, months and days f the week
    cities = ['chicago','new york city', 'new york','washington']
    months = ['january', 'february','march', 'may', 'june', 'july', 'august', 'september', 'october', 'november', 'december', 'all']
    days = ['monday', 'thuesday', 'wednesday', 'thursday', 'friday', 'saturday', 'sunday', 'all']

    # TO DO: get user input for city (chicago, new york city, washington). HINT: Use a while loop to handle invalid inputs
    while True:
        try:
            c = input('\nPlease enter which of the three cities you would like to explore (chicago, new york city or washington):\n')
            city = c.lower()

            if city in cities:
                break
            else:
                print('\nThat is not a valid city. Please select chicago, new york city or washington.')
                
        except:
            print('\n That is not a valid value. Please select chicago, new york city or washington.')

    # TO DO: get user input for month (all, january, february, ... , june)
    while True:
        try:
            m = input('\nPlease enter which month ou would like to consult or type "all" in case you do not want to filter by month:\n')
            month = m.lower()

            if month in months:
                break
            else:
                print('\nThat is not a valid month.')
                
        except:
            print('\n That is not a valid value. Please enter a valid month.')

    # TO DO: get user input for day of week (all, monday, tuesday, ... sunday)
    while True:
        try:
            d = input('\nPlease enter which day of the week you would like to consult or type "all" in case you do not want to filter by a day of the week:\n')
            day = d.lower()

            if day in days:
                break
            else:
                print('\nThat is not a valid day. Please select a valid day of the week.')
                
        except:
            print('\n That is not a valid value. Please select a valid day of the week.')

    print('-'*40)
    return city, month, day


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
    months = ['january', 'february','march', 'may', 'june', 'july', 'august', 'september', 'october', 'november', 'december']

    #update name of new york in case it is incomplete
    if city == 'new york':
        city+=' city'

    df = pd.read_csv(CITY_DATA[city])

    df['Start Time'] = pd.to_datetime(df['Start Time'])
    df['month'] = df['Start Time'].dt.month
    df['day_of_week'] = df['Start Time'].dt.weekday_name

    #filter by month
    if month != 'all':
        m = months.index(month) + 1
        df = df[df['month']==m]

    #filter by day
    if day != 'all':
        df = df[df['day_of_week'] == day.title()]      

    return df


def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    months = ['january', 'february','march', 'may', 'june', 'july', 'august', 'september', 'october', 'november', 'december']

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    # TO DO: display the most common month
    common_month = df['month'].mode()[0]
    print('\n{} is the most common month to rent a bike.'.format(months[common_month-1].title()))

    # TO DO: display the most common day of week
    common_day = df['day_of_week'].mode()[0]
    print('\n{} is the most common day of the week to rent a bike.'.format(common_day))

    # TO DO: display the most common start hour
    df['Start hour'] = df['Start Time'].dt.hour
    common_hour = df['Start hour'].mode()[0]
    print('\n{}h is the most common hour of the day to rent a bike.'.format(common_hour))

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # TO DO: display most commonly used start station
    df['Start Station'] = df['Start Station'].str.title()
    common_start_station = df['Start Station'].mode()[0]
    count1 = df['Start Station'].value_counts().max()
    print('\n"{}" is the most common start station. Count: {}'.format(common_start_station, count1))

    # TO DO: display most commonly used end station
    df['End Station'] = df['End Station'].str.title()
    common_end_station = df['End Station'].mode()[0]
    count2 = df['End Station'].value_counts().max()
    print('\n"{}" is the most common end station. Count: {}'.format(common_end_station, count2))

    # TO DO: display most frequent combination of start station and end station trip
    df['Station Combination'] = df['Start Station'] + " --> " + df['End Station']
    common_station_combination = df['Station Combination'].mode()[0]
    count3 =  df['Station Combination'].value_counts().max()
    print('\n"{}" is the most frequent combination of start station and end station trip. Count: {}'.format(common_station_combination, count3))

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def time_conversion(seconds):
    """Converts seconds to the format hh:mm:ss
    """
    hour = int(seconds//3600)
    rest_hour = seconds%3600
    minute = int(rest_hour//60)
    second = rest_hour%60

    return hour, minute, second


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # TO DO: display total travel time
    total_travel_time = df['Trip Duration'].sum()
    travel_hours, travel_minutes, travel_seconds = time_conversion(total_travel_time)
    print('\nTotal travel time is: {}:{}:{}s'.format(travel_hours, travel_minutes, travel_seconds))

    # TO DO: display mean travel time
    mean_travel_time = df['Trip Duration'].mean()
    mean_travel_hours, mean_travel_minutes, mean_travel_seconds = time_conversion(mean_travel_time)
    print('\nThe mean travel time is: {}:{}:{}s'.format(mean_travel_hours, mean_travel_minutes, mean_travel_seconds))

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # TO DO: Display counts of user types
    print('\nThe count of user types is:')
    users = df['User Type'].value_counts()
    for user in users.index:
        print('{}: {}'.format(user,users[user]))

    # TO DO: Display counts of gender
    if 'Gender' in df:
        print('\nThe count of genders is:')
        genders = df['Gender'].value_counts()
        for gender in genders.index:
            print('{}: {}'.format(gender,genders[gender]))

    # TO DO: Display earliest, most recent, and most common year of birth
    if 'Birth Year' in df:
        earliest_year = int(df['Birth Year'].min())
        most_recent_year = int (df['Birth Year'].max())
        most_common_birth_year = int(df['Birth Year'].mode()[0])
        print('\nThe earliest year of birth is: {}\nThe most recent year of birth is: {}\nThe most common year of birth is: {}'.format(earliest_year, most_recent_year, most_common_birth_year))

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def raw_data(df):
    ''' Function that return five rows of raw data every time you enter Y 
    '''
    #counters
    start_row = 0
    end_row = 6 
    max_row= df.shape[0] #total number of rows in the data set

    while True:
        c = input('\nWould you like to see the raw data? Enter yes or no.\n')
        go_on = c.lower()

        if go_on != 'yes':
            break
        else:
            print(df[start_row:end_row])

            start_row = end_row
            end_row += 5

            if end_row > max_row:
                end_row = max_row

            if start_row >= max_row:
                break



def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)

        raw_data(df)

        stats = input('\nWould you like to see the stats? Enter yes or no.\n')
        if stats.lower() == 'yes':
            time_stats(df)
            station_stats(df)
            trip_duration_stats(df)
            user_stats(df)

        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break


if __name__ == "__main__":
	main()
