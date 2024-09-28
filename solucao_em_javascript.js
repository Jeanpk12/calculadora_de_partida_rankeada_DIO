function calcularPartidaRankeada(vitorias, derrotas) {
  return vitorias - derrotas;
}

let vitorias = 90;
let derrotas = 50;
let saldo = calcularPartidaRankeada(vitorias, derrotas);

if (saldo >= 101) {
  nivel = "Imortal";
} else if (saldo >= 91) {
  nivel = "Lendário";
} else if (saldo >= 81) {
  nivel = "Diamante";
} else if (saldo >= 51) {
  nivel = "Ouro";
} else if (saldo >= 21) {
  nivel = "Prata";
} else if (saldo >= 11) {
  nivel = "Bronze";
} else {
  nivel = "Ferro";
}

console.log(`O Herói de saldo de ${saldo} está no nível ${nivel}`);
