sample = [18, 7, 27, 43, 25, 22, 9, 45, 20, 6, 29, 5, 10, 14, 42, 36, 28, 33, 19, 30, 38, 16, 12, 15, 23, 44, 37, 32, 31, 24, 35, 21, 41, 39, 11, 40, 17, 13, 26, 8, 34]

#random.sample(xrange(v,end+1),end-v)
#VIEWTEXT("", "", sample.GET_TEXT())
#import time
#v = 4
#time.sleep(v*3600)
#XCMD('lock D2O',WAIT_TILL_DONE)
#time.sleep(60*10)
for i in sample:
	XCMD('re '+str(i),WAIT_TILL_DONE)
	XCMD('qu zg',WAIT_TILL_DONE)
	

