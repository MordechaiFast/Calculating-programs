from timeMeasures import *
BHRD = TimeInterval(2,5,204)

def test_fractions():
    assert TimeInterval(1.25) == (1,6)
    assert TimeInterval(0, 7.5) == (0,7,540)
    assert TimeInterval(1.1) == (1,2,432)
    assert TimeInterval(0,0,1.5) == (0,0,1)
def test_nagative_input():
    assert TimeInterval(2,-1) == (1,23)
    assert TimeInterval(-1,-1,-1) == (-2,22,1079)
    assert TimeInterval(0,-30) == (-2,18)
    assert TimeInterval(-29.5) == (-30,12)

def test_adding_tuple():
    assert BHRD + (1, 12) == (3, 17, 204)

def test_negetive_result():
    assert BHRD - (7,) == (-5, 5, 204)
    assert BHRD - (7, 5, 204) == (-5,)
    assert BHRD - (7, 6) == (-6, 23, 204)

def test_index_retreval():
    assert BHRD[0] == 2
    assert BHRD[1] == 5
    assert BHRD[2] == 204
    #assert BHRD['days'] == 2
    #assert BHRD['hours'] == 5
    #assert BHRD['chalakim'] == 204
def test_index_setting():
    newExample = TimeInterval()
    newExample[0] = 1
    newExample[1] = 2
    newExample[2] = 3
    assert newExample[0] == 1
    assert newExample[1] == 2
    assert newExample[2] == 3
    #newExample['days'] = 4
    #newExample['hours'] = 5
    #newExample['chalakim'] = 6
    #assert newExample.days == 4
    #assert newExample.hours == 5
    #assert newExample.chalakim == 6
def test_index_out_of_bounds():
    try: assert BHRD[3]
    except IndexError : pass

def test_non_tuple_comparison():
    try: assert BHRD == 2
    except TypeError: pass 
    try: assert BHRD >= 2
    except TypeError: pass
def test_non_tuple_math():
    try: BHRD + 2
    except TypeError: pass
    try: BHRD - 2
    except TypeError: pass

def test_eq():
    assert     BHRD == (2, 5, 204)
    assert not BHRD == (1, 2, 3)
    assert not BHRD == (2, 5, 200)
    assert not BHRD == (2, 5)
def test_gt():
    assert     BHRD > (2, 5, 203)
    assert not BHRD > (2, 5, 204)
    assert not BHRD > (2, 5, 205)
def test_ge():
    assert     BHRD >= (2, 5, 204)
    assert     BHRD >= (2, 5, 203)
    assert not BHRD >= (2, 5, 205)
def test_lt():
    assert     BHRD < (2, 5, 205)
    assert not BHRD < (2, 5, 204)
    assert not BHRD < (2, 5, 203)

def test_subtraction():
    assert BHRD - (1, 2, 3) == (1, 3, 201)

from calendarUnits import Year
def test_negetive_year():
    assert Year(0 ).molad == (3, 7, 695)
    assert Year(-1).molad == (5, 22, 899)