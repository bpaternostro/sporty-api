import json
import gspread
import time


# from gspread_dataframe import set_with_dataframe
class Util:
    def __init__(self, google_file):
        self.gc = gspread.service_account(
            filename="/home/bruno/repob/sporty-api/brunopage-992-9768668e5eec.json"
        )
        self.sh = self.gc.open_by_key(google_file)

    def send_to_google_sheet(self, range, values):
        self.sh.sheet1.update(range, [values])

    # verifico si es divisible por 60
    def avoid_over_quota(self, counter):
        if counter % 60 == 0:
            time.sleep(65)

    # def export_to_excel(self, df, sheet):
    #    worksheet = self.sh.get_worksheet(sheet)
    #    set_with_dataframe(worksheet, df)

    def get_data_from_sheet(self, sheet):
        worksheet = self.sh.worksheet(sheet)
        return worksheet.get_all_records()
