from django.urls import reverse
import pytest
from rest_framework.test import APIClient


@pytest.fixture
def client_api():
    client = APIClient()
    return client

# test for index urls
@pytest.mark.django_db
class TestIndexUrls:
    def test_accounts_index_urls_view(self, client_api):
        url = reverse("accounts:api-v1:index")
        response = client_api.get(url)
        assert response.status_code == 200
