from django.shortcuts import render,redirect
from .models import List
from .forms import ListForm
from django.views.decorators.http import require_POST

# Create your views here.
def home(request):
	allitems=List.objects.order_by('id')
	form=ListForm()
	context={'allitems':allitems,'form':form}
	return render(request,'todo/index.html',context)


@require_POST
def add(request):
	form=ListForm(request.POST)
	if form.is_valid():
		item=List(item=request.POST['item'])
		item.save()
	return redirect('index')

def complete(request,item_id):
	item=List.objects.get(pk=item_id)
	item.done=True
	item.save()

	return redirect('index')

def deletecomplete(request):
	List.objects.filter(done=True).delete()
	return redirect('index')

def deleteall(request):
	List.objects.all().delete()
	return redirect('index')