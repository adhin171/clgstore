from django.db import models

class Store(models.Model):
    class Meta:
        verbose_name = "Store"
        verbose_name_plural = "Stores"
    GENDER_CHOICES = [
        ('Male', 'Male'),
        ('Female', 'Female'),
        ('Other', 'Other'),
    ]
    DEPARTMENT_CHOICES = [
        ('Electronics','Electronics'),
        ('IT','IT'),
        ('Business','Business'),
    ]
    COURSE_CHOICES = {
        'Electronics': [
            ('Bsc.Electronics','Bsc.Electronics'),
        ],
        'IT': [
            ('Bsc.Computer Science','Bsc.Computer Science'),
            ('BCA','BCA'),
        ],
        'Business': [
            ('BBA', 'BBA'),
            ('BA.Economics', 'BA.Economics'),
        ],
    }
    PURPOSE_CHOICES = [
        ('Enquiry','Enquiry'),
        ('Place Order', 'Place Order'),
        ('Return', 'Return'),
    ]
    MATERIALS_CHOICES = [
        ('NoteBook','NoteBook'),
        ('Pen','Pen'),
        ('Paper','Paper'),
    ]


    name = models.CharField(max_length=250)
    dateofbirth = models.DateField()
    age = models.IntegerField(default=0)
    gender = models.CharField(max_length=10, choices=GENDER_CHOICES)
    phonenumber = models.IntegerField(default=0)
    email = models.EmailField()
    address = models.CharField(max_length=250)
    department = models.CharField(max_length=20, choices=DEPARTMENT_CHOICES)
    course = models.CharField(max_length=20, choices=[], blank=True)
    purpose = models.CharField(max_length=20, choices=PURPOSE_CHOICES)
    materials = models.CharField(max_length=10, choices=MATERIALS_CHOICES)

    def __str__(self):
        return self.name




