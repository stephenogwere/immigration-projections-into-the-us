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
    Collect processed_immigrants_abroad figures from the user.
    Run a while loop to get valid string of data from the user that must be a string
    of six numbers separated by commas. The loop will repeatedly request for data input
    until, valid data is provided by user.
    """

    while True:
        print("Please enter processed_immigrants_abroad data from the last year")
        print("Data should be six numbers separated by commas")
        print("Example: 20,30,40,50,60\n")
        
        data_str = input("Enter your data here: ")
        
        processed_immigrants_abroad_data = data_str.split(",")
        
        if validate_data(processed_immigrants_abroad_data):
            print("Data is valid!")
            break

    return processed_immigrants_abroad_data
    



def validate_data(values):
    """
    Inside the try, converts all string values into integers.
    Raises ValueError if strings can't be converted to integers
    or if there aren't excactly six values.
    """
    try:
        [int(value) for value in values]
        if len(values) != 6:
            raise ValueError(
                f"Exactly 6 values required, you provided {len(values)}"
            )
    except ValueError as e:
        print(f"Invalid data: {e}, please try again.\n")
        return False


    return True


def update_processed_immigrants_abroad_worksheet(data):
    """
    Update processed_immigrants_abroad worksheet, add new row with the list data provided.
    """
    print("Updating processed_immigrants_abroad worksheet...\n ")
    processed_immigrants_abroad_worksheet = SHEET.worksheet("processed_immigrants_abroad")
    processed_immigrants_abroad_worksheet.append_row(data)
    print("Processed immigrants abroad worksheet updated successfully.\n")


data = get_processed_immigrants_abroad_data()
processed_immigrants_abroad_data = [int(num)  for num in data]
update_processed_immigrants_abroad_worksheet(processed_immigrants_abroad_data)



# You can delete these comments, but do not change the name of this file
# Write your code to expect a terminal of 80 characters wide and 24 rows high
