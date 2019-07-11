#test file __init__.py

import pytest
import funct 

def test_score_imgeq():
    args={'first': "../image1.png", 'second':"../image11.png" }
    assert funct.diff(args)==1

def test_score_imgdif():
    args={'first': "../image1.png", 'second':"../image2.png" }
    assert funct.diff(args)<1


