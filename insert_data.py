import gspread 
import scraping

# Access service account using json credentials on %AppData%\Roaming\gspread\service_account.json
sa = gspread.service_account()

# Open spreadsheet and get worksheet
sh = sa.open('NFTmarketing')

wks = sh.worksheet('Growth')

# Get number of columns in the worksheet
columnCount = wks.col_count

ann, en, pt, es, vt, disc, twit, insta, (likes, followers), price, hold, vol, btc, game, legH, t1, t2, t3, t4, t5, t6, seatH = scraping.main()

wks.add_cols(1)
# Insert a new column at the end of the worksheet with data
wks.insert_cols([['Saturday 13', ann, en, pt , es, vt, (int(en) + int(pt) + int(es) + int(vt)), disc, twit, insta, likes, followers, price, hold, vol, btc, game, '-', legH, '-', '-', t1, '0', t2, '0', t3, '0', t4, '0', t5, '0', t6, '0', seatH, '0']], columnCount+1)
