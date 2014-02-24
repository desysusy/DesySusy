#!/usr/bin/python
import sys, os
import commands as com
from SetUpSample import SetUpSampleAndScript


#
#
def SampleFromSubSamples(SubSampleList):
    """dont know yet """
    
def cleanUpDir(outdir):
    #out=com.getoutput("rm -f merge_script.o*")
    file=open("cleanUpDir","w")
    out=com.getoutput('chmod u+x cleanUpDir')
    print outdir
    line='rm -f merge_script.o*'
    file.write(line+'\n')
    file.close()
    out=com.getoutput("mv cleanUpDir "+outdir+"/")

def makeScriptFromInfoPack(Sample,Config,InfoPack,makeAllScript):
    Scripts=[]
    for pack in InfoPack:
        SubSample=pack[0]
        FilesDir=pack[1]
        nFiles=pack[2]
        script=SetUpSampleAndScript(Sample,SubSample,FilesDir,Config,nFiles)        
        cleanUpDir('./'+Sample+'/'+SubSample)
        Scripts.append(script)
    #
    
    if makeAllScript:
        allfile=open('runall_'+Sample+'_ALL','w')
        for scr in Scripts:
            line='./'+scr+' $1 $2'
            allfile.write(line+'\n')
            #
        #
        allfile.close()
        out=com.getoutput('chmod u+x runall_'+Sample+'_ALL')

def MuHad():
    Sample='SingleMu'
    Config='config_Data_Stop.txt'
    nFiles=6
    InfoPack=[]

    SubSample='Run2012A-13JulReReco'
    FilesDir='/nfs/dust/cms/user/sahin/ntuple14_v1/CMSSW_5_3_3_patch2/src/SUSYBSMAnalysis/SusyCAF/test/naf_MuHad_Run2012A13Jul_cfg/'
    InfoPack.append((SubSample,FilesDir,nFiles))
    #
    SubSample='Run2012A-06AugReReco'
    FilesDir='/nfs/dust/cms/user/fcost/store/NTuple13_v2/MuHad/Run2012A-recover-06Aug2012-v1/'
    InfoPack.append((SubSample,FilesDir,nFiles))
    #
    SubSample='Run2012B-13JulReReco'
    FilesDir='/nfs/dust/cms/user/sahin/ntuple14_v1/CMSSW_5_3_3_patch2/src/SUSYBSMAnalysis/SusyCAF/test/naf_MuHad_Run2012B13Jul_cfg/'
    InfoPack.append((SubSample,FilesDir,nFiles))    
    #
    #
    makeScriptFromInfoPack(Sample,Config,InfoPack,True)        
    #=======================================        

def SingleMu():

    Sample='SingleMu'
    Config='config_Data_Stop.txt'
    nFiles=6
    InfoPack=[]
    
    SubSample='Run2012A-13JulReReco'
    FilesDir='/nfs/dust/cms/user/fcost/store/NTuple13_v2/SingleMu/Run2012A-13Jul2012-v1/'
    InfoPack.append((SubSample,FilesDir,nFiles))
    #
    SubSample='Run2012A-06AugReReco'
    FilesDir='/nfs/dust/cms/user/fcost/store/NTuple13_v2/SingleMu/Run2012A-recover-06Aug2012-v1/'
    InfoPack.append((SubSample,FilesDir,nFiles))
    #
    SubSample='Run2012B-13JulReReco'
    FilesDir='/nfs/dust/cms/user/fcost/store/NTuple13_v2/SingleMu/Run2012B-13Jul2012-v1/'
    InfoPack.append((SubSample,FilesDir,nFiles))    
    #
    SubSample='Run2012C-24Aug2012-v1'
    FilesDir='/pnfs/desy.de/cms/tier2/store/user/fcostanz/NTuple13_v1/SingleMu/Run2012C-24Aug2012-v1/'
    InfoPack.append((SubSample,FilesDir,nFiles))    
    #
    SubSample='Run2012C-PromptReco-v2'
    FilesDir='/pnfs/desy.de/cms/tier2/store/user/fcostanz/NTuple13_v1/SingleMu/Run2012C-PromptReco-v2/'
    InfoPack.append((SubSample,FilesDir,nFiles))    
    #    
    SubSample='Run2012D-PromptReco-v1'
    FilesDir='/pnfs/desy.de/cms/tier2/store/user/fcostanz/NTuple13_v1/SingleMu/Run2012D-PromptReco-v1/'
    InfoPack.append((SubSample,FilesDir,nFiles))
    #
    #
    makeScriptFromInfoPack(Sample,Config,InfoPack,True)        
    #=======================================

def SingleElectron():

    Sample='SingleElectron'
    Config='config_Data_Stop.txt'
    InfoPack=[]
    nFiles=6
    
    SubSample='Run2012A-13JulReReco'
    FilesDir='/nfs/dust/cms/user/lobanov/SUSY/nTupler13/data/SingleElectron/Run2012A-13Jul2012-v1/'
    InfoPack.append((SubSample,FilesDir,nFiles))
    #
    SubSample='Run2012A-06AugReReco'
    FilesDir='/nfs/dust/cms/user/lobanov/SUSY/nTupler13/data/SingleElectron/Run2012A-recover-06Aug2012-v1/'
    InfoPack.append((SubSample,FilesDir,nFiles))
    #
    SubSample='Run2012B-13JulReReco'
    FilesDir='/nfs/dust/cms/user/lobanov/SUSY/nTupler13/data/SingleElectron/Run2012B-13Jul2012-v1/'
    InfoPack.append((SubSample,FilesDir,nFiles))    
    #
    SubSample='Run2012C-24Aug2012-v1'
    FilesDir='/nfs/dust/cms/user/lobanov/SUSY/nTupler13/data/SingleElectron/Run2012C-24Aug2012-v1/'
    InfoPack.append((SubSample,FilesDir,nFiles))    
    #
    SubSample='Run2012C-PromptReco-v2'
    FilesDir='/nfs/dust/cms/user/lobanov/SUSY/nTupler13/data/SingleElectron/Run2012C-PromptReco-v2/'
    InfoPack.append((SubSample,FilesDir,nFiles))    
    #    
    SubSample='Run2012D-PromptReco-v1'
    FilesDir='/nfs/dust/cms/user/kruecker/desysusy/artur/nTupler13/data/SingleElectron/Run2012D-PromptReco-v1/'
    InfoPack.append((SubSample,FilesDir,nFiles))
    #
    #
    makeScriptFromInfoPack(Sample,Config,InfoPack,True)        
    #=======================================

def TTJetsPOWHEG():
    Sample='TTJetsPOWHEG'
    Config='config_FullSim_Stop.txt'
    nFiles=8
    InfoPack=[]
    #
    SubSample='DR53-v1'    
    FileDir='/pnfs/desy.de/cms/tier2/store/user/msahin/nTuple13_v2/mc/TT_CT10_TuneZ2star_8TeV-powheg-tauola/Summer12_DR53X-PU_S10_START53_V7A-v1/'
    InfoPack.append((SubSample,FilesDir,nFiles))    
    #
    SubSample='DR53-v2'
    FileDir='/pnfs/desy.de/cms/tier2/store/user/fcostanz/nTuple13_v2/TT_CT10_TuneZ2star_8TeV-powheg-tauola/Summer12_DR53X-PU_S10_START53_V7A-v2/'
    InfoPack.append((SubSample,FilesDir,nFiles))
    #
    SubSample='DiLeptv1'    
    FileDir='/pnfs/desy.de/cms/tier2/store/user/msahin/nTuple13_v2/mc/TT_CT10_TuneZ2star_8TeV-powheg-tauola/Summer12_DR53X-PU_S10_START53_V7A-v1/'
    InfoPack.append((SubSample,FilesDir,nFiles))    
    #
    SubSample='SemiLeptv1'    
    FileDir='/pnfs/desy.de/cms/tier2/store/user/msahin/nTuple13_v2/mc/TT_CT10_TuneZ2star_8TeV-powheg-tauola/Summer12_DR53X-PU_S10_START53_V7A-v1/'
    InfoPack.append((SubSample,FilesDir,nFiles))    
    #
    SubSample='DR53-v1'    
    FileDir='/pnfs/desy.de/cms/tier2/store/user/msahin/nTuple13_v2/mc/TT_CT10_TuneZ2star_8TeV-powheg-tauola/Summer12_DR53X-PU_S10_START53_V7A-v1/'
    InfoPack.append((SubSample,FilesDir,nFiles))    
    #
    SubSample='FullyHadv2'
    FileDir='/pnfs/desy.de/cms/tier2/store/user/fcostanz/nTuple13_v2/TT_CT10_TuneZ2star_8TeV-powheg-tauola/Summer12_DR53X-PU_S10_START53_V7A-v2/'
    InfoPack.append((SubSample,FilesDir,nFiles))
    #
    SubSample='SemiLeptv2'
    FileDir='/pnfs/desy.de/cms/tier2/store/user/fcostanz/nTuple13_v2/TT_CT10_TuneZ2star_8TeV-powheg-tauola/Summer12_DR53X-PU_S10_START53_V7A-v2/'
    InfoPack.append((SubSample,FilesDir,nFiles))
    #
    SubSample='DiLeptv2'
    FileDir='/pnfs/desy.de/cms/tier2/store/user/fcostanz/nTuple13_v2/TT_CT10_TuneZ2star_8TeV-powheg-tauola/Summer12_DR53X-PU_S10_START53_V7A-v2/'
    InfoPack.append((SubSample,FilesDir,nFiles))
    #
    #
    makeScriptFromInfoPack(Sample,Config,InfoPack,True)        
    #=======================================

                    
def TTJetsMG():
    Sample='TTJetsMG'
    Config='config_FullSim_Stop.txt'
    nFiles=3
    InfoPack=[]
    #
    SubSample='FullyHad'
    FileDir='/nfs/dust/cms/user/fcost/store/NTuple13_v2/TTJets_HadronicMGDecays_8TeV-madgraph/Summer12_DR53X-PU_S10_START53_V7A_ext-v1/'
    InfoPack.append((SubSample,FilesDir,nFiles))
    #
    SubSample='SemiLept'
    FileDir='/pnfs/desy.de/cms/tier2/store/user/fcostanz/nTuple13_v2/mc/TTJets_SemiLeptMGDecays_8TeV-madgraph/Summer12_DR53X-PU_S10_START53_V7A_ext-v1/'
    InfoPack.append((SubSample,FilesDir,nFiles))        
    #
    SubSample='DiLept'
    FileDir='/nfs/dust/cms/user/fcost/store/NTuple13_v2/TTJets_FullLeptMGDecays_8TeV-madgraph/Summer12_DR53X-PU_S10_START53_V7A-v2/'
    InfoPack.append((SubSample,FilesDir,nFiles))        
    #
    #
    makeScriptFromInfoPack(Sample,Config,InfoPack,True)        
    #=======================================

def TTJetsMCatNLO():
    Sample='TTJetsMCatNLO'
    Config='config_FullSim_Stop.txt'
    nFiles=16
    InfoPack=[]
    
    SubSample='NoSub'
    FileDir='/pnfs/desy.de/cms/tier2/store/user/fcostanz/nTuple13_v2/mc/TT_8TeV-mcatnlo/Summer12_DR53X-PU_S10_START53_V7A-v1'
    InfoPack.append((SubSample,FilesDir,nFiles))
    #
    SubSample='FullyHad'
    FileDir='/pnfs/desy.de/cms/tier2/store/user/fcostanz/nTuple13_v2/mc/TT_8TeV-mcatnlo/Summer12_DR53X-PU_S10_START53_V7A-v1'
    InfoPack.append((SubSample,FilesDir,nFiles))
    #
    SubSample='SemiLept'
    FileDir='/pnfs/desy.de/cms/tier2/store/user/fcostanz/nTuple13_v2/mc/TT_8TeV-mcatnlo/Summer12_DR53X-PU_S10_START53_V7A-v1'
    InfoPack.append((SubSample,FilesDir,nFiles))
    #
    SubSample='DiLept'
    FileDir='/pnfs/desy.de/cms/tier2/store/user/fcostanz/nTuple13_v2/mc/TT_8TeV-mcatnlo/Summer12_DR53X-PU_S10_START53_V7A-v1'
    InfoPack.append((SubSample,FilesDir,nFiles))
    #    
    #
    makeScriptFromInfoPack(Sample,Config,InfoPack,True)        
    #=======================================


def TTJetsSys():
    Sample='TTJetsSys'
    Config='config_FullSim_Stop.txt'
    nFiles=8
    InfoPack=[]
    
    SubSample='ScaleUpSemiLept'
    FileDir='/pnfs/desy.de/cms/tier2/store/user/fcostanz/nTuple13_v2/mc/TTJets_scaleup_TuneZ2star_8TeV-madgraph-tauola/Summer12_DR53X-PU_S10_START53_V7A-v1/'
    InfoPack.append((SubSample,FilesDir,nFiles))
    #
    SubSample='ScaleUpDiLept'
    FileDir='/pnfs/desy.de/cms/tier2/store/user/fcostanz/nTuple13_v2/mc/TTJets_scaleup_TuneZ2star_8TeV-madgraph-tauola/Summer12_DR53X-PU_S10_START53_V7A-v1/'
    InfoPack.append((SubSample,FilesDir,nFiles))
    #
    SubSample='ScaleDownSemiLept'
    FileDir='/pnfs/desy.de/cms/tier2/store/user/fcostanz/nTuple13_v2/mc/TTJets_scaledown_TuneZ2star_8TeV-madgraph-tauola/Summer12_DR53X-PU_S10_START53_V7A-v1/'
    InfoPack.append((SubSample,FilesDir,nFiles))
    #    
    SubSample='ScaleDownDiLept'
    FileDir='/pnfs/desy.de/cms/tier2/store/user/fcostanz/nTuple13_v2/mc/TTJets_scaledown_TuneZ2star_8TeV-madgraph-tauola/Summer12_DR53X-PU_S10_START53_V7A-v1/'
    InfoPack.append((SubSample,FilesDir,nFiles))
    #
    SubSample='MatchUpSemiLept'
    FileDir='/pnfs/desy.de/cms/tier2/store/user/fcostanz/nTuple13_v2/mc/TTJets_matchingup_TuneZ2star_8TeV-madgraph-tauola/Summer12_DR53X-PU_S10_START53_V7A-v1/'
    InfoPack.append((SubSample,FilesDir,nFiles))
    #  
    SubSample='MatchUpDiLept'
    FileDir='/pnfs/desy.de/cms/tier2/store/user/fcostanz/nTuple13_v2/mc/TTJets_matchingup_TuneZ2star_8TeV-madgraph-tauola/Summer12_DR53X-PU_S10_START53_V7A-v1/'
    InfoPack.append((SubSample,FilesDir,nFiles))
    #
    SubSample='MatchDownSemiLept'
    FileDir='/pnfs/desy.de/cms/tier2/store/user/fcostanz/nTuple13_v2/mc/TTJets_matchingdown_TuneZ2star_8TeV-madgraph-tauola/Summer12_DR53X-PU_S10_START53_V7A-v1/'
    InfoPack.append((SubSample,FilesDir,nFiles))
    #
    SubSample='MatchDownDiLept'
    FileDir='/pnfs/desy.de/cms/tier2/store/user/fcostanz/nTuple13_v2/mc/TTJets_matchingdown_TuneZ2star_8TeV-madgraph-tauola/Summer12_DR53X-PU_S10_START53_V7A-v1/'
    InfoPack.append((SubSample,FilesDir,nFiles))
    #
    SubSample='Mass166p5SemiLept'
    FileDir='/pnfs/desy.de/cms/tier2/store/user/fcostanz/nTuple13_v2/mc2/TTJets_mass166_5_TuneZ2star_8TeV-madgraph-tauola/Summer12_DR53X-PU_S10_START53_V7A-v1/'
    InfoPack.append((SubSample,FilesDir,nFiles))
    #
    SubSample='Mass166p5DiLept'
    FileDir='/pnfs/desy.de/cms/tier2/store/user/fcostanz/nTuple13_v2/mc2/TTJets_mass166_5_TuneZ2star_8TeV-madgraph-tauola/Summer12_DR53X-PU_S10_START53_V7A-v1/'
    InfoPack.append((SubSample,FilesDir,nFiles))
    #
    SubSample='Mass178p5SemiLept'
    FileDir='/pnfs/desy.de/cms/tier2/store/user/fcostanz/nTuple13_v2/mc2/TTJets_mass178_5_TuneZ2star_8TeV-madgraph-tauola/Summer12_DR53X-PU_S10_START53_V7A-v1/'
    InfoPack.append((SubSample,FilesDir,nFiles))
    #
    SubSample='Mass178p5DiLept'
    FileDir='/pnfs/desy.de/cms/tier2/store/user/fcostanz/nTuple13_v2/mc2/TTJets_mass178_5_TuneZ2star_8TeV-madgraph-tauola/Summer12_DR53X-PU_S10_START53_V7A-v1/'
    InfoPack.append((SubSample,FilesDir,nFiles))
    #
    #
    makeScriptFromInfoPack(Sample,Config,InfoPack,True)        
    #=======================================
    
def DYJetsToLL():
    Sample='DYJetsToLL'
    Config='config_FullSim_Stop.txt'
    nFiles=5
    InfoPack='[]'
    
    SubSample='M10To50'
    FileDir='/nfs/dust/cms/user/fcost/store/NTuple13_v2/DYJetsToLL_M-10To50_TuneZ2Star_8TeV-madgraph/Summer12_DR53X-PU_S10_START53_V7A-v1/'
    InfoPack.append((SubSample,FilesDir,nFiles))
    #
    SubSample='M50ToInf'
    FileDir='/pnfs/desy.de/cms/tier2/store/user/fcostanz/nTuple13_v2/mc/DYJetsToLL_M-50_TuneZ2Star_8TeV-madgraph-tarball/Summer12_DR53X-PU_S10_START53_V7A-v1/'
    InfoPack.append((SubSample,FilesDir,nFiles))
    #
    #
    makeScriptFromInfoPack(Sample,Config,InfoPack,True)        
    #=======================================
    
def WJetsToLNu():
    Sample='WJetsToLNu'
    Config='config_FullSim_Stop.txt'
    nFiles=9
    InfoPack=[]
    
    SubSample='Inclusive'
    FileDir='/pnfs/desy.de/cms/tier2/store/user/fcostanz/nTuple13_v2/mc/WJetsToLNu_TuneZ2Star_8TeV-madgraph-tarball/Summer12_DR53X-PU_S10_START53_V7A-v1/'
    InfoPack.append((SubSample,FilesDir,nFiles))
    #
    SubSample='1Jet'
    FileDir='/nfs/dust/cms/user/kruecker/desysusy/francesco/NTuple13_v2/W1JetsToLNu_TuneZ2Star_8TeV-madgraph/Summer12_DR53X-PU_S10_START53_V7A-v1/'
    InfoPack.append((SubSample,FilesDir,nFiles))
    #
    SubSample='2Jets'
    FileDir='/nfs/dust/cms/user/kruecker/desysusy/francesco/NTuple13_v2/W2JetsToLNu_TuneZ2Star_8TeV-madgraph/Summer12_DR53X-PU_S10_START53_V7A-v1/'
    InfoPack.append((SubSample,FilesDir,nFiles))
    #
    SubSample='3Jets'
    FileDir='/nfs/dust/cms/user/kruecker/desysusy/francesco/NTuple13_v2/W3JetsToLNu_TuneZ2Star_8TeV-madgraph/Summer12_DR53X-PU_S10_START53_V7A-v1/'
    InfoPack.append((SubSample,FilesDir,nFiles))
    #
    SubSample='4Jets'
    FileDir='/nfs/dust/cms/user/kruecker/desysusy/francesco/NTuple13_v2/W4JetsToLNu_TuneZ2Star_8TeV-madgraph/Summer12_DR53X-PU_S10_START53_V7A-v1/'
    InfoPack.append((SubSample,FilesDir,nFiles))
    #
    #
    makeScriptFromInfoPack(Sample,Config,InfoPack,True)        
    #=======================================


def SingleTop():
    Sample='SingleTop'
    Config='config_FullSim_Stop.txt'
    nFiles=9
    InfoPack=[]
    
    SubSample='TBarToDilepton-tW'
    FileDir='/nfs/dust/cms/user/fcost/store/NTuple13_v2/TBarToDilepton_tW-channel-DR_8TeV-powheg-tauola/Summer12_DR53X-PU_S10_START53_V7A-v1/'
    InfoPack.append((SubSample,FilesDir,nFiles))
    #
    SubSample='TBarToLeptons-s'
    FileDir='/nfs/dust/cms/user/fcost/store/NTuple13_v2/TBarToLeptons_s-channel_8TeV-powheg-tauola/Summer12_DR53X-PU_S10_START53_V7A-v1/'
    InfoPack.append((SubSample,FilesDir,nFiles))
    #
    SubSample='TBarToLeptons-t'
    FileDir='/nfs/dust/cms/user/fcost/store/NTuple13_v2/TBarToLeptons_t-channel_8TeV-powheg-tauola/Summer12_DR53X-PU_S10_START53_V7A-v1/'
    InfoPack.append((SubSample,FilesDir,nFiles))
    #
    SubSample='TBarToThadWlep-tW'
    FileDir='/nfs/dust/cms/user/fcost/store/NTuple13_v2/TBarToThadWlep_tW-channel-DR_8TeV-powheg-tauola/Summer12_DR53X-PU_S10_START53_V7A-v1/'
    InfoPack.append((SubSample,FilesDir,nFiles))
    #
    SubSample='TBarToTlepWhad-tW'
    FileDir='/nfs/dust/cms/user/fcost/store/NTuple13_v2/TBarToTlepWhad_tW-channel-DR_8TeV-powheg-tauola/Summer12_DR53X-PU_S10_START53_V7A-v1/'
    InfoPack.append((SubSample,FilesDir,nFiles))
    #
    SubSample='TToDilepton-tW'
    FileDir='/nfs/dust/cms/user/fcost/store/NTuple13_v2/TToDilepton_tW-channel-DR_8TeV-powheg-tauola/Summer12_DR53X-PU_S10_START53_V7A-v1/'
    InfoPack.append((SubSample,FilesDir,nFiles))
    #
    SubSample='TToLeptons-s'
    FileDir='/nfs/dust/cms/user/fcost/store/NTuple13_v2/TToLeptons_s-channel_8TeV-powheg-tauola/Summer12_DR53X-PU_S10_START53_V7A-v1/'
    InfoPack.append((SubSample,FilesDir,nFiles))
    #
    SubSample='TToLeptons-t'
    FileDir='/nfs/dust/cms/user/fcost/store/NTuple13_v2/TToLeptons_t-channel_8TeV-powheg-tauola/Summer12_DR53X-PU_S10_START53_V7A-v1/'
    InfoPack.append((SubSample,FilesDir,nFiles))
    #
    SubSample='TToThadWlep-tW'
    FileDir='/nfs/dust/cms/user/fcost/store/NTuple13_v2/TToThadWlep_tW-channel-DR_8TeV-powheg-tauola/Summer12_DR53X-PU_S10_START53_V7A-v1/'
    InfoPack.append((SubSample,FilesDir,nFiles))
    #
    SubSample='TToTlepWhad-tW'
    FileDir='/nfs/dust/cms/user/fcost/store/NTuple13_v2/TToTlepWhad_tW-channel-DR_8TeV-powheg-tauola/Summer12_DR53X-PU_S10_START53_V7A-v1/'
    InfoPack.append((SubSample,FilesDir,nFiles))
    #
    #
    makeScriptFromInfoPack(Sample,Config,InfoPack,True)        
    #=======================================    


def DiBoson():
    Sample='DiBoson'
    Config='config_FullSim_Stop.txt'
    nFiles=6
    InfoPack=[]
    #
    SubSample='ZZJetsTo4'
    FilesDir='/pnfs/desy.de/cms/tier2/store/user/fcostanz/NTuple13_v1/ZZJetsTo4L_TuneZ2star_8TeV-madgraph-tauola/Summer12_DR53X-PU_S10_START53_V7A-v1/'
    InfoPack.append((SubSample,FilesDir,nFiles))
    #
    SubSample='WZJetsTo3LNu'
    FilesDir='/pnfs/desy.de/cms/tier2/store/user/fcostanz/NTuple13_v1/WZJetsTo3LNu_TuneZ2_8TeV-madgraph-tauola/Summer12_DR53X-PU_S10_START53_V7A-v1/'
    InfoPack.append((SubSample,FilesDir,nFiles))
    #
    SubSample='WWJetsTo2L2Nu'
    FilesDir='/pnfs/desy.de/cms/tier2/store/user/fcostanz/NTuple13_v1/WWJetsTo2L2Nu_TuneZ2star_8TeV-madgraph-tauola/Summer12_DR53X-PU_S10_START53_V7A-v1/'
    InfoPack.append((SubSample,FilesDir,nFiles))
    #
    SubSample='ZZJetsTo2L2Nu'
    FilesDir='/pnfs/desy.de/cms/tier2/store/user/fcostanz/NTuple13_v1/ZZJetsTo2L2Nu_TuneZ2star_8TeV-madgraph-tauola/Summer12_DR53X-PU_S10_START53_V7A-v3/'
    InfoPack.append((SubSample,FilesDir,nFiles))
    #
    SubSample='ZZJetsTo2L2Q'
    FilesDir='/pnfs/desy.de/cms/tier2/store/user/fcostanz/NTuple13_v1/ZZJetsTo2L2Q_TuneZ2star_8TeV-madgraph-tauola/Summer12_DR53X-PU_S10_START53_V7A-v1/'
    InfoPack.append((SubSample,FilesDir,nFiles))
    #
    SubSample='WZJetsTo2L2Q'
    FilesDir='/pnfs/desy.de/cms/tier2/store/user/fcostanz/NTuple13_v1/WZJetsTo2L2Q_TuneZ2star_8TeV-madgraph-tauola/Summer12_DR53X-PU_S10_START53_V7A-v1/'
    InfoPack.append((SubSample,FilesDir,nFiles))
    #
    SubSample='WGstarToLNu2E'
    FilesDir='/pnfs/desy.de/cms/tier2/store/user/fcostanz/NTuple13_v1/WGstarToLNu2E_TuneZ2star_8TeV-madgraph-tauola/Summer12_DR53X-PU_S10_START53_V7A-v1/'
    InfoPack.append((SubSample,FilesDir,nFiles))
    #
    SubSample='WGstarToLNu2Mu'
    FilesDir='/pnfs/desy.de/cms/tier2/store/user/fcostanz/NTuple13_v1/WGstarToLNu2Mu_TuneZ2star_7TeV-madgraph-tauola/Summer12_DR53X-PU_S10_START53_V7A-v1/'
    InfoPack.append((SubSample,FilesDir,nFiles))
    #
    SubSample='WGstarToLNu2Tau'
    FilesDir='/pnfs/desy.de/cms/tier2/store/user/fcostanz/NTuple13_v1/WGstarToLNu2Tau_TuneZ2star_7TeV-madgraph-tauola/Summer12_DR53X-PU_S10_START53_V7A-v1/'
    InfoPack.append((SubSample,FilesDir,nFiles))
    #
    #
    makeScriptFromInfoPack(Sample,Config,InfoPack,True)        
    #=======================================    

    
def TriBoson():
    Sample='TriBoson'
    Config='config_FullSim_Stop.txt'
    nFiles=6
    InfoPack=[]
    #
    SubSample='ZZZNoGstarJets'
    FilesDir='/pnfs/desy.de/cms/tier2/store/user/fcostanz/NTuple13_v1/ZZZNoGstarJets_8TeV-madgraph/Summer12_DR53X-PU_S10_START53_V7A-v1/'
    InfoPack.append((SubSample,FilesDir,nFiles))
    #
    SubSample='WWWJets'
    FilesDir='/pnfs/desy.de/cms/tier2/store/user/fcostanz/NTuple13_v1/WWWJets_8TeV-madgraph/Summer12_DR53X-PU_S10_START53_V7A-v1/'
    InfoPack.append((SubSample,FilesDir,nFiles))
    #
    SubSample='WWZNoGstarJets'
    FilesDir='/pnfs/desy.de/cms/tier2/store/user/fcostanz/NTuple13_v1/WWZNoGstarJets_8TeV-madgraph/Summer12_DR53X-PU_S10_START53_V7A-v1/'
    InfoPack.append((SubSample,FilesDir,nFiles))
    #
    SubSample='WZZNoGstarJets'
    FilesDir='/pnfs/desy.de/cms/tier2/store/user/fcostanz/NTuple13_v1/WZZNoGstarJets_8TeV-madgraph/Summer12_DR53X-PU_S10_START53_V7A-v1/'
    InfoPack.append((SubSample,FilesDir,nFiles))
    #
    SubSample='WWGJets'
    FilesDir='/pnfs/desy.de/cms/tier2/store/user/fcostanz/NTuple13_v1/WWGJets_8TeV-madgraph/Summer12_DR53X-PU_S10_START53_V7A-v1/'
    InfoPack.append((SubSample,FilesDir,nFiles))
    #
    #
    makeScriptFromInfoPack(Sample,Config,InfoPack,True)        
    #=======================================    
    

def TTV():
    Sample='TTV'
    Config='config_FullSim_Stop.txt'
    nFiles=6
    InfoPack=[]
    #    
    SubSample='TTZJets'
    FilesDir='/pnfs/desy.de/cms/tier2/store/user/fcostanz/NTuple13_v1/TTZJets_8TeV-madgraph_v2/Summer12_DR53X-PU_S10_START53_V7A-v1/'
    InfoPack.append((SubSample,FilesDir,nFiles))
    #
    SubSample='TTWJets'
    FilesDir='/pnfs/desy.de/cms/tier2/store/user/fcostanz/NTuple13_v1/TTWJets_8TeV-madgraph/Summer12_DR53X-PU_S10_START53_V7A-v1/'
    InfoPack.append((SubSample,FilesDir,nFiles))
    #
    SubSample='TTGJets'
    FilesDir='/pnfs/desy.de/cms/tier2/store/user/fcostanz/NTuple13_v1/TTGJets_8TeV-madgraph/Summer12_DR53X-PU_S10_START53_V7A-v1/'
    InfoPack.append((SubSample,FilesDir,nFiles))
    #
    SubSample='TTWWJets'
    FilesDir='/pnfs/desy.de/cms/tier2/store/user/fcostanz/NTuple13_v1/TTWWJets_8TeV-madgraph/Summer12_DR53X-PU_S10_START53_V7A-v1/'
    InfoPack.append((SubSample,FilesDir,nFiles))
    #
    SubSample='TBZToLL'
    FilesDir='/pnfs/desy.de/cms/tier2/store/user/fcostanz/NTuple13_v1/TBZToLL_4F_TuneZ2star_8TeV-madgraph-tauola/Summer12_DR53X-PU_S10_START53_V7C-v1/'
    InfoPack.append((SubSample,FilesDir,nFiles))
    #
    #
    makeScriptFromInfoPack(Sample,Config,InfoPack,True)        
    #=======================================


def QCD():
    Sample='QCD'
    Config='config_FullSim_Stop.txt'
    nFiles=6
    InfoPack=[]
    
    SubSample='HTbinned-100To250'
    FileDir='/nfs/dust/cms/user/fcost/store/NTuple13_v2/QCD_HT-100To250_TuneZ2star_8TeV-madgraph-pythia/Summer12_DR53X-PU_S10_START53_V7A-v1/'
    InfoPack.append((SubSample,FilesDir,nFiles))
    #
    SubSample='HTbinned-250To500'
    FileDir='/nfs/dust/cms/user/fcost/store/NTuple13_v2/QCD_HT-250To500_TuneZ2star_8TeV-madgraph-pythia6/Summer12_DR53X-PU_S10_START53_V7A-v1/'
    InfoPack.append((SubSample,FilesDir,nFiles))
    #
    SubSample='HTbinned-500To1000'
    FileDir='/nfs/dust/cms/user/fcost/store/NTuple13_v2/QCD_HT-500To1000_TuneZ2star_8TeV-madgraph-pythia6/Summer12_DR53X-PU_S10_START53_V7A-v1/'
    InfoPack.append((SubSample,FilesDir,nFiles))
    #
    SubSample='HTbinned-1000ToInf'
    FileDir='/nfs/dust/cms/user/fcost/store/NTuple13_v2/QCD_HT-1000ToInf_TuneZ2star_8TeV-madgraph-pythia6/Summer12_DR53X-PU_S10_START53_V7A-v1/'
    InfoPack.append((SubSample,FilesDir,nFiles))
    #
    #
    SubSample='MuEnriched'
    FileDir='/nfs/dust/cms/user/sahin/nTuple13_v2/mc/QCD_Pt_20_MuEnrichedPt_15_TuneZ2star_8TeV_pythia6/Summer12_DR53X-PU_S10_START53_V7A-v3/'
    InfoPack.append((SubSample,FilesDir,nFiles))
    #
    SubSample='EMEnriched-20To30'
    FileDir='/nfs/dust/cms/user/fcost/store/NTuple13_v2/QCD_Pt_20_30_EMEnriched_TuneZ2star_8TeV_pythia6/Summer12_DR53X-PU_S10_START53_V7A-v1/'
    InfoPack.append((SubSample,FilesDir,nFiles))
    #
    SubSample='EMEnriched-30To80'
    FileDir='/nfs/dust/cms/user/kruecker/desysusy/francesco/NTuple13_v2/QCD_Pt_30_80_EMEnriched_TuneZ2star_8TeV_pythia6/Summer12_DR53X-PU_S10_START53_V7A-v1/'
    InfoPack.append((SubSample,FilesDir,nFiles))
    #
    SubSample='EMEnriched-80To170'
    FileDir='/nfs/dust/cms/user/sahin/nTuple13_v2/mc/QCD_Pt80To170EMEnriched/'
    InfoPack.append((SubSample,FilesDir,nFiles))
    #
    SubSample='EMEnriched-170To250'
    FileDir='/nfs/dust/cms/user/sahin/nTuple13_v2/mc/QCD_Pt170To250EMEnriched/'
    InfoPack.append((SubSample,FilesDir,nFiles))
    #
    SubSample='EMEnriched-250To350'
    FileDir='/nfs/dust/cms/user/sahin/nTuple13_v2/mc/QCD_Pt250To350EMEnriched/'
    InfoPack.append((SubSample,FilesDir,nFiles))
    #
    SubSample='EMEnriched-350ToInf'
    FileDir='/nfs/dust/cms/user/sahin/nTuple13_v2/mc/QCD_Pt350ToInfEMEnriched/'
    InfoPack.append((SubSample,FilesDir,nFiles))
    #
    #
    makeScriptFromInfoPack(Sample,Config,InfoPack,True)        
    #=======================================

def T2tb():
    Sample='T2tb'
    Config='config_Scan_Stop.txt'
    nFiles=6
    InfoPack=[]

    SubSample='mStop100To375mLSP1To275'
    FileDir='/nfs/dust/cms/user/fcost/store/NTuple13_v2/SMS-T2tb_2J_mStop-100to375_mLSP-1to275_TuneZ2star_8TeV-madgraph-tauola/Summer12-START53_V19_FSIM_PU_S12-v2/'
    InfoPack.append((SubSample,FilesDir,nFiles))
    #
    SubSample='mStop400To475mLSP1To375'
    FileDir='/nfs/dust/cms/user/fcost/store/NTuple13_v2/SMS-T2tb_2J_mStop-400to475_mLSP-1to375_TuneZ2star_8TeV-madgraph-tauola/Summer12-START53_V19_FSIM_PU_S12-v2/'
    InfoPack.append((SubSample,FilesDir,nFiles))
    #
    SubSample='mStop500To575mLSP1To475'
    FileDir='/nfs/dust/cms/user/fcost/store/NTuple13_v2/SMS-T2tb_2J_mStop-500to575_mLSP-1to475_TuneZ2star_8TeV-madgraph-tauola/Summer12-START53_V19_FSIM_PU_S12-v2/'
    InfoPack.append((SubSample,FilesDir,nFiles))
    #
    SubSample='mStop600To675mLSP1To575'
    FileDir='/nfs/dust/cms/user/fcost/store/NTuple13_v2/SMS-T2tb_2J_mStop-600to675_mLSP-1to575_TuneZ2star_8TeV-madgraph-tauola/Summer12-START53_V19_FSIM_PU_S12-v2/'
    InfoPack.append((SubSample,FilesDir,nFiles))
    #
    SubSample='mStop700To750mLSP1To650'
    FileDir='/nfs/dust/cms/user/fcost/store/NTuple13_v2/SMS-T2tb_2J_mStop-700to750_mLSP-1to650_TuneZ2star_8TeV-madgraph-tauola/Summer12-START53_V19_FSIM_PU_S12-v2/'
    InfoPack.append((SubSample,FilesDir,nFiles))
    #
    SubSample='mStop775To800mLSP1To700'
    FileDir='/nfs/dust/cms/user/fcost/store/NTuple13_v2/SMS-T2tb_2J_mStop-775to800_mLSP-1to700_TuneZ2star_8TeV-madgraph-tauola/Summer12-START53_V19_FSIM_PU_S12-v2/'
    InfoPack.append((SubSample,FilesDir,nFiles))
    #
    #
    makeScriptFromInfoPack(Sample,Config,InfoPack,True)        
    #=======================================

def T2tbPoints():
    Sample='T2tbPoints'
    Config='config_Scan_Stop.txt'
    nFiles=12
    InfoPack=[]

    SubSample='mStop175-mLSP50'
    FileDir='/nfs/dust/cms/user/fcost/store/NTuple13_v2/SMS-T2tb_2J_mStop-100to375_mLSP-1to275_TuneZ2star_8TeV-madgraph-tauola/Summer12-START53_V19_FSIM_PU_S12-v2/'
    InfoPack.append((SubSample,FilesDir,nFiles))
    #
    SubSample='mStop200-mLSP25'
    FileDir='/nfs/dust/cms/user/fcost/store/NTuple13_v2/SMS-T2tb_2J_mStop-100to375_mLSP-1to275_TuneZ2star_8TeV-madgraph-tauola/Summer12-START53_V19_FSIM_PU_S12-v2/'
    InfoPack.append((SubSample,FilesDir,nFiles))
    #   
    SubSample='mStop375-mLSP50'
    FileDir='/nfs/dust/cms/user/fcost/store/NTuple13_v2/SMS-T2tb_2J_mStop-100to375_mLSP-1to275_TuneZ2star_8TeV-madgraph-tauola/Summer12-START53_V19_FSIM_PU_S12-v2/'
    InfoPack.append((SubSample,FilesDir,nFiles))
    #
    SubSample='mStop250-mLSP25'
    FileDir='/nfs/dust/cms/user/fcost/store/NTuple13_v2/SMS-T2tb_2J_mStop-100to375_mLSP-1to275_TuneZ2star_8TeV-madgraph-tauola/Summer12-START53_V19_FSIM_PU_S12-v2/'
    InfoPack.append((SubSample,FilesDir,nFiles))
    #
    SubSample='mStop325-mLSP100'
    FileDir='/nfs/dust/cms/user/fcost/store/NTuple13_v2/SMS-T2tb_2J_mStop-100to375_mLSP-1to275_TuneZ2star_8TeV-madgraph-tauola/Summer12-START53_V19_FSIM_PU_S12-v2/'
    InfoPack.append((SubSample,FilesDir,nFiles))
    #    
    SubSample='mStop450-mLSP150'
    FileDir='/nfs/dust/cms/user/fcost/store/NTuple13_v2/SMS-T2tb_2J_mStop-400to475_mLSP-1to375_TuneZ2star_8TeV-madgraph-tauola/Summer12-START53_V19_FSIM_PU_S12-v2/'
    InfoPack.append((SubSample,FilesDir,nFiles))
    #
    SubSample='mStop550-mLSP1'
    FileDir='/nfs/dust/cms/user/fcost/store/NTuple13_v2/SMS-T2tb_2J_mStop-500to575_mLSP-1to475_TuneZ2star_8TeV-madgraph-tauola/Summer12-START53_V19_FSIM_PU_S12-v2/'
    InfoPack.append((SubSample,FilesDir,nFiles))
    #
    #
    makeScriptFromInfoPack(Sample,Config,InfoPack,True)        
    #=======================================


def T2ttPoints():
    Sample='T2ttPoints'
    Config='config_FullSim_Stop.txt'
    nFiles=12
    InfoPack=[]
    
    SubSample='Stop400-LSP150'
    FilesDir='/nfs/dust/cms/user/fcost/store/NTuple13_v2/SMS-T2tt_2J_mStop-400_mLSP-150_TuneZ2star_8TeV-madgraph-tauola/Summer12_DR53X-PU_S10_START53_V7C-v1/'
    InfoPack.append((SubSample,FilesDir,nFiles))
    #
    SubSample='Stop500-LSP300'
    FilesDir='/nfs/dust/cms/user/fcost/store/NTuple13_v2/SMS-T2tt_2J_mStop-500_mLSP-300_TuneZ2star_8TeV-madgraph-tauola/Summer12_DR53X-PU_S10_START53_V7C-v1/'
    InfoPack.append((SubSample,FilesDir,nFiles))
    #
    SubSample='Stop600-LSP50'
    FilesDir='/nfs/dust/cms/user/fcost/store/NTuple13_v2/SMS-T2tt_2J_mStop-600_mLSP-50_TuneZ2star_8TeV-madgraph-tauola/Summer12_DR53X-PU_S10_START53_V7C-v1/'
    InfoPack.append((SubSample,FilesDir,nFiles))
    #    
    SubSample='Stop750-LSP25'
    FilesDir='/nfs/dust/cms/user/fcost/store/NTuple13_v2/SMS-T2tt_2J_mStop-750_mLSP-25_TuneZ2star_8TeV-madgraph-tauola/Summer12_DR53X-PU_S10_START53_V7C-v1/'
    InfoPack.append((SubSample,FilesDir,nFiles))
    #
    #
    makeScriptFromInfoPack(Sample,Config,InfoPack,True)        
    #=======================================

def T2tt():
    Sample='T2tt'
    Config='config_Scan_Stop.txt'
    nFiles=9
    InfoPack=[]

    SubSample='mStop150To350mLSP0To250'
    FileDir='/pnfs/desy.de/cms/tier2/store/user/fcostanz/nTuple13_v2/mc/SMS-T2tt_mStop-150to350_mLSP-0to250_8TeV-Pythia6Z/Summer12-START52_V9_FSIM-v1/'
    InfoPack.append((SubSample,FilesDir,nFiles))
    #
    SubSample='mStop375To475mLSP0To375'
    FileDir='/nfs/dust/cms/user/fcost/store/NTuple13_v2/SMS-T2tt_mStop-375to475_mLSP-0to375_8TeV-Pythia6Z/Summer12-START52_V9_FSIM-v1/'
    InfoPack.append((SubSample,FilesDir,nFiles))
    #
    SubSample='mStop500To650mLSP0To225'
    FileDir='/nfs/dust/cms/user/fcost/store/NTuple13_v2/SMS-T2tt_mStop-500to650_mLSP-0to225_8TeV-Pythia6Z/Summer12-START52_V9_FSIM-v1/'
    InfoPack.append((SubSample,FilesDir,nFiles))
    #
    SubSample='mStop500To650mLSP250To550'
    FileDir='/nfs/dust/cms/user/fcost/store/NTuple13_v2/SMS-T2tt_mStop-500to650_mLSP-250to550_8TeV-Pythia6Z/Summer12-START52_V9_FSIM-v1/'
    InfoPack.append((SubSample,FilesDir,nFiles))
    #
    SubSample='mStop675To800mLSP0To275'
    FileDir='/pnfs/desy.de/cms/tier2/store/user/fcostanz/nTuple13_v2/mc/SMS-T2tt_mStop-675to800_mLSP-0to275_8TeV-Pythia6Z/Summer12-START52_V9_FSIM-v1/'
    InfoPack.append((SubSample,FilesDir,nFiles))
    #
    SubSample='T2tt_mStop675To800mLSP300To700'
    FileDir='/pnfs/desy.de/cms/tier2/store/user/fcostanz/nTuple13_v2/SMS-T2tt_mStop-675to800_mLSP-300to700_8TeV-Pythia6Z/Summer12-START52_V9_FSIM-v1/'
    InfoPack.append((SubSample,FilesDir,nFiles))
    #
    SubSample='mStop150To475mLSP1'
    FileDir='/nfs/dust/cms/user/fcost/store/NTuple13_v2/SMS-8TeV-Pythia6Z_T2tt_mStop-150to475_mLSP-1/Summer12-START52_V9_FSIM-v1/'
    InfoPack.append((SubSample,FilesDir,nFiles))
    #
    SubSample='mStop500To800mLSP1'
    FileDir='/nfs/dust/cms/user/fcost/store/NTuple13_v2/SMS-8TeV-Pythia6Z_T2tt_mStop-500to800_mLSP-1/Summer12-START52_V9_FSIM-v1/'
    InfoPack.append((SubSample,FilesDir,nFiles))
    #
    SubSample='mStop100To200mLSP1To100LepFilter'
    FileDir='/nfs/dust/cms/user/fcost/store/NTuple13_v2/SMS-T2tt_2J_mStop-100to200_mLSP-1to100_LeptonFilter_TuneZ2star_8TeV-madgraph-tauola/Summer12-START52_V9_FSIM-v1/'
    InfoPack.append((SubSample,FilesDir,nFiles))
    #
    SubSample='mStop225To350mLSP25To250LepFilter'
    FileDir='/nfs/dust/cms/user/fcost/store/NTuple13_v2/SMS-T2tt_2J_mStop-225to350_mLSP-25to250_LeptonFilter_TuneZ2star_8TeV-madgraph-tauola/Summer12-START52_V9_FSIM-v1/'
    InfoPack.append((SubSample,FilesDir,nFiles))
    #
    #
    makeScriptFromInfoPack(Sample,Config,InfoPack,True)        
    #=======================================

def T2bw():
    Sample='T2bw'
    Config='config_Scan_Stop.txt'
    nFiles=9
    InfoPack=[]

    SubSample='mStop100To475mLSP0To300x0p25LepFilter'
    FileDir='/nfs/dust/cms/user/fcost/store/NTuple13_v2/SMS-T2bw_2J_mStop-100to475_mLSP-0to300_x-025_LeptonFilter_TuneZ2star_8TeV-madgraph-tauola/Summer12-START53_V7C_FSIM-v1/'
    InfoPack.append((SubSample,FilesDir,nFiles))
    #
    SubSample='mStop500To800mLSP0To700x0p25'
    FileDir='/nfs/dust/cms/user/fcost/store/NTuple13_v2/SMS-T2bw_2J_mStop-500to800_mLSP-0to700_x-025_TuneZ2star_8TeV-madgraph-tauola/Summer12-START53_V7C_FSIM-v1/'
    InfoPack.append((SubSample,FilesDir,nFiles))
    #
    SubSample='mStop100To475mLSP1x0p25'
    FileDir='/nfs/dust/cms/user/fcost/store/NTuple13_v2/SMS-T2bw_2J_mStop-100to475_mLSP-1_x-025_TuneZ2star_8TeV-madgraph-tauola/Summer12-START53_V7C_FSIM-v1/'
    InfoPack.append((SubSample,FilesDir,nFiles))
    #
    SubSample='mStop500To800mLSP1x0p25'
    FileDir='/nfs/dust/cms/user/fcost/store/NTuple13_v2/SMS-T2bw_2J_mStop-500to800_mLSP-1_x-025_TuneZ2star_8TeV-madgraph-tauola/Summer12-START53_V7C_FSIM-v1/'
    InfoPack.append((SubSample,FilesDir,nFiles))
    #
    SubSample='mStop100To475mLSP0To375x0p25'
    FileDir='/nfs/dust/cms/user/fcost/store/NTuple13_v2/SMS-T2bw_2J_mStop-100to475_mLSP-0to375_x-025_TuneZ2star_8TeV-madgraph-tauola/Summer12-START53_V7C_FSIM-v1'
    InfoPack.append((SubSample,FilesDir,nFiles))
    #
    SubSample='mStop500To650mLSP150To300x0p25LepFilter'
    FileDir='/nfs/dust/cms/user/fcost/store/NTuple13_v2/SMS-T2bw_2J_mStop-500to650_mLSP-150to300_x-025_LeptonFilter_TuneZ2star_8TeV-madgraph-tauola/Summer12-START53_V7C_FSIM-v1/'
    InfoPack.append((SubSample,FilesDir,nFiles))
    #
    #
    SubSample='mStop100To475mLSP0To300x0p50LepFilter'
    FileDir='/nfs/dust/cms/user/fcost/store/NTuple13_v2/SMS-T2bw_2J_mStop-100to475_mLSP-0to300_x-050_LeptonFilter_TuneZ2star_8TeV-madgraph-tauola/Summer12-START53_V7C_FSIM-v1/'
    InfoPack.append((SubSample,FilesDir,nFiles))
    #
    SubSample='mStop500To800mLSP0To700x0p50'
    FileDir='/nfs/dust/cms/user/fcost/store/NTuple13_v2/SMS-T2bw_2J_mStop-500to800_mLSP-0to700_x-050_TuneZ2star_8TeV-madgraph-tauola/Summer12-START53_V7C_FSIM-v1/'
    InfoPack.append((SubSample,FilesDir,nFiles))
    #
    SubSample='mStop100To475mLSP1x0p50'
    FileDir='/nfs/dust/cms/user/fcost/store/NTuple13_v2/SMS-T2bw_2J_mStop-100to475_mLSP-1_x-050_TuneZ2star_8TeV-madgraph-tauola/Summer12-START53_V7C_FSIM-v1/'
    InfoPack.append((SubSample,FilesDir,nFiles))
    #
    SubSample='mStop500To800mLSP1x0p50'
    FileDir='/pnfs/desy.de/cms/tier2/store/user/fcostanz/nTuple13_v2/mc/SMS-T2bw_2J_mStop-500to800_mLSP-1_x-050_TuneZ2star_8TeV-madgraph-tauola/Summer12-START53_V7C_FSIM-v1/'
    InfoPack.append((SubSample,FilesDir,nFiles))
    #
    SubSample='mStop100To475mLSP0To375x0p50'
    FileDir='/nfs/dust/cms/user/fcost/store/NTuple13_v2/SMS-T2bw_2J_mStop-100to475_mLSP-0to375_x-050_TuneZ2star_8TeV-madgraph-tauola/Summer12-START53_V7C_FSIM-v1'
    InfoPack.append((SubSample,FilesDir,nFiles))
    #
    SubSample='mStop500To650mLSP150To300x0p50LepFilter'
    FileDir='/nfs/dust/cms/user/fcost/store/NTuple13_v2/SMS-T2bw_2J_mStop-500to650_mLSP-150to300_x-050_LeptonFilter_TuneZ2star_8TeV-madgraph-tauola/Summer12-START53_V7C_FSIM-v1/'
    InfoPack.append((SubSample,FilesDir,nFiles))
    #
    #
    SubSample='mStop100To475mLSP0To300x0p75LepFilter'
    FileDir='/pnfs/desy.de/cms/tier2/store/user/fcostanz/nTuple13_v2/mc/SMS-T2bw_2J_mStop-100to475_mLSP-0to300_x-075_LeptonFilter_TuneZ2star_8TeV-madgraph-tauola/Summer12-START53_V7C_FSIM-v1/'
    InfoPack.append((SubSample,FilesDir,nFiles))
    #
    SubSample='mStop500To800mLSP0To700x0p75'
    FileDir='/pnfs/desy.de/cms/tier2/store/user/fcostanz/nTuple13_v2/mc/SMS-T2bw_2J_mStop-500to800_mLSP-0to700_x-075_TuneZ2star_8TeV-madgraph-tauola/Summer12-START53_V7C_FSIM-v1/'
    InfoPack.append((SubSample,FilesDir,nFiles))
    #
    SubSample='mStop100To475mLSP1x0p75'
    FileDir='/pnfs/desy.de/cms/tier2/store/user/fcostanz/nTuple13_v2/mc/SMS-T2bw_2J_mStop-100to475_mLSP-1_x-075_TuneZ2star_8TeV-madgraph-tauola/Summer12-START53_V7C_FSIM-v1/'
    InfoPack.append((SubSample,FilesDir,nFiles))
    #
    SubSample='mStop500To800mLSP1x0p75'
    FileDir='/pnfs/desy.de/cms/tier2/store/user/fcostanz/nTuple13_v2/mc/SMS-T2bw_2J_mStop-500to800_mLSP-1_x-075_TuneZ2star_8TeV-madgraph-tauola/Summer12-START53_V7C_FSIM-v1/'
    InfoPack.append((SubSample,FilesDir,nFiles))
    #
    SubSample='mStop100To475mLSP0To375x0p75'
    FileDir='/pnfs/desy.de/cms/tier2/store/user/fcostanz/nTuple13_v2/mc/SMS-T2bw_2J_mStop-100to475_mLSP-0to375_x-075_TuneZ2star_8TeV-madgraph-tauola/Summer12-START53_V7C_FSIM-v1'
    InfoPack.append((SubSample,FilesDir,nFiles))
    #
    SubSample='mStop500To650mLSP150To300x0p75LepFilter'
    FileDir='/pnfs/desy.de/cms/tier2/store/user/fcostanz/nTuple13_v2/mc/SMS-T2bw_2J_mStop-500to650_mLSP-150to300_x-075_LeptonFilter_TuneZ2star_8TeV-madgraph-tauola/Summer12-START53_V7C_FSIM-v1/'
    InfoPack.append((SubSample,FilesDir,nFiles))
    #
    #
    makeScriptFromInfoPack(Sample,Config,InfoPack,True)        
    #=======================================

    
if __name__=='__main__':
    #MuHad()
    #SingleMu()
    #SingleElectron()
    TTJetsPOWHEG() 
    #TTJetsMG()
    #DYJetsToLL()
    WJetsToLNu()
    SingleTop()
    DiBoson()
    TriBoson()
    TTV()
    #QCD()
    #T2tb()
    T2ttPoints()
    #T2ttPoints()
    #T2tt()
    #T2bw()
    #T2tb()