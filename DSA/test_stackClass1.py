from stack import *
import pytest

@pytest.fixture
def stk():    
    return Stack(5)

def test_PushOneItemInEmptyStack_ItemWillbePushedSuccessfully(stk):    
    # Act    
    stk.push('a')  
    
    # Assert    
    assert stk.peek() == 'a'    
    assert stk.get_size() == 1

def test_PushOneListItemInEmptyStack_ItemShouldbePushedSuccessfully(stk):    
    # Act    
    stk.push([1, 2, 3])    
    
    # Assert    
    assert stk.peek() == [1, 2, 3]    
    assert stk.get_size() == 1

def test_PushNothingInEmptyStack_TypeErrorShouldBeThrown(stk):    
    with pytest.raises(TypeError):        
        stk.push()
        
def test_PopOnAnEmptyStack(stk):    
    #Act    
    assert stk.pop() == 'Stack is empty. Nothing to pop.'
    
def test_PopFromStackWithOneItem_ShouldBeRemoved(stk):    
    stk.push('Bugatti Chiron')    
    
    # Act    
    assert stk.pop() == 'Bugatti Chiron'