curdata = CURDATA();

if (curdata == None):
	MSG("Abra la carpeta")
	EXIT()
	
result = INPUT_DIALOG("","1 -> single\n2 -> Multi",\
					["Value:"],["2"])
	
if (result[0] == "2"):
	folders = INPUT_DIALOG("","Please, put the range of the folders",\
	["First:","Last:","LB:"],["","",""])
	first = int(folders[0]); last=int(folders[1]);LB = folders[2];
	List = [i for i in range(first,last+1)]
elif (result[0] == "1"):
	List = [int(curdata[1])]
else: MSG("Value not available"); EXIT()

#VIEWTEXT("","",str(List))
for expno in List:
	curdata[1] = str(expno)
	RE(curdata)	
	PUTPAR('LB',LB)
	PUTPAR('PHC0','0');PUTPAR('PHC1','0')
	EFP()
	APK()

		
		
#XCMD('efp',WAIT_TILL_DONE)
#XCMD('apk',WAIT_TILL_DONE)