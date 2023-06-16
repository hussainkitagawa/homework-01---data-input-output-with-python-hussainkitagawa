###############

import numpy
import os   #These two are useful modules
import sys
import numpy as np #Numerical Python
import matplotlib.pyplot as plt

#Work directory
work_dir = os.getcwd()
print("Work dir %s" % work_dir)

#find main directory
main_dir =os.path.dirname(work_dir)
print("Main directory is %s" % main_dir)

#find data directory
data_dir = os.path.join(main_dir,"data")
print("data dir is %s" % data_dir)

#Create result
results_dir = os.path.join(main_dir,"results")
##if the directory does not exist, you can create it
if not os.path.exists(results_dir):
    os.mkdir(results_dir)
    print("Directory %s created !" % results_dir)


#File name in data direcory
data_filename = "catalog_exoplanets_nasa.csv"
#Read file
data_filename = open(os.path.join(data_dir,data_filename),"r")  #r means reading mode

#Readlines: a list with a line each
divine_lines = data_filename.readlines()

#count total line in file
total = len(divine_lines)
print("** Total lines in file = %d" % total)

#print the first 20 lines
#print(divine_lines[0:20])


#loop for the first 10 lines; the line number; the length of each line and the line content 
#for li in range(10):
    #print(li,len(divine_lines[li]),divine_lines[li])


#loop for the first 10 lines: create an output list with only the lines that we want
out_list=[]
#for li in range(10): #read first 10 lines
for li in range(total):# read all lines
    line = divine_lines[li].strip("\n")
    if (len(line)>0): #check if value exist
        #comments lines start with #
        if (line[0]!="#"):
          #print(line)
          out_list.append(line)

print("** File contains %d data lines" % len(out_list))

#use the first line as header containing the column names
header = out_list[0]
column_names = header.split(",")
print("** header contains %d columns" % len(column_names))
print(column_names)

#create and init a dictionary of lists:
data_dict={}
for ci in range(len(column_names)):
    data_dict[column_names[ci]]=[]


#start from index 1 (skip the first line containing the headers)
for ri in range(1,len(out_list)):
    data_line = out_list[ri].split(",")
    #print("Processing row %d" % ri)
    for ci in range(len(column_names)):
        data_dict[column_names[ci]].append(data_line[ci])

#print pl_hostname
#print(data_dict["pl_name"])   

#convert list to numpy arrays
data_dict["pl_massj"]=np.asarray(data_dict["pl_massj"])# Planet mass (Jupiter mass)
data_dict["pl_masse"]=np.asarray(data_dict["pl_masse"])# Planet mass (Earth mass)
data_dict["pl_rade"]=np.asarray(data_dict["pl_rade"])# Planet radius (Earth radius)

#scatter plot
plt.scatter(data_dict["pl_masse"],data_dict["pl_rade"],marker="o",color="red")
plt.ylabel("Planet radius [arth radius]")
plt.xlabel("Planet mass [Earth mass]")

#histograms

