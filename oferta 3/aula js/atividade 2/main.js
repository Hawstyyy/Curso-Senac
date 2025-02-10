async function request (url) {
  const resposta = await fetch(url);
  const json = await(await resposta).json();

  const body = await json;
  const pokemon =  {
    nome: body.name,
    habilidades: body.abilities,
    imagem: body.sprites.front_default
  };

  const div = document.createElement("div");
  const span = document.createElement("span");
  const img = document.createElement("img");
  img.src = pokemon.imagem;
  span.innerText = pokemon.nome;
  div.appendChild(img);
  div.appendChild(span);
  document.getElementById("pokemon").appendChild(div);
}

request("https://pokeapi.co/api/v2/pokemon/1");
request("https://pokeapi.co/api/v2/pokemon/5");
request("https://pokeapi.co/api/v2/pokemon/10");
request("https://pokeapi.co/api/v2/pokemon/15");
request("https://pokeapi.co/api/v2/pokemon/20");
request("https://pokeapi.co/api/v2/pokemon/25");
request("https://pokeapi.co/api/v2/pokemon/30");
request("https://pokeapi.co/api/v2/pokemon/35");
request("https://pokeapi.co/api/v2/pokemon/40");
request("https://pokeapi.co/api/v2/pokemon/45");
