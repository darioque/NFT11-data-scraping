import gspread 

# Access service account using json credentials on %AppData%\Roaming\gspread\service_account.json
sa = gspread.service_account()

# Open spreadsheet and get worksheet
sh = sa.open('NFTmarketing')

wks = sh.worksheet('Growth')

# Get number of columns in the worksheet
columnCount = wks.col_count

# Insert a new column at the end of the worksheet with data
wks.insert_cols([['test', 'test2']], columnCount)