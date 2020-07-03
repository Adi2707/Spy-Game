from IPython.display import clear_output
import time


print('++++++++++++++++++++++++++++')
print()
print('+++++  Welcome to the SPY GAME  +++++')
print()
print('++++++++++++++++++++++++++++')
time.sleep(2.5)
clear_output()

print ('Enter your name.')
name = input()
clear_output()

print('Checking database, please wait...')
for x in range (0,5):  
    b = "Loading" + "." * x
    print (b, end="\r")
    time.sleep(1)
clear_output()

print(f'Welcome SECRET AGENT #{name.upper()}_007.')
time.sleep(2)

history = ''

def encode(code):
    global history
    
    for x in range (0,5):  
        b = "Encoding" + "." * x
        print (b, end="\r")
        time.sleep(1)
    finalcode = ''
    change =''
    dic = {' ':'~', '0':'A!', '1':'A^', '2':'B!', '3':'B^', '4':'C!', '5':'C^', '6':'D!', '7':'D^', '8':'E!', '9':'E^', 'a':'A@', 'b':'A#', 'c':'A$', 'd':'A%', 'e':'B@', 'f': 'B#','g':'B$', 'h':'B%', 'i':'C@', 'j': 'C#', 'k':'C$', 'l':'C%','m':'D@', 'n':'D#', 'o':'D$', 'p':'D%', 'q':'E@','r':'E#','s':'E$','t':'E%','u':'F!', 'v':'F@','w':'F#', 'x':'F$', 'y':'F%', 'z':'F^'}
    for char in code:
        change =dic[char]
        finalcode+=change
    history+= f' --> Input:{code}  :::  Encoded code: {finalcode}\n'
    print(f'Encrypted code: {finalcode}')
  
    
    
def decode(code):
    
    global history
    
    for x in range (0,5):  
        b = "Decoding" + "." * x
        print (b, end="\r")
        time.sleep(1)
    finalcode = ''
    change =''
    
    dic = {'~':' ', 'A!':'0', 'A^':'1', 'B!':'2', 'B^':'3', 'C!':'4', 'C^':'5', 'D!':'6', 'D^':'7', 'E!':'8', 'E^':'9', 'A@':'a', 'A#':'b', 'A$':'c', 'A%':'d', 'B@':'e', 'B#':'f','B$':'g', 'B%':'h', 'C@':'i', 'C#': 'j', 'C$':'k', 'C%':'l','D@':'m', 'D#':'n', 'D$':'o', 'D%':'p', 'E@':'q','E#':'r','E$':'s','E%':'t','F!':'u', 'F@':'v','F#':'w', 'F$':'x', 'F%':'y', 'F^':'z'}
   
    i=0
    while i <=len(code)-2:
        
        if code[i] == '~':
            change = dic['~']
            finalcode+=change
            i+=1
        else:
            change=dic[code[i:i+2]]
            finalcode+=change
            i+=2
    finalcode = finalcode.upper()
    history+= f'--> Input: {code}  :::  Decoded code: {finalcode}\n'
    print(f'Decoded code: {finalcode}')     
    
    
def main():    
    print("Do you want to 'Encode' or 'Decode'?\n1) To Encode, enter: E\n2) To Decode, enter: D")
    response = input()
    for x in range (0,4):  
        b = "Wait" + "." * x
        print (b, end="\r")
        time.sleep(1)
    clear_output()
    
    
    if response == 'E':
        print('Encoding process begins...')
        time.sleep(2.5)
        clear_output()
        print('Enter the code to be encoded. ')
        code = input().lower()
        clear_output()
        encode(code)
        
        reply = ''
        print('Do you want to use the system again? (Y/N)')
        reply = input()
        if reply == 'Y':
            clear_output()
            for x in range (0,3):  
                b = "Wait" + "." * x
                print (b, end="\r")
                time.sleep(1)
            main()
        else:
            clear_output()
            permission = ''
            print('Do you want to see the history? (Y/N)')
            permission = input()
            clear_output()
            for x in range (0,2):
                b = "Wait" + "." * x
                print (b, end="\r")
                time.sleep(1)
            clear_output()
            if permission == 'Y':
                print('History: ')
                print(history)
                print(f'Thanks for using the system SECRET AGENT #{name.upper()}_007.\nHope to see you soon.\nTake care.')
            else:
                print(f'Thanks for using the system SECRET AGENT #{name.upper()}_007.\nHope to see you soon.\nTake care.')
            
        
    
        
    elif response == 'D':
        print('Decoding process begins...')
        time.sleep(2.5)
        clear_output()
        print('Enter the code to be decoded. ')
        code = input()
        clear_output()
        decode(code)    
        
        reply = ''
        print('Do you want to use the system again? (Y/N)')
        reply = input()
        if reply == 'Y':
            clear_output()
            for x in range (0,3):  
                b = "Wait" + "." * x
                print (b, end="\r")
                time.sleep(1)
            main()
        else:
            clear_output()
            permission = ''
            print('Do you want to see the history? (Y/N)')
            permission = input()
            clear_output()
            for x in range (0,2):
                b = "Wait" + "." * x
                print (b, end="\r")
                time.sleep(1)
            clear_output()
            if permission == 'Y':
                print('History: ')
                print(history)
                print(f'Thanks for using the system SECRET AGENT #{name.upper()}_007.\nHope to see you soon.\nTake care.')
            else:
                print(f'Thanks for using the system SECRET AGENT #{name.upper()}_007.\nHope to see you soon.\nTake care.')
            
            
main()
