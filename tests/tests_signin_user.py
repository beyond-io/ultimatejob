def test_with_authenticated_client(client, django_user_model):
	username = "test"
	password = "test"
	user = django_user_model.objects.create_user(username=username, password=password)
	client.force_login(user)
	respons = client.get('/personal_area')
	assert respons.status_code == 301


