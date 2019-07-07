import os
# the module for reading csv file
import csv
# this line will help us to set the csv file path
csvpath= os.path.join('..','Resources','budget_data.csv')
output_file = os.path.join('..','Resources','Financial_Analysis.txt')
#initialize the variable
Total_Months=[]
Total_Revenue=[]
Monthly_Amount_Change=[]
max_increase_Amount=0
max_decrease_Amount=0
max_decrease_month=0
max_increase_month=0
with open(csvpath,newline='') as csvfile:
   csvreader= csv.reader(csvfile, delimiter=',')
   next(csvreader)
   # set the date counter to zero value
  # loop through to csv file to find the date number and net total amount
   for row in  csvreader:
      
      Total_Months.append(row[0])
      Total_Revenue.append(int(row[1]))
      
   print(f"Total Months: {len(Total_Months)}")
   print(f"Total Revenue :${sum(Total_Revenue)}")
   # loop through to get the Amount
   for i in range(len(Total_Revenue)-1):
     Monthly_Amount_Change.append(Total_Revenue[i+1]-Total_Revenue[i])
         
   print(f" The Average Change: {round(sum(Monthly_Amount_Change)/len(Monthly_Amount_Change),2)}")
   
      #look for higher and lower Monthly Amount Change
   max_increase_Amount= max(Monthly_Amount_Change)   

   max_decrease_Amount= min(Monthly_Amount_Change)
   #
   max__decrease_month=Monthly_Amount_Change.index(max(Monthly_Amount_Change))
   max_increase_month= Monthly_Amount_Change.index(max(Monthly_Amount_Change))
   print(f" Greatest Increase in Profits:{Total_Months[max_increase_month]} (${(str(max_increase_Amount))})")
   print(f" Greatest Decrease in Profits: {Total_Months[max_decrease_month]} (${(str(max_decrease_Amount))})")
   
       
   # Output files
  
   
with open(output_file,"w") as file:
  # csvwriter = csv.writer(file, delimiter=',')
   # Write methods to print to Financial_Analysis_Summary 
       file.write("Financial Analysis")
       file.write("\n")
       file.write("----------------------------")
       file.write("\n")
       file.write(f"Total Months: {len(Total_Months)}")
       file.write("\n")
       file.write(f"Total: ${sum(Total_Revenue)}")
       file.write("\n")
       file.write(f"Average Change: {round(sum(Monthly_Amount_Change)/len(Monthly_Amount_Change),2)}")
       file.write("\n")
       file.write(f"Greatest Increase in Profits: {Total_Months[max_increase_month]} (${(str(max_increase_Amount))})")
       file.write("\n")
       file.write(f"Greatest Decrease in Profits: {Total_Months[max_decrease_month]} (${(str(max_decrease_Amount))})")
