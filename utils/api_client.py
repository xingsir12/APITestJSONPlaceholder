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
    
    def _log_response(self, response: requests.Response):
        """Логирование ответа"""
        logger.info(f"Status: {response.status_code}")
        logger.debug(f"Time: {response.elapsed.total_seconds():.3f}s")

    # == USERS ==

    def get_users(self) -> requests.Response:
        # Получить список всех пользователей
        url = f"{self.base_url}/users"
        self._log_request("GET", url)
        response = self.session.get(url)
        self._log_response(response)
        return response
    
    def get_user(self, user_id: int) -> requests.Response:
        # Получить пользователя по ID
        url = f"{self.base_url}/users/{user_id}"
        self._log_request("GET", url)
        response = self.session.get(url)
        self._log_response(response)
        return response
    
    def create_user(self, user_data: Dict) -> requests.Response:
        # Создать нового пользователя
        url = f"{self.base_url}/users"
        self._log_request("POST", url, json=user_data)
        response = self.session.post(url, json=user_data)
        self._log_response(response)
        return response
    
    def update_user(self, user_id: int, user_data: Dict) -> requests.Response:
        # Обновить пользователя
        url = f"{self.base_url}/users/{user_id}"
        self._log_request("PUT", url, json=user_data)
        response = self.session.put(url, json=user_data)
        self._log_response(response)
        return response

    def delete_user(self, user_id: int) -> requests.Response:
        # Удалить пользователя
        url = f"{self.base_url}/users/{user_id}"
        self._log_request("DELETE", url)
        response = self.session.delete(url)
        self._log_response(response)
        return response
    
    # == POSTS ==
    def get_posts(self, user_id: Optional[int] = None) -> requests.Response:
        # Получить список постов (по user_id)
        url = f"{self.base_url}/posts"
        params = {"userId": user_id} if user_id else {}
        self._log_request("GET", url)
        response = self.session.get(url, params=params)
        self._log_response(response)
        return response
    
    def get_post(self, post_id: int) -> requests.Response:
        # Получить 1 пост по его id
        url = f"{self.base_url}/posts/{post_id}"
        self._log_request("GET", url)
        response = self.session.get(url)
        self._log_response(response)
        return response
    
    def create_post(self, post_data: Dict) -> requests.Response:
        # Создать новый пост
        url = f"{self.base_url}/posts"
        self._log_request("POST", url, json=post_data)
        response = self.session.post(url, json=post_data)
        self._log_response(response)
        return response

    def update_post(self, post_id: int, post_data: Dict) -> requests.Response:
        # Обновить пост
        url = f"{self.base_url}/posts/{post_id}"
        self._log_request("PUT", url, json=post_data)
        response = self.session.put(url, json=post_data)
        self._log_response(response)
        return response
    
    def delete_post(self, post_id: int) -> requests.Response:
        # Удалить пост
        url = f"{self.base_url}/posts/{post_id}"
        self._log_request("DELETE", url)
        response = self.session.delete(url)
        self._log_response(response)
        return response
    
    # == COMMENTS ==
    
    def get_comments(self, post_id: Optional[int] = None) -> requests.Response:
        # Получить комментарии (по post_id)
        url = f"{self.base_url}/comments"
        params = {"postId": post_id} if post_id else {}
        response = self.session.get(url, params=params)
        self._log_response(response)
        return response
    
    def get_comment(self, comment_id: int) -> requests.Response:
        # Получить комментарий по ID
        url = f"{self.base_url}/comments/{comment_id}"
        self._log_request("GET", url)
        response = self.session.get(url)
        self._log_response(response)
        return response
