import pandas

import num2words
df = pandas.read_csv(filepath_or_buffer="all_seasons.csv")


user = input("What is your name: ")
print("Hi " + user + "!")

ages = list(df["age"])
value = input("Enter age of player in question: ")
value = float(value)
limit = input("Enter the threshold number we want to use to compare the frequency of occurrence: ")
limit = float(limit)
print("We will analyze the number of " + str(int(value)) + " year olds using a occurrence threshold of " + str(int(limit)) + "!")

numb_of_25yearolds = ages.count(value)
print(numb_of_25yearolds)
if numb_of_25yearolds > limit:
    print("There are more than 500 players over the age of " + str(value) + " years")
elif numb_of_25yearolds < limit:
    if (value in ages):
        print("There are actually " + str(numb_of_25yearolds) + " " + str(int(value)) + "year olds in the NBA!")
    else:
        print("There are no " + str(value) + "year olds in the NBA!")















