import zipfile
import glob, os, os.path
import MySQLdb
import csv
import datetime
import time
import sys


#find zip file
os.chdir('C:\myproject\API')
filename = glob.glob("*.zip")
new = str(filename).strip("'[]'")
##unzip
path = 'C:\myproject\API\\' + new
zip_ref = zipfile.ZipFile(path, 'r')
zip_ref.extractall('C:\myproject\API')
zip_ref.close()
print new + ' is unzipped'

#os.remove(path)

#uplaod files to DB & delete files
##1st name & path (intensities)
filename = glob.glob(r'C:\myproject\API\*.csv')
new1 = str(filename[0]).strip("''") #no quotation marks
new2 = os.path.splitext(os.path.basename(new1))[0]
print new1
print new2
path = 'C:\\myproject\\API\\minuteIntensitiesNarrow_merged.csv'
query = "LOAD DATA LOCAL INFILE {0} INTO TABLE intens FIELDS TERMINATED BY ',' IGNORE 1 LINES (ID, @timevar, intensity) \
         set in_time = STR_TO_DATE(@timevar, '%m/%d/%Y %r'), record_ID = LAST_INSERT_ID()".format(path,)
print query

                   
def insert_intens():
    conn = MySQLdb.connect (user="root", host="localhost", db="fitabase")
    cursor = conn.cursor()
    try:
        new2 = os.path.splitext(os.path.basename(new1))[0]
        path = new1
    
        if new2:
            cursor.execute("INSERT INTO history (name) VALUES (%s)", {new2})
            cursor.execute(query)
            conn.commit()
            return "Done"
        else:
            return "Nothing"
    except:
        print("Unexpected error:", sys.exc_info()[0])
        raise

def main():
   insert_intens()
 
if __name__ == '__main__':
    main()
    

##os.remove(path1)
##time.sleep(10)

####2nd (sleep)
#os.chdir('C:\myproject\API')
##filename = glob.glob('*.csv')
##new1 = str(filename[0]).strip("''") #no quotation marks
##path1 =  'C:\myproject\API\\' + new1 #no quotation marks
##path2 = '"'+path1+'"' #with quotation marks
##print path1
##print path2
##
##def insert_intens():
##    conn = MySQLdb.connect (user="root", host="localhost", db="fitabase")
##    cursor = conn.cursor()
##    try:
##        new2 = os.path.splitext(os.path.basename(path2))[0]
##        path = path1
##        if new2:
##            cursor.execute("INSERT INTO history (name) VALUES (%s)", {new2})
##            cursor.execute('LOAD DATA INFILE %s INTO TABLE intens IGNORE 1 LINES (ID, in_time, intensity) set record_ID = LAST_INSERT_ID()', (path,))
##            conn.commit()
##            return "Done"
##        else:
##            return "Nothing"
##    except:
##        print("Unexpected error:", sys.exc_info()[0])
##        raise
##
##def main():
##   insert_intens()
## 
##if __name__ == '__main__':
##    main()
##    
##         
##os.remove(path1)
##time.sleep(10)
##
####3rd (step)
##os.chdir('C:\myproject\API')
##filename = glob.glob('*.csv')
##new1 = str(filename[0]).strip("''")
##path1 =  'C:\myproject\API\\' + new1
##print path1
##book = csv.reader(file(path1))
##sheet = book.sheet_by_index(0)
##for r in range(1, book.nrows): #1 stands for the 2nd row
##         ID            = sheet.cell(r,0).value
##         st_time       = sheet.cell(r,1).value
##         step          = sheet.cell(r,2).value
##         cursor.execute('INSERT INTO history VALUES (new1)')
##         cursor.execute('INSERT INTO intens (ID, st_time, step) VALUES (%s, %s, %s)',
##                        (ID, st_time, step))
##os.remove(path1)
##
##
##cursor.close()
##database.commit()
##database.close()
##
##print "Done!"
##
##
