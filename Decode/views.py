from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .forms import DecodedDataForm
from .Decoder import decode
from .models import DecodedData

# Create your views here.
@login_required
def decodePage(request):
    form = DecodedDataForm()
    if request.method == "POST":
        form = DecodedDataForm(request.POST, request.FILES)

        if form.is_valid:
            instance = form.save(commit=False)
            instance.user = request.user

            String = decode(instance.Starting_Index, instance.Ghap, instance.Add_a_Value, instance.LengthOfString, instance.ImagePath)

            instance.Data=String
            instance.save()
            return redirect('showdata')
    context = {
        'form': form
    }
    return render(request, 'Decode/Decode.html', context)

@login_required
def showdata(request):

    return render(request, 'Decode/ShowData.html')