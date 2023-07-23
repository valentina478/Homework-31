import gspread
from oauth2client.service_account import ServiceAccountCredentials
import matplotlib.pyplot as plt
 
scope = ['https://www.googleapis.com/auth/spreadsheets', 'https://www.googleapis.com/auth/drive']
creds = ServiceAccountCredentials.from_json_keyfile_name('creds.json', scope)
client = gspread.authorize(creds)
 
data = client.open_by_key('1Bc82ddka4pFeDx4y700q3bVtQ7Ffx_brf54_MiKmLUI')

data.add_worksheet('Homework 31', rows=10, cols=10)
data_my_sheet = data.worksheet('Homework 31')
data_my_sheet.update('A1:C1', [['Місяці', 'Години навчання', 'Години хобі']])
data_my_sheet.update('A2:A7', [['Лютий'], ['Березень'], ['Квітень'], ['Травень'], ['Червень'], ['Липень']])
data_my_sheet.update('B2:B7', [[14], [16.5], [14], [16], [5], [6]])
data_my_sheet.update('C2:C7', [[17], [18], [20], [19], [16], [14]])

Months = []
Study = []
Hobby = []
for el in data_my_sheet.get_values('A2:A7'):
    for e in el:
        Months.append(e)
for el in data_my_sheet.get_values('B2:B7'):
    for e in el:
        Study.append(e)
for el in data_my_sheet.get_values('C2:C7'):
    for e in el:
        Hobby.append(e)

x_indexes = range(len(Months))
hobby_shift = [x + 0.4 for x in x_indexes]

plt.bar(x_indexes, Study, width=0.4, align='center', label='Study')
plt.bar(hobby_shift, Hobby, width=0.4, align='center', label='Hobby')

plt.xlabel('Місяці')
plt.ylabel('Години')
plt.title('Години, витрачені на навчання та хобі кожного місяца')
plt.xticks(x_indexes, Months)
plt.legend()

plt.show()