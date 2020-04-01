
'''
Author: Filippo Falezza
Co-owner and contributor: Eric Liu
'''
#Write v_ref
V_ = open("/sd/voltage_ref-F6_dist.txt","w")
V_.write('%f\n' % (pyb.ADCAll(12).read_vref()))
V_.close()
#Write mag 0 data, then mag 1
list0 = [rx0_0,rx1_0,rx2_0,rx3_0]
list1 = [rx0_1,rx1_1,rx2_1,rx3_1]
f0 = open("/sd/MagF6_0_dist.csv", "w")
for item0 in list0:
	for i0 in item0:
		f0.write('%d\n' % (i0))
#stop copy here
f0.close()
f1 = open("/sd/MagF6_1_dist.csv","w")
for item1 in list1:
	for i1 in item1:
		f1.write('%d\n' % (i1))
#stop copy here
f1.close()
