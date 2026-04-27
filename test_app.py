from app import app

def test_app_exists():
    assert app is not None

def test_home_status_code():
    tester = app.test_client()
    response = tester.get('/')
    assert response.status_code == 200

def test_home_data():
    tester = app.test_client()
    response = tester.get('/')
    assert b'Professor' in response.data

def test_404_page():
    tester = app.test_client()
    response = tester.get('/pagina-que-nao-existe')
    assert response.status_code == 404

def test_method_not_allowed():
    tester = app.test_client()
    response = tester.post('/')
    assert response.status_code == 405

# comentário para gerar PR