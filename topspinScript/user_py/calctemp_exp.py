expno = 253;

## the temperature ramp 
jump_T = 5; T_ini = 275; T_end = 300;
T_precision = 0.1; T_delay = 10; 

#----------------------#

curdata = CURDATA();
if (curdata == None):
        MSG("Por favor abra la carpeta del experimento")
        EXIT()
curdata[1] = str(expno)

DELTA_T = (T_end - T_ini)/jump_T;
if (DELTA_T<0):
	DELTA_T = (-1)*DELTA_T;
if (T_ini>T_end):
        T_ini,T_end = (-1)*T_ini,(-1)*T_end;
        list_T = [(-1)*i for i in range(T_ini,T_end+1,jump_T)];
else: list_T = [i for i in range(T_ini,T_end+1,jump_T)];

VIEWTEXT("","",str(list_T))
EXIT()
for T in list_T:
	XCMD('teset '+str(T),WAIT_TILL_DONE)
	XCMD('teready '+str(T_delay*60)+' '+str(T_precision),WAIT_TILL_DONE)
	XCMD('lock meod',WAIT_TILL_DONE)
	SLEEP(3)
	XCMD('atma',WAIT_TILL_DONE)
	SLEEP(3)
	XCMD('t',WAIT_TILL_DONE)
	SLEEP(3)
	for i in range(3):
		WR(curdata,"y"); RE(curdata)
		expno += 1; curdata[1] = str(expno)
		ZG()
		SLEEP(10)
			
MSG("CULMINACION DEL EXPERIMENTO")