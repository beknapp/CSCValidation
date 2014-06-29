#!/bin/bash
cd /afs/cern.ch/user/b/beknapp/RAWruns/CMSSW_6_2_8/src/
eval `scramv1 runtime -sh`
cd - 

cmsRun /afs/cern.ch/user/b/beknapp/RAWruns/CMSSW_6_2_8/src/RecoLocalMuon/CSCValidation/LOCALRUN_OUTPUT/COMPLETE_AUTO/scratch/process_run_222065.py

cp *root /afs/cern.ch/user/b/beknapp/RAWruns/CMSSW_6_2_8/src/RecoLocalMuon/CSCValidation/LOCALRUN_OUTPUT/COMPLETE_AUTO/scratch
