def getsubnet(cidr,nmask):
	print('cidr',cidr)
	c =16
	if(cidr == 32):
		nmask[0] = 255; nmask[1] = 255;nmask[2] = 255;nmask[3] = 255;
	if(cidr == 31):
		nmask[0] = 255; nmask[1] = 255;nmask[2] = 255;nmask[3] = 254;
	if(cidr == 30):
		nmask[0] = 255; nmask[1] = 255;nmask[2] = 255;nmask[3] = 252;
	if(cidr == 29):
		nmask[0] = 255; nmask[1] = 255;nmask[2] = 255;nmask[3] = 248;
	if(cidr == 28):
		nmask[0] = 255; nmask[1] = 255;nmask[2] = 255;nmask[3] = 240;
	if(cidr == 27):
		nmask[0] = 255; nmask[1] = 255;nmask[2] = 255;nmask[3] = 224;
	if(cidr == 26):
		nmask[0] = 255; nmask[1] = 255;nmask[2] = 255;nmask[3] = 192;
	if(cidr == 25):
		nmask[0] = 255; nmask[1] = 255;nmask[2] = 255;nmask[3] = 128;
	if(cidr == 24):
		nmask[0] = 255; nmask[1] = 255;nmask[2] = 255;nmask[3] = 0;
	if(cidr == 23):
		nmask[0] = 255; nmask[1] = 255;nmask[2] = 254;nmask[3] = 0;
	if(cidr == 22):
		nmask[0] = 255; nmask[1] = 255;nmask[2] = 252;nmask[3] = 0;
	if(cidr == 21):
		nmask[0] = 255; nmask[1] = 255;nmask[2] = 248;nmask[3] = 0;
	if(cidr == 20):
		nmask[0] = 255; nmask[1] = 255;nmask[2] = 240;nmask[3] = 0;
	if(cidr == 19):
		nmask[0] = 255; nmask[1] = 255;nmask[2] = 224;nmask[3] = 0;
	if(cidr == 18):
		nmask[0] = 255; nmask[1] = 255;nmask[2] = 192;nmask[3] = 0;
	if(cidr == 17):
		nmask[0] = 255; nmask[1] = 255;nmask[2] = 128;nmask[3] = 0;
	if(cidr == 16):
		nmask[0] = 255; nmask[1] = 255;nmask[2] = 0;nmask[3] = 0;
	if(cidr == 15):
		nmask[0] = 255; nmask[1] = 254;nmask[2] = 0;nmask[3] = 0;
	if(cidr == 14):
		nmask[0] = 255; nmask[1] = 252;nmask[2] = 0;nmask[3] = 0;
	if(cidr == 13):
		nmask[0] = 255; nmask[1] = 248;nmask[2] = 0;nmask[3] = 0;
	if(cidr == 12):
		nmask[0] = 255; nmask[1] = 240;nmask[2] = 0;nmask[3] = 0;
	if(cidr == 11):
		nmask[0] = 255; nmask[1] = 224;nmask[2] = 0;nmask[3] = 0;
	if(cidr == 10):
		nmask[0] = 255; nmask[1] = 192;nmask[2] = 0;nmask[3] = 0;
	if(cidr == 9):
		nmask[0] = 255; nmask[1] = 128;nmask[2] = 0;nmask[3] = 0;
	if(cidr == 8):
		nmask[0] = 255; nmask[1] = 0;nmask[2] = 0;nmask[3] = 0;
	if(cidr == 7):
		nmask[0] = 254; nmask[1] = 0;nmask[2] = 0;nmask[3] = 0;
	if(cidr == 6):
		nmask[0] = 252; nmask[1] = 0;nmask[2] = 0;nmask[3] = 0;
	if(cidr == 5):
		nmask[0] = 248; nmask[1] = 0;nmask[2] = 0;nmask[3] = 0;
	if(cidr == 4):
		nmask[0] = 240; nmask[1] = 0;nmask[2] = 0;nmask[3] = 0;
	if(cidr == 3):
		nmask[0] = 224; nmask[1] = 0;nmask[2] = 0;nmask[3] = 0;
	if(cidr == 2):
		nmask[0] = 192; nmask[1] = 0;nmask[2] = 0;nmask[3] = 0;
	if(cidr == 1):
		nmask[0] = 128; nmask[1] = 0;nmask[2] = 0;nmask[3] = 0;
	if(cidr == 0):
		nmask[0] = 0; nmask[1] = 0;nmask[2] = 0;nmask[3] = 0;
		print('****** print nmask ******',nmask)
	return nmask
	
def main():
	cidr = -1
	ipv4 = [-1,-1,-1,-1]
	nmask =  [-1,-1,-1,-1]
	netid = [-1,-1,-1,-1]
	bcast = [-1,-1,-1,-1]
	startingip = [-1,-1,-1,-1]
	endingip = [-1,-1,-1,-1]
	
	print ('Input an IP and CIDR with 5 inputs.')
	o1 = input("OCTET 1 : ")
	o2 = input("OCTET 2 : ")
	o3 = input("OCTET 3 : ")
	o4 = input("OCTET 4 : ")
	cidr = input("CIDR :")
	print (o1,o2,o3,o4, "/", cidr)
	ipv4[0] = o1; ipv4[1] = o2; ipv4[2] = o3;	ipv4[3] = o4;
	nmask = getsubnet(cidr,nmask)
	print(ipv4,nmask,end=' ')
main()
