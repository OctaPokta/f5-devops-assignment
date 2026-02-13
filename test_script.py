import sys
import requests
import time

def run_tests():
    print("Waiting for Nginx to start...")
    time.sleep(3)
    
    url_ok = "http://nginx_server:8080"
    url_error = "http://nginx_server:8081"
    
    try:
        # Test 1: Expecting 200 OK
        print(f"Testing {url_ok}...")
        resp = requests.get(url_ok)
        if resp.status_code == 200:
            print("SUCCESS: Got 200 OK")
        else:
            print(f"FAIL: Expected 200, got {resp.status_code}")
            sys.exit(1)

        # Test 2: Expecting 500 Error
        print(f"Testing {url_error}...")
        resp = requests.get(url_error)
        if resp.status_code == 500:
             print("SUCCESS: Got 500 Error")
        else:
            print(f"FAIL: Expected 500, got {resp.status_code}")
            sys.exit(1)

    except Exception as e:
        print(f"CRITICAL FAIL: {e}")
        sys.exit(1)

if __name__ == "__main__":
    run_tests()