

import csv

def read_row(y):
    with open('In.csv', 'rU') as f:
        reader = csv.reader(f)
        y_count = 0
        for n in reader:
            if y_count == y:
                cell = n
                return cell
            y_count += 1
 
data = read_row(1)  
            
aa,ab,ac,ad,ae,af,ag,ah,ai,aj,ak,al,am,an,ao,ap,aq,ar,ba,bb,bc,bd,be,bf,bg,bh,bi = data
data.remove(aa)
data.remove(ab)
data.remove(ac)

print data    
     
#Figuring out how to write the data, but currently incomplete

with open('out.csv','wb') as dataout:
	writer = csv.writer(dataout)
	writer.writerows(data)
	
#Now I want a way of searching for the appropriate rows to pull the data from, because they vary
#Search terms of 'WPS.KEWAUKEWA' Want to check the first column (column 0 for 'WPS.KEWAUKEWA')

import csv 

with open('FILENAMEHERE.csv',rU) as g:
	reader=csv.reader(g)
	for row in reader:
		if row[1] == 'WPS.KEWAUKEWA'
			return row

# method read 1 row of MISO Wide hourly data
# def read_miso_wide_hourly_data
#     load_csv_row
#     hourly_data = csv_row[3:26]
#     return hourly_data


# def convert_daily_to_yearly(daily_data)
#     for each date in daily_data
#         for each hour daily_data[date]
#             yearhour = date * 100 + hour
#             year_data[yearhour] = daily_data[date][hour]

# open file
# skip first row
# skip second row
# read date from third row
#      load_csv_row
#      date = csv_row[0]
#      convert date format (e.g. MM/DD/YYYY => YYYYMMDD)
# skip rows 4,5
# miso_wide[date] = read_miso_wide_hourly_data

# when done, we have a data structure as follows:
#
# miso_wide[date] = array of 24 MCP values.
#

#
