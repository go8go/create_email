import time

import pandas as pd
from selenium import webdriver

default_password = "T1002001"
total_complete = 0
completed_username = []
retry = False

read_dataFile = pd.read_excel("output_names.xlsx")
# change to dataFrame
df = pd.DataFrame(read_dataFile)

for i in range(0, len(df)):
    username = (df.iloc[i][0])
    first_name = (df.iloc[i][1])
    last_name = (df.iloc[i][2])

    try:
        # url of outlook
        url = 'https://outlook.live.com'
        driver = webdriver.Chrome("/home/shawan/Script/chromedriver")
        driver.get(url)

        # get Create free account button and click it
        driver.find_element_by_link_text("Create free account").click()
        time.sleep(2)
        try:
            # username field
            driver.find_element_by_id("MemberName").send_keys(username)
            time.sleep(1)

            driver.find_element_by_id("iSignupAction").click()
        except AttributeError:
            print(AttributeError)

        time.sleep(2)
        # password field
        driver.find_element_by_id("PasswordInput").send_keys(
            default_password)
        time.sleep(1)

        driver.find_element_by_id("iSignupAction").click()
        time.sleep(2)

        # FirstName field
        driver.find_element_by_id("FirstName").send_keys(first_name)
        # Lastname field
        driver.find_element_by_id("LastName").send_keys(last_name)
        time.sleep(1)

        driver.find_element_by_id("iSignupAction").click()
        time.sleep(2)

        # country select field
        driver.find_element_by_id("Country").send_keys('United States')
        # Birthdate
        # Month
        driver.find_element_by_id("BirthMonth").send_keys("May")
        driver.find_element_by_id("BirthDay").send_keys("15")
        driver.find_element_by_id("BirthYear").send_keys("1988")
        driver.find_element_by_id("iSignupAction").click()
        time.sleep(5)

        total_complete += 1
        com_username = username + "@outlook.com"
        completed_username.append(com_username)

        driver.find_element_by_id("idBtn_Back").click()
        time.sleep(2)
        driver.close()
        time.sleep(4)
    except:
        print("Username already exist")
        driver.close()

print(f'Summery: Total username: {len(df)} & Completed: {total_complete}')
username_df = pd.DataFrame(completed_username)
username_df.to_csv("Completed Account.csv", index=False)
print("All done. Programme Terminated")
