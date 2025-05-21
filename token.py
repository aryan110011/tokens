import requests

def check_token(token):
    url = f"https://graph.facebook.com/me?access_token={token}"
    try:
        response = requests.get(url)
        data = response.json()

        if 'name' in data:
            print("\n✅ Token is VALID!")
            print(f"👤 Name: {data['name']}")
            print(f"🆔 ID: {data['id']}")
        elif 'error' in data:
            print("\n❌ Token is INVALID!")
            print(f"🚫 Error: {data['error']['message']}")
        else:
            print("\n⚠️ Unexpected response format!")
    except Exception as e:
        print(f"\n❗ Request failed: {e}")

if __name__ == "__main__":
    token = input("🔑 Enter your Facebook Access Token:\n> ").strip()
    check_token(token)
