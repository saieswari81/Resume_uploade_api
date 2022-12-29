from django.db import models

# Create your models here.

STATE_CHOICES = (
    ('Alabama', 'Alabama'),
    ('Alaska', 'Alaska'),
    ('Arizona', 'Arizona'),
    ('Arkansas', 'Arkansas'),
    ('California', 'California'),
    ('Colorado', 'Colorado'),
    ('Connecticut', 'Connecticut'),
    ('Delaware', 'Delaware'),
    ('Florida', 'Florida'),
    ('Georgia', 'Georgia'),
    ('Hawaii', 'Hawaii'),
    ('Idaho', 'Idaho'),
    ('Illinois', 'Illinois'),
    ('Indiana', 'Indiana'),
    ('Iowa', 'Iowa'),
    ('Kansas', 'Kansas'),
    ('Kentucky', 'Kentucky'),
    ('Louisiana', 'Louisiana'),
    ('Maine', 'Maine'),
    ('Maryland', 'Maryland'),
    ('Massachusetts', 'Massachusetts'),
    ('Michigan', 'Michigan'),
    ('Minnesota', 'Minnesota'),
    ('Mississippi', 'Mississippi'),
    ('Missouri', 'Missouri'),
    ('Montana', 'Montana'),
    ('Nebraska', 'Nebraska'),
    ('Neveda', 'Neveda'),
    ('New Hampshire', 'New Hampshire'),
    ('New Jersey', 'New Jersey'),
    ('New Mexico', 'New Mexico'),
    ('New York', 'New York'),
    ('North Carolina', 'North Carolina'),
    ('North Dakota', 'North Dakota'),
    ('Ohio', 'Ohio'),
    ('Oklahoma', 'Oklahoma'),
    ('Oregon', 'Oregon'),
    ('Pennsylvania', 'Pennsylvania'),
    ('Rhode Island', 'Rhode Island'),
    ('South Carolina', 'South Carolina'),
    ('South Dakota', 'South Dakota'),
    ('Tennessee', 'Tennessee'),
    ('Texas', 'Texas'),
    ('Utah', 'Utah'),
    ('Vermont', 'Vermont'),
    ('Virginia', 'Virginia'),
    ('Washington', 'Washington'),
    ('West Virginia', 'West Virginia'),
    ('Wisconsin', 'Wisconsin'),
    ('Wyoming', 'Wyoming'),
)


class Profile(models.Model):
    name = models.CharField(max_length=100)
    dob = models.DateField()
    gender = models.CharField(max_length=30)  # This will be a radio button in the front end
                                              # (we will not implement this here in this project). For more details see
                                              # resumeuploader project.
    email = models.EmailField()
    address = models.CharField(max_length=250)
    state = models.CharField(choices=STATE_CHOICES, max_length=100)  # this will be drop down menu in the front end.
    mobile_num = models.PositiveIntegerField()
    pimage = models.ImageField(upload_to='pimages', blank=True, null=True)
    rdoc = models.FileField(upload_to='rdocs', blank=False)
