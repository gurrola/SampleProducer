cmsDriver.py Configuration/GenProduction/python/ThirteenTeV/ZprimeToTauTau_M_4500_TuneCUETP8M1_tauola_13TeV_pythia8_cfi.py --fileout AODSIM.root --conditions MCRUN2_74_V9 --fast  -n 1000 --eventcontent AODSIM -s GEN,SIM,RECOBEFMIX,DIGI,L1,L1Reco,RECO,HLT:@frozen25ns --datatier AODSIM --beamspot NominalCollision2015 --customise SLHCUpgradeSimulations/Configuration/postLS1Customs.customisePostLS1 --magField 38T_PostLS1 --python_filename fastsim_zprime_cfg.py
