import os

def initialize():
    os.makedirs("memory", exist_ok=True)
    os.makedirs("logs", exist_ok=True)

