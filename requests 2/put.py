import requests

id = 10

url = f"https://68641b8088359a373e978349.mockapi.io/produto/{id}"

produto = {
    "marca": "nike-Daniel",
    "tamanho": "G",
    "preco": 150.00
}

resposta = requests.put(url, data=produto)
print(resposta.status_code)
