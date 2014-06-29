import FWCore.ParameterSet.Config as cms

process = cms.Process("reader")

process.maxEvents = cms.untracked.PSet( input = cms.untracked.int32(500) )

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
,        RUI01 = cms.untracked.vstring('/afs/cern.ch/user/b/beknapp/localruns/run222065/csc_00222065_EmuRUI01_Monitor_000.raw')
,        RUI02 = cms.untracked.vstring('/afs/cern.ch/user/b/beknapp/localruns/run222065/csc_00222065_EmuRUI02_Monitor_000.raw')
,        RUI03 = cms.untracked.vstring('/afs/cern.ch/user/b/beknapp/localruns/run222065/csc_00222065_EmuRUI03_Monitor_000.raw')
,        RUI04 = cms.untracked.vstring('/afs/cern.ch/user/b/beknapp/localruns/run222065/csc_00222065_EmuRUI04_Monitor_000.raw')
,        RUI05 = cms.untracked.vstring('/afs/cern.ch/user/b/beknapp/localruns/run222065/csc_00222065_EmuRUI05_Monitor_000.raw')
,        RUI06 = cms.untracked.vstring('/afs/cern.ch/user/b/beknapp/localruns/run222065/csc_00222065_EmuRUI06_Monitor_000.raw')
,        RUI07 = cms.untracked.vstring('/afs/cern.ch/user/b/beknapp/localruns/run222065/csc_00222065_EmuRUI07_Monitor_000.raw')
,        RUI08 = cms.untracked.vstring('/afs/cern.ch/user/b/beknapp/localruns/run222065/csc_00222065_EmuRUI08_Monitor_000.raw')
,        RUI09 = cms.untracked.vstring('/afs/cern.ch/user/b/beknapp/localruns/run222065/csc_00222065_EmuRUI09_Monitor_000.raw')
,        RUI10 = cms.untracked.vstring('/afs/cern.ch/user/b/beknapp/localruns/run222065/csc_00222065_EmuRUI10_Monitor_000.raw')
,        RUI11 = cms.untracked.vstring('/afs/cern.ch/user/b/beknapp/localruns/run222065/csc_00222065_EmuRUI11_Monitor_000.raw')
,        RUI12 = cms.untracked.vstring('/afs/cern.ch/user/b/beknapp/localruns/run222065/csc_00222065_EmuRUI12_Monitor_000.raw')
,        RUI13 = cms.untracked.vstring('/afs/cern.ch/user/b/beknapp/localruns/run222065/csc_00222065_EmuRUI13_Monitor_000.raw')
,        RUI14 = cms.untracked.vstring('/afs/cern.ch/user/b/beknapp/localruns/run222065/csc_00222065_EmuRUI14_Monitor_000.raw')
,        RUI15 = cms.untracked.vstring('/afs/cern.ch/user/b/beknapp/localruns/run222065/csc_00222065_EmuRUI15_Monitor_000.raw')
,        RUI16 = cms.untracked.vstring('/afs/cern.ch/user/b/beknapp/localruns/run222065/csc_00222065_EmuRUI16_Monitor_000.raw')
,        RUI17 = cms.untracked.vstring('/afs/cern.ch/user/b/beknapp/localruns/run222065/csc_00222065_EmuRUI17_Monitor_000.raw')
,        RUI18 = cms.untracked.vstring('/afs/cern.ch/user/b/beknapp/localruns/run222065/csc_00222065_EmuRUI18_Monitor_000.raw')
,        RUI19 = cms.untracked.vstring('/afs/cern.ch/user/b/beknapp/localruns/run222065/csc_00222065_EmuRUI19_Monitor_000.raw')
,        RUI20 = cms.untracked.vstring('/afs/cern.ch/user/b/beknapp/localruns/run222065/csc_00222065_EmuRUI20_Monitor_000.raw')
,        RUI21 = cms.untracked.vstring('/afs/cern.ch/user/b/beknapp/localruns/run222065/csc_00222065_EmuRUI21_Monitor_000.raw')
,        RUI22 = cms.untracked.vstring('/afs/cern.ch/user/b/beknapp/localruns/run222065/csc_00222065_EmuRUI22_Monitor_000.raw')
,        RUI23 = cms.untracked.vstring('/afs/cern.ch/user/b/beknapp/localruns/run222065/csc_00222065_EmuRUI23_Monitor_000.raw')
,        RUI24 = cms.untracked.vstring('/afs/cern.ch/user/b/beknapp/localruns/run222065/csc_00222065_EmuRUI24_Monitor_000.raw')
,        RUI25 = cms.untracked.vstring('/afs/cern.ch/user/b/beknapp/localruns/run222065/csc_00222065_EmuRUI25_Monitor_000.raw')
,        RUI26 = cms.untracked.vstring('/afs/cern.ch/user/b/beknapp/localruns/run222065/csc_00222065_EmuRUI26_Monitor_000.raw')
,        RUI27 = cms.untracked.vstring('/afs/cern.ch/user/b/beknapp/localruns/run222065/csc_00222065_EmuRUI27_Monitor_000.raw')
,        RUI28 = cms.untracked.vstring('/afs/cern.ch/user/b/beknapp/localruns/run222065/csc_00222065_EmuRUI28_Monitor_000.raw')
,        RUI29 = cms.untracked.vstring('/afs/cern.ch/user/b/beknapp/localruns/run222065/csc_00222065_EmuRUI29_Monitor_000.raw')
,        RUI30 = cms.untracked.vstring('/afs/cern.ch/user/b/beknapp/localruns/run222065/csc_00222065_EmuRUI30_Monitor_000.raw')
,        RUI31 = cms.untracked.vstring('/afs/cern.ch/user/b/beknapp/localruns/run222065/csc_00222065_EmuRUI31_Monitor_000.raw')
,        RUI32 = cms.untracked.vstring('/afs/cern.ch/user/b/beknapp/localruns/run222065/csc_00222065_EmuRUI32_Monitor_000.raw')
,        RUI33 = cms.untracked.vstring('/afs/cern.ch/user/b/beknapp/localruns/run222065/csc_00222065_EmuRUI33_Monitor_000.raw')
,        RUI34 = cms.untracked.vstring('/afs/cern.ch/user/b/beknapp/localruns/run222065/csc_00222065_EmuRUI34_Monitor_000.raw')
,        RUI35 = cms.untracked.vstring('/afs/cern.ch/user/b/beknapp/localruns/run222065/csc_00222065_EmuRUI35_Monitor_000.raw')
,        RUI36 = cms.untracked.vstring('/afs/cern.ch/user/b/beknapp/localruns/run222065/csc_00222065_EmuRUI36_Monitor_000.raw')
  )
)

process.FEVT = cms.OutputModule("PoolOutputModule",
        fileName = cms.untracked.string("localrun_222065.root"),
        outputCommands = cms.untracked.vstring("keep *")
)

process.outpath = cms.EndPath(process.FEVT)
