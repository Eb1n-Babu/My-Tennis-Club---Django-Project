from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.template import loader
from .models import Member


def main(request):
    template = loader.get_template('main.html')
    return HttpResponse(template.render())


def member(request):
    my_members = Member.objects.all()
    # return HttpResponse("Hello, world. You're at the polls page.")
    context = {"my_members": my_members}
    return render(request, 'all_members.html', context)
    # template = loader.get_template("myfirst.html")
    #return HttpResponse(template.render(context, request))

def details(request,id):
    my_members = Member.objects.get(id=id)
    context = {"my_members": my_members}
    return render(request,"details.html",context)

def test(request):
    template = loader.get_template('test.html')
    context = {"fruits":["apples","oranges","pears","bananas"]}
    return HttpResponse(template.render(context,request))

def add_member(request):
    if request.method == "POST":
        first_name = request.POST.get("first_name")
        last_name = request.POST.get("last_name")
        phone_number = request.POST.get("phone_number")
        joining_date = request.POST.get("joining_date")

        if Member.objects.filter(first_name=first_name, last_name=last_name, phone_number=phone_number).exists():
            return HttpResponse("Member already exists")

        Member.objects.create(first_name=first_name, last_name=last_name, phone_number=phone_number,joining_date=joining_date)
        return redirect('main.html')

    return render(request,"add_member.html")

def test2(request):
    datas = Member.objects.all()
    context = {"datas":datas}
    return render(request,"test2.html",context)

def test3(request):
  mydata = Member.objects.all().values()
  template = loader.get_template('test3.html')
  context = {
    'my_members': mydata,
  }
  return HttpResponse(template.render(context, request))

def test4(request):
    mydata = Member.objects.values_list("first_name", flat=True)
    context = {"mydata": mydata}
    return render(request,"test4.html",context)