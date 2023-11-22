import pytest


@pytest.fixture
def smart():
    global a,b 
    a=int(input("Enter a first number:-"))
    b=int(input("Enter a second number:-"))
    yield
    
    
@pytest.mark.run(order=2)    
def test_add(smart):
    global res
    res=a+b
    print(res)
    
@pytest.mark.run(order=1)    
def test_sub(smart):
    res=a-b
    print(res)
    
@pytest.mark.run(depends=['test_div'])
def test_mul(smart):
    res=a*b
    print(res)
    
@pytest.mark.skip
def test_div(smart):
    res=a/b
    print(res)
    

    
    

    
    
    
    
    
    
