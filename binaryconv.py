import binascii

fobj = open("File1.txt",'rb')
s = fobj.read()

#converting the input file to binary

hex_str = str(binascii.hexlify(s))
bin_data = bin(int(hex_str,16)).replace('b','')

binconverted = open("binconv.txt",'w')
binconverted.write(bin_data)

temp_trans = bin_data[0]
nrz_trans = 0

#Logic to calculate the number of transitions for NRZ

for i in bin_data:
    if(temp_trans != i):
        nrz_trans += 1
        temp_trans = i

#logic to calculate the number of transitions for Manchester
prev = ""
mc_trans = 0
for i in bin_data:
	nxt = i
	if((prev == "1" and nxt == "1") or (prev == "0" and nxt == "0")):
		mc_trans += 2
		prev = i
	else:
		mc_trans += 1
		prev = i


wave_data = bin_data[:16]    #Slicing the data for a smaple to generate waveforms

print("sample data from the file:%s" % wave_data)
nrz_wave = ""
mc_wave = ""


for i in wave_data:
    if(i == '1'):
        nrz_wave += "------"
        mc_wave += " __-- "
    else:
        nrz_wave += "______"
        mc_wave += " --__ "


print("NRZ wave for the sample data:%s" % nrz_wave)
print("Manchester wave for the sample data:%s" % mc_wave)
print("No.of transitions for the entire file")
print("No.of transitions in NRZ:%d" %nrz_trans)
print("No.of transitions in Manchester:%d" %mc_trans)
