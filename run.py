# Import dependencies
import gspread
from google.oauth2.service_account import Credentials

SCOPE = [
    "https://www.googleapis.com/auth/spreadsheets",
    "https://www.googleapis.com/auth/drive.file",
    "https://www.googleapis.com/auth/drive"
    ]

CREDS = Credentials.from_service_account_file('creds.json')
SCOPED_CREDS = CREDS.with_scopes(SCOPE)
GSPREAD_CLIENT = gspread.authorize(SCOPED_CREDS)
SHEET = GSPREAD_CLIENT.open('immigration_projections_into_the_us')


def get_processed_immigrants_abroad_data():
    """
    Collect processed_immigrants_abroad figures from the user
    """
    print("Please enter processed_immigrants_abroad data from the last year")
    print("Data should be six numbers separated by commas")
    print("Example: 40,60,80")

    data_str = input("Enter your data here: ")
    print(f"The data provided is {data_str}")


get_processed_immigrants_abroad_data()
# You can delete these comments, but do not change the name of this file
# Write your code to expect a terminal of 80 characters wide and 24 rows high
