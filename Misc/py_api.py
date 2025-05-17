import requests

BASE_URL = "http://example.com/api"  # Replace with your real API base URL


def test_login_success():
    # Step 1: Login with valid credentials
    response = requests.post(f"{BASE_URL}/login", json={
        "username": "valid_user",
        "password": "valid_password"
    })

    assert response.status_code == 200
    data = response.json()
    assert "token" in data


def test_login_failure():
    # Step 2: Login with invalid credentials
    response = requests.post(f"{BASE_URL}/login", json={
        "username": "wrong_user",
        "password": "wrong_password"
    })

    assert response.status_code == 401  # Unauthorized


def test_access_protected_endpoint_with_token():
    # Step 3: Login to get the token
    login_response = requests.post(f"{BASE_URL}/login", json={
        "username": "valid_user",
        "password": "valid_password"
    })
    token = login_response.json()["token"]

    # Step 4: Use token to access protected endpoint
    headers = {
        "Authorization": f"Bearer {token}"
    }
    response = requests.get(f"{BASE_URL}/user/profile", headers=headers)

    assert response.status_code == 200
    assert "username" in response.json()


def test_access_protected_endpoint_without_token():
    # Step 5: Access protected endpoint without token
    response = requests.get(f"{BASE_URL}/user/profile")

    assert response.status_code == 401  # Unauthorized
