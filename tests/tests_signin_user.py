def test_with_authenticated_client(client, django_user_model):
    username = "test"
    password = "test"
    django_user_model.objects.create_user(username=username, password=password)
    client.force_login(user)
    respons = client.get('/')
    assert respons.status_code == 200
