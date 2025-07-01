import requests

url = "https://68641b8088359a373e978349.mockapi.io/produto"

produto = {
    "marca": "nike-Daniel",
    "tamanho": "G",
    "preco": 150.00
}

resposta = requests.post(url, json=produto)

print(resposta.status_code)
print(resposta.json())