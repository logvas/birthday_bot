import gspread
from oauth2client.service_account import ServiceAccountCredentials

scope = [ 'https://www.googleapis.com/auth/spreadsheets',
         "https://www.googleapis.com/auth/drive"]
credentials = ServiceAccountCredentials.from_json_keyfile_name('gs_credentials.json', scope)
client = gspread.authorize(credentials)

sh = gc.open_by_url(https://docs.google.com/spreadsheets/d/1vquI_TsT5Lkf0NrTcEtcEq2j2TqIv_GSOvqjPZmU5pk/edit?usp=sharing)
worksheet = sh.get_worksheet(0)    
val = worksheet.acell('B1').value


#sheet = client.create("FirstSheet")
#sheet.share('thelogvasstudio@gmail.com', perm_type='user', role='writer')

sheet = client.open("FirstSheet").sheet1

print(sheet.acell('A9').value)
print(val)
num=2
sheet.update('A'+str(num), val)

