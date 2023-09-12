from django.db import models

# Create your models here.

class Students(models.Model):
    name=models.CharField(max_length=300, default='none')
    age=models.IntegerField(default=18)
    gender=models.CharField(max_length=2, default='M')
    email=models.EmailField(max_length=100, default='test@gmail.com')

    def __str__(self) -> str:
        return f'name: {self.name}, email: {self.email}, age: {self.email}, gender: {self.gender}'
    
class Account(models.Model):
    pass




############                  LEARNING CRUD OPERATION IN DJANGO SHELL

# >>> from home.models import *
# >>> student = Students.objects.create(name='Shivam', age=23, gender='M', email='shivam@gmail.com')
# >>> student
# <Students: name: Shivam, email: shivam@gmail.com, age: shivam@gmail.com, gender: M>
# >>> student = Students(name='Ankit', age=24, email='ankit@gmail.com', gender='F')
# >>> student.save()
# >>> student
# <Students: name: Ankit, email: ankit@gmail.com, age: ankit@gmail.com, gender: F>
# >>> Students.objects.all()
# <QuerySet [<Students: name: Shivam, email: shivam@gmail.com, age: shivam@gmail.com, gender: M>, <Students: name: Ankit, email: ankit@gmail.com, age: ankit@gmail.com, gender: F>]>
# >>> student = {'name':'Shivansh', 'age':34, 'email':'shivansh@gmail.com', 'gender':'M'}
# >>> Students.objects.create(**student)
# <Students: name: Shivansh, email: shivansh@gmail.com, age: shivansh@gmail.com, gender: M>
# >>> Students.objects.all()
# <QuerySet [<Students: name: Shivam, email: shivam@gmail.com, age: shivam@gmail.com, gender: M>, <Students: name: Ankit, email: ankit@gmail.com, age: ankit@gmail.com, gender: F>, <Students: name: Shivansh, email: shivansh@gmail.com, age: shivansh@gmail.com, gender: M>]>
# >>> Students.objects.get(name='Ankit')
# <Students: name: Ankit, email: ankit@gmail.com, age: ankit@gmail.com, gender: F>
# >>> Students.objects.get(id=2)         
# <Students: name: Ankit, email: ankit@gmail.com, age: ankit@gmail.com, gender: F>
# >>> Students.objects.get(id=0) 
# Traceback (most recent call last):
#   File "<console>", line 1, in <module>
#   File "D:\glitch\django\learn_django\venv\Lib\site-packages\django\db\models\manager.py", line 87, in manager_method
#     return getattr(self.get_queryset(), name)(*args, **kwargs)
#            ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
#   File "D:\glitch\django\learn_django\venv\Lib\site-packages\django\db\models\query.py", line 637, in get
#     raise self.model.DoesNotExist(
# home.models.Students.DoesNotExist: Students matching query does not exist.
# >>> Students.objects.get(id=1) 
# <Students: name: Shivam, email: shivam@gmail.com, age: shivam@gmail.com, gender: M>
# >>> Students.objects.get(id=3) 
# <Students: name: Shivansh, email: shivansh@gmail.com, age: shivansh@gmail.com, gender: M>
# >>> Students.objects.get(id=3).update(email='newemail@gmail.com')
# Traceback (most recent call last):
#   File "<console>", line 1, in <module>
# AttributeError: 'Students' object has no attribute 'update'
# >>> Students.objects.all()[1]
# <Students: name: Ankit, email: ankit@gmail.com, age: ankit@gmail.com, gender: F>
# >>> Students.objects.all()[1].email
# 'ankit@gmail.com'
# >>> for student in Students.objects.all():
# ...     print(f'Name of student is {student.name}')
# ...
# Name of student is Shivam
# Name of student is Ankit
# Name of student is Shivansh
# >>> Students.objects.filter(id=2)
# <QuerySet [<Students: name: Ankit, email: ankit@gmail.com, age: ankit@gmail.com, gender: F>]>
# >>> Students.objects.filter(name='Shivam')
# <QuerySet [<Students: name: Shivam, email: shivam@gmail.com, age: shivam@gmail.com, gender: M>]>
# >>> Students.objects.filter(name='invalid')
# <QuerySet []>
# >>> Students.objects.get(name='Shivam').email = 'updatedemail@gmail.com'
# >>> Students.objects.get(name='Shivam').age = 55                        
# >>> Students.objects.all()                      
# <QuerySet [<Students: name: Shivam, email: shivam@gmail.com, age: shivam@gmail.com, gender: M>, <Students: name: Ankit, email: ankit@gmail.com, age: ankit@gmail.com, gender: F>, <Students: name: Shivansh, email: shivansh@gmail.com, age: shivansh@gmail.com, gender: M>]>
# >>> shiv=Students.objects.get(name='Shivam')    
# >>> shiv.email='updatedemail@gmail.com'
# >>> shiv.age=55                        
# >>> shiv.save()
# >>> Students.objects.all()
# <QuerySet [<Students: name: Shivam, email: updatedemail@gmail.com, age: updatedemail@gmail.com, gender: M>, <Students: name: Ankit, email: ankit@gmail.com, age: ankit@gmail.com, gender: F>, <Students: name: Shivansh, email: shivansh@gmail.com, age: shivansh@gmail.com, gender: M>]>
# >>> shiv
# <Students: name: Shivam, email: updatedemail@gmail.com, age: updatedemail@gmail.com, gender: M>
# >>> shiv.age
# 55
# >>> shiv
# <Students: name: Shivam, email: updatedemail@gmail.com, age: updatedemail@gmail.com, gender: M>
# >>> Students.objects.filter(id=2).update(name='new_name')
# 1
# >>> Students.objects.all()
# <QuerySet [<Students: name: Shivam, email: updatedemail@gmail.com, age: updatedemail@gmail.com, gender: M>, <Students: name: new_name, email: ankit@gmail.com, age: ankit@gmail.com, gender: F>, <Students: name: Shivansh, email: shivansh@gmail.com, age: shivansh@gmail.com, gender: M>]>
# >>> Students.objects.filter(id=1).delete()
# (1, {'home.Students': 1})
# >>> Students.objects.all()
# <QuerySet [<Students: name: new_name, email: ankit@gmail.com, age: ankit@gmail.com, gender: F>, <Students: name: Shivansh, email: shivansh@gmail.com, age: shivansh@gmail.com, gender: M>]>
# >>> Students.objects.get(name='new_name').delete()
# (1, {'home.Students': 1})
# >>> Students.objects.all()
# <QuerySet [<Students: name: Shivansh, email: shivansh@gmail.com, age: shivansh@gmail.com, gender: M>]>
# >>> Students.objects.all().delete()
# (1, {'home.Students': 1})
# >>> Students.objects.all()         
# <QuerySet []>
