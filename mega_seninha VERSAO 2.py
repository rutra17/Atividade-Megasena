"""
Mega-Seninha - Paradigmas de Linguagens de Programação - Atividade 1
Solução puramente imperativa: apenas procedimentos e funções.

Lê APOSTAS.TXT e escreve em GANHADORES.TXT o CPF (com pontuação)
de quem acertou os 6 números sorteados.

Formato de APOSTAS.TXT:
    linha 1: os 6 números sorteados, separados por espaço
    depois, para cada apostador, duas linhas:
        - CPF (apenas dígitos)
        - os 6 números apostados, separados por espaço
"""

ARQUIVO_ENTRADA = "APOSTAS.TXT"
ARQUIVO_SAIDA = "GANHADORES.TXT"
QTD_NUMEROS = 6


def ler_linhas(nome_arquivo):
    """Lê o arquivo e devolve a lista de linhas não vazias, sem quebras de linha."""
    linhas = []
    # utf-8-sig lê o arquivo com ou sem BOM (marca que o Bloco de Notas pode gravar)
    with open(nome_arquivo, "r", encoding="utf-8-sig") as arquivo:
        for linha in arquivo:
            linha = linha.strip()
            if linha != "":
                linhas.append(linha)
    return linhas


def converter_numeros(linha):
    """Converte '14 23 53 56 57 60' em uma lista de inteiros."""
    numeros = []
    partes = linha.split()
    for parte in partes:
        numeros.append(int(parte))
    return numeros


def contar_acertos(sorteados, aposta):
    """Conta quantos números sorteados aparecem na aposta (a ordem não importa).

    O laço externo percorre os sorteados e o interno para no primeiro acerto,
    então números repetidos na aposta não são contados mais de uma vez.
    """
    acertos = 0
    for numero_sorteado in sorteados:
        for numero_aposta in aposta:
            if numero_sorteado == numero_aposta:
                acertos = acertos + 1
                break
    return acertos


def formatar_cpf(cpf):
    """Transforma '12345678909' em '123.456.789-09'."""
    return cpf[0:3] + "." + cpf[3:6] + "." + cpf[6:9] + "-" + cpf[9:11]


def encontrar_ganhadores(linhas):
    """Percorre as apostas (de duas em duas linhas) e devolve os CPFs formatados dos ganhadores."""
    sorteados = converter_numeros(linhas[0])
    ganhadores = []

    i = 1
    while i + 1 < len(linhas):  # garante que existe o par CPF + aposta
        cpf = linhas[i]
        aposta = converter_numeros(linhas[i + 1])
        if contar_acertos(sorteados, aposta) == QTD_NUMEROS:
            ganhadores.append(formatar_cpf(cpf))
        i = i + 2

    return ganhadores


def escrever_ganhadores(nome_arquivo, ganhadores):
    """Escreve um CPF por linha no arquivo de saída."""
    with open(nome_arquivo, "w", encoding="utf-8") as arquivo:
        for cpf in ganhadores:
            arquivo.write(cpf + "\n")


def main():
    try:
        linhas = ler_linhas(ARQUIVO_ENTRADA)
    except FileNotFoundError:
        print("Erro: o arquivo " + ARQUIVO_ENTRADA + " não foi encontrado nesta pasta.")
        return

    if len(linhas) == 0:
        print("Erro: o arquivo " + ARQUIVO_ENTRADA + " está vazio.")
        return

    ganhadores = encontrar_ganhadores(linhas)
    escrever_ganhadores(ARQUIVO_SAIDA, ganhadores)
    print("Ganhadores encontrados:", len(ganhadores))


if __name__ == "__main__":
    main()
