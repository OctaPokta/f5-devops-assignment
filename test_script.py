import sys
import requests
import time

def run_tests():
    # Wait a moment for Nginx to start up
    time.sleep(2)
    
    # We use the hostname 'nginx_server' which we will define in Docker Compose later
    url_ok = "http://nginx_server:8080"
    url_error = "http://nginx_server:8081"
    
    try:
        # Test 1: Expecting 200 OK
        print(f"Testing {url_ok}...")
        response = requests.get(url_ok)
        if response.status_code == 200:
            print("SUCCESS: Got 200 OK")
        else:
            print(f"FAIL: Expected 200, got {response.status_code}")
            sys.exit(1) # Exit with non-zero code on failure [cite: 22]

        # Test 2: Expecting 500 Error [cite: 16]
        print(f"Testing {url_error}...")
        response = requests.get(url_error)
        if response.status_code == 500:
             print("SUCCESS: Got 500 Error as expected")
        else:
            print(f"FAIL: Expected 500, got {response.status_code}")
            sys.exit(1)

    except requests.exceptions.RequestException as e:
        print(f"CRITICAL FAIL: Could not connect to server. {e}")
        sys.exit(1)

if __name__ == "__main__":
    run_tests()