from datetime import datetime

def user_schema(name, email, password_hash):
    return {
        "name": name,
        "email": email,
        "password_hash": password_hash,
        "created_at": datetime.utcnow()
    }
