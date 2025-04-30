import os

class Config:
    # Generate a strong, random secret key (this is just an example, don't use this exact one)
    SECRET_KEY = os.urandom(24).hex()  # Use a truly random key
    SQLALCHEMY_DATABASE_URI = 'mysql://your_username:your_password@localhost/smart_donation' # Replace with your credentials
    SQLALCHEMY_TRACK_MODIFICATIONS = False