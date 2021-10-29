

def test_registration(client):
    """
    TESTS THE WHOLE REGISTRATION MODULE
    :param client:
    :return:
    """
    # checking if registration get request works well
    response = client.get("/register")
    assert response.status_code == 200

    # VALID POST REQUEST
    response = client.post('/register', data=dict(
        username="farazer",
        email="faraz@flaskbloger.com",
        password="faraz123",
        confirm_password="faraz123"
    ), follow_redirects=True)
    assert b'Your account has been created!' in response.data
    assert response.status_code == 200 or 302


def test_login_route(client):
    """
    TESTS THE WHOLE LOGIN MODULE
    :param client:
    :return:
    """
    # checking if login get request works well
    response = client.get("/login")
    assert response.status_code == 200

    # INVALID POST REQUEST USING UNREGISTERED USER
    response1 = client.post('/login', data=dict(
        email="abc@email.com",
        password="abc"
    ), follow_redirects=True)
    assert b'Login Unsuccessful. Please check email and password' in response1.data

    # VALID POST REQUEST USING A REGISTERED USER
    response = client.post('/login',  data=dict(
        email="faraz@flaskbloger.com",
        password="faraz123"
    ), follow_redirects=True)
    assert b'Logout' in response.data
    assert response.status_code == 200 or 302




