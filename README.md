# Author:  Alfredo Gurrola (Vanderbilt University), Anirban Saha (INFN)

1. export SCRAM_ARCH=slc6_amd64_gcc491  (or  setenv SCRAM_ARCH slc6_amd64_gcc491)
2. cmsrel CMSSW_7_1_14
3. cd CMSSW_7_1_14/src
4. cmsenv
5. git clone https://github.com/gurrola/SampleProducer
6. mv SampleProducer/script.csh .
7. mv SampleProducer/Configuration .
8. rm -rf SampleProducer
9. scramv1 b
10. ./script.csh
11. cmsRun STEP1_GEN-SIM.py
12. cmsRun STEP2.py
13. cmsRun STEP3.py
14. cmsRun STEP4.py
