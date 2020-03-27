# 1. Posicionarse en la ultima carpeta
# 2. dar el numero de experimentos ha correr
# 3. dar el intervalo de espera entre adquisición

N_exp = 300
delta_t = 2  # delta en minutos

v = CURDATA() [1]
for i in range(1,N_exp + 1):
	XCMD('re '+str(v),WAIT_TILL_DONE)
	XCMD('wra '+str(int(v)+i),WAIT_TILL_DONE)
	XCMD('re '+str(int(v)+i),WAIT_TILL_DONE)
	ZG()
	PUTPAR('PHC0','0');PUTPAR('PHC1','0')
	XCMD('efp',WAIT_TILL_DONE)
	XCMD('apk',WAIT_TILL_DONE)
	SLEEP(60*delta_t)

	