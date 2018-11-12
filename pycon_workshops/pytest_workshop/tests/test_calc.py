#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
test_pytest_workshop
----------------------------------

Tests for `pytest_workshop` module.
"""

# so before we start writing the code and features, we write these tests
import pytest
from pytest_workshop.calc import Calc
# there is no such class yet; but we will implement it later

def test_add():
    c = Calc()
    result = c.add(5,4)

    assert result == 9   # this is not enough of a test bc we can just hardcode 9
    
def test_add_three_numbers():
    c = Calc()
    result = c.add(5,4,1)

    assert result == 10

def test_add_multiple_items():
    c = Calc()
    result = c.add(*range(1,100))
    
    assert result == 4950
    
def test_subtract_two_numbers():
    assert Calc().sub(9,4) == 5
    
def test_multiply_two_numbers():
    assert Calc().mult(3,4) == 12
    
def test_divide_two_numbers():
    assert Calc().div(22,2) == 11
    
def test_divide_by_zero():
    assert Calc().div(10,0) == 'inf'
    
def test_multiply_by_zero_raises_exception():
    with pytest.raises(ValueError): # contects manager
        Calc().mult(4,0)
        
def test_average():
    assert Calc().avg(range(0,101)) == 50
    
def test_average_empty():
    assert Calc().avg([]) == 'inf'
    
def test_average_upp_treshold():
    assert Calc().avg(range(0,101), upLimit = 51) == 25
    
def test_average_down_treshold():
    assert Calc().avg(range(0,101), downLimit = 50) == 75.5
    
def test_average_thresholds_equal_thresholds():
    assert Calc().avg([2,3,5,6,4,36,7,1], downLimit = 0, upLimit = 0) == 'inf'
    
def test_outlier_removal_from_empty_list():
    assert Calc().avg([], upLimit = 3) == 'inf'
    
def test_avg_manages_non_iterable_type():
    with pytest.raises(TypeError):
        Calc().avg(123)
    # this indeed raises TypeError because len(integer) is not defined in python