"""
API Client client for interacting with Flask API
"""

import requests
import json
import os
from dotenv import load_dotenv

load_dotenv()

# API Configuration
API_BASE_URL = os.getenv("FLASK_API_URL", "http://localhost:5000")

def get_api_info():
    """Get API information"""
    try:
        response = requests.get(f"{API_BASE_URL}/")
        response.raise_for_status()
        return response.json()
    except requests.exceptions.RequestException as e:
        return {"error": str(e)}

# Monitoring endpoint when the API is running
def check_health():
    """Check API health"""
    try:
        response = requests.get(f"{API_BASE_URL}/health")
        response.raise_for_status()
        return response.json()
    except requests.exceptions.RequestException as e:
        return {"error": str(e)}

def main():
    # Test API info
    print("1. Getting API information...")
    info = get_api_info()
    if "error" in info:
        print(f" Error: {info['error']}")
        print(" Make sure Flask API is running")
    else:
        print(" API Information:")
        print(json.dumps(info, indent=2))
    
    print()
    
    # Test health
    health = check_health()
    if "error" in health:
        print(f" Error: {health['error']}")
    else:
        print(" Health Status:")
        print(json.dumps(health, indent=2))

if __name__ == "__main__":
    main()
