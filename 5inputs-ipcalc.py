def getsubnet(cidr,nmask):
	print('cidr', cidr, nmask)
	cidr = int(cidr)
	if cidr == 32:
		nmask = [255,255,255,255]
	if cidr == 31:
		nmask = [255,255,255,254]
	if cidr == 30:
		nmask = [255,255,255,252]
	if cidr == 32:
		nmask = [255,255,255,255]
	if cidr == 31:
		nmask = [255,255,255,254]
	if cidr == 30:
		nmask = [255,255,255,252]
	if cidr == 29:
		nmask = [255,255,255,248]
	if cidr == 28:
		nmask = [255,255,255,240]
	if cidr == 27:
		nmask = [255,255,255,224]
	if cidr == 26:
		nmask = [255,255,255,192]
	if cidr == 25:
		nmask = [255,255,255,128]
	if cidr == 24:
		nmask = [255,255,255,0]
	if cidr == 23:
		nmask = [255,255,254,0]
	if cidr == 22:
		nmask = [255,255,252,0]
	if cidr == 21:
		nmask = [255,255,248,0]
	if cidr == 20:
		nmask = [255,255,240,0]
	if cidr == 19:
		nmask = [255,255,224,0]
	if cidr == 18:
		nmask = [255,255,192,0]
	if cidr == 17:
		nmask = [255,255,128,0]
	if cidr == 16:
		nmask = [255,255,0,0]
	if cidr == 15:
		nmask = [255,254,0,0]
	if cidr == 14:
		nmask = [255,252,0,0]
	if cidr == 13:
		nmask = [255,248,0,0]
	if cidr == 12:
		nmask = [255,240,0,0]
	if cidr == 11:
		nmask = [255,224,0,0]
	if cidr == 10:
		nmask = [255,192,0,0]
	if cidr == 9:
		nmask = [255,128,0,0]
	if cidr == 8:
		nmask = [255,0,0,0]
	if cidr == 7:
		nmask = [254,0,0,0]
	if cidr == 6:
		nmask = [252,0,0,0]
	if cidr == 5:
		nmask = [248,0,0,0]
	if cidr == 4:
		nmask = [240,0,0,0]
	if cidr == 3:
		nmask = [224,0,0,0]
	if cidr == 2:
		nmask = [192,0,0,0]
	if cidr == 1:
		nmask = [128,0,0,0]
	if cidr == 0:
		nmask = [0,0,0,0]
	return nmask
def getnetworkid(ipv4,nmask,netid):
	for i in range (0,4):
		netid[i] = (int(ipv4[i]) & int(nmask[i]))
	return netid
	
def getbroadcast(nmask,netid,bcast):
	imask = [-1,-1,-1,-1]
	for i in range(0,4):
		imask[i] = ~int(nmask[i])&255
		bcast[i] = int(netid[i])^int(imask[i])
	return bcast

def getstartip(netid, startingip):
	startingip = (netid[0], netid[1], netid[2], netid[3]+1)
	return startingip

def getendip(bcast, endingip):
	endingip = (bcast[0], bcast[1], bcast[2], bcast[3]-1)
	return endingip

def gethostipa(startingip):
	hostipa = (startingip[0], startingip[1], startingip[2], 0)
	return hostipa
	
def gethostipb(endingip):
	hostipb = (endingip[0], endingip[1], endingip[2], 255)
	return hostipb

def main():
	cidr = -1
	ipv4 = [-1,-1,-1,-1]
	nmask =  [-1,-1,-1,-1]
	netid = [-1,-1,-1,-1]
	bcast = [-1,-1,-1,-1]
	startingip = [-1,-1,-1,-1]
	endingip = [-1,-1,-1,-1]
	
	print ('Input an IP and CIDR with 5 inputs.')
	ipv4[0] = input("OCTET 1: ")
	ipv4[1] = input("OCTET 2: ")
	ipv4[2] = input("OCTET 3: ")
	ipv4[3] = input("OCTET 4: ")
	cidr = input("CIDR: ")  
	nmask = getsubnet(cidr,nmask)
	netid = getnetworkid(ipv4,nmask,netid)
	bcast = getbroadcast(nmask,netid,bcast)
	startingip = getstartip(netid, startingip)
	endingip = getendip(bcast, endingip)
	hostip1 = gethostipa(startingip)
	hostip2 = gethostipb(endingip)
	print("IP:",ipv4)
	print("NETMASK:",nmask)
	print("NETWORK ID:",netid)
	print("BROADCAST ADDRESS:",bcast)
	print("HOST IPS:",hostip1, "-", hostip2)
	print("HOST RANGE:",startingip, "-", endingip)
main()
