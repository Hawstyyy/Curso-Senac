const botao = document.querySelector("#menu-header>nav>button");
const listaMenu = document.querySelector("#menu-header>nav>ul");

botao.addEventListener("click", function () {
  listaMenu.classList.toggle("ativo");
});
