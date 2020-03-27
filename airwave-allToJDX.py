#script para generar jcamps del proyecto airwave 
import os
from os.path import join

dataPath = '/home/abolanos/homeHost/decompressTest';
pathForSave = '/home/abolanos/homeHost/airwaveJres';

folderList = os.listdir(dataPath);
nmrTypePosition = 1; # esta variable deberia desaparecer porque no todos los archivos tienen la dimension en el nombre.
nbBrukerData = 0
nbOneDBruker = 0
nbTwoDBruker = 0
nbOneD = 0
varianList = [];
counter = 1
for folder in folderList:
	exist = False;
	splittedFolderName = folder.split('_');
	rackNumber = int(splittedFolderName[2].replace('Rack', ''));
	if rackNumber > 9: continue
	rackNumber = str(rackNumber)
	for root, dirs, files in os.walk(join(dataPath,folder), topdown=True):
		isBruker = False; isOneD = False; isTwoD = False;
		for file in files:
			if file.lower() == 'fid':
				isOneD = True
				if os.access(join(root, 'acqu'), os.F_OK):
					isBruker = True
				break
			if file.lower() ==  'ser':
				isTwoD = True
				if os.access(join(root, 'acqu2s'), os.F_OK):
					isBruker = True
				break
		if isBruker:
			nbBrukerData += 1
			if isOneD:
				nbOneDBruker += 1
			if isTwoD:
				nbTwoDBruker += 1
				splittedDirs = root.split('/');
				expno = str(int(splittedDirs[len(splittedDirs)-1]))
				#MSG(nameFile);
				nameFile = 'Airwave-'+rackNumber+'-'+expno+'-1'
				tempath = os.path.join(pathForSave, nameFile)
				expno = str(int(expno) - 1)
				RE_PATH(os.path.join(root, 'pdata', '1'))
				nameFile = 'Airwave-'+rackNumber+'-'+expno+'-1'
				title = 'C:'+nameFile+'\n'+'B:001\nE:admin@cheminfo.org'
				tojdx = "tojdx \""+ tempath + ".jdx" + "\"" + " 1 3 " + "\"" +title + "\"" + " BRUKER *"
				XCMD(tojdx, WAIT_TILL_DONE)
				counter +=1;
		elif isOneD:
			MSG(folder)
			#tempath = os.path.join(pathForSave, folder);
			#mytitle = '*';
			#e = 'vconv ' + root + ' ' + folder + ' ' + str(counter) + ' C:/Users/JuanCBA/Desktop/desktop/varianData Bruker';
			#result = XCMD(e, NO_WAIT_TILL_DONE);
			#MSG(folder)
			#varianList.append()
			#tojdx = "tojdx \""+ tempath + ".jdx" + "\"" + " 2 3 " + mytitle + " BRUKER *"
			#XCMD(tojdx, WAIT_TILL_DONE)
			#counter +=1;
		#if counter > 1: break;
	
MSG(str(nbTwoDBruker))

	



	
