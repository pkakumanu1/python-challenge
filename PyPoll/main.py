import os
import csv

VoterCount = 0
Khan = 0
Correy = 0
Li = 0
OTooley = 0
Winner = ''


csvpath = os.path.join('..','Resources','election_data.csv')



with open(csvpath) as csvfile:

    csvreader =csv.reader(csvfile,delimiter=',')

    csv_header = next(csvreader)
    #print(f"CSV  Header : {csv_header}")

    for row in csvreader:
        VoterCount =VoterCount + 1
        if row[2] == "Khan" :
            Khan = Khan +1
        elif row[2] == "Correy" :
            Correy = Correy +1
        elif row[2] == "Li" :
            Li = Li +1
        elif row[2] == "O'Tooley" :
            OTooley = OTooley + 1
        else:
            print("None of these candidates match")
    
if Khan >= Correy and Khan >= Li and Khan >= OTooley :
    Winner = "Khan"
elif Correy >= Khan and Correy >= Li and Correy >= OTooley :
    Winner = "Correy"
elif Li >= Khan and Li >= Correy and Li >= OTooley :
    Winner = "Li"
else:
    Winner = "O'Tooley"

KhanPercent = round((Khan/VoterCount) * 100,4)
CorreyPercent = round((Correy/VoterCount)*100,4)
LiPercent = round((Li/VoterCount)*100,4)
OTooleyPercent = round((OTooley/VoterCount)*100,4)

print("Election Results")
print("-----------------------------------") 
print (f'Total Votes:  {VoterCount}') 
print("-----------------------------------")  
print(f'Khan: {KhanPercent}%    ({Khan})')
print(f'Correy: {CorreyPercent}%  ({Correy})')
print(f'Li: {LiPercent}%  ({Li})')
print(f"O'Tooley: {OTooleyPercent}%  ({OTooley})")
print("-----------------------------------") 
print(f'Winner:  {Winner}')
print("-----------------------------------") 


output_file = os.path.join("output.txt")

with open(output_file, "w") as datafile:
    writer = csv.writer(datafile)
    writer.writerow(["Election Results"])
    writer.writerow(["-----------------------------------"]) 
    writer.writerow (['Total Votes:  ' +  str(VoterCount)]) 
    writer.writerow(["-----------------------------------"])  
    writer.writerow(['Khan:   ' + str(KhanPercent)+'%    '    +'('+str(Khan)+')'])
    writer.writerow(['Correy: '+str(CorreyPercent)+'%    '+  '('+str(Correy)+')'])
    writer.writerow(['Li:  '+str(LiPercent)+'%     ' + '('+str(Li)+')'])
    writer.writerow(["O'Tooley: "+ str(OTooleyPercent) +"%    "+  "("+str(OTooley) +")"])
    writer.writerow(["-----------------------------------"]) 
    writer.writerow(['Winner:  '+Winner])
    writer.writerow(["-----------------------------------"]) 











