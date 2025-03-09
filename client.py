import requests
import os

BASE_URL = "http://127.0.0.1:8000/api/"  # Change this if deployed
TOKEN_FILE = "token.txt"

def save_token(token):
    """ Save the token to a file """
    with open(TOKEN_FILE, "w") as f:
        f.write(token)

def load_token():
    """ Load the token from a file """
    if os.path.exists(TOKEN_FILE):
        with open(TOKEN_FILE, "r") as f:
            return f.read().strip()
    return None

def delete_token():
    """ Delete the saved token (logout) """
    if os.path.exists(TOKEN_FILE):
        os.remove(TOKEN_FILE)

def is_logged_in():
    """ Check if user is logged in """
    return load_token() is not None

def login():
    """ Authenticate user and get a token """
    username = input("🔑 Enter username: ")
    password = input("🔒 Enter password: ")

    response = requests.post(BASE_URL + "login/", json={"username": username, "password": password})

    if response.status_code == 200:
        token = response.json().get("token")
        save_token(token)
        print(f"✅ Login successful! You are now logged in.")
    else:
        print("❌ Login failed:", response.json())

def logout():
    """ Log out by deleting the saved token """
    delete_token()
    print("👋 Logged out successfully!")

def list_professors():
    """ Fetch and display the list of professors (authenticated request) """
    token = load_token()
    headers = {"Authorization": f"Token {token}"} if token else {}

    response = requests.get(BASE_URL + "professors/", headers=headers)

    if response.status_code == 200:
        print("\n📚 Professors Available:")
        for professor in response.json():
            print(f"🧑‍🏫 {professor['id']} - {professor['name']}")
    else:
        print("❌ Failed to fetch professors:", response.json())

def submit_rating():
    """ Submit a rating for a professor """
    token = load_token()
    if not token:
        print("❌ Please login first.")
        return

    professor_id = input("Enter Professor ID: ")
    module_instance_id = input("Enter Module Instance ID: ")
    rating = input("Enter Rating (1-5): ")

    headers = {"Authorization": f"Token {token}"}
    data = {"professor": professor_id, "module_instance": module_instance_id, "rating": int(rating)}

    response = requests.post(BASE_URL + "ratings/", json=data, headers=headers)

    if response.status_code == 201:
        print("✅ Rating submitted successfully!")
    else:
        print("❌ Failed to submit rating:", response.json())

def view_ratings():
    """ View all ratings (authenticated request) """
    token = load_token()
    headers = {"Authorization": f"Token {token}"} if token else {}

    response = requests.get(BASE_URL + "ratings/", headers=headers)

    if response.status_code == 200:
        print("\n⭐ Ratings Available:")
        for rating in response.json():
            print(f"📌 Professor: {rating['professor']} | Module: {rating['module_instance']} | Rating: {rating['rating']}")
    else:
        print("❌ Failed to fetch ratings:", response.json())

def main():
    """ Command-line interface for the client """
    while True:
        print("\n📌 Available Commands:")
        if is_logged_in():
            print("1️⃣ Logout")
        else:
            print("1️⃣ Login")
        print("2️⃣ List Professors")
        print("3️⃣ Submit a Rating")
        print("4️⃣ View Ratings")
        print("5️⃣ Exit")

        choice = input("👉 Enter your choice: ")

        if choice == "1":
            if is_logged_in():
                logout()
            else:
                login()
        elif choice == "2":
            list_professors()
        elif choice == "3":
            submit_rating()
        elif choice == "4":
            view_ratings()
        elif choice == "5":
            print("👋 Exiting...")
            break
        else:
            print("❌ Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
