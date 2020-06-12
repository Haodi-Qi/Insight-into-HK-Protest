lines_seen = set() # holds lines already seen
outfile = open("2019-10-09-combi_wod.txt", "wb")
for line in open("2019-10-09-combi.txt", "rb"):
    if line not in lines_seen: # not a duplicate
        outfile.write(line)
        lines_seen.add(line)
outfile.close()