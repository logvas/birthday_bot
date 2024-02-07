import gspread
from oauth2client.service_account import ServiceAccountCredentials

scope = [ 'https://www.googleapis.com/auth/spreadsheets',
         "https://www.googleapis.com/auth/drive"]
credentials = ServiceAccountCredentials.from_json_keyfile_name('gs_credentials.json', scope)
client = gspread.authorize(credentials)
sheet = client.open("FirstSheet").sheet1
num=4
sheet.update('B'+str(num), "2120")

