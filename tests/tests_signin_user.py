from django.test import Client


def test_with_authenticated_client(client, django_user_model):
    username = "test"
    password = "test"
    user = django_user_model.objects.create_user(username=username, password=password)
    client.force_login(user)
    respons = client.get('/personal_area', follow=True)
    assert respons.status_code == 200
    respons2 = client.post('/personal_area')
    assert respons2.content.find(b"run your job search now") == -1
