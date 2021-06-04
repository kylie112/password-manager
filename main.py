import pyrebase
import stdiomask
firebaseConfig={ 'apiKey': "AIzaSyA-EuY1Bz2iy3CxOtzKbbeb0ifg_qV5ppE",
    'databaseURL': 'https://passwdmanager-39c62-default-rtdb.firebaseio.com',
    'authDomain': "passwdmanager-39c62.firebaseapp.com",
    'projectId': "passwdmanager-39c62",
    'storageBucket': "passwdmanager-39c62.appspot.com",
    'messagingSenderId': "621867461176",
    'appId': "1:621867461176:web:bee7d43dc5eefbe82914cd"
}
firebase = pyrebase.initialize_app(firebaseConfig)

auth= firebase.auth()
db= firebase.database()

# verification
def authO(email,password):
    try:
        auth.sign_in_with_email_and_password(email,password)
        return 1
    except:
        return 0

#database queries handling

def createPasswd():
    site=input("Site: ")
    email=input("Email: ")
    Password=stdiomask.getpass()
    data={'password':Password,'email':email}
    
    users=db.child("data").get()
    db.child("data").child(site).push(data)

    print("\t password saved!!! ")

ccc=0
def searchSite(searchQ):
    sites=db.child("data").get()
    for ss in sites.each():
        if ss.key()==searchQ:
            kk=ss.key()
            dumpData(kk)
            ccc=1
            break
    return ccc

def dumpData(kk):
    sites=db.child("data").child(kk).get()
    print('\n')
    for ss in sites.each():
        print("Email: ", ss.val()['email']," |  Password: ",ss.val()['password'])
        print("-"*60)

# menu

def menu():
    option=""
    while option !='q':
         #print("-"*40)
        print("-"*40)
        print("-"*17,"MENU","-"*17)
        print("1. Create New password")
        print("2. Find a password for a site or app")
        print("q. Exit ")
        option=input(" ")
        if option=='1':
            createPasswd()
        elif option=='2':
            searchQ=input("Enter site or app name: ")
            out=searchSite(searchQ)
            if out < 1:
                print("\nPassword for this website or app doesn't exist in database. ")
                print("If Want to same password for ",searchQ," Enter 1\n ")

        elif option=='q':
            break
        else:
            continue


c=0
while c==0:
    email=input("Email: ")
    password=stdiomask.getpass()
    out=authO(email,password)
    if out!=c:
        menu()
        break
    else:
        print("Invaid user or password.\n ")
        continue