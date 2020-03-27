curdata = CURDATA();

if (curdata == None):
	MSG("Abra la carpeta")
	EXIT()
	
result = INPUT_DIALOG("Range of folders","Please input the folder range:",\
					["First","Last","Jump"],["","",""])

first = int(result[0]); last=int(result[1]); jump = int(result[2]);

if (first > last):
	first = (-1)*first; last = (-1)*last;
	List = [i for i in range(first,last+1,jump)];
else: List = [i for i in range(first,last+1,jump)];
		
result = INPUT_DIALOG("Range of integration and AZFW parameter","Please input the integration range:",\
					["low field","High field","AZFW","AZFE","ABSL"],\
					["6","0","0.05","0.05","3"])
					
absf1 = result[0]; absf2 = result[1]; azfw = result[2];
azfe = result[3]; absl = result[4];
for f in List:
	curdata[1] = str(f);
	RE(curdata)
	PUTPAR('ABSF1',absf1);
	PUTPAR('ABSF2',absf2)
	PUTPAR('AZFW',azfw);
	PUTPAR('AZFE',azfe);
	PUTPAR('ABSL',absl);
	XCMD("absf",WAIT_TILL_DONE);
	#XCMD("lil",WAIT_TILL_DONE)