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

    valid_city = ['chicago', 'new york city', 'washington']
    valid_months = ['january', 'february', 'march', 'april', 'may', 'june', 'all']
    valid_day = ['sunday', 'monday', 'tuesday', 'wednesday', 'thrusday', 'friday', 'saturday', 'all']
    inputs_needed = {
        "city": valid_city,
        "month": valid_months,
        "day": valid_day
    }
    inputs = {};
    for input_, valid_inputs in inputs_needed.items():
        while True:
            input_entered = input("Please enter value for " + input_ + " [Note: valid values are: " + str(valid_inputs) + "] : ").lower()
            if input_entered in valid_inputs:
                print("You entered " + input_entered + " for " + input_)
                inputs[input_] = input_entered
                break
            else:
                print("Invalid choice, try again please")
                continue
    return inputs['city'], inputs['month'], inputs['day']

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
    df = pd.read_csv(CITY_DATA[city])
    df['Start Time'] = pd.to_datetime(df['Start Time'])

    # extract month and day of week from Start Time to create new columns
    df['month'] = df['Start Time'].dt.month
    df['day'] = df['Start Time'].dt.weekday_name

    # filter by month if applicable
    if month != 'all':
        # use the index of the months list to get the corresponding int
        months = ['january', 'february', 'march', 'april', 'may', 'june']
        month = months.index(month) + 1

        # filter by month to create the new dataframe
        df = df[df['month'] == month]

    # filter by day of week if applicable
    if day != 'all':
        # filter by day of week to create the new dataframe
        df = df[df['day'] == day.title()]
    return df

def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    # TO DO: display the most common month
    most_common_month = df['month'].mode()[0]
    print('Most Common Month:', most_common_month)

    # TO DO: display the most common day of week
    most_common_day = df['day'].mode()[0]
    print('Most Common Day:', most_common_day)

    # TO DO: display the most common start hour
    df['hour'] = df['Start Time'].dt.hour
    most_common_starthour = df['hour'].mode()[0]
    print('Most Common Start Hour:', most_common_starthour)

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # TO DO: display most commonly used start station
    most_common_startstation = df['Start Station'].mode()[0]
    print('Most Common Start Station:', most_common_startstation)

    # TO DO: display most commonly used end station
    most_common_endstation = df['End Station'].mode()[0]
    print('Most Common End Station:', most_common_endstation)

    # TO DO: display most frequent combination of start station and end station trip
    df['start_end_stations'] = df['Start Station'] + "-" + df['End Station']
    most_frequent_combination = df['start_end_stations'].mode()[0]
    print('Most frequent combination of start station and end station trip:', most_frequent_combination)
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # TO DO: display total travel time
    total_travel_time= df['Trip Duration'].sum()
    print('Total Travel Time:', total_travel_time)

    # TO DO: display mean travel time
    average_travel_time= df['Trip Duration'].mean()
    print('Average Travel Time:', average_travel_time)


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_stats(df, city):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # TO DO: Display counts of user types
    user_types = df['User Type'].value_counts()
    print('Counts of user types:', user_types)


    # TO DO: Display counts of gender
    if city == 'new york city' or city == 'chicago':
        gender_types = df['Gender'].value_counts()
        print('Counts of gender types:', gender_types)
    else:
        print('Gender data not present')


    # TO DO: Display earliest, most recent, and most common year of birth

    if city == 'new york city' or city == 'chicago':
        earliest_birthyear = df['Birth Year'].min()
        recent_birthyear = df['Birth Year'].max()
        common_birthyear = df['Birth Year'].mode()
        print('Earliest birth year:', earliest_birthyear)
        print('Most recent birth year:', recent_birthyear)
        print('Most common birth year:', common_birthyear)
    else:
        print('Birth year data not present')

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)

def display_data(df):
    i = 0
    response = input("Do you want to see raw data?. Answer in Yes/No").lower()
    while response == "yes":
        print(df.iloc[i: i + 5])
        i += 5
        response = input("Do you want to see raw data?. Answer in Yes/No").lower()
        if response == "no":
            print("No rows will be displayed.")
            break

def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)

        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df, city)
        display_data(df)

        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break


if __name__ == "__main__":
	main()
