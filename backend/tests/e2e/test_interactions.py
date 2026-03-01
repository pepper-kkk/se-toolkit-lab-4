import os
import httpx


def test_get_interactions_returns_200() -> None:
    base_url = os.environ["API_BASE_URL"]
    token = os.environ["API_TOKEN"]

    r = httpx.get(f"{base_url}/interactions/", headers={"X-API-Key": token})
    assert r.status_code == 200
    base_url = os.environ["API_BASE_URL"].rstrip("/")


def test_get_interactions_response_is_a_list() -> None:
    base_url = os.environ["API_BASE_URL"].rstrip("/")
    token = os.environ["API_TOKEN"]

    r = httpx.get(f"{base_url}/interactions/", headers={"X-API-Key": token})
    assert r.status_code == 200
    assert isinstance(r.json(), list)
