expno = 1; ##carpeta de la cual se copiara el experimento

## the temperature ramp 
#jump_T = 1; T_ini = 287; T_end = 28;

T_precision = 0.05; 
T_delay = 10; # tiempo en minutos

#----------------------#

curdata = CURDATA();
if (curdata == None):
        MSG("Por favor abra la carpeta del experimento")
        EXIT()
curdata[1] = str(expno)

#DELTA_T = (T_end - T_ini)/jump_T;
#if (DELTA_T<0):
#	DELTA_T = (-1)*DELTA_T;

#DELTA_T = int(DELTA_T)
#VIEWTEXT("","",str(DELTA_T))
#if (int(jump_T) != jump_T):
#if (T_ini>T_end):
#        T_ini,T_end = (-1)*T_ini,(-1)*T_end;
#        list_T = [(-1)*i for i in range(T_ini,T_ini+DELTA_T+1,jump_T)];
#else: list_T = [i for i in range(T_ini,T_ini+DELTA_T+1,jump_T)];

list_T = [285.0, 285.5, 286.0, 286.5, 287.0, 287.5, 288.0, 288.5, 289.0, 289.5, 290.0, 290.5, 291.0, 291.5, 292.0, 292.5, 293.0, 293.5, 294.0, 294.5, 295.0]
list_dt = [0]+[30]*20

for T in list_T:
	XCMD('teset '+str(T),WAIT_TILL_DONE)
	XCMD('teget '+str(T),WAIT_TILL_DONE)
	XCMD('teready '+str(T_delay*60)+' '+str(T_precision),WAIT_TILL_DONE)
	XCMD('atma',WAIT_TILL_DONE)
	SLEEP(5)
	XCMD('lock meod',WAIT_TILL_DONE)
	SLEEP(5)
	XCMD('topshim',WAIT_TILL_DONE)
	SLEEP(120)
	for t in list_dt:
		SLEEP(60*t)
		RE(curdata)
		expno += 1
		curdata[1] = str(expno)
		WR(curdata,"y")
		RE(curdata)
		ZG()
			
			

				
MSG("CULMINACION DEL EXPERIMENTO")