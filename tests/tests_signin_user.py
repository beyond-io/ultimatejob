def test_with_authenticated_client(client, django_user_model):
	username = "test"
	password = "test"
	user = django_user_model.objects.create_user(username=username, password=password)
	client.force_login(user)
	respons1 = client.get('/sign_in')
	respons2 = client.get('/personal_area')
	assert respons1.status_code == 301
	assert respons2.status_code == 301

