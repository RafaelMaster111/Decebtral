from django.shortcuts import render, redirect
from .functions import *
import base64
import string
import random
from io import BytesIO

# Create your views here.
def fnGenerateCaptcha(request):

    # call random.choices() string module to find the string in Uppercase + numeric data. 
    ran = ''.join(random.choices(string.ascii_uppercase + string.digits, k = 4))
    base32_letters = base64.b32encode(bytearray(str(ran), 'ascii')).decode('utf-8')[0:6]
    myFont = ImageFont.truetype('Roboto-Regular.ttf', 35)
    myImage = create_image((200, 100), 'yellow', base32_letters, myFont, 'black')
    buffered = BytesIO()
    myImage.save(buffered, format='JPEG')
    img_str = base64.b64encode(buffered.getvalue()).decode('utf-8')
    request.session['real_code'] = base32_letters
    return render(request, "main.html", {'image':img_str})

def fncheckcode(request):
    if request.method == 'POST':
        print("111")
        code = request.POST.get('captcha-code')
        real_code = request.session.get('real_code')
        print(real_code)
        print(code)
        if real_code == code:
            return redirect("https://www.apple.com/macbook-pro/")
        else:
            return redirect('/')