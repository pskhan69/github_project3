import time
import pandas as pd
import numpy as np

# Define needed data here

CITY_DATA = { 'chicago': 'chicago.csv',
              'new york city': 'new_york_city.csv',
              'washington': 'washington.csv' }

CITIES = ['chicago','new york city','washington']

MONTHS = ['january', 'february', 'march', 'april', 'may', 'june']

DAYS = ['sunday', 'monday', 'tuesday', 'wednesday','thursday', 'friday', 'saturday' ]

# Now get the filters by this function

def get_filters():
    """
    Asks user to specify a city, month, and day to analyze.

    Returns:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    """
    print('Hello! Let\'s explore some US bikeshare data!')
   
    # get user input for city (chicago, new york city, washington). HINT: Use a while loop to handle invalid inputs
    while True:
           city = input('Which city do you want to explore Chicago, New York City or Washington? \n> ').lower() 
           if city in CITIES:
              break
    
    # get user input for month (all, january, february, ... , june)
    month = get_user_input('All right! now it\'s time to provide us a month name '\
            'or just say \'all\' to apply no month filter. \n(e.g. all, january, february, march, april, may, june) \n> ', MONTHS)

    # get user input for day of week (all, monday, tuesday, ... sunday)
    day = get_user_input('One last thing. Could you type one of the week day you want to analyze?'\
                        ' You can type \'all\' again to apply no day filter. \n(e.g. all, monday, tuesday, ... sunday) \n> ', DAYS)

    print('-'*40)

    # return values city,month,day
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
    # load data file into a dataframe
    df = pd.read_csv(CITY_DATA[city])
    #print(df) 

    # convert the Start Time column to datetime
    df['Start Time'] = pd.to_datetime(df['Start Time'])

    # extract month and day of week and hour from Start Time to create new columns
    df['month'] = df['Start Time'].dt.month
    df['day_of_week'] = df['Start Time'].dt.day_name()
    df['hour'] = df['Start Time'].dt.hour

    # filter by month if applicable
    if month != 'all':
        month =  MONTHS.index(month) + 1
        df = df[ df['month'] == month ]

    # filter by day of week if applicable
    if day != 'all':
        # filter by day of week to create the new dataframe
        df = df[ df['day_of_week'] == day.title()]

    return df

# show stat by time span
def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    # display the most common month
    most_common_month = df['month'].value_counts().idxmax()
    print("The most common month is :", most_common_month)

    # display the most common day of week
    most_common_day_of_week = df['day_of_week'].value_counts().idxmax()
    print("The most common day of week is :", most_common_day_of_week)

    # display the most common start hour
    most_common_start_hour = df['hour'].value_counts().idxmax()
    print("The most common start hour is :", most_common_start_hour)

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)

# function to show station stats
def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()
 
    # display most commonly used start station
    most_common_start_station = df['Start Station'].value_counts().idxmax()
    print("The most commonly used start station :", most_common_start_station)

    # display most commonly used end station
    most_common_end_station = df['End Station'].value_counts().idxmax()
    print("The most commonly used end station :", most_common_end_station)

    # display most frequent combination of start station and end station trip
    most_common_start_end_station = df[['Start Station', 'End Station']].mode().loc[0]
    print("The most commonly used start station and end station : {}, {}"\
            .format(most_common_start_end_station[0], most_common_start_end_station[1]))

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # display total travel time
    total_travel = df['Trip Duration'].sum()
    print("Total travel time :", total_travel)

    # display mean travel time
    mean_travel = df['Trip Duration'].mean()
    print("Mean travel time :", mean_travel)

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # Display counts of user types
    
    print("Counts of user types:\n")
    user_counts = df['User Type'].value_counts()
    
    # iteratively print out the total numbers of user types 
    
    for index, user_count in enumerate(user_counts):
        print("  {}: {}".format(user_counts.index[index], user_count))
    
    print()

    if 'Gender' in df.columns:
        user_stats_gender(df)

    if 'Birth Year' in df.columns:
        user_stats_birth(df)

def user_stats_gender(df):
        """Displays statistics of analysis based on the gender of bikeshare users."""

    # Display counts of gender
        print("Counts of gender:\n")
        gender_counts = df['Gender'].value_counts()
     
        for index,gender_count   in enumerate(gender_counts):
            print("  {}: {}".format(gender_counts.index[index], gender_count))
    
        print()

def user_stats_birth(df):
        """Displays statistics of analysis based on the birth years of bikeshare users."""
    
        print('\nCalculating User birth Stats...\n')
        start_time = time.time()
        
    # Display earliest, most recent, and most common year of birth

        birth_year = df['Birth Year']

    # the most common birth year
        most_common_year = birth_year.value_counts().idxmax()
        print("The most common birth year:", most_common_year)

    # the most recent birth year
        most_recent = birth_year.max()
        print("The most recent birth year:", most_recent)

    # the most earliest birth year
        earliest_year = birth_year.min()
        print("The most earliest birth year:", earliest_year)

       
        print("\nThis took %s seconds." % (time.time() - start_time))
        print('-'*40)


def get_user_input(message, user_list):
    
    """
    An utility function to obtain user specific input value
    Args:
        (str) message - an information message for a particular request
    Returns:
        (str) user_data - requested data from user
    """

    while True:
        user_data = input(message).lower()
        if user_data in user_list:
            break
        if user_data == 'all':
            break
    
    return user_data

def display_data(df):

    #Ask user for choice 
    view_data = input('\nWould you like to view 5 rows of individual trip data? Enter yes or no\n')

    #initialize the fields
    start_loc = 0
    choice = True

    #define do while loop
    while (choice):

        #show the 5 rows from data frame
        print(df.iloc[start_loc:start_loc + 5])
        
        #increment by 5 the start location
        start_loc += 5

        #Ask user for choice if wants to repeat the data display
        view_display = input("Do you wish to continue?: ").lower()

        #Check the choice and act accordingly (if yes show data for more 5 rows if no the break the loop)    
        if view_display == "no": 
            choice = False
            break


def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)

        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df)
        display_data(df)
         
        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break

if __name__ == "__main__":
	main()