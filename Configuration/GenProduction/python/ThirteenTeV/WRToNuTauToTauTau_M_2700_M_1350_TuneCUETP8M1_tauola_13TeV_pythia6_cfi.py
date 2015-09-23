import FWCore.ParameterSet.Config as cms

from Configuration.Generator.PythiaUEZ2starSettings_cfi import *

generator = cms.EDFilter("Pythia6GeneratorFilter",
    pythiaHepMCVerbosity = cms.untracked.bool(False),
    maxEventsToPrint = cms.untracked.int32(0),
    pythiaPylistVerbosity = cms.untracked.int32(1),
    filterEfficiency = cms.untracked.double(1.),
    crossSection = cms.untracked.double(0.0343),
    comEnergy = cms.double(13000.0),
    PythiaParameters = cms.PSet(
        pythiaUESettingsBlock,
        processParameters = cms.vstring(
            'MSEL = 0      ! User defined process',
            'MSUB(354) = 1 ! Heavy neutrino',
            'MSTJ(41) = 2  ! Pythia QED bremsshtrahlung',
            'PMAS(C9900024,1) = 2700. ! WR Mass',
            'PMAS(C9900012,1) = 1350. ! nu_Re',
            'PMAS(C9900014,1) = 1350. ! nu_Rmu',
            'PMAS(C9900016,1) = 1350. ! nu_Rtau',
            '9900024:alloff',
            '9900024:onifany = 9900016'),
        parameterSets = cms.vstring('pythiaUESettings', 'processParameters')
    )
)

ProductionFilterSequence = cms.Sequence(generator)
