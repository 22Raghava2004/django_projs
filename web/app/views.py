from django.shortcuts import render,redirect
from app.forms import contactForm

def index(request):
    form=contactForm()
    if request.method=='POST':
        form=contactForm(request.POST)
        if form.is_valid():
            return redirect('calc')


    
    return render(request,'index.html',{'form':form})
def calculator(request):
    result=None
    if request.method=='POST':
        num1=int(request.POST['num1'])
        num2=int(request.POST['num2'])
        operation=request.POST['operations']
        if operation=='add':
            result=num1+num2
        elif operation=='subtract':
            result=num1-num2
        elif operation=='multiply':
            result=num1*num2
        elif operation=='divide':
            result=num1/num2
        
    return render(request,'calc.html',{'result':result})

# Create your views here.
'''🔹 Example

models.py

from django.db import models

class Student(models.Model):
    name = models.CharField(max_length=100)
    age = models.IntegerField()


forms.py

from django import forms
from .models import Student

class StudentForm(forms.ModelForm):
    class Meta:
        model = Student
        fields = ['name', 'age']


views.py

from django.shortcuts import render
from .forms import StudentForm   # ✅ only import the form

def register(request):
    if request.method == 'POST':
        form = StudentForm(request.POST)
        if form.is_valid():
            form.save()  # saves data into Student model automatically
    else:
        form = StudentForm()
    return render(request, 'register.html', {'form': form})

register.html
<form method="post">
    {% csrf_token %}
    <input type="text" name="name" placeholder="Enter name">
    <input type="number" name="age" placeholder="Enter age">
    <button type="submit">Add</button>
</form>

<h3>All Students:</h3>
<ul>
    {% for s in students %}
        <li>{{ s.name }} - {{ s.age }}</li>
    {% endfor %}
</ul>


✅ No need to from .models import Student —
because your StudentForm already does that connection.

🔹 When you do need to import the model

Only if you’re directly interacting with the model yourself — for example:

students = Student.objects.all()


or

Student.objects.filter(age__gte=18)


Then you’ll need:

from .models import Student

🔹 Summary
Task	What to import
Submitting form data	✅ Only import form
Querying or displaying data	✅ Import both model and form
Admin panel	✅ Only register model in admin.py

Would you like me to show how to display all saved students from the database on the same page after form submission?'''
