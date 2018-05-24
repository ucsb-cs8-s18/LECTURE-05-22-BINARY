
import pytest

def toBinary(decimalNumber):
    if decimalNumber == 0:
      return "0"
    elif decimalNumber ==1:
      return "1"
    else:
      lastBit = decimalNumber % 2
      return toBinary( decimalNumber  // 2 )  + str(lastBit)

def toBinaryExplained(decimalNumber):
    print("computing toBinaryExplained("+str(decimalNumber)+")")
    
    if decimalNumber == 0:
      return "0"
    elif decimalNumber ==1:
      return "1"
    else:
      
      lastBit = decimalNumber % 2
      print("otherBits = __________  lastBit=", lastBit)      
      otherBits = toBinaryExplained( decimalNumber  // 2 )
      answer = otherBits + str(lastBit)
      print("otherBits = ", otherBits,  "lastBit=", lastBit)
      return answer


  
def test_toBinary_7():
  assert toBinary(7)=="111"
    
def test_toBinary_3():
  assert toBinary(3)=="11"

def test_toBinary_24():
  assert toBinary(24)=="11000"

def test_toBinary_65():
  assert toBinary(65)=="1000001"

  
