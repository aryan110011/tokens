import requests

def check_token(token):
    url = f"https://graph.facebook.com/v17.0/me?access_token={token}"
    try:
        res = requests.get(url)
        data = res.json()

        if "name" in data:
            print(f"\n✅ Valid Token\n👤 Name: {data['name']}\n🆔 ID: {data['id']}")
        elif "error" in data:
            print(f"\n❌ Invalid Token\n🚫 Error: {data['error']['message']}")
        else:
            print("\n⚠️ Unexpected response received.")
    except Exception as e:
        print(f"\n❗ Error during request: {e}")

if __name__ == "__main__":
    token = input("🔑 Enter your Facebook Token: ").strip()
    check_token(token)
