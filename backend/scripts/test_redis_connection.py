import os
import sys
import urllib.parse
from datetime import datetime

# Add the parent directory to sys.path to ensure we can import open_webui
current_dir = os.path.dirname(os.path.abspath(__file__))
parent_dir = os.path.dirname(current_dir)
sys.path.append(parent_dir)

try:
    from open_webui.utils.redis import get_redis_client
except ImportError:
    # If running from backend/ directly, this might happen if open_webui is not a package or path issue
    # But open_webui seems to be a package in backend/
    print("Could not import get_redis_client. Ensure you are running this from the backend directory.")
    sys.exit(1)

def test_redis_connection():
    print("Testing Redis connection using open_webui.utils.redis.get_redis_client...")
    
    try:
        # Get connection using the utility function
        # This function reads REDIS_URL and other configs from env.py (which loads .env)
        r = get_redis_client()
        
        if r is None:
            print("Failed to get Redis client. Check your configuration.")
            return

        # Test 1: Ping
        print("1. Testing Ping...")
        if r.ping():
            print("   Ping successful!")
        else:
            print("   Ping failed.")
            return

        # Test 2: Write
        test_key = "test_connection_key"
        test_value = f"Hello Redis! {datetime.now().isoformat()}"
        print(f"2. Testing Write (Set {test_key})...")
        r.set(test_key, test_value)
        print("   Write successful!")

        # Test 3: Read
        print(f"3. Testing Read (Get {test_key})...")
        value = r.get(test_key)
        print(f"   Read value: {value}")
        
        if value == test_value:
            print("   Read verification successful!")
        else:
            print(f"   Read verification failed! Expected '{test_value}', got '{value}'")

        # Clean up
        print("4. Cleaning up...")
        r.delete(test_key)
        print("   Cleanup successful!")
        
        print("\nAll Redis tests passed successfully!")

    except Exception as e:
        print(f"\nError during Redis test: {e}")
        import traceback
        traceback.print_exc()

if __name__ == "__main__":
    # We rely on open_webui.env loading the .env file automatically
    # or the user setting environment variables before running the script
    
    # Print REDIS_URL from os.environ to verify what's being used
    # Note: open_webui.env loads .env into os.environ
    env_redis_url = os.environ.get("REDIS_URL")
    if env_redis_url:
        masked_url = env_redis_url
        if "@" in env_redis_url:
            parts = env_redis_url.split("@")
            masked_url = f"****@{parts[-1]}"
        print(f"Using REDIS_URL from environment: {masked_url}")
    else:
        print("WARNING: REDIS_URL not found in environment variables.")
    
    test_redis_connection()
