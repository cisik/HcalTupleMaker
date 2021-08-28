#------------------------------------------------------------------------------------
# Imports
#------------------------------------------------------------------------------------
import FWCore.ParameterSet.Config as cms
import FWCore.ParameterSet.VarParsing as VarParsing
from Configuration.StandardSequences.Eras import eras

#------------------------------------------------------------------------------------
# Options
#------------------------------------------------------------------------------------
options = VarParsing.VarParsing()

options.register('skipEvents',
                 0, # default value
                 VarParsing.VarParsing.multiplicity.singleton,
                 VarParsing.VarParsing.varType.int,
                 "Number of events to skip")

options.register('processEvents',
                 -1, # default value
                 VarParsing.VarParsing.multiplicity.singleton,
                 VarParsing.VarParsing.varType.int,
                 "Number of events to process")

options.register('inputFiles',
                 "file:/afs/cern.ch/work/o/oviazlo/HCAL_PMG/CMSSW_11_3_0/src/HCALPFG/HcalTupleMaker/test/DATA/00bdf81d-eb84-4f5e-ae0d-9760eb633271.root",
                 VarParsing.VarParsing.multiplicity.list,
                 VarParsing.VarParsing.varType.string,
                 "Input files")

options.register('outputFile',
                 "file:HcalTupleMaker_test.root", # default value
                 VarParsing.VarParsing.multiplicity.singleton,
                 VarParsing.VarParsing.varType.string,
                 "Output file")

options.parseArguments()

print " "
print "Using options:"
print " skipEvents    =", options.skipEvents
print " processEvents =", options.processEvents
print " inputFiles    =", options.inputFiles
print " outputFile    =", options.outputFile
print " "

#------------------------------------------------------------------------------------
# Declare the process and input variables
#------------------------------------------------------------------------------------
process = cms.Process('PFG',eras.Run3)

#------------------------------------------------------------------------------------
# Get and parse the command line arguments
#------------------------------------------------------------------------------------
process.maxEvents = cms.untracked.PSet( input = cms.untracked.int32(options.processEvents) )

process.source = cms.Source(
    "PoolSource",
    fileNames  = cms.untracked.vstring(options.inputFiles),
    skipEvents = cms.untracked.uint32(options.skipEvents)
    )

process.TFileService = cms.Service(
    "TFileService",
    fileName = cms.string(options.outputFile)
    )

#------------------------------------------------------------------------------------
# import of standard configurations
#------------------------------------------------------------------------------------
process.load('Configuration.StandardSequences.Services_cff')
process.load('FWCore.MessageService.MessageLogger_cfi')
process.MessageLogger.cerr.FwkReport.reportEvery = cms.untracked.int32(100)
process.load('Configuration.EventContent.EventContent_cff')
#  process.load('Configuration.Geometry.GeometryExtended2026D76Reco_cff')
#  process.load('Configuration.Geometry.GeometryExtended2021_cff')
process.load('Configuration.Geometry.GeometryExtended2021Reco_cff')


#  process.load('Configuration.StandardSequences.RawToDigi_Data_cff')
process.load("EventFilter.HcalRawToDigi.HcalRawToDigi_cfi")

#process.load('Configuration.StandardSequences.L1Reco_cff')
#process.load('Configuration.StandardSequences.Reconstruction_Data_cff')
process.load("RecoLocalCalo.Configuration.hcalLocalReco_cff")
#process.load("RecoLocalCalo.Configuration.RecoLocalCalo_Cosmics_cff")

process.load('Configuration.StandardSequences.EndOfProcess_cff')
process.load('RecoMET.METProducers.hcalnoiseinfoproducer_cfi')
process.load("CommonTools.RecoAlgos.HBHENoiseFilter_cfi")
process.load("CommonTools.RecoAlgos.HBHENoiseFilterResultProducer_cfi")
process.load("CondCore.CondDB.CondDB_cfi")

#------------------------------------------------------------------------------------
# Set up our analyzer
#------------------------------------------------------------------------------------
process.load("HCALPFG.HcalTupleMaker.HcalTupleMaker_cfi") # loads all modules

#  process.hcalDigis.InputLabel = cms.InputTag("hltHcalCalibrationRaw")

#------------------------------------------------------------------------------------
# Which trigger to use
#------------------------------------------------------------------------------------
process.my_hlt = cms.EDFilter("HLTHighLevel",
     TriggerResultsTag = cms.InputTag("TriggerResults","","HLT"),
     # provide list of HLT paths (or patterns) you want
     HLTPaths = cms.vstring("HLT_L1SingleMuCosmics_v1"),
     #  HLTPaths = cms.vstring("HLT_HcalCalibration_v1"), # provide list of HLT paths (or patterns) you want
     # not empty => use read paths from AlCaRecoTriggerBitsRcd via this key
     eventSetupPathsKey = cms.string(''),
     # how to deal with multiple triggers: True (OR) accept if ANY is true, False (AND) accept if ALL are true
     andOr = cms.bool(True),
     throw = cms.bool(False)    # throw exception on unknown path names
)

#------------------------------------------------------------------------------------
# QIE11 and QIE10 Unpacker
#------------------------------------------------------------------------------------
process.qie11Digis = process.hcalDigis.clone()
process.hcalTupleQIE11Digis.chargeSkim = cms.untracked.double(0)
process.qie10Digis = process.hcalDigis.clone()
process.hcalTupleQIE10Digis.chargeSkim = cms.untracked.double(0)
#------------------------------------------------------------------------------------
# Specify Global Tag
#------------------------------------------------------------------------------------
process.load('Configuration.StandardSequences.FrontierConditions_GlobalTag_cff')
from Configuration.AlCa.GlobalTag import GlobalTag
#  process.GlobalTag = GlobalTag(process.GlobalTag, 'auto:phase2_realistic_T21', '')
#  process.GlobalTag = GlobalTag(process.GlobalTag, 'auto:phase1_2021_cosmics_0T', '')
process.GlobalTag.globaltag ='113X_dataRun3_HLT_v3'
#  process.GlobalTag.globaltag ='113X_dataRun3_HLT_Candidate_2021_07_02_14_05_25'
print "GlobalTag = ", str(process.GlobalTag.globaltag).split("'")[1]
print " "

print("Point 1")

#------------------------------------------------------------------------------------
# HcalTupleMaker sequence definition
#------------------------------------------------------------------------------------
process.tuple_step = cms.Sequence(
    ## Make HCAL tuples: Event info
    process.hcalTupleEvent*

    ## Make HCAL tuples: FED info
    #process.hcalTupleFEDs*

    ## Make HCAL tuples: digi info
    #  process.hcalTupleHBHEDigis*
    #  process.hcalTupleHODigis*
    #  process.hcalTupleHFDigis*
    process.hcalTupleQIE10Digis* # for HF
    process.hcalTupleQIE11Digis*
    #  process.hcalTupleHBHECosmicsDigis*

    ## Make HCAL tuples: reco info
    #process.hcalTupleHBHERecHits*
    #  process.hcalTupleHFRecHits*
    #process.hcalTupleHORecHits*

    ## Make HCAL tuples: trigger info
    #process.hcalTupleTrigger*
    #process.hcalTupleTriggerPrimitives*
    #process.hcalTupleTriggerObjects*

    # noise filter
#    process.hcalTupleHcalNoiseFilters*

    ## Package everything into a tree
    process.hcalTupleTree
)

#  from Configuration.StandardSequences.RawToDigi_Data_cff import RawToDigi

#  import inspect
#  print(inspect.getmembers(process.hcalTupleHFDigis))

print("Point 2")

#-----------------------------------------------------------------------------------
# Path and EndPath definitions
#-----------------------------------------------------------------------------------
process.preparation = cms.Path(
    process.my_hlt *
    #  process.hcalDigis*
    process.qie10Digis*
    process.qie11Digis*

    ## reconstruction
    #process.L1Reco*
    #process.reconstruction*
    #process.hcalLocalRecoSequence*

    ## Do energy reconstruction
    #process.horeco*
#    process.hfprereco*
#    process.hfreco*
#    process.hbheprereco*
#    process.hbheplan1*

    ## For noise filter
#    process.hcalnoise*
#    process.HBHENoiseFilterResultProducer*
    #process.ApplyBaselineHBHENoiseFilter*

    ## Make the ntuples
    process.tuple_step
)

print("Point 3")
