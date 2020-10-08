# pandas pip install pandas
# numpy pip install numpy
# xlrd pip install xlrd
# openpyxl pip install openpyxl

import numpy as np
import pandas as pd

# read data from file
# if want to read excel file then change it to pd.read_excel()
all_data = pd.read_csv("test_data.csv")  # read only csv file

# make dataframe
all_data_df = pd.DataFrame(all_data)

# get first_name column data

first_name = all_data_df["first_name"]
first_name = first_name.str.lower()  # converts all data to lowercase
# get last_name column data

last_name = all_data_df["last_name"]
last_name = last_name.str.lower()  # converts all data to lowercase

# Generate random number

random_number = np.random.randint(2999, 9999, size=first_name.size)
random_number_df = pd.DataFrame(random_number, columns=["random_numbers"])

numbers = random_number_df["random_numbers"]

# combine first_name and last_name

# combined_name = first_name + "." + last_name + numbers
# filtered_data_frame = pd.DataFrame(combined_name, columns=["Name"])
filtered_data_frame = pd.concat([first_name, last_name, numbers], axis=1)

filtered_data_frame = filtered_data_frame.assign(combined_value=filtered_data_frame.first_name.astype(
    str) + "." + filtered_data_frame.last_name.astype(str) + filtered_data_frame.random_numbers.astype(str)

                                                 )

final_data = filtered_data_frame["combined_value"]

final_data_frame = pd.DataFrame(final_data)

final_data = pd.concat([final_data_frame, all_data_df], axis=1, ignore_index=True)

final_data.to_excel("output_names.xlsx",
                    sheet_name='Person`s Name', index=False)
