expno = 132;

## spoffs0 variation configuration
sp_ini = 20000 ; sp_end = -20000;
jump_sp = 1000

## the temperature ramp 
jump_T = 2; T_ini = 280; T_end = 284;
T_precision = 0.1; T_delay = 6;

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
else: list_T = [i for i in range(T_ini,T_end,jump_T)];
        
DELTA_SP = (sp_end-sp_ini)/jump_sp;
sp = sp_ini; 
if (DELTA_SP < 0):
	DELTA_SP = (-1)*DELTA_SP;
if (sp_ini>sp_end):
	jump_sp = (-1)*jump_sp;

for T in list_T:
	XCMD('teset '+str(T),WAIT_TILL_DONE)
	XCMD('teready '+str(T_delay*3600)+' '+str(T_precision),WAIT_TILL_DONE)
	sp = sp_ini
	XCMD('lock d2o',WAIT_TILL_DONE)
	SLEEP(60*2)
	XCMD('atma',WAIT_TILL_DONE)
	SLEEP(60*2)
	for i in range(DELTA_SP+1):
		WR(curdata,"y")
		RE(curdata)
		XCMD('spoffs0 '+str(sp),WAIT_TILL_DONE)
		ZG()
		expno += 1
		curdata[1] = str(expno)
		sp = sp_ini + jump_sp
		sp_ini = sp
		
MSG("CULMINACION DEL EXPERIMENTO")


#VIEWTEXT("", "", str(DELTA))
