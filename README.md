Alfredo Gurrola (Vanderbilt University), Anirban Saha (INFN), Stephan Lammel (FNAL)
===================================================================================

## Setup
```
export SCRAM_ARCH=slc6_amd64_gcc491  #or  setenv SCRAM_ARCH slc6_amd64_gcc491
cmsrel CMSSW_7_4_4
cd CMSSW_7_4_4/src
cmsenv
source /cvmfs/cms.cern.ch/crab3/crab.sh
git clone git@github.com:cms-sw/genproductions.git Configuration/GenProduction
scp Configuration/GenProduction/python/ThirteenTeV/Hadronizer_TuneCUETP8M1_13TeV_generic_LHE_pythia8_cff.py .
git clone https://github.com/gurrola/SampleProducer
mv SampleProducer/*.csh .
mv SamplerProducer/MadGraph5_v1.5.13.tar.gz .
mv SampleProducer/Configuration/GenProduction/python/ThirteenTeV/* Configuration/GenProduction/python/ThirteenTeV
rm -rf SampleProducer
tar -zxvf MadGraph5_v1.5.13.tar.gz
# open the relevant .csh file and change the number of events to generate:
#    --no_exec -n 10     change to     --no_exec -n 1
#    * above will set the number of events to generate to 1
scramv1 b
```

## To run:

### FullSim Zprime with PU (using Pythia8 as the generator)
```
./script.csh
cmsRun STEP1_GEN-SIM.py > GenOutput.log
cmsRun STEP2.py
cmsRun STEP3.py
cmsRun STEP4.py
```

### FastSim HeavyNu without PU (using Pythia6 as the generator)
```
./fastsim_heavyNu_pythia6_noPU.csh
./aodToMiniaod.csh
```

### FastSim Zprime without PU (using Pythia8 as the generator)
```
./fastsim_zprime.csh
./aodToMiniaod.csh 
```

### FastSim using an input LHE file
```
./fastsim_inputLHE.csh
./aodToMiniaod.csh
```

### Examine Generator
Let's look at:  `Configuration/GenProduction/python/ThirteenTeV/ZprimeToTauTau_M_4500_TuneCUETP8M1_tauola_13TeV_pythia8_cfi.py`
1. specifies the "generator":
    `generator = cms.EDFilter("Pythia8GeneratorFilter",`
2. specifies the center-of-mass energy:
    `comEnergy = cms.double(13000.0),`
3. dumps information for only 1 event:
    `maxEventsToPrint = cms.untracked.int32(1),`
4. tau decays are handled by another package (tauola):
    `ExternalDecays = cms.PSet(Tauola = cms.untracked.PSet(TauolaPolar, TauolaDefaultInputCards ),`
5. specifies the type of process (i.e. feynman diagram. In this case it's fermion+antifermion production a new boson)
    `'NewGaugeBoson:ffbar2gmZZprime = on',`
6. the new gauge boson is a Z':
    `'Zprime:gmZmode = 3',`
7. specifies the mass of the Z' (4500 GeV in this case):
    `'32:m0 = 4500',`
8. force the Z' to decay to a pair of tau leptons
    `'32:onIfAny = 15',`

### Examine Step1
Let's look at the cmsDriver commands for step #1:
1. uses the file `ZprimeToTauTau_M_4500_TuneCUETP8M1_tauola_13TeV_pythia8_cfi.py` as a template:
    `cmsDriver.py  Configuration/GenProduction/python/ThirteenTeV/ZprimeToTauTau_M_4500_TuneCUETP8M1_tauola_13TeV_pythia8_cfi.py`
2. name of the output file from step #1 (generation step):
    `--fileout GENSIM.root`
3. specifies the detector conditions that will be used for the RAW+SIM step ... need to specify this is Monte Carlo:
    `--customise SLHCUpgradeSimulations/Configuration/postLS1Customs.customisePostLS1`
    `--conditions auto:run2_mc`
4. specify the magnetic field strength:
    `--magField 38T_PostLS1`
5. produces a python file with all the above information that is ready for the user to run:
    `--python_filename STEP1_GEN-SIM.py`
6. how many events to generate?:
    `--no_exec -n 10`

### Examine Step2
Let's look at the cmsDriver commands for step #2:
1. specify input file from step #1
    `--filein file:GENSIM.root`
2. name of the output root file from step #2 (detector simulation):
    `--fileout RAWSIM.root`
3. energy from pileup is added "on top" of the "hard scatter" generation. This is taken from a separate file:
    ```--pileup_input dbs:/MinBias_TuneA2MB_13TeV-pythia8/Fall13-POSTLS162_V1-v1/GEN-SIM
    --pileup AVE_20_BX_25ns```
*** you need a grid certificate for this part to work ... otherwise, remove the above two lines from the cmsDriver command

### Examine Step3
Let's look at the cmsDriver commands for step #3:
1. specify the "CMS sequences"/"algorithms" used to produce "objects" (electrons, muons, taus, jets, etc.):
    `--step RAW2DIGI,L1Reco,RECO,EI`

### Examine Step4
Let's look at the cmsDriver commands for step #4:
1. specify the "CMS sequences" used to produce slimmed objects:
    `--step PAT`
