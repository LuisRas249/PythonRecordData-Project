# COM101 CW File Luis Ras: B00790794
# Program reads in a list of records items and parses themes items into a 2d list
# From here,a menu is displayed to the user to facilitate a number of queries on the data.
# v1.0 26/10/2021
# 254 lines (Comments Included) # 12 total functions
# Import matplotlib that provides charting features which will be used for option 6 to display a bar chart that presents the number of titles existing in each genre type
import matplotlib.pyplot as plt
options=True
# Set Record Data list
record_data_list = []
while options:
    print("""
               ********** Vinyl Record Inventory Program **********
               Basic Features:
               1: Output record titles and information, Summary report on (a)Total Number of Titles and (b)Value of records in stock.
               2: Output a list of record titles and their respective details which are above a user provided price threshold.
               3: Feature 3: Output a report giving a number of records existing in each genre type.\n
               Advanced Features:
               4: Option to add a new record and present a summary report that displays: (a)the new total number of titles in stock (b)the new total value of records in stock
               5: Query if a record title is available and present option (a)increasing the stock level (b)decreasing the stock level
               6: plot a labelled bar chart that presents the number of titles existing in each genre type
               7: Quit the program.
               """)
    # User must select an option from 1-7
    # If not an error will appear in the menu
    options= input("What would you like to do? ")


# OPTION 1
    if options=='1':

        def read_file():
            # Output record titles and information, Summary report on
            # (a)Total Number of Titles and (b)Value of records in stock.
            infile = open('RECORD_DATA.txt', 'r')
            # Search through a parse in the file to the list
            for row in infile:
                start = 0  # Used to point to the current position in each line
                string_builder = []
                if not row.startswith('#'):
                    for index in range(len(row)):
                        # Go to each row and go through until we reach a comma or the end of the line
                        if row[index] == ',' or index == len(row) - 1:
                            string_builder.append(row[start:index])
                            start = index + 1
                        # Build up our list
                    record_data_list.append(string_builder)
            infile.close()

        def print_record_summary():
            # Create a variable and set the total value to 0
            total_value = 0
            print('********** RECORD DETAILS **********')
            # For each record in the list that i have created print each row and seperate them with --> for readability
            for each_record in record_data_list:
                print(each_record[0], each_record[1], each_record[2], each_record[3], each_record[4], each_record[5], each_record[6], sep='-->')
                # This will calculate the total value of the RECORD_DATA file
                total_value += float(each_record[5]) * float(each_record[6])
            print('*************************************')
                # Get the number of titles of the file by getting the length of the list
            print('The total number of titles is: ', len(record_data_list))
            print('The total value is (stock * price): £', format(total_value, '.2f'), '\n', sep='')
        read_file()
        print_record_summary()

# OPTION 2
    if options=='2':

        # 2: Output a list of record titles and their respective details
        # which are above a user provided price threshold.
        def records_titles():
            infile = open('RECORD_DATA.txt', 'r') # Read the file
            for row in infile:
                if not row.startswith('#'):
                    row = row.rstrip('\n').split(', ')
                    record_data_list.append(row)
            infile.close()
        def threshold():
            # Create a variable input
            threshold_input = float(input('What would you like the record cost threshold to be? '))
            print('********** RECORD TITLES WITH INDIVIDUAL PRICE >', threshold_input, '**********')
            # For each threshold in the list
            for each_threshold in record_data_list:
                threshold_cost = float(each_threshold[6])
                # If the threshold is above the input then print the following Artist(s) and Title(s) that are above the user input
                if threshold_cost > threshold_input:
                    print(each_threshold[0], each_threshold[1], threshold_cost, sep='-->')
            print('*************************************')
        records_titles()
        threshold()
# OPTION 3
    elif options=='3':
        # 3: Feature 3: Output a report giving a number of records existing in each genre type.
        def read_file():
            infile = open('RECORD_DATA.txt', 'r')
            for row in infile:
                if not row.startswith('#'):
                    row = row.rstrip('\n').split(', ')
                    record_data_list.append(row)
            infile.close()

        def titles_genre_type(gL):
            # Create a dictionary that gets the number of records in each genre type
            titles_genre_dict = {}
            # For each genre in the list
            for each_titles in gL:
                # If each GENRE in the dictionary then get the GENRE's in the file and count them and add 1 since it starts counting from 0
                if each_titles[2] in titles_genre_dict:
                    titles_genre_dict[each_titles[2]] = int(titles_genre_dict[each_titles[2]]) + 1
                else:
                    titles_genre_dict[each_titles[2]] = 1
            print('********** RECORD GENRE SUMMARY ************')
            # This will print the keys(GENRE) and values(STOCK) that are currently in the file
            for key, value in titles_genre_dict.items():
                print(key + '--> ', value)
            print("*************************************")
        read_file()
        titles_genre_type(record_data_list)
# OPTION 4
    elif options=='4':
        # 4: Option to add a new record and present a summary report that displays:
        # (a)the new total number of titles in stock
        # (b)the new total value of records in stock The record which you should add is one copy
        # of ‘LP Radio Silence’, by ‘Neil Cowley Trio’, at ‘£12.99’, and as a ‘Jazz Group’
        def records_titles():
            infile = open('RECORD_DATA.txt', 'r')
            for row in infile:
                if not row.startswith('#'):
                    row = row.rstrip('\n').split(', ')
                    record_data_list.append(row)
            infile.close()
        def report_input():
            artist_details = str(input('Enter artist name: '))
            record_title = str(input('Enter record title: '))
            artist_format = str(input('Enter format (Rock, Classical, Pop, Jazz): '))
            record_playlength = input('Enter condition (LP, EP, 45, 78): ')
            record_condition = str(input('Enter condition (As New, Very Good, Acceptable): '))
            record_stock = input('Enter initial stock level: ')
            record_cost = input('Enter cost per record: ')
            # Open the file and add to the data by appending 'a'
            # And in the file it will write the following input the user has entered
            infile = open('RECORD_DATA.txt', 'a')
            infile.write("\n"+ artist_details +', '+ record_title +', '+ artist_format +', '+ record_playlength +', '+ record_condition +', '+ record_stock +', '+ record_cost)
            infile.close()
            print('Record Data Added!')

            total_value = 0 # set the total value to 0
            new_value = 0 # set the new value to 0
            total_value += float(record_stock) * float(record_cost) # This adds two values together and assigns the final value to a variable
            print('********** Summary Report **********')
            for each_summary in record_data_list:
                new_value += float(each_summary[5]) * float(each_summary[6]) # This adds two values together and assigns the final value to a variable this will calculate the new amount of records and new total value
            print('New total record now stands at: ', len(record_data_list)+ 1)
            print('The total value now changed by (record stock * price): £', format(total_value, '.2f'), sep='')
            print('The new total stock value is now (total stocks * total price): £', format(new_value + total_value, '.2f'), sep='')
            print('*************************************')
        records_titles()
        report_input()
# OPTION 5
    elif options=='5':
        def read_file():
            infile = open('RECORD_DATA.txt')
            for row in infile:
                if not row.startswith('#'):
                    row = row.rstrip('\n').split(', ')
                    record_data_list.append(row)
            infile.close()
        # 5: Query if a record title is available and present option
        # (a)an increasing stock level
        # (b)decreasing the stock level,
        # due to a sale If the stock level is decreased to zero
        # indicate to the user that the record is currently out of stock.'
        infile = open("RECORD_DATA.txt", "r")  # opens the file and make it readable
        record = input("Enter record you wish to search: ")  # gets the input from the user
        found = False  # stores whether the record is found in the file, set to False at the beginning
        for line in infile:  # reads each line in the file
            each_record = line.split(",")  # splits the line into the record data list
            if each_record[0] == record:  # checks if  entered is in element 0 of the list
                # If it is it prints the record that has been found
                print('Record found', each_record[0], each_record[1], sep='-->')
                # After the record that has been searched is found give the user an input that allows them to either choose a or b
                stock_level = input('Do you wish to (a) increase or (b) decrease its stock level? ')
                write_file = open('RECORD_DATA.txt', 'a')
                # If the user enters 'b' create an int input to allow the user to enter the amount they wish to put in a certain record
                if stock_level == 'a':
                    # This will help check if the user has enter a whole number
                    # Will display an error if the user enters anything other than a whole number
                    while True:
                        try:
                            increase_stock_a = int(input('Increase the stock by how many? '))
                            # Once the user enters the amount it will then add the current stock of the record and the user input
                            increase_stock = int(each_record[5]) + int(increase_stock_a)
                            print('New stock record is now ', increase_stock)  # print the calculation of the new record stock
                        except ValueError:
                            print('Please enter a whole number')
                        write_file.close()
                # If the user enters 'b' create an int input to allow the user to enter the amount they wish to put in a certain record
                if stock_level == 'b':
                    while True:
                        try:
                            decrease_stock_b = int(input('Decrease the stock by how many? '))
                            # Once the user enters the amount it will then subtract the current stock of the record and the user input
                            decrease_stock = int(each_record[5]) - int(decrease_stock_b)
                            print('New stock record is now ', decrease_stock)# print the calculation of the new record stock
                            if decrease_stock < 1:
                                print('This is now currently out of stock...')
                        except ValueError:
                            print('Please enter a whole number')
                            # If the following record has 0 stocks left print this below
                write_file.close()
                # sets found to True as a match is found
                found = True
        if found == False:  # after the loops checks if found if still False
            # displays a message if it is
            print("Record not found, please enter valid record name")
        read_file()
# OPTION 6
    elif options=='6':
        def read_file():
            infile = open('RECORD_DATA.txt')
            for row in infile:
                if not row.startswith('#'):
                    row = row.rstrip('\n').split(', ')
                    record_data_list.append(row)
            infile.close()
        def titles_genre_type(gL):
            titles_genre_dict = {} # Create a dictionary that gets the number of records in each genre type
            for each_titles in gL: # For each titles in the list
                if each_titles[2] in titles_genre_dict: # If each GENRE in the dictionary then get the GENRE's in the file and count them and add 1 since it starts from 0
                    titles_genre_dict[each_titles[2]] = int(titles_genre_dict[each_titles[2]]) + 1
                else:
                    titles_genre_dict[each_titles[2]] = 1
            print('********** RECORD GENRE SUMMARY ************')
            for key, value in titles_genre_dict.items():
                print(key + '--> ', value) # This will print the keys(GENRE) and values(STOCK) that are currently in the file
            print("*************************************")
        def plot_record_summary():
            genres =['Rock', 'Classical', 'Pop', 'Jazz', 'Spoken Word'] # Create a list of the current genres and their stock details
            stock_details =[2, 5, 3, 3, 1]

            plt.bar(genres, stock_details) # Create a bar chart for the genres and their stock details
            plt.title('Record Genre') # Bar chart title
            plt.xlabel('Genres') # x axis label/title
            plt.ylabel('Stock') # y axis label/title
            plt.show() # This will show the bar chart
        read_file()
        titles_genre_type(record_data_list)
        plot_record_summary()

# OPTION 7
    #This option will close the program for the user if 7 is entered
    elif options=='7':
        print("\n Goodbye, Program Closing...")
        quit() # Quits/Closes the program
# Any other input such as more than 7 or a string will display an error message and will open the menu again for the user
    elif options> '7':
        print('Invalid input, please enter options between 1 to 7')
else:
    print('Error, Program will close')
