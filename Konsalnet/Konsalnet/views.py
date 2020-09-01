from django.shortcuts import render, redirect
from django.http import HttpResponse
from Spec.forms import ChoiceFieldOrder, OptionsField,OptionValue
from Spec.models import SpecRamAdd, Options
from django.http import JsonResponse
from django.core import mail
from django.template.loader import render_to_string
from django.utils.html import strip_tags


def Index(request):
    return render(request, 'index.html')


def Add(request):
    return render(request, 'Add.html')

def AddRam(request):
    nowa_zamowienie = ChoiceFieldOrder()
    if request.method == "POST":
        nowa_zamowienie = ChoiceFieldOrder(request.POST)
        Text = "Can't download data."
        DictModels = {}
        Thenumber = 0
        numberTake = 0
        NrChild = request.POST.get('NrPop')
        for i in range(int(NrChild)):
            if i==0:
                Text = str(request.POST.get('GB')) + "GB" 
                title = request.POST.get('ChoiceFieldComputer')
                Text += " " + SpecRamAdd.objects.get(id=int(title)).Ram + " "
                DictModels[Text] = int(request.POST.get('NrStack'))
                continue
            else:
                numberTake = str(i+1)
                Text = str(request.POST.get('GB' + numberTake)) + "GB"
                title = request.POST.get('ChoiceFieldComputer' + numberTake)
                Text += " " + SpecRamAdd.objects.get(id=int(title)).Ram + " "
                for j in range(len(DictModels)):
                    if Text in DictModels:
                        Thenumber = int(DictModels[Text])
                    else:
                        Thenumber = 0
            DictModels[Text] = 0
            DictModels[Text] = Thenumber + int(request.POST.get('NrStack' + str(numberTake)))       
        Text = ""
        for i in range(len(DictModels)):
            Text += str(list(DictModels)[i]) + " x" + str(list(DictModels.values())[i]) + " <br />"
        return redirect('/Order.html/?TextMail=%s'%Text)

    context = {
         'form': nowa_zamowienie,
     }
    return render(request, 'AddRam.html', context)

def OptionsAct(request):
    if request.method == "POST":
        obj = Options.objects.get(id=1)
        form = OptionValue(request.POST or None, instance=obj)
        if form.is_valid():
            form.save()
    OptionsWindow = OptionsField()
    OptionsWindow["NameHost"].initial = Options.objects.get(id=1).NameHost
    OptionsWindow['NameMail'].initial = Options.objects.get(id=1).NameMail
    OptionsWindow['PassMail'].initial = Options.objects.get(id=1).PassMail
    OptionsWindow['NameToSend'].initial = Options.objects.get(id=1).NameToSend
    OptionsWindow['NamePort'].initial = Options.objects.get(id=1).NamePort
    context = {
        "OptionsWin" : OptionsWindow
    }
    return render(request, 'Options.html', context)

def Trip(request):
    return render(request, 'Trip.html')

def Order(request):
    TextMail = request.GET.get('TextMail')
    if request.method == "POST":
        ValueOpt = Options.objects.get(id=1)
        try:
            connection = mail.get_connection(
                host = ValueOpt.NameHost,
                port = ValueOpt.NamePort,
                username = ValueOpt.NameMail,
                password = ValueOpt.PassMail,
                use_tls = True
            )

            msg = mail.EmailMessage(
                'Ramy i dyski do zamówienia',
                '---------------- <br />' + TextMail + '<br />----------------',
                str(ValueOpt.NameMail),
                [str(ValueOpt.NameToSend),str(ValueOpt.NameMail) ],
                connection=connection,
            )
            msg.content_subtype = 'html'
            msg.send()
        except Exception as e:
            return HttpResponse(e)     
    data_dict = {
        'TextMail':TextMail
    }
    return render(request, 'Order.html', data_dict)