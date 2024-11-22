function atividade1(){
  let valorConvertido;

  function convert(valor){
    valorConvertido = (5/9) * (valor - 32);
    return valorConvertido;
  }

  let valor = window.prompt('Insira o valor em Fahrenheit');
  let resultado = convert(valor);
  window.alert(`O valor convertido é: ${resultado.toFixed(2)}`);
}

function atividade2(){
  function total(quantidade, valorUnitario, desconto) {
    let somaQuantidade = (quantidade * valorUnitario);
    let descontoFinal = (desconto / 100) * somaQuantidade;
    return descontoFinal
  }

  let produto = window.prompt('Insira o nome do produto');
  let quantidade = window.prompt(`Insira a quantidade do produto ${produto}`);
  let valorUnitario = window.prompt(`Insira o valor unitário do produto ${produto}`);
  let desconto = window.prompt(`Insira a porcentagem de desconto do produto ${produto}`);

  let totalFinal = total(quantidade, valorUnitario, desconto);
  window.alert(`
- Produto: ${produto}
- Preço Unitário: ${valorUnitario}
- Desconto: ${desconto}
- Total final: ${totalFinal}`);
};

function atividade3(){
  function convert(cotacao, real) {
    floatDolar = parseFloat(cotacao)
    floatReal = parseFloat(real)
    let total = floatReal / floatDolar
    return total
  };

  let cotacao = window.prompt('Insira a cotação atual do dólar');
  let real = window.prompt('Insira o valor em reais');
  let total = convert(cotacao, real)

  window.alert(`O valor da compra em dolares será de: ${total.toFixed(2)}`)
};