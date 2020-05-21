#!/usr/bin/python

import os, time

cmd = "leetcode-cli list -q d > log"
os.system(cmd)
f = open("log", "r")
lines = f.readlines()

done = set()
for name in lines:
	num = name.split("[")[1].split("]")[0]
	done.add(int(num))

maxn = max(done)
#maxn = 1

exist = set()
for name in os.listdir("."):
	if os.path.isdir(name):
		num = int(name.split(".")[0])
		exist.add(num)

for i in range(1, maxn + 1):
	if i not in exist and i in done:
		cmd = "leetcode-cli submission " + str(i) + " -o ../../../tmp"
		os.system(cmd)
		time.sleep(2)

for name in os.listdir("../../../tmp"):
	num, title = name.split(".")[: 2]
	if int(num) in exist: continue
	folder = "0" * (4 - len(num)) + str(num) + "."
	ntitle = ""
	for i, c in enumerate(title):
		if c == "-":
			ntitle += c
		elif i == 0 or title[i - 1] == "-":
			ntitle += c.upper()
		else:
			ntitle += c
	folder += ntitle
	cmd = "mkdir " + folder
	os.system(cmd)
	cmd = "mv ../../../tmp/" + name + " " + folder + "/" + ntitle + ".py"
	os.system(cmd)

cmd = "rm log"
os.system(cmd)