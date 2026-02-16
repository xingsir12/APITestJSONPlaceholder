import requests

from typing import Dict, List, Optional
from utils.logger import logger

class APIClient:
    #Клиент для работы с JSONPlaceholder API

    def __init__(self, base_url: str):
        self.base_url = base_url
        self.session = requests.Session()
        self.session.headers.update({
            "Content-Type" : "application/json"
        })
        logger.info(f"API Client initialized with base URL: {base_url}")

    def _log_request(self, method: str, url: str, **kwargs):
        """Логирование запроса"""
        logger.debug(f"{method} {url}")
        if 'json' in kwargs:
            logger.info(f"Body: {kwargs['json']}")
    
    def _log_responce(self, response: requests.Response):
        """Логирование ответа"""
        logger.info(f"Status: {response.status_code}")
        logger.debug(f"Time: {response.elapsed.total_seconds():.3f}s")

    # == USERS ==

    def get_users(self) -> requests.Response:
        # Получить список всех пользователей
        return self.session.get(f"{self.base_url}/users")
    
    def get_user(self, user_id: int) -> requests.Response:
        # Получить пользователя по ID
        return self.session.get(f"{self.base_url}/users/{user_id}")
    
    def create_user(self, user_data: Dict) -> requests.Response:
        # Создать нового пользователя
        return self.session.post(f"{self.base_url}/users", json=user_data)
    
    def update_user(self, user_id: int, user_data: Dict) -> requests.Response:
        # Обновить пользователя
        return self.session.put(f"{self.base_url}/users/{user_id}", json=user_data)

    def delete_user(self, user_id: int) -> requests.Response:
        # Удалить пользователя
        return self.session.delete(f"{self.base_url}/users/{user_id}")
    
    # == POSTS ==
    def get_posts(self, user_id: Optional[int] = None) -> requests.Response:
        # Получить список постов (по user_id)
        url = f"{self.base_url}/posts"
        params = {"userId": user_id} if user_id else {}
        return self.session.get(url, params=params)
    
    def get_post(self, post_id: int) -> requests.Response:
        # Получить 1 пост по его id
        return self.session.get(f"{self.base_url}/posts/{post_id}")
    
    def create_post(self, post_data: Dict) -> requests.Response:
        # Создать новый пост
        return self.session.post(f"{self.base_url}/posts", json=post_data)

    def update_post(self, post_id: int, post_data: Dict) -> requests.Response:
        # Обновить пост
        return self.session.put(f"{self.base_url}/posts/{post_id}", json=post_data)
    
    def delete_post(self, post_id: int) -> requests.Response:
        # Удалить пост
        return self.session.delete(f"{self.base_url}/posts/{post_id}")
    
    # == COMMENTS ==
    
    def get_comments(self, post_id: Optional[int] = None) -> requests.Response:
        # Получить комментарии (по post_id)
        url = f"{self.base_url}/comments"
        params = {"postId": post_id} if post_id else {}
        return self.session.get(url, params=params)
    
    def get_comment(self, comment_id: int) -> requests.Response:
        # Получить комментарий по ID
        return self.session.get(f"{self.base_url}/comments/{comment_id}")
