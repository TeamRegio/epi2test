import os
import sys
from django.conf import settings
#sys.path.insert(1, r'website/')#tell python the path of the project

from draftEpi2 import setup #setup function defined in __init__.py of the project (here website)
setup()

from django.db import models
from table_manager.models import *



#test functions
#TODO: write proper unitests
def __main__():

	print("API functions")
	print("Is the database accessible?")

	REM = REMAnnotation.objects.get(pk = "REM0000001")
	print("For a single REM: " + str(REM))

	print("all REMs of a gene")
	REMs = REMAnnotation.objects.filter(geneID = 'ENSG00000139874')
	for i in REMs:
		print(i)

	print("samlpeInfo")
	sample = sampleInfo.objects.get(sampleID = 'R_ENCBS336CDQ')
	print(sample)

#This is not working because of the missing primary key, which is geneExpressionID in the database ->same for REMActivity TODO: rausfinden wie man combined primary key angibt in mysql
#	print("geneExpression")
#	geneExp = geneExpression.objects.get(geneID = 'ENSG00000139874')
#	print(geneExp)

	print("genomeAnnotation")
	genome = genomeAnnotation.objects.all()
	print(genome)
	
	print("celltypes")
	cellType = cellTypes.objects.get(cellTypeID = 'CTID_0000001')
	print(cellType)

	print("geneAnnotation")
	geneAnno = geneAnnotation.objects.get(geneID = 'ENSG00000223972')
	print(geneAnno)


if __name__ == "__main__":
	__main__()


