curdata = CURDATA();

folders = INPUT_DIALOG("","Please, put the range of the folders",\
	["First:","Last:"],["",""])

first = int(folders[0]); last=int(folders[1])
List = [i for i in range(first,last+1)]
for expno in List:
	curdata[1] = str(expno)
	RE(curdata)
	XCMD('tojdx /home/abolanos/'+curdata[1]+'.dx 1 0 '+curdata[1]+' * *' ,WAIT_TILL_DONE)