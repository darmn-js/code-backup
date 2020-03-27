curdata = CURDATA(); 
if curdata == None:
	MSG("Abra la carpeta")
	EXIT()

folders = INPUT_DIALOG("","Please, put the range of the folders",\
	["First:","Last:","Jump"],["","","1"])
	
first = int(folders[0]); last=int(folders[1]); p = 1;

if (first > last):
	first = (-1)*first ; last = (-1)*last;
	list_f = [(-1)*i for i in range(first,last+1)]
else: list_f = [i for i in range(first,last+1)]

for f in list_f:
	curdata[1] = str(f)
	RE(curdata)
	if p == 1:
		XCMD(".md",WAIT_TILL_DONE)
		p = 0;
	
	