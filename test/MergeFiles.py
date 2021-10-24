#! /usr/bin/env python
import os
import getopt
import sys

path        = "/tmp/cisik/"
prefix      = "/tmp/cisik/"
destination = "/tmp/cisik/CRAFT"

DIR = os.listdir(path)

ss = "Tree"

for dd in DIR:
  print "Reading directory "+dd
  ROOTFILES = os.listdir(path+"/"+dd)
  command = "hadd -f "+destination+"/"+dd+"_"+ss+".root "
  for ll in ROOTFILES:
    command += prefix+dd+"/"+ll+" "
  print command
  os.system(command)
