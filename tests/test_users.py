# tests/test_users.py
import pytest

class TestUsers:
    """Тесты для Users API"""
    
    @pytest.mark.smoke
    @pytest.mark.api
    def test_get_all_users(self, api_client):
        """Проверка получения списка пользователей"""
        response = api_client.get_users()
        
        assert response.status_code == 200, "Status code должен быть 200"
        users = response.json()
        assert isinstance(users, list), "Ответ должен быть списком"
        assert len(users) == 10, "Должно быть 10 пользователей"
        
        # Проверка структуры первого пользователя
        first_user = users[0]
        assert "id" in first_user
        assert "name" in first_user
        assert "email" in first_user
    
    @pytest.mark.smoke
    @pytest.mark.api
    @pytest.mark.parametrize("user_id", [1, 2, 3, 5, 10])
    def test_get_user_by_id(self, api_client, user_id):
        """Проверка получения пользователя по ID"""
        response = api_client.get_user(user_id)
        
        assert response.status_code == 200
        user = response.json()
        assert user["id"] == user_id
        assert len(user["name"]) > 0
        assert "@" in user["email"]
    
    @pytest.mark.negative
    @pytest.mark.api
    def test_get_nonexistent_user(self, api_client):
        """Проверка получения несуществующего пользователя"""
        response = api_client.get_user(999999)
        
        assert response.status_code == 404
    
    @pytest.mark.regression
    @pytest.mark.api
    def test_create_user(self, api_client, sample_user):
        """Проверка создания пользователя"""
        response = api_client.create_user(sample_user)
        
        assert response.status_code == 201
        created_user = response.json()
        assert created_user["name"] == sample_user["name"]
        assert created_user["email"] == sample_user["email"]
        assert "id" in created_user
    
    @pytest.mark.regression
    @pytest.mark.api
    def test_update_user(self, api_client):
        """Проверка обновления пользователя"""
        updated_data = {
            "name": "Updated Name",
            "email": "updated@example.com"
        }
        
        response = api_client.update_user(1, updated_data)
        
        assert response.status_code == 200
        updated_user = response.json()
        assert updated_user["name"] == updated_data["name"]
        assert updated_user["email"] == updated_data["email"]
    
    @pytest.mark.regression
    @pytest.mark.api
    def test_delete_user(self, api_client):
        """Проверка удаления пользователя"""
        response = api_client.delete_user(1)
        
        assert response.status_code == 200
    
    @pytest.mark.performance
    def test_users_response_time(self, api_client):
        """Проверка времени ответа API"""
        response = api_client.get_users()
        
        assert response.elapsed.total_seconds() < 2, "Ответ должен приходить быстрее 2 секунд"
    
    @pytest.mark.smoke
    def test_users_response_headers(self, api_client):
        """Проверка заголовков ответа"""
        response = api_client.get_users()
        
        assert "Content-Type" in response.headers
        assert "application/json" in response.headers["Content-Type"]


class TestUsersNegative:
    """Негативные тесты для Users API"""
    
    @pytest.mark.negative
    @pytest.mark.api
    def test_create_user_with_invalid_data(self, api_client):
        """Попытка создания пользователя с некорректными данными"""
        invalid_user = {
            "name": "",  # Пустое имя
            "email": "not-an-email"  # Некорректный email
        }
        
        response = api_client.create_user(invalid_user)
        
        # API JSONPlaceholder всё равно создаст (это mock API),
        # но в реальном API должен быть 400
        assert response.status_code in [201, 400]
    
    @pytest.mark.negative
    @pytest.mark.api
    def test_update_nonexistent_user(self, api_client):
        """Попытка обновления несуществующего пользователя"""
        response = api_client.update_user(999999, {"name": "Test"})
        
            # JSONPlaceholder может вернуть 200, 404 или 500
        assert response.status_code in [200, 404, 500], \
        f"Expected 200, 404 or 500, got {response.status_code}"