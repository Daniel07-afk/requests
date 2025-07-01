import requests

url = "https://68641b8088359a373e978349.mockapi.io/produto"

resposta = requests.get(url)

print(resposta.text)