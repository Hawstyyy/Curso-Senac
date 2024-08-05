import wikipedia
import requests

wikipedia.set_lang("pt")

busca = wikipedia.search(input("- Insira a sua busca: ").capitalize())

pagina = wikipedia.page(busca[0])

print(pagina.summary)
imagens = pagina.images
i = 1
for imagem in imagens:
  image_data = requests.get(imagem, headers={"User-agent":"Mozilla/5.0 (Macintosh; Intel Mac OS X x.y; rv:42.0) Gecko/20100101 Firefox/42.0"}).content
  
  with open('teste' + str(i) +'.png', "wb") as archive:
    archive.write(image_data)
  i += 1