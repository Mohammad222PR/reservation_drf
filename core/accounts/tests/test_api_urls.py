from django.urls import reverse
import pytest
from rest_framework.test import APIClient


# test for index urls
@pytest.mark.django_db
class TestIndexUrls:
    def test_accounts_index_urls_view(self):
        client = APIClient()
        url = reverse("accounts:api-v1:index")
        response = client.get(url)
        assert response.status_code == 200
