#!/usr/bin/env python

import pytest
import subprocess
from contextlib import contextmanager
from laymansHGVS import laymansHGVS

@contextmanager
def not_raises(exception, msg):
    try:
        yield
    except exception:
        raise pytest.fail(msg)


def test_import():
    interpretation = laymansHGVS.interpret("Genome1(Gene1):c.25A>G")
    assert interpretation
    for interpretation_substring in ["Genome1", "25", "has a A", "has a G"]:
        assert interpretation_substring in interpretation


def test_cli():
    output = subprocess.run(['explain_HGVS', '--variant',
                            'Genome1(Gene1):c.25A>G'],
                            stdout=subprocess.PIPE)
    output = output.stdout.decode('utf-8')
    for interpretation_substring in ["Genome1", "25", "has a A", "has a G"]:
        assert interpretation_substring in output


def test_protein_sub():
    test_set = ['LRG_199p1:p.Trp24Cys',
                'LRG_199p1:p.Trp24Ter']
    interpretations = map(laymansHGVS.interpret, test_set)
    assert all(interpretations)


def test_protein_del():
    test_set = ['LRG_199p1:p.Trp24*',
                'LRG_199p1:p.Val7del',
                'LRG_199p1:p.(Val7del)',
                'LRG_199p1:p.Trp4del',
                'NP_003997.1:p.Lys23_Val25del',
                'LRG_232p1:p.(Pro458_Gly460del)',
                'NP_000213.1:p.(Val559_Glu561del)',
                'p.Gly2_Met46del']
    interpretations = map(laymansHGVS.interpret, test_set)
    assert all(interpretations)


def test_protein_indel():
    test_set = ['p.Cys28delinsTrpVal',
                'p.Cys28_Lys29delinsTrp',
                'NP_004371.2:p.(Asn47delinsSerSerTer)',
                'p.(Pro578_Lys579delinsLeuTer)',
                'NP_003070.3:p.(Glu125_Ala132delinsGlyLeuHisArgPheIleValLeu)']
    interpretations = map(laymansHGVS.interpret, test_set)
    assert all(interpretations)


def test_protein_ins():
    test_set = ['p.His4_Gln5insAla',
                'p.Lys2_Gly3insGlnSerLys',
                'p.(Met3_His4insGlyTer)',
                'NP_004371.2:p.(Pro46_Asn47insSerSerTer)']
    interpretations = map(laymansHGVS.interpret, test_set)
    assert all(interpretations)
