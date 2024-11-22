// window.alert('alert')
// window.confirm('confirm')
// window.prompt('prompt da silva')

// let x = BigInt(218331983792132132);
// console.log(x);

// let tipo = typeof x;
// console.log(tipo);

// let nota = 10.5;
// console.log(nota.toFixed(2).replace('.',','));

// let nome = 'nome doido';
// console.log('sem crase: ' + nome);
// console.log(`com crase: ${nome}`)

// let nomeAlert = window.prompt('bota o teu nome ai');
// window.alert(`bem-vindo ${nomeAlert}`);

// let x = 10;
// while (x < 50){
//   x++;
//   console.log(x);
// };

// logicos - &&(and), ||(or), !(not)

// operador ternario - condico ?(if) expressao1 :(else) expressao2

// let media = 4
// media >= 7 ? console.log('aprovado') : console.log('reprovado')

// let nomeAlert = window.prompt('bota o teu nome ai');
// document.write(`bem-vindo ${nomeAlert}`);

// document.write(Date());

// window.alert('sudo rm -rf /');

// let string = 'hello';
// console.log(string.length);
// console.log(string.charAt(0));
// console.log(string.toLowerCase())
// console.log(string.toUpperCase())

// let stringbranco = 'hello world'
// console.log(stringbranco.trim())
// console.log(stringbranco.repeat(2))

// function funcao(p1,p2){ 
//   return p1 * p2
// }
// funcao(1,2)

// window.onload = function(){
//   let h1 = window.document.getElementsByTagName('h1')[0]
//   console.log(h1)
//   h1.style.background="blue"
// };

// window.onclick = function(){
//   let h1 = window.document.getElementsByTagName('h1')[0]
//   h1.innerText='boom'
// };

// window.ondblclick = function(){
//   let h1 = window.document.getElementsByTagName('h1')[0]
//   h1.innerText='bang'
// };

// function correto(){
//   let a = window.document.getElementById('a')
//   a.innerText = 'ta certo'
//   a.style.backgroundColor = 'green'
// };

let i = 0;

function add(){
  let a = window.document.getElementsByTagName('button')[1]
  a.innerText = `Clicou ${i++} vezes`
};