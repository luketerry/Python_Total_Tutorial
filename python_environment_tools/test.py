
from func_oper import multiply,summing

def test_multiply():
    assert multiply(2,3)==6
def test_multiply_n():
    assert multiply('baka~',3)=='baka~baka~baka~'
    
def test_summing():
    assert summing(2,3) == 5
def test_mul_sum():
    assert summing(multiply(2,3),multiply(2,3)) == 12