import csv
import sys

Dengue_1 = ""
Dengue_2 = ""
Dengue_3 = ""
Dengue_4  = ""
similarity =""
# -----------------------Reading Data file----------------------------

with open(sys.argv[1]) as f:
    lines = f.readlines()

for eachline in lines:
    if "Dengue4" in eachline:
        Dengue_4 += eachline.split("      ")[1]
    elif "Dengue3" in eachline:
        Dengue_3 += eachline.split("      ")[1]
    elif "Dengue2" in eachline:
        Dengue_2 += eachline.split("      ")[1]
    elif "Dengue1" in eachline:
        Dengue_1 += eachline.split("      ")[1]
    elif ((":" in eachline) or ("." in eachline) or ("*" in eachline)):
        if("CLUSTAL" in eachline):
            continue
        else:
            similarity+=eachline[13:]

Dengue_4 = Dengue_4.replace('\n','')
Dengue_3 = Dengue_3.replace('\n','')
Dengue_2 = Dengue_2.replace('\n','')
Dengue_1 = Dengue_1.replace('\n','')
similarity = similarity.replace('\n','')
print(Dengue_4)
print(Dengue_3)
print(Dengue_2)
print(Dengue_1)
print(similarity)
print('\n')
for i in range (len(similarity)):
    print(i+1,'\t',Dengue_1[i]," ",Dengue_2[i]," ",Dengue_3[i]," ",Dengue_4[i]," ",similarity[i])

    #--------------------------writing CSV --------------------------------------------

    # name of csv file
out_filename = "output.csv"
titles = ['No.','Dengue_4', 'Dengue_3', 'Dengue_2', 'Dengue_1','similarity']
list = [Dengue_4[0],Dengue_3[0],Dengue_2[0],Dengue_1[0]]

# writing to csv file
with open(out_filename, 'w') as csvfile:
    # creating a csv writer object
    csvwriter = csv.writer(csvfile)
    csvwriter.writerow(titles)
    list = [1,Dengue_4[0],Dengue_3[0],Dengue_2[0],Dengue_1[0],similarity[0]]
    for i in range (len(similarity)):
        list[0] = i + 1

        if (i >= len(Dengue_4)):
            list[1] = " "
        else:
            list[1] = Dengue_4[i]
      
        if (i >= len(Dengue_3)):
            list[2] = " "
        else:
            list[2] = Dengue_3[i]
      
        if (i >= len(Dengue_2)):
            list[3] = " "
        else:
            list[3] = Dengue_2[i]
      
        if (i >= len(Dengue_1)):
            list[4] = " "
        else:
            list[4] = Dengue_1[i]
      
        list[5] = similarity[i]

        csvwriter.writerow(list)

print("Output file generated successfully")