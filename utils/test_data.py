VALID_USER = {
    "name": "John Doe",
    "username": "johndoe",
    "email": "john@example.com",
    "phone": "1-770-736-8031",
    "website": "johndoe.com"
}

VALID_POST = {
    "title": "Test Post Title",
    "body": "Test post content goes here",
    "userId": 1
}

VALID_COMMENT = {
    "postId": 1,
    "name": "Test Comment",
    "email": "test@example.com",
    "body": "This is a test comment"
}

INVALID_USER = {
    "name": "",  # Пустое имя
    "username": "",
    "email": "invalid-email"  # Некорректный email
}