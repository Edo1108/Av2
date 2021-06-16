import random


class Entradas():
    def __init__(self, valor, pesos):
        self.valor = int(valor)
        self.pesos = dict(pesos)


def somatorio(entradas, peso):
    print(f'Peso do Somatório = {peso}')
    const = 0
    valorDeSoma = 0
    for e in entradas:
        valorDeSoma += e['valor'] * e['pesos'][peso]
    return round(valorDeSoma + const, 2)


def custo(valorObtido, valorIdeal):
    return round(((valorObtido - valorIdeal) ** 2), 2)


def geradorDePesos(quantidadePesos):
    pesos = {}
    for numeroPeso in range(quantidadePesos):
        pesos[f'w{numeroPeso}'] = round(random.random(), 2)
    return pesos


def geraListaEntradas(quantidadeEntrada, quantidadePesosPorEntradas):
    entradas = []
    for numeroEntradas in range(quantidadeEntrada):
        vars()[f'e{str(numeroEntradas)}'] = {
            "nome": f'Entrada {str(numeroEntradas)}',
            "valor": round(random.random(), 2),
            "pesos": geradorDePesos(quantidadePesosPorEntradas)
        }
        entradas.append(vars()[f'e{str(numeroEntradas)}'])
    return entradas


def chamadaPesoRandomico(entrada):
    return f'w{str(random.randint(0, len(entrada["pesos"]) - 1))}'


def chamadaPesoRandomico(valor):
    return f'w{str(random.randint(0, int(valor) - 1))}'


def printListaEntradas(entradas):
    for item in entradas:
        print(f'{item["nome"]}: valor = {item["valor"]}, pesos = {item["pesos"]} ')
    print('\n')


def printListaEntradasBruta(entradas):
    for item in entradas:
        print(item)
    print("\n")


def calibrar(entradas, peso):
    for entrada in entradas:
        if(round(random.random(), 2) <= 0.50):
            entrada['pesos'][peso] = round(random.random(), 2) * -1
    return entradas



def run():
    # variaveis de entradas e pesos
    quantidadeEntrada = 10
    quantidadePesos = 10

    print('\n-------------- Começo --------------\n')
    print(f'Quantidade de entradas: {quantidadeEntrada}\nQuantidade de pesos por entrada: {quantidadePesos}\n')

    entradas = geraListaEntradas(quantidadeEntrada, quantidadePesos)
    custoFinal = 0
    printListaEntradas(entradas)

    listaSomatorio = []
    listaIdeais = []
    for x in range(quantidadePesos):
        somat = somatorio(entradas, f"w{x}")
        ideal = round(random.random(), 2)
        listaSomatorio.append(somat)
        listaIdeais.append(ideal)
        custoFinal += custo(somat, ideal)



    somatorios = somatorio(entradas, chamadaPesoRandomico(quantidadePesos))

    print(f"Lista de somatorios {listaSomatorio}")
    print(f"Lista de ideais {listaIdeais}")
    print(f"Custo final {custoFinal}")


    novasEntradas = calibrar(entradas, chamadaPesoRandomico(quantidadePesos))
    for x in range(6):
        print("##################    Novas entradas     ######################")
        printListaEntradas(novasEntradas)
        somatorios = somatorio(novasEntradas, chamadaPesoRandomico(quantidadePesos))
        custos = custo(somatorios, 1)
        print(f'Valor da Função de Ativação: {somatorios}')
        print(f'Valor da Função de Custo: {custos}')
        novasEntradas = calibrar(entradas, chamadaPesoRandomico(quantidadePesos))
        print("###############      Fim novas entradas      ########################")



    print(f"entradas {(entradas[1])}")
    print(f"entradas {(entradas[2])}")

if __name__ == '__main__':
    run()