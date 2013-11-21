

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
	
	