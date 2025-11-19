from runpy import run_path


def test_integration_example():
    module = run_path("app/app.py")
    app = module['app']
    client = app.test_client()
    response = client.get('/')
    assert response.status_code == 200