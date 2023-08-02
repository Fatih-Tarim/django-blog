from rest_framework.test import APITestCase
from django.urls import reverse, include, path

##Models
from blogapp.models import YazilarModel, KategoriModel, YorumModel
from django.contrib.auth.models import User

import json


#urls
from dj_rest_auth import urls as rest_urls

urlpatterns = [
    path('api/', include(rest_urls)),
]

class PostCreate(APITestCase):
    login_url = rest_urls.reverse('rest-login')

    def setUp(self):
        self.create_url = reverse("yazilar")
        self.username= "asus"
        self.password= "asus.123"
        self.user = User.objects.create(username=self.username, password=self.password)
        self.api_login()
    
    def api_login(self):
        response = self.client.post(self.login_url, data = {"username":"asus", "password":"asus.123"})
        self.assertEqual(200, response.status_code)
        self.assertTrue("key" in json.loads(response.content))
        self.token = response.data["access"]
        self.client.credentials(HTTP_AUTHORIZATION='Bearer ' + self.token)

    




