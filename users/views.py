from django.shortcuts import render
import pyrebase



config = {
      "databaseURL": "https://appstore-c6abb-default-rtdb.firebaseio.com",
     "apiKey": "AIzaSyDQR2koeUIL7AKS1gyYpMaOx5tmiEifeAo",

    "authDomain": "appstore-c6abb.firebaseapp.com",

  

    "projectId": "appstore-c6abb",

    "storageBucket": "appstore-c6abb.appspot.com",

    "messagingSenderId": "875358590820",

    "appId": "1:875358590820:web:786e1b3fda9791c5a80c71",
    "measurementId": "G-J0LMCBEFXM"



}

firebase = pyrebase.initialize_app(config)
authe = firebase.auth()
database= firebase.database()


# Create your views here.
def index(request):
    channel_name = database.child('Data').child('Name').get().val()
    channel_age = database.child('Data').child('Age').get().val()

    return render (request,'users/index.html',{
        "channel_name":channel_name,
        "channel_age":channel_age,
    })


def sigIn(request):

    if request.method =="POST":
        email= request.POST.get('email')
        password = request.POST.get('password')
        try:
            user = authe.sign_in_with_email_and_password(email,password)
        except:
            message = "invalid credential"
            return render(request, 'users/signin.html', {'message':message})

        return render(request, 'users/welcome.html',{'email':email, })

        
    return render(request, "users/signin.html")

