#You talk about your friend Alice, which then reminds you of a story about your coworker Bob. 
#But first you have to explain something about your cousin Carol. 
#You finish you story about Carol and go back to talking about Bob, 
#and when you finish your story about Bob, you go back to talking about Alice. 
#But then you are reminded about your brother David, so you tell a story about him, 
#and then get back to finishing your original story about Alice. 
#Your conversation followed a stack-like structure. 
#The conversation is stack-like because the current topic is always at the top of the stack.
def a():
    print("a() starts")
    b()
    d()
    print("a() returns")

def b():
    print("b() starts")
    c()
    print("b() returns")

def c():
    print("c() starts")
    print("c() returns")

def d():
    print("d() starts")
    print("d() returns")

a()