# TODO: FIRST INSTALL THIS PACKAGES BEFORE RUN THIS FILE

# pandas -> pip install pandas
# numpy -> pip install numpy
# xlrd -> pip install xlrd
# openpyxl -> pip install openpyxl
# faker -> pip install Faker

import numpy as np
import pandas as pd
from faker import Faker

fake = Faker()

# how many user name you want to generate
ammount_of_names = int(input("How many names you want to generate: "))

step = 1
first_name = []
last_name = []

try:
    # generate and first name modify and store in the lists
    while step <= ammount_of_names:
        name = [str(name) for name in fake.name().split()]
        first_name.append(name[0].lower())
        last_name.append(name[1].lower())
        step = step + 1

    # change first_name and last_name to panda series
    first_name = pd.Series(first_name, name="first_name")
    last_name = pd.Series(last_name, name="last_name")

    # Generate random number
    random_number = np.random.randint(2999, 9999, size=ammount_of_names)

    # Convert random numbers to pandas series
    numbers = pd.Series(random_number, name="random_numbers")

    # combine first_name and last_name and numbers make username
    combined_value = pd.concat([first_name, last_name], axis=1)

    usernames = combined_value.assign(username=combined_value.first_name.astype(
        str) + "." + combined_value.last_name.astype(str) + numbers.astype(str)

    )

    try:
        usernames.to_excel("output_names.xlsx",
                           sheet_name='Person`s Name', index=False)

        print("Data saved to [output_names.xlsx] file successfully")
    except:
        print("Data does not save into file")
except:
    print("Something wrong!! Please try again.")
