import requests

## Example usage for post
url = "http://127.0.0.1:8000/api/turkish-natural-disaster/istanbul"
headers = {
    "Content-Type": "application/json",
    "Authorization": "Bearer admin123"  # Replace with your actual token
}
data = {
    "title": "İstanbul",
    "content": [
        "1999 Marmara Depremi: 17 Ağustos 1999’da gerçekleşen 7.4 büyüklüğündeki deprem, İstanbul’da da hissedilmiş ve şehirde hasara yol açmıştır.",
        "1509 İstanbul Depremi ('Küçük Kıyamet'): 7.2 büyüklüğündeki deprem, büyük yıkıma ve can kaybına neden olmuştur.",
        "2009 İstanbul Sel Felaketi: Şiddetli yağış nedeniyle özellikle Esenler ve çevresinde büyük sel olayları yaşanmıştır."
    ]
}

response = requests.post(url, json=data, headers=headers)

print(response.status_code)
print(response)

## Example usage for get
url = "http://127.0.0.1:8000/api/turkish-natural-disaster/istanbul"
headers = {
    "Authorization": "Bearer admin123"  # Replace with your actual token
}

response = requests.get(url, headers=headers)

print(response.status_code)
print(response.json())

### Output
""""
    {'title': 'İstanbul', 'content': ['1999 Marmara Depremi: 
    17 Ağustos 1999’da gerçekleşen 7.4 büyüklüğündeki deprem, İstanbul’da da hissedilmiş ve şehirde hasara yol açmıştır.', 
    "1509 İstanbul Depremi ('Küçük Kıyamet'): 7.2 büyüklüğündeki deprem, büyük yıkıma ve can kaybına neden olmuştur.", 
    '2009 İstanbul Sel Felaketi: Şiddetli yağış nedeniyle özellikle Esenler ve çevresinde büyük sel olayları yaşanmıştır.']}"
"""