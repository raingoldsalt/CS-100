# DATA INDEX VALUES
# Use to access certain data fields in the list
GAME_TITLE = 0
PUBLISHER = 1
REVIEW_SCORE = 2
USED_PRICE = 3
CONSOLE_NAME = 4
ESRB_RATING = 5
RELEASE_YEAR = 6


# return game data as a list of records
# where each record is a list of string fields
def get_data():
    data_records = []
    game_data = open('video_games.tsv', 'r')
    
    # dispose of TSV header
    game_data.readline()
        
    # collect all records
    for line in game_data:
        allFields = line.split('\t')   # separated by tabs
        allFields[-1] = allFields[-1].replace("\n","") # get rid of newline
        data_records.append(allFields) # each record contains list of all fields
    
    game_data.close()
    return data_records


# return the average price of a Nintendo game
def avg_nintendo_game_price():
    count = 0          # count of games
    running_total = 0  # running total of prices used to calculate average

    # Go through each record from the file.
    # Each record is a list of fields.
    for record in get_data():

        # Use the PUBLISHER index to get the name of the publisher
        if record[PUBLISHER] == 'Nintendo':
            # Use the USED_PRICE index to get the used cost of the game
            running_total += float(record[USED_PRICE])
            count += 1
    
    # Use the count and the sum of all prices to compute an average
    # Then, round to nearest 2 decimal places
    avg = running_total / count
    return round(avg, 2)

def num_titles_released_by(publisher):
    count = 0
    for record in get_data():
        if record[PUBLISHER] == publisher:
            count+=1
    return count, publisher

def highest_used_price():
    maximum = float('-inf')
    for record in get_data():
        used_price = float(record[USED_PRICE])
        if(used_price > maximum):
            maximum = used_price
    return maximum
            
def release_year(year):
    count = 0
    for record in get_data():
        if(record[RELEASE_YEAR] == year):
            count+=1
    return count

# TODO: Define your functions here (all function definitions MUST
#    return data and NOT use the print function)


# TODO: Call the functions you defined here and print the data they return neatly
# For example, this prints the result of the function call to find the average nintendo price
print("Average price of Nintendo Games: ${0}".format(avg_nintendo_game_price()) )

# How many game titles were released by a certain publisher?
count, publisher = num_titles_released_by('Nintendo')
print("{} produced {} games.".format(publisher, count))
print(release_year('2004'))
print(highest_used_price())
