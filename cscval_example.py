# This represents a simple CSC Validation on a local run file. Ben Knapp, 28 May 2014.


import FWCore.ParameterSet.Config as cms

process = cms.Process("TEST")

process.load("Configuration/StandardSequences/Geometry_cff")
process.load("Configuration/StandardSequences/MagneticField_cff")
process.load("Configuration/StandardSequences/FrontierConditions_GlobalTag_cff")
process.load("Configuration/StandardSequences/RawToDigi_Data_cff")
process.load("Configuration.StandardSequences.Reconstruction_cff")
process.load('Configuration.StandardSequences.EndOfProcess_cff')

# As of 09.09.2013 only a temp gloabl tag exists for 620/700
process.GlobalTag.globaltag = 'GR_E_V37::All'

process.maxEvents = cms.untracked.PSet( input = cms.untracked.int32(1000) )
process.options = cms.untracked.PSet( SkipEvent = cms.untracked.vstring('ProductNotFound') )
process.source = cms.Source("PoolSource",
    fileNames = cms.untracked.vstring(
            'file:localrun_221859_01.root'
)
)

#The fileNames option uses 'file:' for local files, while those contained elsewhere may use their path names 





#This begins the modifications present in Tim Cox's codes

"""Customise digi/reco geometry to use unganged ME1/a channels"""
process.CSCGeometryESModule.useGangedStripsInME1a = False
process.idealForDigiCSCGeometry.useGangedStripsInME1a = False

"""Settings for the upgrade raw vs offline condition channel translation"""
process.CSCIndexerESProducer.AlgoName=cms.string("CSCIndexerPostls1")
process.CSCChannelMapperESProducer.AlgoName=cms.string("CSCChannelMapperPostls1")

process.csc2DRecHits.readBadChannels = cms.bool(False)
process.csc2DRecHits.CSCUseGasGainCorrection = cms.bool(False)


""" Pick up upgrade condions data directly from DB tags using ESPrefer's.
Might be useful when dealing with a global tag that doesn't include
'unganged' CSC conditions.
"""
myconds = [
        ('CSCDBGainsRcd', 'CSCDBGains_ungangedME11A_mc'),
        ('CSCDBNoiseMatrixRcd', 'CSCDBNoiseMatrix_ungangedME11A_mc'),
        ('CSCDBCrosstalkRcd', 'CSCDBCrosstalk_ungangedME11A_mc'),
        ('CSCDBPedestalsRcd', 'CSCDBPedestals_ungangedME11A_mc'),
        ('CSCDBGasGainCorrectionRcd', 'CSCDBGasGainCorrection_ungangedME11A_mc'),
        ('CSCDBChipSpeedCorrectionRcd', 'CSCDBChipSpeedCorrection_ungangedME11A_mc')
]

from CalibMuon.Configuration.getCSCConditions_frontier_cff import cscConditions
for (classname, tag) in myconds:
      print classname, tag
      sourcename = 'unganged_' + classname
      process.__setattr__(sourcename, cscConditions.clone())
      process.__getattribute__(sourcename).toGet = cms.VPSet( cms.PSet( record = cms.string(classname), tag = cms.string(tag)) )
      process.__getattribute__(sourcename).connect = cms.string('frontier://FrontierProd/CMS_COND_CSC_000')
      process.__setattr__('esp_' + classname, cms.ESPrefer("PoolDBESSource", sourcename) )

del cscConditions

#This ends the detector modification section






process.cscValidation = cms.EDAnalyzer("CSCValidation",
    rootFileName = cms.untracked.string('localrun_221859_01_out.root'),
    isSimulation = cms.untracked.bool(False),
    writeTreeToFile = cms.untracked.bool(True),
    useDigis = cms.untracked.bool(True),
    detailedAnalysis = cms.untracked.bool(False),
    useTriggerFilter = cms.untracked.bool(False),
    useQualityFilter = cms.untracked.bool(False),
    makeStandalonePlots = cms.untracked.bool(False),
    makeTimeMonitorPlots = cms.untracked.bool(True),
    rawDataTag = cms.InputTag("rawDataCollector"),
    alctDigiTag = cms.InputTag("muonCSCDigis","MuonCSCALCTDigi"),
    clctDigiTag = cms.InputTag("muonCSCDigis","MuonCSCCLCTDigi"),
    corrlctDigiTag = cms.InputTag("muonCSCDigis","MuonCSCCorrelatedLCTDigi"),
    stripDigiTag = cms.InputTag("muonCSCDigis","MuonCSCStripDigi"),
    wireDigiTag = cms.InputTag("muonCSCDigis","MuonCSCWireDigi"),
    compDigiTag = cms.InputTag("muonCSCDigis","MuonCSCComparatorDigi"),
    cscRecHitTag = cms.InputTag("csc2DRecHits"),
    cscSegTag = cms.InputTag("cscSegments"),
    saMuonTag = cms.InputTag("standAloneMuons"),
    l1aTag = cms.InputTag("gtDigis"),
    hltTag = cms.InputTag("TriggerResults::HLT"),
    makeHLTPlots = cms.untracked.bool(True),
    simHitTag = cms.InputTag("g4SimHits", "MuonCSCHits")
)

# From RECO
# process.p = cms.Path(process.cscValidation)
# From RAW
process.p = cms.Path(process.muonCSCDigis * process.csc2DRecHits * process.cscSegments * process.cscValidation)


# Path and EndPath definitions
##process.raw2digi_step = cms.Path(process.RawToDigi)
##process.reconstruction_step = cms.Path(process.reconstruction)
##process.cscvalidation_step = cms.Path(process.cscValidation)
process.endjob_step = cms.EndPath(process.endOfProcess)

# Schedule definition
##process.schedule = cms.Schedule(process.raw2digi_step,process.reconstruction_step,process.cscvalidation_step,process.endjob_step)
process.schedule = cms.Schedule(process.p,process.endjob_step)

