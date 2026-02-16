# tests/test_posts.py
import pytest

class TestPosts:
    """Тесты для Posts API"""
    
    @pytest.mark.smoke
    @pytest.mark.api
    def test_get_all_posts(self, api_client):
        """Проверка получения всех постов"""
        response = api_client.get_posts()
        
        assert response.status_code == 200
        posts = response.json()
        assert len(posts) == 100  # Всего 100 постов
        
        # Проверка структуры поста
        first_post = posts[0]
        assert "id" in first_post
        assert "title" in first_post
        assert "body" in first_post
        assert "userId" in first_post
    
    @pytest.mark.regression
    @pytest.mark.api
    def test_get_posts_by_user(self, api_client):
        """Проверка получения постов конкретного пользователя"""
        user_id = 1
        response = api_client.get_posts(user_id=user_id)
        
        assert response.status_code == 200
        posts = response.json()
        assert len(posts) > 0
        
        # Все посты должны принадлежать указанному пользователю
        for post in posts:
            assert post["userId"] == user_id
    
    @pytest.mark.smoke
    @pytest.mark.api
    @pytest.mark.parametrize("post_id", [1, 5, 10, 50, 100])
    def test_get_post_by_id(self, api_client, post_id):
        """Проверка получения поста по ID"""
        response = api_client.get_post(post_id)
        
        assert response.status_code == 200
        post = response.json()
        assert post["id"] == post_id
        assert len(post["title"]) > 0
        assert len(post["body"]) > 0
    
    @pytest.mark.regression
    @pytest.mark.api
    def test_create_post(self, api_client, sample_post):
        """Проверка создания поста"""
        response = api_client.create_post(sample_post)
        
        assert response.status_code == 201
        created_post = response.json()
        assert created_post["title"] == sample_post["title"]
        assert created_post["body"] == sample_post["body"]
        assert created_post["userId"] == sample_post["userId"]
        assert "id" in created_post
    
    @pytest.mark.regression
    @pytest.mark.api
    def test_update_post(self, api_client):
        """Проверка обновления поста"""
        updated_data = {
            "title": "Updated Title",
            "body": "Updated content",
            "userId": 1
        }
        
        response = api_client.update_post(1, updated_data)
        
        assert response.status_code == 200
        updated_post = response.json()
        assert updated_post["title"] == updated_data["title"]
    
    @pytest.mark.regression
    @pytest.mark.api
    def test_delete_post(self, api_client):
        """Проверка удаления поста"""
        response = api_client.delete_post(1)
        
        assert response.status_code == 200