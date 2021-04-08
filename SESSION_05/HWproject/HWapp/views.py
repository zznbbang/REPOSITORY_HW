from django.shortcuts import render

# Create your views here.

def count(request):
    return render(request,'count.html')

def result(request):
    text = request.POST['text'] #여기 text는 name='text'인가용?
    total_len = len(text)
    no_space = len(text.replace(" ",""))
    if (len(text)==0):
        word_count=0;
    else:
        word_count = len(text.split(" "))
    
    return render(request,'result.html',{
        'text' : text,
        'total_len' : total_len,
        'no_space' : no_space,
        'word_count' : word_count
    })