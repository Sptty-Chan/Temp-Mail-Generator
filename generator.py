import requests, random, re, string
from urllib.parse import quote
from bs4 import BeautifulSoup as parser

def emailParser(emailTable):
    emailFrom = re.search("<span>From: </span><span>(.*?)<", emailTable).group(1)
    emailSubject = re.search("<span>Subject: </span><div.*?<h1.*?;\">(.*?)</h1>", emailTable).group(1)
    emailBody = re.search("<div class=\"e7m mess_bodiyy\"><div dir=\"auto\">(.*?)</div></div>", emailTable).group(1)
    results = f"""\r                                        
\rDari: {emailFrom}
\rSubjek: {emailSubject}
\rPesan: {emailBody}
\r{'='*50}"""
    print(results)

domainList = [
    "puxa.top",
    "domaain34.online",
    "hieu.in",
    "eliotkids.com",
    "jojoo.online",
    "mailngon.top",
    "motquephu.online",
    "wilsonmade.net",
    "disipulo.com",
    "annoysa.shop",
    "gmailbrt.com",
    "setxko.com",
    "filevino.com",
    "pdaworld.store",
    "likevip.net",
]

username = "".join(random.choice(f"{string.ascii_lowercase}{string.ascii_uppercase}{string.digits}") for z in range(15))
domain = random.choice(domainList)
cookies = f"surl={domain}/{username}/"
email = f"{username}@{domain}"
print(f"Email anda: {email}")
print("Tekan ctrl + z untuk berhenti")
print("="*50)
print("="*50)
url_validator = 'https://generator.email/check_adres_validation3.php'
headers  = {
    'authority': 'generator.email',
    'accept': '*/*',
    'accept-language': 'id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7',
    'content-type': 'application/x-www-form-urlencoded; charset=UTF-8',
    'cookie': cookies,
    'origin': 'https://generator.email',
    'sec-ch-ua': '" Not A;Brand";v="99", "Chromium";v="101"',
    'sec-ch-ua-mobile': '?1',
    'sec-ch-ua-platform': '"Android"',
    'sec-fetch-dest': 'empty',
    'sec-fetch-mode': 'cors',
    'sec-fetch-site': 'same-origin',
    'user-agent': 'Mozilla/5.0 (Linux; Android 11; Infinix X688B) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/101.0.4951.40 Mobile Safari/537.36',
    'x-requested-with': 'XMLHttpRequest',
}
encodedMail = quote("[\"{email}\"]")
cookies_2 = f"embx={encodedMail}; surl={domain}/{username}"
payloadString = f"usr={username}&dmn={domain}"
response = requests.post(url_validator, headers=headers, data=payloadString).json()
if response["status"] != "good":
    print("Domain tidak valid, coba jalankan ulang script ini.")
    exit()
headers_2 = headers.copy()
headers_2.update({
    "cookie": cookies_2,
})

ifonemail = 0
readedMail = []
while True:
    print("\rMenunggu email masuk", end="")
    response_2 = requests.get("https://generator.email/inbox1/", headers=headers_2, allow_redirects=True)
    noe = re.search("This mailbox  have <span id=\"mess_number\">(\d+)</span>", response_2.text)
    if noe:
        if int(noe.group(1)) == 1:
            if not ifonemail:
                emailParser(response_2.text)
                ifonemail = 1
        else:
            emailTable = parser(response_2.text, "html.parser").find("div", {"id": "email-table"})
            if emailTable:
                for i in emailTable:
                    try:
                        ahref = i["href"]
                        cookies_3 = f"embx={encodedMail}; surl={ahref[1:]}"
                        tokensgn = ahref.split("/")[-1]
                        if tokensgn not in readedMail:
                            readedMail.append(tokensgn)
                            headers_2.update({
                                "cookie": cookies_3,
                            })
                            response_3 = requests.get("https://generator.email/inbox1/", headers=headers_2, allow_redirects=True)
                            emailParser(response_3.text)
                    except KeyError:
                        pass

