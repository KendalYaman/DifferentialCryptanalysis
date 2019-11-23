table1S1 = [14, 4, 13,1 , 2, 15, 11, 8, 3, 10, 6, 12, 5, 9, 0, 7]

table2S1 = [0, 15, 7, 4, 14, 2, 13, 1, 10, 6, 12, 11, 9, 5, 3, 8]

table3S1 = [4, 1, 14, 8, 13, 6,2, 11, 15, 12, 9, 7, 3, 10, 5, 0]

table4S1 = [15, 12, 8, 2, 4, 9,1, 7, 5, 11, 3, 14, 10, 0, 6, 13]
#4 tables for 00 01 10 11

def s1(val):
	
	if(val[0] == "0" and val[5] == "0"):
   		return table1S1[int(val[1:5],2)]
   	elif(val[0] == "0" and val[5] == "1"):
   		return table2S1[int(val[1:5],2)]
   	elif(val[0] == "1" and val[5] == "0"):
   		return table3S1[int(val[1:5],2)]
   	elif(val[0] == "1" and val[5] == "1"):
   		return table4S1[int(val[1:5],2)]

for x in xrange(64): #from 000000 to 111111
	
	t = s1(bin(int('3d',16)^x)[2:].zfill(6)) #I calculate 3d xor possible key
	
	t2 = s1(bin(int('0b',16)^x)[2:].zfill(6)) #I calculate 3d xor 36 (which is 0b)  xor possible key
	
	if (int(bin(t^t2),2) == 11): #I check if t xor t2 are equal to 0b (11 in decimal)
		#print 
		#print int(bin(t^t2),2)
		#print bin(x)[2:].zfill(6)
		print hex(x)
		#print int(bin(t^t2),2)

