def calcular_partida_rankeada(vitorias: int, derrotas: int) -> int:
    return vitorias - derrotas

vitorias = 100
derrotas = 20
saldo_de_vitorias = calcular_partida_rankeada(vitorias, derrotas)
nivel = ''

if saldo_de_vitorias >= 101:
    nivel = 'Imortal'
elif saldo_de_vitorias >= 91:
    nivel = 'Lendário'
elif saldo_de_vitorias >= 81:
    nivel = 'Diamante'
elif saldo_de_vitorias >= 51:
    nivel = 'Ouro'
elif saldo_de_vitorias >= 21:
    nivel = 'Prata'
elif saldo_de_vitorias >= 11:
    nivel = 'Bronze'
else:
    nivel = 'Ferro'

print(f'O Herói de saldo de {saldo_de_vitorias} está no nível {nivel}')