v = 131
sp_ini = 20000; sp_fin = -20000
jump = 1000
#----------------------#
DELTA = sp_fin-sp_ini 
#VIEWTEXT("", "", str(DELTA))

sp = sp_ini; 
if (DELTA < 0):
	DELTA = (-1)*DELTA
incremento = []
if (sp_ini > sp_fin):
	incremento = (-1)*jump
else: 
	incremento = jump
XCMD('qu zg',WAIT_TILL_DONE)	
for i in range(v,v+DELTA/jump+1):
	XCMD('wra '+str(i),WAIT_TILL_DONE)
	XCMD('re '+str(i),WAIT_TILL_DONE)
	XCMD('spoffs0 '+str(sp),WAIT_TILL_DONE)
	sp = sp_ini + incremento
	sp_ini = sp
	XCMD('qu zg',WAIT_TILL_DONE)


#XCMD('qu zg',WAIT_TILL_DONE)
#VIEWTEXT("", "", str(DELTA))