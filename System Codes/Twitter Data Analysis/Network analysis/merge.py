filenames = [ '2019-10-09.txt','HKProtests_cloud_9.txt']
with open('2019-10-09-combi.txt', 'w') as outfile:
    for fname in filenames:
        with open(fname) as infile:
            for line in infile:
                outfile.write(line)