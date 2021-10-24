import ROOT
import numpy as np
#import pandas as pd
#import uproot
import sys
#import seaborn as sns
import matplotlib.pyplot as plt
#plt.style.use('seaborn-white')
from ROOT import gROOT, gBenchmark

ROOT.gROOT.SetBatch(True)


from optparse import OptionParser
parser = OptionParser()
parser.add_option("--plotvar", dest="plotvar", default="HB", action="store", help="name of the variable")
(options, args) = parser.parse_args()

myfirst_file = ROOT.TFile("HcalTupleMaker_test.root")
mdir = myfirst_file.Get("hcalTupleTree")
myTree = mdir.Get("tree")
myTree.GetListOfBranches().ls()
print("I have my tree")
plotvar = options.plotvar
#plotDir = "/afs/cern.ch/work/c/cisik/CRUZET_ANA/CMSSW_11_3_0/src/HCALPFG/HcalTupleMaker/test/plots/"
plotDir = "/eos/user/c/cisik/www/HCAL/CRUZET_plots/"
nEntry = myTree.GetEntries()
print("Number of entries: ", nEntry)


#i=0
#for eventIds in myTree:
#	print("event number: ", eventIds)
#	i +=1

#for eventNumber in range (0 , myTree . GetEntries ()):
#	myTree . GetEntry (eventNumber)
#	eventNumber = getattr(myTree,"eventNumber")
#	print("event number: ", eventNumber)
	

#sys.exit()

def recHitPlot():

	c1 = ROOT.TCanvas("c1","c1",850,600)
	pad1 = ROOT.TPad("pad1","This is pad1",0.02,0.02,0.98,0.98,21)
	pad1.UseCurrentStyle()
	pad1.Draw()
	pad1.cd()
	pad1.SetGrid();
	h1= ROOT.TH1F("h1","HBHE RecHit Energy",100, -1, 2)
	h1.GetXaxis().SetTitle("GeV")
	h1.GetYaxis().SetTitle("Number of RecHits")
	h1.GetYaxis().SetLabelOffset(0.007)
	h1.SetTitleOffset(1.3)
	h1.SetStats(0)
	h1.SetLineColor(2)
	h1.SetFillColor(2)
	c1.SetHighLightColor(2)
	c1.Range(0,0,1,1)
	c1.SetFillColor(0)
	c1.SetBorderMode(0)
	c1.SetBorderSize(2)
	c1.SetTickx(1)
	c1.SetTicky(1)
	c1.SetLeftMargin(0.18)
	c1.SetRightMargin(0.04)
	c1.SetTopMargin(0.05)
	c1.SetBottomMargin(0.13)
	c1.SetFrameFillStyle(0)
	c1.SetFrameBorderMode(0)
	c1.SetFrameFillStyle(0)

	myTree.Draw("HBHERecHitEnergy>>h1","", "")
	c1.cd()
	c1.Update();
	c1.SaveAs(plotDir + "HBHERecHitEnergy" + ".png")
	c1.SaveAs(plotDir + "HBHERecHitEnergy" + ".pdf")
	c1.SaveAs(plotDir + "HBHERecHitEnergy" + ".root")


	c2 = ROOT.TCanvas("c2","c2",850,600)
	pad2 = ROOT.TPad("pad2","This is pad2",0.02,0.02,0.98,0.98,21)
	pad2.UseCurrentStyle()
	pad2.Draw()
	pad2.cd()
	pad2.SetGrid();
	h2= ROOT.TH1F("h2","HF RecHit Energy",100, -5, 5)
	h2.GetXaxis().SetTitle("GeV")
	h2.GetYaxis().SetTitle("Number of RecHits")
	h2.GetYaxis().SetLabelOffset(0.007)
	h2.SetTitleOffset(1.3)
	h2.SetStats(0)
	h2.SetLineColor(2)
	h2.SetFillColor(2)
	c2.SetHighLightColor(2)
	c2.Range(0,0,1,1)
	c2.SetFillColor(0)
	c2.SetBorderMode(0)
	c2.SetBorderSize(2)
	c2.SetTickx(1)
	c2.SetTicky(1)
	c2.SetLeftMargin(0.18)
	c2.SetRightMargin(0.04)
	c2.SetTopMargin(0.05)
	c2.SetBottomMargin(0.13)
	c2.SetFrameFillStyle(0)
	c2.SetFrameBorderMode(0)
	c2.SetFrameFillStyle(0)

	myTree.Draw("HFRecHitEnergy>>h2","", "")
	c2.cd()
	c2.Update();
	c2.SaveAs(plotDir + "HFRecHitEnergy" + ".png")
	c2.SaveAs(plotDir + "HFRecHitEnergy" + ".pdf")
	c2.SaveAs(plotDir + "HFRecHitEnergy" + ".root")

	c3 = ROOT.TCanvas("c3","c3",850,600)
	pad3 = ROOT.TPad("pad3","This is pad3",0.02,0.02,0.98,0.98,21)
	pad3.UseCurrentStyle()
	pad3.Draw()
	pad3.cd()
	pad3.SetGrid();
	h3= ROOT.TH1F("h3","HBHE RecHit Time",100, -15000, 5000)
	h3.GetXaxis().SetTitle("ns")
	h3.GetYaxis().SetTitle("Number of RecHits")
	h3.GetYaxis().SetLabelOffset(0.007)
	h3.SetTitleOffset(1.3)
	h3.SetStats(0)
	h3.SetLineColor(2)
	h3.SetFillColor(2)
	c3.SetHighLightColor(2)
	c3.Range(0,0,1,1)
	c3.SetFillColor(0)
	c3.SetBorderMode(0)
	c3.SetBorderSize(2)
	c3.SetTickx(1)
	c3.SetTicky(1)
	c3.SetLeftMargin(0.18)
	c3.SetRightMargin(0.04)
	c3.SetTopMargin(0.05)
	c3.SetBottomMargin(0.13)
	c3.SetFrameFillStyle(0)
	c3.SetFrameBorderMode(0)
	c3.SetFrameFillStyle(0)

	myTree.Draw("HBHERecHitTime>>h3","", "")
	c3.cd()
	c3.Update();
	c3.SaveAs(plotDir + "HBHERecHitTime" + ".png")
	c3.SaveAs(plotDir + "HBHERecHitTime" + ".pdf")
	c3.SaveAs(plotDir + "HBHERecHitTime" + ".root")

	c5 = ROOT.TCanvas("c5","c5",850,600)
	pad5 = ROOT.TPad("pad5","This is pad5",0.02,0.02,0.98,0.98,21)
	pad5.UseCurrentStyle()
	pad5.Draw()
	pad5.cd()
	pad5.SetGrid();
	h5= ROOT.TH1F("h5","HF RecHit Time",100, -120, -80)
	h5.GetXaxis().SetTitle("ns")
	h5.GetYaxis().SetTitle("Number of RecHits")
	h5.GetYaxis().SetLabelOffset(0.007)
	h5.SetTitleOffset(1.3)
	h5.SetStats(0)
	h5.SetLineColor(2)
	h5.SetFillColor(2)
	c5.SetHighLightColor(2)
	c5.Range(0,0,1,1)
	c5.SetFillColor(0)
	c5.SetBorderMode(0)
	c5.SetBorderSize(2)
	c5.SetTickx(1)
	c5.SetTicky(1)
	c5.SetLeftMargin(0.18)
	c5.SetRightMargin(0.04)
	c5.SetTopMargin(0.05)
	c5.SetBottomMargin(0.13)
	c5.SetFrameFillStyle(0)
	c5.SetFrameBorderMode(0)
	c5.SetFrameFillStyle(0)

	myTree.Draw("HFRecHitTime>>h5","", "")
	c5.cd()
	c5.Update();
	c5.SaveAs(plotDir + "HFRecHitTime" + ".png")
	c5.SaveAs(plotDir + "HFRecHitTime" + ".pdf")
	c5.SaveAs(plotDir + "HFRecHitTime" + ".root")


	for x in range(1,8):

		c13 = ROOT.TCanvas("c13_%d" % x,"c13",850,600)
		pad13 = ROOT.TPad("pad13_%d" % x,"This is pad13",0.02,0.02,0.98,0.98,21)
		pad13.UseCurrentStyle()
		pad13.Draw()
		pad13.cd()
		pad13.SetLogz()
		h13= ROOT.TH2F("h13_%d" % x, "HBHE i#eta versus i#phi weighted by energy for Depth"+ str(x) + " ", 60,-41.5,41.5,72,0.5,72.5)
		h13.GetXaxis().SetTitle("ieta") 
		h13.GetYaxis().SetTitle("iphi")
		h13.GetYaxis().SetLabelOffset(0.007)
		h13.GetYaxis().SetTitleOffset(1.3)
		h13.SetStats(0)
		c13.SetHighLightColor(2)
		c13.Range(0,0,1,1)
		c13.SetFillColor(0)
		c13.SetBorderMode(0)
		c13.SetBorderSize(2)
		c13.SetTickx(1)
		c13.SetTicky(1)
		#c13.SetLeftMargin(0.18)
		#c13.SetRightMargin(0.04)
		c13.SetTopMargin(0.05)
		c13.SetBottomMargin(0.13)
		c13.SetFrameFillStyle(0)
		c13.SetFrameBorderMode(0)
		c13.SetFrameFillStyle(0)

		myTree.Draw("HBHERecHitIPhi:HBHERecHitIEta:HBHERecHitEnergy>>h13_%d" % x,"(HBHERecHitDepth==%d)" % x, "COLZ")
		#myTree.Draw("HFRecHitIEta:HFRecHitIPhi>>h1","(HFRecHitDepth=="+ str(x) +")", "COLZ")
		c13.cd()
		c13.Update();
		c13.SaveAs(plotDir + "HBHEIEtaIPhibyED" + str(x) + ".png")
		c13.SaveAs(plotDir + "HBHEIEtaIPhibyED" + str(x) + ".pdf")
		c13.SaveAs(plotDir + "HBHEIEtaIPhibyED" + str(x) + ".root")




def digi():

	for x in range(1,8):

		c4 = ROOT.TCanvas("c4_%d" % x,"c4",850,600)
		pad4 = ROOT.TPad("pad4_%d" % x,"This is pad4",0.02,0.02,0.98,0.98,21)
		pad4.UseCurrentStyle()
		pad4.Draw()
		pad4.cd()
		pad4.SetLogz()
		h4= ROOT.TH2F("h4_%d" % x, "HBHE Digi Depth"+ str(x) + " ",83,-41.5,41.5,72,0.5,72.5)
		h4.GetXaxis().SetTitle("ieta")
		h4.GetYaxis().SetTitle("iphi")
		h4.GetYaxis().SetLabelOffset(0.007)
		h4.GetYaxis().SetTitleOffset(1.3)
		h4.SetStats(0)
		c4.SetHighLightColor(2)
		c4.Range(0,0,1,1)
		c4.SetFillColor(0)
		c4.SetBorderMode(0)
		c4.SetBorderSize(2)
		c4.SetTickx(1)
		c4.SetTicky(1)
		#c4.SetLeftMargin(0.18)
		#c4.SetRightMargin(0.04)
		c4.SetTopMargin(0.05)
		c4.SetBottomMargin(0.13)
		c4.SetFrameFillStyle(0)
		c4.SetFrameBorderMode(0)
		c4.SetFrameFillStyle(0)

		myTree.Draw("QIE11DigiIPhi:QIE11DigiIEta>>h4_%d" % x,"(QIE11DigiDepth==%d)" % x, "COLZ")
		#myTree.Draw("HFRecHitIEta:HFRecHitIPhi>>h1","(HFRecHitDepth=="+ str(x) +")", "COLZ")
		c4.cd()
		c4.Update();
		c4.SaveAs(plotDir + "HBHEDigiIEtaIPhiD" + str(x) + ".png")
		c4.SaveAs(plotDir + "HBHEDigiIEtaIPhiD" + str(x) + ".pdf")
		c4.SaveAs(plotDir + "HBHEDigiIEtaIPhiD" + str(x) + ".root")



c6 = ROOT.TCanvas("c6","c6",850,600)
pad6 = ROOT.TPad("pad6","This is pad6",0.02,0.02,0.98,0.98,21)
pad6.UseCurrentStyle()
pad6.Draw()
pad6.cd()
pad6.SetLogz()
h6= ROOT.TH2F("h6","HF Digi Depth",83,-41.5,41.5,72,0.5,72.5)
h6.GetXaxis().SetTitle("ieta")
h6.GetYaxis().SetTitle("iphi")
h6.GetYaxis().SetLabelOffset(0.007)
h6.GetYaxis().SetTitleOffset(1.3)
h6.SetStats(0)
c6.SetHighLightColor(2)
c6.Range(0,0,1,1)
c6.SetFillColor(0)
c6.SetBorderMode(0)
c6.SetBorderSize(2)
c6.SetTickx(1)
c6.SetTicky(1)
c6.SetLeftMargin(0.18)
c6.SetRightMargin(0.04)
c6.SetTopMargin(0.05)
c6.SetBottomMargin(0.13)
c6.SetFrameFillStyle(0)
c6.SetFrameBorderMode(0)
c6.SetFrameFillStyle(0)

myTree.Draw("QIE10DigiIPhi:QIE10DigiIEta>>h6","(QIE10DigiDepth)", "COLZ")
c6.cd()
c6.Update();
c6.SaveAs(plotDir + "HFDigi" + "D5" + ".png")
c6.SaveAs(plotDir + "HFDigi" + "D5" + ".pdf")
c6.SaveAs(plotDir + "HFDigi" + "D5" + ".root")


c7 = ROOT.TCanvas("c7","c7",850,600)
pad7 = ROOT.TPad("pad7","This is pad7",0.02,0.02,0.98,0.98,21)
pad7.UseCurrentStyle()
pad7.Draw()
pad7.cd()
pad7.SetGrid();
#h7 = gROOT.FindObject('QIE11DigiFC, run')
h7= ROOT.TH1F("h7","QIE11 Digi fC",100, 0, 2000)
h7.GetXaxis().SetTitle("Charge (fC)")
h7.GetXaxis().CenterTitle(True)
#h7.GetYaxis().CenterTitle(True)
#h7.GetYaxis().SetTitle("Count")
#h7.GetYaxis().SetTitleOffset(2.3)
h7.SetLineColor(45)
h7.SetFillColor(4)
h7.GetYaxis().SetLabelOffset(0.007)
h7.GetYaxis().SetTitleOffset(1.3)
h7.SetStats(0)
c7.SetHighLightColor(2)
c7.Range(0,0,1,1)
c7.SetFillColor(0)
c7.SetBorderMode(0)
c7.SetBorderSize(2)
c7.SetTickx(1)
c7.SetTicky(1)
c7.SetLeftMargin(0.18)
c7.SetRightMargin(0.04)
c7.SetTopMargin(0.05)
c7.SetBottomMargin(0.13)
c7.SetFrameFillStyle(0)
c7.SetFrameBorderMode(0)
c7.SetFrameFillStyle(0)

myTree.Draw("QIE11DigiTotFC>>h7","","")
c7.cd()
c7.Update();
c7.SaveAs(plotDir + "QIE11DigiFC" + ".png")
c7.SaveAs(plotDir + "QIE11DigiFC" + ".pdf")
c7.SaveAs(plotDir + "QIE11DigiFC" + ".root")

c8 = ROOT.TCanvas("c8","c8",850,600)
pad8 = ROOT.TPad("pad8","This is pad8",0.02,0.02,0.98,0.98,21)
pad8.UseCurrentStyle()
pad8.Draw()
pad8.cd()
pad8.SetGrid();
#h7 = gROOT.FindObject('QIE11DigiFC, run')
h8= ROOT.TH1F("h8","QIE10 Digi fC",100, 0, 100)
h8.GetXaxis().SetTitle("Charge (fC)")
h8.GetXaxis().CenterTitle(True)
#h8.GetYaxis().CenterTitle(True)
#h8.GetYaxis().SetTitle("Count")
#h8.GetYaxis().SetTitleOffset(2.3)
h8.SetLineColor(45)
h8.SetFillColor(4)
h8.GetYaxis().SetLabelOffset(0.007)
h8.GetYaxis().SetTitleOffset(1.3)
h8.SetStats(0)
c8.SetHighLightColor(2)
c8.Range(0,0,1,1)
c8.SetFillColor(0)
c8.SetBorderMode(0)
c8.SetBorderSize(2)
c8.SetTickx(1)
c8.SetTicky(1)
c8.SetLeftMargin(0.18)
c8.SetRightMargin(0.04)
c8.SetTopMargin(0.05)
c8.SetBottomMargin(0.13)
c8.SetFrameFillStyle(0)
c8.SetFrameBorderMode(0)
c8.SetFrameFillStyle(0)

myTree.Draw("QIE10DigiFC>>h8","","")
c8.cd()
c8.Update();
c8.SaveAs(plotDir + "QIE10DigiFC" + ".png")
c8.SaveAs(plotDir + "QIE10DigiFC" + ".pdf")
c8.SaveAs(plotDir + "QIE10DigiFC" + ".root")


c9 = ROOT.TCanvas("c9","c9",850,600)
pad9 = ROOT.TPad("pad9","This is pad9",0.02,0.02,0.98,0.98,21)
pad9.UseCurrentStyle()
pad9.Draw()
pad9.cd()
pad9.SetGrid();
#h7 = gROOT.FindObject('QIE11DigiFC, run')
h9= ROOT.TH1F("h9","QIE11 Digi TDC",100, -10, 80)
h9.GetXaxis().SetTitle("TDC")
h9.GetXaxis().CenterTitle(True)
#h9.GetYaxis().CenterTitle(True)
#h9.GetYaxis().SetTitle("Count")
#h9.GetYaxis().SetTitleOffset(2.3)
h9.SetLineColor(45)
h9.SetFillColor(4)
h9.GetYaxis().SetLabelOffset(0.007)
h9.GetYaxis().SetTitleOffset(1.3)
h9.SetStats(0)
c9.SetHighLightColor(2)
c9.Range(0,0,1,1)
c9.SetFillColor(0)
c9.SetBorderMode(0)
c9.SetBorderSize(2)
c9.SetTickx(1)
c9.SetTicky(1)
c9.SetLeftMargin(0.18)
c9.SetRightMargin(0.04)
c9.SetTopMargin(0.05)
c9.SetBottomMargin(0.13)
c9.SetFrameFillStyle(0)
c9.SetFrameBorderMode(0)
c9.SetFrameFillStyle(0)

myTree.Draw("QIE11DigiTDC>>h9","","")
c9.cd()
c9.Update();
c9.SaveAs(plotDir + "QIE11DigiTDC" + ".png")
c9.SaveAs(plotDir + "QIE11DigiTDC" + ".pdf")
c9.SaveAs(plotDir + "QIE11DigiTDC" + ".root")

c10 = ROOT.TCanvas("c10","c10",850,600)
pad10 = ROOT.TPad("pad10","This is pad10",0.02,0.02,0.98,0.98,21)
pad10.UseCurrentStyle()
pad10.Draw()
pad10.cd()
pad10.SetGrid();
#h7 = gROOT.FindObject('QIE11DigiFC, run')
h10= ROOT.TH1F("h10","QIE10 Digi LETDC",100, 40, 80)
h10.GetXaxis().SetTitle("TDC")
h10.GetXaxis().CenterTitle(True)
#h10.GetYaxis().CenterTitle(True)
#h10.GetYaxis().SetTitle("Count")
#h10.GetYaxis().SetTitleOffset(2.3)
h10.SetLineColor(45)
h10.SetFillColor(4)
h10.GetYaxis().SetLabelOffset(0.007)
h10.GetYaxis().SetTitleOffset(1.3)
h10.SetStats(0)
c10.SetHighLightColor(2)
c10.Range(0,0,1,1)
c10.SetFillColor(0)
c10.SetBorderMode(0)
c10.SetBorderSize(2)
c10.SetTickx(1)
c10.SetTicky(1)
c10.SetLeftMargin(0.18)
c10.SetRightMargin(0.04)
c10.SetTopMargin(0.05)
c10.SetBottomMargin(0.13)
c10.SetFrameFillStyle(0)
c10.SetFrameBorderMode(0)
c10.SetFrameFillStyle(0)

myTree.Draw("QIE10DigiLETDC>>h10","","")
c10.cd()
c10.Update();
c10.SaveAs(plotDir + "QIE10DigiLETDC" + ".png")
c10.SaveAs(plotDir + "QIE10DigiLETDC" + ".pdf")
c10.SaveAs(plotDir + "QIE10DigiLETDC" + ".root")

c11 = ROOT.TCanvas("c11","c11",850,600)
pad11 = ROOT.TPad("pad11","This is pad11",0.02,0.02,0.98,0.98,21)
pad11.UseCurrentStyle()
pad11.Draw()
pad11.cd()
pad11.SetGrid();
#h7 = gROOT.FindObject('QIE11DigiFC, run')
h11= ROOT.TH1F("h11","QIE11 Digi CapID",0, -2, 4)
h11.GetXaxis().SetTitle("QIE11 CapID")
h11.GetXaxis().CenterTitle(True)
#h11.GetYaxis().CenterTitle(True)
#h11.GetYaxis().SetTitle("Count")
#h11.GetYaxis().SetTitleOffset(2.3)
h11.SetLineColor(4)
#h11.SetFillColor(4)
h11.GetYaxis().SetLabelOffset(0.007)
h11.GetYaxis().SetTitleOffset(1.3)
h11.SetStats(0)
c11.SetHighLightColor(2)
c11.Range(0,0,1,1)
c11.SetFillColor(0)
c11.SetBorderMode(0)
c11.SetBorderSize(2)
c11.SetTickx(1)
c11.SetTicky(1)
c11.SetLeftMargin(0.18)
c11.SetRightMargin(0.04)
c11.SetTopMargin(0.05)
c11.SetBottomMargin(0.13)
c11.SetFrameFillStyle(0)
c11.SetFrameBorderMode(0)
c11.SetFrameFillStyle(0)

myTree.Draw("QIE11DigiCapID>>h11","","")
c11.cd()
c11.Update();
c11.SaveAs(plotDir + "QIE11DigiCapID" + ".png")
c11.SaveAs(plotDir + "QIE11DigiCapID" + ".pdf")
c11.SaveAs(plotDir + "QIE11DigiCapID" + ".root")

c12 = ROOT.TCanvas("c12","c12",850,600)
pad12 = ROOT.TPad("pad12","This is pad12",0.02,0.02,0.98,0.98,21)
pad12.UseCurrentStyle()
pad12.Draw()
pad12.cd()
pad12.SetGrid();
#h7 = gROOT.FindObject('QIE11DigiFC, run')
h12= ROOT.TH1F("h12","QIE10 Digi CapID",0, 0, 6)
h12.GetXaxis().SetTitle("QIE10 CapID")
h12.GetXaxis().CenterTitle(True)
#h12.GetYaxis().CenterTitle(True)
#h12.GetYaxis().SetTitle("Count")
#h12.GetYaxis().SetTitleOffset(2.3)
h12.SetLineColor(4)
#h12.SetFillColor(4)
h12.GetYaxis().SetLabelOffset(0.007)
h12.GetYaxis().SetTitleOffset(1.3)
h12.SetStats(0)
c12.SetHighLightColor(2)
c12.Range(0,0,1,1)
c12.SetFillColor(0)
c12.SetBorderMode(0)
c12.SetBorderSize(2)
c12.SetTickx(1)
c12.SetTicky(1)
c12.SetLeftMargin(0.18)
c12.SetRightMargin(0.04)
c12.SetTopMargin(0.05)
c12.SetBottomMargin(0.13)
c12.SetFrameFillStyle(0)
c12.SetFrameBorderMode(0)
c12.SetFrameFillStyle(0)

myTree.Draw("QIE10DigiCapID>>h12","","")
c12.cd()
c12.Update();
c12.SaveAs(plotDir + "QIE10DigiCapID" + ".png")
c12.SaveAs(plotDir + "QIE10DigiCapID" + ".pdf")
c12.SaveAs(plotDir + "QIE10DigiCapID" + ".root")



	#pass


def fC():

	pass	


if __name__ == "__main__":


	recHitPlot()
	#digi()
	#fC()




