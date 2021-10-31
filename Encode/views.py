from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .forms import EncodedDataForm
from .Encoder import encode

# Create your views here.
@login_required
def encodePage(request):
    form = EncodedDataForm()
    if request.method == "POST":
        form = EncodedDataForm(request.POST, request.FILES)

        if form.is_valid:
            instance = form.save(commit=False)
            instance.user = request.user

            StringLength = encode(instance.SavingPath, instance.Starting_Index, instance.Ghap, instance.Add_a_Value, instance.HiddenData)

            instance.LengthOfString=StringLength
            instance.save()
            return redirect('profile')
    context = {
        'form': form
    }
    return render(request, 'Encode/Encode.html', context)