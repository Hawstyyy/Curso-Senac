// document.write(/[az]/i.test('AZ'));
// document.write('<br>');
// document.write(/love/i.test('LovE'));
// document.write('<br>');
// document.write(/[\bx]/i.test('123x'));
// document.write('<br>');
// document.write(/\s/i.test(' w'));
// document.write('<br>');

// document.write(/^\d{2}\/\d{2}\/\d{4}$/.test('33/33/3333'));

// let dia = /^(0[1-9]|1[0-9]|2[0-9]|3[0-1])$/;
// document.write(dia.test('32'));

// let ano = /^\d{4}$/;
// document.write(ano.test('24'));
// document.write(ano.test('2024'));

// let data = /^(0[1-9]|1[0-9]|2[0-9]|3[0-1]\/0[1-9]|1[0-2])\/\d{4}$/;
// document.write(data.test('22/04/2120'))

// let cpf = /^([0-9]{3}\.[0-9]{3}\.[0-9]{3}\-[0-9]{2})$/
// document.write(cpf.test('111.222.333-69'))

const email = /^[a-zA-Z0-9._%+-]+\@[a-zA-Z0-9.-]+\.[a-zA-Z.-]{2,}$/;
const inputs = window.document.getElementsByClassName('input-required');
const span = window.document.getElementsByClassName('span-required')

function emailValidate() {
  if (email.test(inputs[0].value)){
    removeError(0)
  }
  else {
    setError(0)
  }
}

function removeError(index) {
  span[index].style.display = 'none'
}

function setError(index) {
  span[index].style.display = 'block'
}