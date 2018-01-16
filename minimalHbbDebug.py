#!/usr/bin/env python
"""
Test module for Hbb workspaces
"""

########################################
# Imports
########################################

import os, itertools
import ROOT

########################################
# Main
########################################

def main():

    rootFile = 'comb_2017_ggHbb.root'
    rootFp = ROOT.TFile.Open(rootFile)
    w = rootFp.Get('w')
    rootFp.Close()


    # Create range over which the r*p* variables are scanned
    rp_min  = 0.9
    rp_max  = 5.0
    nPoints = 4
    rp_testValues = [ rp_min + (rp_max-rp_min)/(nPoints-1)*i for i in xrange(nPoints) ]

    pars = [
        'r1p0',
        'r2p0',
        'r3p0',
        'r0p1',
        'r1p1',
        'r2p1',
        'r3p1',
        ]

    # Loop over permutations and check if all bins are positive
    for perm in itertools.product( rp_testValues, repeat=len(pars) ):

        for iPar, par in enumerate(pars):
            w.var(par).setVal( perm[iPar] )

        for b in bins:
            val = w.function(b).getVal()
            if val < 0.0:
                print 'Permutation', perm, 'NOT passed'
                print 'Found a set of parameter values that yield a negative bin'
                print '  {0:20} = {1}'.format( b, val )

                for par in pars:
                    print '  {0:20} = {1}'.format( par, w.var(par).getVal() )

                return

        print 'Permutation', perm, 'passed'



bins = [
    'qcd_pass_cat1_Bin1',
    'qcd_pass_cat1_Bin2',
    'qcd_pass_cat1_Bin3',
    'qcd_pass_cat1_Bin4',
    'qcd_pass_cat1_Bin5',
    'qcd_pass_cat1_Bin6',
    'qcd_pass_cat1_Bin7',
    'qcd_pass_cat1_Bin8',
    'qcd_pass_cat1_Bin9',
    'qcd_pass_cat1_Bin10',
    'qcd_pass_cat1_Bin11',
    'qcd_pass_cat1_Bin12',
    'qcd_pass_cat1_Bin13',
    'qcd_pass_cat1_Bin14',
    'qcd_pass_cat1_Bin15',
    'qcd_pass_cat1_Bin16',
    'qcd_pass_cat1_Bin17',
    'qcd_pass_cat1_Bin18',
    'qcd_pass_cat1_Bin19',
    'qcd_pass_cat1_Bin20',
    'qcd_pass_cat1_Bin21',
    'qcd_pass_cat1_Bin22',
    'qcd_pass_cat1_Bin23',
    'qcd_pass_cat2_Bin1',
    'qcd_pass_cat2_Bin2',
    'qcd_pass_cat2_Bin3',
    'qcd_pass_cat2_Bin4',
    'qcd_pass_cat2_Bin5',
    'qcd_pass_cat2_Bin6',
    'qcd_pass_cat2_Bin7',
    'qcd_pass_cat2_Bin8',
    'qcd_pass_cat2_Bin9',
    'qcd_pass_cat2_Bin10',
    'qcd_pass_cat2_Bin11',
    'qcd_pass_cat2_Bin12',
    'qcd_pass_cat2_Bin13',
    'qcd_pass_cat2_Bin14',
    'qcd_pass_cat2_Bin15',
    'qcd_pass_cat2_Bin16',
    'qcd_pass_cat2_Bin17',
    'qcd_pass_cat2_Bin18',
    'qcd_pass_cat2_Bin19',
    'qcd_pass_cat2_Bin20',
    'qcd_pass_cat2_Bin21',
    'qcd_pass_cat2_Bin22',
    'qcd_pass_cat2_Bin23',
    ]

########################################
# End of Main
########################################
if __name__ == "__main__":
    main()