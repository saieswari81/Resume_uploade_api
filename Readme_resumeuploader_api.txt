You need to have a look at the imageuploader project before going into this.

There in the imageuploader project, we have discussed in detail about how to handle a image field. How to save it.
How to delete it, when the instance get deleted.
How the image files are stored inside the media files.
How the root url for the media are configured inside the settings.py file.

Like so....

Next when u type 
pip freeze

You need to have virtualenv and virtualenvwrapper-win both installed in your system.
If you dont have it, go to pypi.org and search for these and install it first.

------------------

First create an virutal environment for this project:

mkvirtualenv resumeuploader (this is as per his videos)

In our case we have our virutal environment as 'geekyshows'

pip freeze for this new virutal environment will be empty. So we need to install all the necessagy packages first.

go to pypi.org and 
search for django

pip install django


pip install djangorestframework


to use the image field or file field in database, we need to have pillow installed

pip install Pillow

---------------------------------

To have your image files and docs files uploaded by the user in your local system/external storage, we need to configure the location.
Or else it will be stored in the main project directory under the name (what you have given in the upload_to) in the models.py

In that case, the instance will be stored, but when you try to view the image or access the file(doc) from the admin panel , you wont
be able to see or download it.

Because django does not know where to look for the the stored files in your localsyste/external storage.

To make django understand on where to go and look for these media files, You need to add a section called static()
inside the urls.py file

from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [] + static(settings.MEDIA_URL + document_root=settings.MEDIA_ROOT)


Now in the settings.py file you can define the MEDIA_ROOT to a particular directory inside your project folder.

settings.py

MEDIA_ROOT = BASE_DIR / 'media'


MEDIA_URL = '/media/'

Generally MEDIA_URL is defined, when you use an external storage to store your media files. But it is always a good practice to 
define it, even when using a local storage.

---------------------------------------

Until now we have only seen the basics of django projects. We have seen how to add data in the admin panel and view the data.

But our job here is to add the data from the front end. That is, if we supply the data from the web browser and add it to the 
database, its a complete django project, which we have seen already.
But here the data will come from the front end in JSON fil. The front end can be a web browser client, or a JAVA appliation or a Android
application or a python application, can be anything. All we need is to add the data coming from the front end (the data is 
usually in the JSON format) and save it in the database.

Similary, deliver the data from the database and deliver it to the front end in the JSON format.

The front end will deal with the data on how to deliver it to the end user, depending in the application they are in.

In this project, we will test our api using POSTMAN.

---------------------------------

To create an api, in the rest framework, we need to have serializers

So we will first create the serializers.py file


from django import serializers
from .models import Profile

class ProfileSerializer(serializers.ModelSerializer):
	class Meta:
		model = Profile
		fields = '__all__' or 
		fields = ['id', 'name', 'gender', 'dob', 'email', 'address', 'state', 'preferred_job_cities', 'pimage', 'rdoc']




---------------------------------
views.py

We need two request types

1. POST (To save the data)

2. GET ( to retrieve the data)

First we need to import several packages from the REST_FRAMEWORK.



from rest_framework.response import Response

from .models import Profile

from .serializer import ProfileSerializer

from rest_framework.views import APIView 

from rest_framework import status

class ProfileView(APIView):
	def post(self, request, format=None):
		serializer = ProfileSerializer(data=request.data)
		if serializer.is_valid():
			serializer.save()
			res = {
				'msg': 'Resume Uploaded Successfully',
				'status' : 'Success',
				'candidate' : serializer.data,
			}
			return Response(res, status=status.HTTP_201_CREATED)
		# res = {'msg': 'Resume Upload Failed', 'candidate': serializer.errors}
		return Respons(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


	def get(self, request, format=None):
		profile = Profile.objects.all()
		serializer = ProfileSerializer(profile, many=True)
		res = {'status': 'Success', 'candidates': serializer.data}
		return Response(res, status=status.HTTP_200_OK)
		# return Response(serializer.data, status=status.HTTP_200_OK)


--------------------------------------------

urls.py

Next we need to define an url for our api

under the prject folder

urlpatterns = [
	path('api/', include('api.urls')),
]


urls.py inside the api folder


from django.urls import path

from api import views

urlpatterns = [
	path('resume/', views.ProfileView.as_view(), name='resume')
]

Here in the video, he did another path for the get reequest like this

	path('listresume/', views.ProfileView.as_view(), name='listresume')

But i understand that you can use the same link or url for both get and post request.

Depending on the request it will delegate the right request.

Lets try this out and see.

--------------------------------------

To create a dependencies file ----> requirements.txt do the following command 


pip freeze > requirements.txt

---------------------

Use postman to test the api which you just created.


for GET or POST request, use the url (the correct one) in the postman http:// area

For get you can just paste the url and say send

for POST request, firt give the correct url and choose form-data in the body. Then a key - value table will be displayed.

Make sure you enter the field names correctly in the key column, that is, whatever field names you used in the models.py file (
in our case Profile Table), you need to use the same field names as the key. In case of any mispelled, it will complain
and Give the corresponding value for the key (or field name) in the value column.

For uploading files like image or docs, use the file options in the key sections right corner drop down menu.

After filling in all the required fields , just send the data.

If eveything is fine, it should save the data in the database.

--------------------------------------------- 









