
from csv import writer
import csv
import os

#if file exists then delete old file
if os.path.exists("version.csv"):
    os.remove("version.csv")
if os.path.exists("bad_version.csv"):
    os.remove("bad_version.csv")

#create a function to create csv file and add a good data in csv file.
def append_list_as_row(file_name, list_of_elem):
    
    if os.path.exists("version.csv") :
        
        # Open file in append mode
        with open(file_name, 'a+', newline='') as write_obj:
            # Create a writer object from csv module
            csv_writer = writer(write_obj)
            # Add contents of list as last row in the csv file
            csv_writer.writerow(list_of_elem)
    else :
    
        with open('version.csv', 'w', newline='') as f:
            # Create a writer object from csv module
            csv_writer = writer(f)
        
        with open(file_name, 'a+', newline='') as first:
            # Create a writer object from csv module
            csv_writer = writer(first)
            # Add contents of list as last row in the csv file
            csv_writer.writerow(['id','version','rateepage','mtime','minor_edit','content','versiondata'])
        
        
        with open(file_name, 'a+', newline='') as write_obj:
            # Create a writer object from csv module
            csv_writer = writer(write_obj)
            # Add contents of list as last row in the csv file
            csv_writer.writerow(list_of_elem)
        f.close()

#create a function to create csv file and add a bad data in csv file.
def append_list_as_badrow(file_name, list_of_elem):
    
    if os.path.exists("bad_version.csv") :
        
        # Open file in append mode
        with open(file_name, 'a+', newline='') as write_obj:
            # Create a writer object from csv module
            csv_writer = writer(write_obj)
            # Add contents of list as last row in the csv file
            csv_writer.writerow(list_of_elem)
    else :
    
        with open('bad_version.csv', 'w', newline='') as f:
            # Create a writer object from csv module
            csv_writer = writer(f)
        
        with open(file_name, 'a+', newline='') as first:
            # Create a writer object from csv module
            csv_writer = writer(first)
            # Add contents of list as last row in the csv file
            csv_writer.writerow(['id','version','rateepage','mtime','minor_edit','content','versiondata'])
        
        
        with open(file_name, 'a+', newline='') as write_obj:
            # Create a writer object from csv module
            csv_writer = writer(write_obj)
            # Add contents of list as last row in the csv file
            csv_writer.writerow(list_of_elem)
        f.close()
        
  
        
#get a file name for process 
name = input("Enter Process File Name: ")
if len(name) < 1:
    name = "dump.txt"
#file open and put in variable 'xopen'    
try:
	xopen=open(name)
except:
    print("Enter Valid file Name ")
    quit()

#ctreate list variable 
list = list()
print("Processing...") 
#reading a file using for loop
for line in xopen :
    	
    #put a if condition to get data from where you want.
    if line.startswith('INSERT INTO `version` VALUES ') :
    
        line=line.lstrip("INSERT INTO `version` VALUES (")
        #whatever data get using split function saperate a data and stored in list.
        line=line.split("),(")
        #print(line)
        
        #reading list variable using for loop
        for dum in line :
             
            #using split function split data
            list=dum.split(",")
           
            #print(list);
        
            #checking length of list if list have more than 7 then stored as bad records and other stored as good records 
            if len(list)>8 :
                
                #Calling function and give CSV file name and value of list to stored in CSV file.
                append_list_as_badrow('bad_version.csv',list)
            else   : 
                #Calling function and give CSV file name and value of list to stored in CSV file.
                append_list_as_row('version.csv',list)
               
print("Job Succeed!!")            

 

