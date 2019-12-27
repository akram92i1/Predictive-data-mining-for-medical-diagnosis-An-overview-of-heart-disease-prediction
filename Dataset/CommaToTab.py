import os

#o = os.path.join("C:\\Users\aroubaz\Desktop", "\TEST.txt")
fin = open("C:/Users/aroubaz/Desktop/coucou.txt", "rt")
fout = open("out.txt", "wt")

for line in fin:
	fout.write(line.replace(',', '	'))
	
fin.close()
fout.close()