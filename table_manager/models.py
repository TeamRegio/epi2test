# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey has `on_delete` set to the desired behavior.
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models
from django import forms


# ==========================================================================
class genomeAnnotation(models.Model):
    genomeVersion = models.CharField(max_length=20, blank=True)
    annotationVersion = models.CharField(max_length=20, primary_key=True)
    databaseName = models.CharField(max_length=30, blank=True)

    class Meta:
        managed = False
        db_table = 'genomeAnnotation'

    def __str__(self):
        return (str(self.genomeVersion) +  " " + str(self.annotationVersion) + " " + str(self.databaseName))
	#return self.genomeVersion


# ==========================================================================
class cellTypes(models.Model):
    cellTypeID = models.CharField(max_length=30, primary_key=True)
    cellTypeName = models.CharField(max_length=30, blank=True)
    cellOntologyTerm = models.CharField(max_length=30, blank=True)

    class Meta:
        managed = False
        db_table = 'cellTypes'

    def __str__(self):
        return (str(self.cellTypeID) + " " + str(self.cellTypeName) + " " + str(self.cellOntologyTerm))
        #return self.cellTypeID


# ==========================================================================
class geneAnnotation(models.Model):
    chr = models.CharField(max_length=10, blank=True)
    start = models.IntegerField(blank=True)
    end = models.IntegerField(blank=True)
    geneID = models.CharField(max_length=40, primary_key=True)
    geneSymbol = models.CharField(max_length=30, blank=True)
    alternativeGeneID = models.CharField(max_length=30, blank=True)
    isTF = models.BooleanField(blank=True, null=True)
    strand = models.CharField(max_length=10, blank=True)
    annotationVersion = models.ForeignKey(genomeAnnotation, to_field="annotationVersion",db_column='annotationVersion', on_delete=models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'geneAnnotation'

    def __str__(self):
        return (str(self.geneID) + " " + str(self.chr) + ":" + str(self.start) + "-" + str(self.end) + " "  + str(self.geneSymbol) + " " + str(self.isTF) + " " + str(self.strand) + " " + str(self.annotationVersion))
        #return self.geneID


# ==========================================================================
class REMAnnotation(models.Model):
    chr = models.CharField(max_length=10, blank=True)
    start = models.IntegerField(blank=True)
    end = models.IntegerField(blank=True)
    geneID = models.ForeignKey(geneAnnotation, to_field="geneID", db_column='geneID', on_delete=models.DO_NOTHING)
    REMID = models.CharField(max_length=30, primary_key=True)
    regressionCoefficient = models.FloatField(blank=True)
    pValue = models.FloatField(blank=True)

    class Meta:
        managed = False
        db_table = 'REMAnnotation'

    def __str__(self):
        return (str(self.REMID)  +  " " + str(self.chr) + ":" + str(self.start) + "-" + str(self.end))
        #return self.REMID


# ==========================================================================
class sampleInfo(models.Model):
    sampleID = models.CharField(max_length=30, primary_key=True)
    originalSampleID = models.CharField(max_length=30, blank=True)
    cellTypeID = models.ForeignKey(cellTypes, to_field="cellTypeID", db_column='cellTypeID', on_delete=models.DO_NOTHING)
    origin = models.CharField(max_length=30, blank=True)
    dataType = models.CharField(max_length=20, blank=True)

    class Meta:
        managed = False
        db_table = 'sampleInfo'

    def __str__(self):
        return (str(self.sampleID) + " " + str(self.originalSampleID) + " " + str(self.cellTypeID) + " " + str(self.origin) + " " + str(self.dataType))
        #return self.sampleID


# ==========================================================================
class geneExpression(models.Model):
    geneExpressionID = models.IntegerField(primary_key=True, db_column='ID')
    geneID = models.ForeignKey(geneAnnotation, to_field="geneID", db_column='geneID', on_delete=models.DO_NOTHING)
    sampleID = models.ForeignKey(sampleInfo, to_field="sampleID", db_column='sampleID', on_delete=models.DO_NOTHING)
    expressionLog2TPM = models.FloatField(blank=True)

    class Meta:
        managed = False
        db_table = 'geneExpression'

    def __str__(self):
        return str(str(self.geneID) + ' ' + str(self.sampleID) + ' ' + str(self.expressionLog2TPM))
       # return str(str(self.geneExpressionID) + ' ' + str(self.geneID))


# ==========================================================================
class REMActivity(models.Model):
    REMActivityID = models.IntegerField(primary_key=True, db_column='ActivID')
    REMID = models.ForeignKey(REMAnnotation, to_field="REMID", db_column='REMID', on_delete=models.DO_NOTHING)
    sampleID = models.ForeignKey(sampleInfo, to_field="sampleID", db_column='sampleID', on_delete=models.DO_NOTHING)
    dnase1Log2 = models.FloatField(blank=True)

    class Meta:
        managed = False
        db_table = 'REMActivity'

    def __str__(self):
        return str(str(self.REMActivityID) + ' ' + str(self.REMID))






