from project.main import app
##comment
def test_home_route():
    response = app.test_client().get("/")
    assert response.status_code == 200