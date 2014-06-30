CSCValidation
=============

* This represents a compilation of scripts necessary to run several CSC Validation protocols. First look at the Twiki page concerning this 
  subject at (https://twiki.cern.ch/twiki/bin/viewauth/CMS/CSCValidationWebsite).:
  
  * Firstly, if the necessary data is contained in ".raw" format, it is likely a local run and will need to be converted. This format is 
    generally output from the RUIs of the subdetector, and are thus segmented in that fashion, i.e. RUI01 to RUI36 for all muon endcap CSCs. 
    Furthermore, these these outputs follow a naming format containing the run number, RUI number, and monitor. An example of how to run an
    automated script is in the folder "raw_process_example":
      
      * The file raw_process.py will use the template raw_template.py to output a configuration file which will be named according to the 
        local run's number. Simply make raw_process.py executable and run it with the appropriate system arguments (This is detailed in the 
        bash script "run_raw_process.sh", which can be run from the terminal). Should you wish to submit the process to batch, the file 
        "rawrun.sh" is a script which can be submitted. This can be modified for each user's working directory so that the root files are
        placed into the correct directories. 
        
  * 
