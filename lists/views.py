from django.core.exceptions import ValidationError
from django.shortcuts import render, redirect
from django.views.generic import FormView, CreateView, DetailView
from django.contrib.auth import get_user_model
from lists.forms import ExistingListItemForm, ItemForm, NewListForm
from lists.models import Item, List
User = get_user_model()

class HomePageView(FormView):
    template_name = 'lists/home.html'
    form_class = ItemForm

class NewListView(CreateView):
    template_name = 'lists/home.html'
    form_class = NewListForm

    def form_valid(self, form):
        list_ = form.save(owner=self.request.user)
        return redirect(str(list_.get_absolute_url()))

def new_list(request):
    form = NewListForm(data=request.POST)
    if form.is_valid():
        list_ = form.save(owner=request.user)
        return redirect(str(list_.get_absolute_url()))
    return render(request, 'lists/home.html', {'form': form})

def view_list(request, list_id):
    list_ = List.objects.get(id=list_id)
    form = ExistingListItemForm(for_list=list_)
    if request.method == 'POST':
        form = ExistingListItemForm(for_list=list_, data=request.POST)
        if form.is_valid():
            form.save()
            return redirect(list_)
    return render(request, 'lists/list.html', {'list': list_, 'form': form})

class ViewAndAddToList(DetailView, CreateView):
    model = List
    template_name = 'lists/list.html'
    form_class = ExistingListItemForm

    def get_form(self):
        self.object = self.get_object()
        return self.form_class(for_list=self.object, data=self.request.POST)

def my_lists(request, email):
    owner = User.objects.get(email=email)
    return render(request, 'lists/my_lists.html', {'owner': owner})

def share_list(request, list_id):
    list_ = List.objects.get(id=list_id)
    list_.shared_with.add(request.POST['sharee'])
    return redirect(list_)
