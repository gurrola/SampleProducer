# Author:  Alfredo Gurrola (Vanderbilt University), Anirban Saha (INFN), Stephan Lammel (FNAL)

1. export SCRAM_ARCH=slc6_amd64_gcc491  (or  setenv SCRAM_ARCH slc6_amd64_gcc491)
2. cmsrel CMSSW_7_4_4
3. cd CMSSW_7_4_4/src
4. cmsenv
5. source /cvmfs/cms.cern.ch/crab3/crab.sh
6. git clone git@github.com:cms-sw/genproductions.git Configuration/GenProduction
7. cp Configuration/GenProduction/python/ThirteenTeV/Hadronizer_TuneCUETP8M1_13TeV_generic_LHE_pythia8_cff.py .
8. git clone https://github.com/gurrola/SampleProducer
9. mv SampleProducer/*.csh .
10. mv SamplerProducer/MadGraph5_v1.5.13.tar.gz .
11. mv SampleProducer/Configuration/GenProduction/python/ThirteenTeV/* Configuration/GenProduction/python/ThirteenTeV
12. rm -rf SampleProducer
13. tar -zxvf MadGraph5_v1.5.13.tar.gz
14. open the relevant .csh file and change the number of events to generate:</br>
    --no_exec -n 10     change to     --no_exec -n 1
    * above will set the number of events to generate to 1
15. scramv1 b
16. To run:

    FullSim Zprime with PU</br>
    A. ./script.csh</br>
    B. cmsRun STEP1_GEN-SIM.py > GenOutput.log</br>
    C. cmsRun STEP2.py</br>
    D. cmsRun STEP3.py</br>
    E. cmsRun STEP4.py</br>

    FastSim HeavyNu without PU</br>
    A. ./fastsim_heavyNu_pythia6_noPU.csh</br>
    B. ./aodToMiniaod.csh </br>

Let's look at:  Configuration/GenProduction/python/ThirteenTeV/ZprimeToTauTau_M_4500_TuneCUETP8M1_tauola_13TeV_pythia8_cfi.py </br>
1. specifies the "generator":</br>
    generator = cms.EDFilter("Pythia8GeneratorFilter",</br>
2. specifies the center-of-mass energy:</br>
    comEnergy = cms.double(13000.0),</br>
3. dumps information for only 1 event:</br>
    maxEventsToPrint = cms.untracked.int32(1),</br>
4. tau decays are handled by another package (tauola):</br>
    ExternalDecays = cms.PSet(Tauola = cms.untracked.PSet(TauolaPolar, TauolaDefaultInputCards ),</br>
5. specifies the type of process (i.e. feynman diagram. In this case it's fermion+antifermion production a new boson)</br>
    'NewGaugeBoson:ffbar2gmZZprime = on',</br>
6. the new gauge boson is a Z':</br>
    'Zprime:gmZmode = 3',</br>
7. specifies the mass of the Z' (4500 GeV in this case):</br>
    '32:m0 = 4500',</br>
8. force the Z' to decay to a pair of tau leptons</br>
    '32:onIfAny = 15',</br>


Let's look at the cmsDriver commands for step #1:</br>
1. uses the file "ZprimeToTauTau_M_4500_TuneCUETP8M1_tauola_13TeV_pythia8_cfi.py" as a template:</br>
    cmsDriver.py  Configuration/GenProduction/python/ThirteenTeV/ZprimeToTauTau_M_4500_TuneCUETP8M1_tauola_13TeV_pythia8_cfi.py</br>
2. name of the output file from step #1 (generation step):</br>
    --fileout GENSIM.root</br>
3. specifies the detector conditions that will be used for the RAW+SIM step ... need to specify this is Monte Carlo:</br>
    --customise SLHCUpgradeSimulations/Configuration/postLS1Customs.customisePostLS1</br>
    --conditions auto:run2_mc</br>
4. specify the magnetic field strength:</br>
    --magField 38T_PostLS1</br>
5. produces a python file with all the above information that is ready for the user to run:</br>
    --python_filename STEP1_GEN-SIM.py</br>
6. how many events to generate?:</br>
    --no_exec -n 10</br>


Let's look at the cmsDriver commands for step #2:</br>
1. specify input file from step #1</br>
    --filein file:GENSIM.root</br>
2. name of the output root file from step #2 (detector simulation):</br>
    --fileout RAWSIM.root</br>
3. energy from pileup is added "on top" of the "hard scatter" generation. This is taken from a separate file:</br>
    --pileup_input dbs:/MinBias_TuneA2MB_13TeV-pythia8/Fall13-POSTLS162_V1-v1/GEN-SIM</br>
    --pileup AVE_20_BX_25ns</br>
*** you need a grid certificate for this part to work ... otherwise, remove the above two lines from the cmsDriver command

Let's look at the cmsDriver commands for step #3:</br>
1. specify the "CMS sequences"/"algorithms" used to produce "objects" (electrons, muons, taus, jets, etc.):</br>
    --step RAW2DIGI,L1Reco,RECO,EI</br>


Let's look at the cmsDriver commands for step #4:</br>
1. specify the "CMS sequences" used to produce slimmed objects:</br>
    --step PAT</br>
