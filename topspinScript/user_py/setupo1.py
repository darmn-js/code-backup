v = 1; end =41
o1 = 10
for i in range(v,end+1):
	XCMD('re '+str(i),WAIT_TILL_DONE)
	#XCMD('gpz1 0',WAIT_TILL_DONE)
	XCMD('d1 '+str(o1),WAIT_TILL_DONE)
	#PUTPAR('O1',str(o1))

#o1 = o1 - 0.1
#o1 = o1 + 0.1