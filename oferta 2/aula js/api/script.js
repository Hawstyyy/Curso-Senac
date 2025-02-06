// fetch('./dados.json').then(function(res) {
//   return res.json();
// }).then(function(json) {
//   console.log(json)
// })

fetch('./dados.json')
  .then(res => res.json())
  .then(json => {const pessoa = document.createElement("div");
  const paragrafo = document.createElement("p");

  let frase = ""

  json["Pessoa"].forEach(element => {
      frase = `Eu sou ${element.nome}, tenho ${element.idade} e sou ${element.profissao}`;
      paragrafo.innerText = frase;
      pessoa.appendChild(paragrafo);
      document.getElementById('app').appendChild(pessoa);
  });

})