import FWCore.ParameterSet.Config as cms

process = cms.Process("reader")

process.maxEvents = cms.untracked.PSet( input = cms.untracked.int32(maxevents) )

process.load("FWCore.MessageLogger.MessageLogger_cfi")
process.MessageLogger.cout.placeholder = cms.untracked.bool(False)
process.MessageLogger.cout.threshold = cms.untracked.string('INFO')
process.MessageLogger.debugModules = cms.untracked.vstring('*')

process.options = cms.untracked.PSet( wantSummary = cms.untracked.bool(True) )

process.source = cms.Source("DaqSource",
    readerPluginName = cms.untracked.string('CSCFileReader'),
    readerPset = cms.untracked.PSet(
        firstEvent  = cms.untracked.int32(0),        
        FED750 = cms.untracked.vstring('RUI01','RUI02','RUI08','RUI09'),
        FED751 = cms.untracked.vstring('RUI03','RUI04','RUI05','RUI06', 'RUI07'),
        FED752 = cms.untracked.vstring('RUI10','RUI11','RUI17','RUI18'),        
        FED753 = cms.untracked.vstring('RUI12','RUI13','RUI14','RUI15','RUI16'),
        FED754 = cms.untracked.vstring('RUI19','RUI20','RUI26','RUI27'),
        FED755 = cms.untracked.vstring('RUI20','RUI21','RUI22','RUI23','RUI24','RUI25'),
        FED756 = cms.untracked.vstring('RUI28','RUI29','RUI35','RUI36'),
        FED757 = cms.untracked.vstring('RUI30','RUI31','RUI32','RUI33','RUI34')
  )
)

process.FEVT = cms.OutputModule("PoolOutputModule",
        fileName = cms.untracked.string("localrun_runnumber.root"),
        outputCommands = cms.untracked.vstring("keep *")
)

process.outpath = cms.EndPath(process.FEVT)
