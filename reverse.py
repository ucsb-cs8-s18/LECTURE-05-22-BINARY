
def reverse(s):
    " print the reverse of a string"
    if len(s)<=1:
        return s
    first = s[0]
    rest = s[1:]

    return reverse(rest) + first

def reverseExplained(s):
    " print the reverse of a string"
    print("Calculating reverse of ",s)
    
    if len(s)<=1:
        return s
    first = s[0]
    rest = s[1:]
    reverseRest = reverseExplained(rest)    
    print("s",s,"rest=",rest,"reverseRest",reverseRest,"first=",first,)
    return reverseRest + first
        



def test_reverse_UCSB():
    assert reverse("UCSB")=="BSCU"

def test_reverse_x():
    assert reverse("x")=="x"

def test_reverse_empty():
    assert reverse("")==""
    
def test_reverse_UCSB():
    assert reverse("Cal Poly")=="yloP laC"
