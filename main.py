import requests
import threading 
import random
threads = 1
invite_link = input("Enter Server Invite Code: ")
file = input("Enter file where tokens are located: ")
proxies_file = input("Enter the file where the proxies are located: ")


discord_tokens = []
discord_proxies = []
current_token = 0
if ".txt" not in file:
    file += '.txt'
elif ".txt" not in proxies_file:
    proxies_file += ".txt"

with open(file, 'r+') as f:
    tokens = f.readlines()
    for token in tokens:
        discord_tokens.append(token)

with open(proxies_file, 'r+') as f:
    proxies = f.readlines()
    for proxy in proxies:
        discord_proxies.append(proxy)


def fetch_cookies(proxy):
    url = 'https://discord.com'
    session = requests.Session()
    session.proxies = {
        'http': f'http://{proxy}',
        'https': f'http://{proxy}'
    }
    data = session.get(url)
    cookies = data.cookies.get_dict()
    dcfduid = cookies.get('__dcfduid')
    sdcfduid = cookies.get('__sdcfduid')
    session.close()
    return dcfduid, sdcfduid

def joiner():
    global current_token
    proxy = random.choice(proxies)
    try:
        token = discord_tokens[current_token]
    except Exception as error:
        print("Joined Server with all tokens in file!")
        input("Click enter to close")
        exit(0)
    current_token += 1 
    dcfduid, sdcfduid = fetch_cookies(proxy)
    url_join = f"https://discord.com/api/v9/invites/{invite_link}"
    session = requests.Session()
    session.proxies = {
        'http': f'http://{proxy}',
        'https': f'http://{proxy}'
    }
    token = token.replace("\n", "")
    session.headers = {
        "accept": "*/*",
        "accept-encoding": "gzip, deflate, br",
        "accept-language": "en-US,en;q=0.9",
        "authorization": token,
        "content-type": "application/json",
        "cookie": f"__dcfduid={dcfduid}; __sdcfduid={sdcfduid}; __cf_bm=aOVlzqMUt8IgO2jMZ6cFXOfYPJkL5QbB1MfilWZvis4-1659138632-0-Afq4IgiiYEDFQE5TSo8ZtmgFyDc4X7d8AqnQcWBUmtjVFLVyrm3xvq0UaXjI/H7m65bN5bsqRXjqSMvr61jO4gcX00kxM8YXm1XP0iHEhP333WtCD3BVdfgSESWeWuBj4g==; locale=en-US; _gcl_au=1.1.557961870.1659138632; _ga=GA1.2.582448974.1659138632; _gid=GA1.2.1597236155.1659138632; OptanonConsent=isIABGlobal=false&datestamp=Fri+Jul+29+2022+19%3A57%3A39+GMT-0400+(Eastern+Daylight+Time)&version=6.33.0&hosts=&landingPath=https%3A%2F%2Fdiscord.com%2F&groups=C0001%3A1%2CC0002%3A1%2CC0003%3A1; _gat_UA-53577205-2=1",
        "origin": "https://discord.com",
        "referer": "https://discord.com/channels/427943860975435779/891351915638714439",
        "sec-ch-ua": '" Not;A Brand";v="99", "Microsoft Edge";v="103", "Chromium";v="103"',
        "sec-ch-ua-mobile": "?0",
        "sec-ch-ua-platform": '"Windows"',
        "sec-fetch-dest": "empty",
        "sec-fetch-mode": "cors",
        "sec-fetch-site": "same-origin",
        "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.5060.134 Safari/537.36 Edg/103.0.1264.71",
        "x-context-properties": "eyJsb2NhdGlvbiI6IkpvaW4gR3VpbGQiLCJsb2NhdGlvbl9ndWlsZF9pZCI6Ijg3NTA5ODM0MjM3ODU5NDM2NSIsImxvY2F0aW9uX2NoYW5uZWxfaWQiOiI4NzUxMDA5NzQ1OTM3NDkwMTQiLCJsb2NhdGlvbl9jaGFubmVsX3R5cGUiOjB9",
        "x-debug-options": "bugReporterEnabled",
        "x-discord-locale": "en-US",
        "x-super-properties": "eyJvcyI6IldpbmRvd3MiLCJicm93c2VyIjoiQ2hyb21lIiwiZGV2aWNlIjoiIiwic3lzdGVtX2xvY2FsZSI6ImVuLVVTIiwiYnJvd3Nlcl91c2VyX2FnZW50IjoiTW96aWxsYS81LjAgKFdpbmRvd3MgTlQgMTAuMDsgV2luNjQ7IHg2NCkgQXBwbGVXZWJLaXQvNTM3LjM2IChLSFRNTCwgbGlrZSBHZWNrbykgQ2hyb21lLzEwMy4wLjUwNjAuMTM0IFNhZmFyaS81MzcuMzYgRWRnLzEwMy4wLjEyNjQuNzEiLCJicm93c2VyX3ZlcnNpb24iOiIxMDMuMC41MDYwLjEzNCIsIm9zX3ZlcnNpb24iOiIxMCIsInJlZmVycmVyIjoiIiwicmVmZXJyaW5nX2RvbWFpbiI6IiIsInJlZmVycmVyX2N1cnJlbnQiOiIiLCJyZWZlcnJpbmdfZG9tYWluX2N1cnJlbnQiOiIiLCJyZWxlYXNlX2NoYW5uZWwiOiJzdGFibGUiLCJjbGllbnRfYnVpbGRfbnVtYmVyIjoxMzg3MzQsImNsaWVudF9ldmVudF9zb3VyY2UiOm51bGx9"
    }
    data = session.post(url_join, json={})
    if int(data.status_code) == 200:
        print(f"Successfully Joined with token {token}\nInvite Code: {invite_link}\n")
    else:
        print(f"Cannot Join with {token} Detected Captcha\n")
    try:
        token = discord_tokens[current_token]
    except Exception as error:
        print("Joined Server with all tokens in file!")
        input("Click enter to close")
        exit(0)




if __name__ == "__main__":
    for i in range(threads):
        threading.Thread(target=joiner).start()


