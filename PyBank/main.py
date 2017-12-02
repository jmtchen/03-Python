import os
import csv

budget1 = os.path.join("raw_data","budget_data_1.csv")
budget2 = os.path.join("raw_data","budget_data_2.csv")
countmonth1 = []
countmonth2 = []
revenue1 = 0
revenue2 = 0
maxrevenue1 = 0
maxrevenue2 = 0
minrevenue1 = 0
minrevenue2 = 0
maxmonth1 = 0
maxmonth2 = 0
minmonth1 = 0
minmonth2 = 0

with open(budget1, newline="") as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")
    next(csvfile)
    
    for row in csvreader:
        countmonth1.append(row[0])
        revenue1 = int(revenue1) + int(row[1])
        
        if maxrevenue1 > int(row[1]):
            maxrevenue1
            maxmonth1
        
        else:
            maxrevenue1 = int(row[1])
            maxmonth1 = row[0]
        
        if minrevenue1 < int(row[1]):
            minrevenue1
            minmonth1
        
        else:
            minrevenue1 = int(row[1])
            minmonth1 = row[0]

    avg1 = revenue1 / int(len(countmonth1))
        
with open(budget2, newline="") as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")
    next(csvfile)
    
    for row in csvreader:
        countmonth2.append(row[0])
        revenue2 = int(revenue2) + int(row[1])
        
        if maxrevenue2 > int(row[1]):
            maxrevenue2
            maxmonth2
        
        else:
            maxrevenue2 = int(row[1])
            maxmonth2 = row[0]
        
        if minrevenue2 < int(row[1]):
            minrevenue2
            minmonth2
        
        else:
            minrevenue2 = int(row[1])
            minmonth2 = row[0]

    avg2 = revenue2 / int(len(countmonth1))

# Print analysis on terminal for file 1
print("Financial Analysis for File 1")
print("-----------------------------------------------")        
print("Total Months: " + str(len(countmonth1)))
print("Total Revenue: " + str(revenue1))
print("Average Revenue Change: " + str(avg1))
print("Greatest Increase in Revenue: " + str(maxrevenue1) + " ($" + str(maxmonth1) + ")")
print("Greatest Decrease in Revenue: " + str(minrevenue1) + " ($"  + str(minmonth1) + ")")

# Print analysis on terminal for file 2
print("")
print("Financial Analysis for File 2")
print("-----------------------------------------------")        
print("Total Months: "  + str(len(countmonth2)))
print("Total Revenue: "  + str(revenue2))
print("Average Revenue Change: " + str(avg2))
print("Greatest Increase in Revenue: " + str(maxrevenue2) + " ($" + str(maxmonth2) + ")")
print("Greatest Decrease in Revenue: " + str(minrevenue2) + " ($"  + str(minmonth2) + ")")

# Save output as text file
with open('output.txt','w', newline = '') as outputfile:
    print("Financial Analysis for File 1", file = outputfile)
    print("-----------------------------------------------", file = outputfile)        
    print("Total Months: "  + str(len(countmonth1)), file = outputfile)
    print("Total Revenue: "  + str(revenue1), file = outputfile)
    print("Average Revenue Change: " + str(avg1), file = outputfile)
    print("Greatest Increase in Revenue: " + str(maxrevenue1) + " ($"  + str(maxmonth1) + ")", file = outputfile)
    print("Greatest Decrease in Revenue: " + str(minrevenue1) + " ($"  + str(minmonth1) + ")", file = outputfile)
    print("", file = outputfile)
    print("Financial Analysis for File 2", file = outputfile)
    print("-----------------------------------------------", file = outputfile)      
    print("Total Months: "   + str(len(countmonth2)), file = outputfile)
    print("Total Revenue: " + str(revenue2), file = outputfile)
    print("Average Revenue Change: " + str(avg2), file = outputfile)
    print("Greatest Increase in Revenue: " + str(maxrevenue2) + " ($"  + str(maxmonth2) + ")", file = outputfile)
    print("Greatest Decrease in Revenue: " + str(minrevenue2) + " ($"  + str(minmonth2) + ")", file = outputfile) 