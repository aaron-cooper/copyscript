import subprocess
import multiprocessing

infile = open("paths.txt", "r")
lists = infile.readlines()
infile.close()

for i in range(len(lists)):
    lists[i] = lists[i].strip()


srcRoot = lists[0] + "\\"
destRoot = lists[1] + "\\"

argsList = []

i = 2
while i < len(lists):
    args = ["robocopy", "/E", f"/MT:{multiprocessing.cpu_count()}"]
    args.append(srcRoot + lists[i])
    args.append(destRoot + lists[i])
    j = i
    i += 1
    if i < len(lists) and lists[i].startswith('-'):
        args.append("/XD")
        while i < len(lists) and lists[i].startswith('-'):
            args.append(srcRoot + lists[j] + "\\" + lists[i][1:])
            i += 1
    argsList.append(args)

    
for args in argsList:
    subprocess.run(args)