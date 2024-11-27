const numproc = window.document.getElementsByClassName('input-required');
const regexNumProc = /^([0-9]{7})\-([0-9]{2})\.([0-9]{4})8\.12\.([0-9]{4})$/;
const span = window.document.getElementsByClassName('span-required');

function numProcVerify() {
  if(regexNumProc.test(numproc[0].value)){
    span[0].style.display = 'block'
    span[0].innerText = 'Consultado com sucesso!'
    span[0].style.color = 'black'
  }
  else {
    span[0].style.display = 'block'
  }
};