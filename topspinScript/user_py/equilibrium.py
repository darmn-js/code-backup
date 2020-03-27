expno = ; 
T = 275; ## temperatura de prueba en Kelvin
list_DT = [0.5,3,6]; # tiempos (horas) de espera entre adquisiciones

## spoffs0 variation configuration
sp_ini = 20000 ; sp_end = -20000;
jump_sp = 10000

curdata = CURDATA();
if (curdata == None):
        MSG("Por favor abra la carpeta del experimento")
        EXIT()
curdata[1] = str(expno)

DELTA_SP = (sp_end-sp_ini)/jump_sp;
sp = sp_ini; 
if (DELTA_SP < 0):
	DELTA_SP = (-1)*DELTA_SP;
if (sp_ini>sp_end):
	jump_sp = (-1)*jump_sp;
	
XCMD('teset '+str(T),WAIT_TILL_DONE)
XCMD('teready '+str(60*3)+' '+str(0.1),WAIT_TILL_DONE)

for T_delay in list_DT:
	SLEEP(T_delay*3600)
	sp = sp_ini
	XCMD('lock d2o',WAIT_TILL_DONE)
	for i in range(DELTA_SP+1):
		WR(curdata,"y")
		RE(curdata)
		XCMD('spoffs0 '+str(sp),WAIT_TILL_DONE)
		ZG()
		expno += 1
		curdata[1] = str(expno)
		sp = sp_ini + jump_sp
		sp_ini = sp