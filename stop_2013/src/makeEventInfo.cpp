#include "makeEventInfo.h"

#include "ConfigReader.h"
#include "Tools.h"
#include "CleaningFilters.h"
#include "ScanInfoProvider.h"

using namespace std;

extern bool pcp;
extern desy_tools::ScanInfoProvider scanInfo;
//======================================================
// make EventInfo
//======================================================

void makeEventInfo(EasyChain* tree, EventInfo& info)
{
  info.isrWeight = 1.;
  info.topPtWeight = 1.;
  
  info.T2ttL = 1.;
  info.T2ttR = 1.;
  
  info.T2bWLR = 1.;
  info.T2bWLS = 1.;
  info.T2bWLL = 1.;
  
  info.T2bWSR = 1.;
  info.T2bWSS = 1.;
  info.T2bWSL = 1.;
  
  info.T2bWRR = 1.;
  info.T2bWRS = 1.;
  info.T2bWRL = 1.;

  info.isrWeight = gen_tools::ISRWeight( info.Sample, tree);
  info.topPtWeight = gen_tools::TopPtWeight( info.Sample, tree);

  float rho = tree->Get( rho, "rho");
  info.rho = rho;
  
  info.LepFromTop = 0;
  info.Charginos = 0;

  if ( info.isData) return;

  vector<LorentzM>& p4     = tree->Get( &p4,          "genP4");
  vector<int>&      pdgId  = tree->Get( &pdgId,       "genPdgId");
  vector<int>&      status = tree->Get( &status,      "genStatus");
  vector<int>& MotherIndex = tree->Get( &MotherIndex, "genMotherIndex");
  vector<int>& MotherPdgId = tree->Get( &MotherPdgId, "genMotherPdgId");
  
  for (int igen=0; igen<status.size(); igen++)
    if (abs(pdgId.at(igen))==6)
      info.LepFromTop += gen_tools::Decay(igen,&MotherIndex,&pdgId,&status,"");
  
  for (int igen=0; igen<status.size(); igen++)
    if (abs(pdgId.at(igen))==1000024)
      info.Charginos++;
   
  if (info.isScan || info.Sample.compare("T2tbPoints") == 0 || info.Sample.compare("T2ttPoints") == 0){
    scanInfo.Set( info.Sample, info.SubSample, tree);
    
    info.mStop   = scanInfo.mStop;
    info.mLSP    = scanInfo.mLSP;
    info.xs      = scanInfo.xs;
    info.NEvents = scanInfo.NEvents;
    info.FE      = scanInfo.FE;    
  }

  if ( info.Sample.find("T2tt") == 0 || info.Sample.find("T2bw") == 0)
    {
      gen_tools::SUSYGenParticle genParticle;
      vector<gen_tools::SUSYGenParticle> genParticles;
      
      for( unsigned int ip = 0; ip < p4.size(); ip++)
	{
	  if( status.at(ip) != 3) continue;
	  
	  genParticle.pt          = p4.at(ip).pt();
	  genParticle.phi         = p4.at(ip).phi();
	  genParticle.eta         = p4.at(ip).eta();
	  genParticle.energy      = p4.at(ip).E();
	  genParticle.pdgId       = pdgId.at(ip);
	  genParticle.firstMother = MotherIndex.at(ip);

	  genParticles.push_back( genParticle);
	}
      
      if ( info.Sample.find("T2tt") == 0)
	{
	  info.T2ttL = gen_tools::Reweight_Stop_to_TopChi0 (genParticles, 0., -1, TString(info.Sample));
	  info.T2ttR = gen_tools::Reweight_Stop_to_TopChi0 (genParticles, 0., -1, TString(info.Sample));
	}      
      if ( info.Sample.find("T2bw") == 0)
	{
	  float pi = acos(-1.0);
	  
	  info.T2bWLR = gen_tools::Reweight_T2bW( 0 , 0      , genParticles );
	  info.T2bWLS = gen_tools::Reweight_T2bW( 0 , pi/4.0 , genParticles );
	  info.T2bWLL = gen_tools::Reweight_T2bW( 0 , pi/2.0 , genParticles );
	  
	  info.T2bWSR = gen_tools::Reweight_T2bW( pi/4.0 , 0      , genParticles );
	  info.T2bWSS = gen_tools::Reweight_T2bW( pi/4.0 , pi/4.0 , genParticles );
	  info.T2bWSL = gen_tools::Reweight_T2bW( pi/4.0 , pi/2.0 , genParticles );
	  
	  info.T2bWRR = gen_tools::Reweight_T2bW( pi/2.0 , 0      , genParticles );
	  info.T2bWRS = gen_tools::Reweight_T2bW( pi/2.0 , pi/4.0 , genParticles );
	  info.T2bWRL = gen_tools::Reweight_T2bW( pi/2.0 , pi/2.0 , genParticles );
	}
    }
}
