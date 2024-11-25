// for (inicialização, condição, final) {};
const inputs = document.querySelectorAll('.required');
const span = window.document.getElementsByClassName('span-required');
let erro = false
const botao = window.document.getElementsByClassName('submit');

function nameValidate() {
  if (inputs[0].value.length <= 3) {
    span[0].style.display = 'block';
    erro = true
  }
  else{
    span[0].style.display = 'none';
    erro = false
  }
}

function senhaValidate1() {
  if (inputs[1].value.length <= 8){
    span[1].style.display = 'block';
    erro = true
  }
  else {
    span[1].style.display = 'none';
    erro = false
  }
};

function senhaValidate2() {
  if (inputs[2].value.length <= 8 || inputs[2].value != inputs[1].value) {
    span[2].style.display = 'block';
    erro = true
  }
  else {
    span[2].style.display = 'none';
    erro = false
  }
};

document.getElementById('submitar').onclick = function submit() {
  if (erro == true) {
    window.alert('Por favor corrija os erros nas informações de login')
  }

  else if (inputs[0].value.length == 0 || inputs[1].value.length == 0 || inputs[2].value.length == 0) {
    window.alert('Preencha todos os campos')
  }

  else {
    window.alert('Cadastrado com sucesso!')
  }
}