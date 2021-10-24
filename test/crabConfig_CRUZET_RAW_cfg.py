from WMCore.Configuration import Configuration
config = Configuration()
config.section_('General')
config.General.requestName = 'CRAFTRuns'
config.General.workArea = 'CRAFTCosRuns'
config.section_('JobType')
config.JobType.pluginName = 'Analysis'
config.JobType.psetName = 'cosmics_overnight_CRUZET_global_runs.py'
#config.JobType.maxMemoryMB = 2500
#config.JobType.inputFiles = ['Run_time.txt']
config.JobType.outputFiles = ['results_R343642.root']
config.section_('Data')
config.Data.inputDataset = '/Cosmics/Commissioning2021-v1/RAW'
config.Data.splitting = 'LumiBased'
#config.Data.totalUnits = -1
config.Data.unitsPerJob = 10
config.Data.outLFNDirBase = '/store/user/cisik/HCAL_CRUZET/'
#config.Data.lumiMask = 'Cert_294927-302663_13TeV_PromptReco_Collisions17_JSON.txt'
config.Data.runRange = '343642'
config.Data.outputDatasetTag = '113X_dataRun3_HLT_v3'
config.section_('Site')
config.Site.storageSite = 'T2_CH_CERN'
#config.Site.storageSite = 'T2_IT_Pisa'
#config.Site.blacklist = ['T3_US_Colorado']
#config.Site.whitelist = ['T2_CH_CERN']
