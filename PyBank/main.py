import os
import csv

DateCounter =0
NetTotal = 0
Averagechange = 0.0
GreatestIncProfit = 0
GreatestDecProfit = 0
Change = []
Diff = 0
PreviousRowamt = 0


csvpath = os.path.join('Resources','budget_data.csv')



with open(csvpath) as csvfile:

    csvreader =csv.reader(csvfile,delimiter=',')

    csv_header = next(csvreader)
    #print(f"CSV  Header : {csv_header}")

    for row in csvreader:
        DateCounter =DateCounter + 1
        NetTotal = NetTotal + int(row[1])
        if PreviousRowamt != 0:
            Diff = int(PreviousRowamt) - int(row[1])
        Change.append(Diff)
        PreviousRowamt = row[1]
        if int(row[1])  > int(GreatestIncProfit) :
            GreatestIncProfit = row[1]
            GreatestIncProfitDt = row[0]
        if int(row[1]) < int(GreatestDecProfit) :
            GreatestDecProfit = row[1]
            GreatestDecProfitDt = row[0]
        
    
    AverageChange = round(sum(Change)/85)
    
    


    print(f'Financial Analysis')
    print("----------------------------")
    print(f'Total Months: {DateCounter}')
    print(f'Total: ${NetTotal}')
    print(f'Average change: {AverageChange}')
    print(f'Greatest Increase in Profits : {GreatestIncProfitDt} ({GreatestIncProfit})')
    print(f'Greatest Decrease in Profits : {GreatestDecProfitDt} ({GreatestDecProfit})')

output_file = os.path.join("output.txt")

with open(output_file, "w") as datafile:
    writer = csv.writer(datafile)
    writer.writerow(["Financial Analysis"])
    writer.writerow(["--------------------------"])
    writer.writerow(['Total Months:  ' +str(DateCounter)]) 
    writer.writerow(['Total: $' +str (NetTotal)])   
    writer.writerow(['Average change: '+str(AverageChange)])
    writer.writerow(['Greatest Increase in Profits : '+str(GreatestIncProfitDt)  +'   ('+ str(GreatestIncProfit) +')'])
    writer.writerow(['Greatest Decrease in Profits : '+str(GreatestDecProfitDt)  +'   ('+str(GreatestDecProfit) +')'])
