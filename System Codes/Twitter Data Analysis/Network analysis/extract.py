#extract lines
outfile = open("2019-10-30.txt", "wb")
inputfile = open("HKProtests_cloud_16.txt", "r")

for line in inputfile:
    # print(type(line))
    if line[0:25] == '{"created_at":"Wed Oct 30':
        line = line.encode()
        outfile.write(line)
    # break    
# outfile.close()
