# tests/test_comments.py
import pytest

class TestComments:
    """Тесты для Comments API"""
    
    @pytest.mark.smoke
    @pytest.mark.api
    def test_get_all_comments(self, api_client):
        """Проверка получения всех комментариев"""
        response = api_client.get_comments()
        
        assert response.status_code == 200
        comments = response.json()
        assert len(comments) == 500  # Всего 500 комментариев
    
    @pytest.mark.regression
    @pytest.mark.api
    def test_get_comments_by_post(self, api_client):
        """Проверка получения комментариев к посту"""
        post_id = 1
        response = api_client.get_comments(post_id=post_id)
        
        assert response.status_code == 200
        comments = response.json()
        assert len(comments) > 0
        
        # Все комментарии должны относиться к указанному посту
        for comment in comments:
            assert comment["postId"] == post_id
    
    @pytest.mark.smoke
    @pytest.mark.api
    @pytest.mark.parametrize("comment_id", [1, 10, 100, 250, 500])
    def test_get_comment_by_id(self, api_client, comment_id):
        """Проверка получения комментария по ID"""
        response = api_client.get_comment(comment_id)
        
        assert response.status_code == 200
        comment = response.json()
        assert comment["id"] == comment_id
        assert "@" in comment["email"]  # Email должен содержать @
    
    @pytest.mark.regression
    def test_comments_have_required_fields(self, api_client):
        """Проверка что комментарии содержат все необходимые поля"""
        response = api_client.get_comments(post_id=1)
        comments = response.json()
        
        required_fields = ["postId", "id", "name", "email", "body"]
        
        for comment in comments:
            for field in required_fields:
                assert field in comment, f"Поле {field} отсутствует"