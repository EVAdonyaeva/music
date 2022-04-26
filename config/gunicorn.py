import os

bind = f"0.0.0.0:{os.getenv('APP_PORT')}"
workers = 1
threads = os.cpu_count() * 4
