"""
Mega-Seninha - Paradigmas de Linguagens de Programação - Atividade 1
Solução estruturada imperativamente com otimização nativa de conjuntos matemáticos e I/O seguro.
"""

ARQUIVO_ENTRADA = "APOSTAS.TXT"
ARQUIVO_SAIDA = "GANHADORES.TXT"

def ler_linhas(nome_arquivo):
    """Lê o arquivo de forma segura, removendo quebras de linha e suportando marcação BOM do Windows."""
    linhas = []
    with open(nome_arquivo, "r", encoding="utf-8-sig") as arquivo:
        for linha in arquivo:
            linha_limpa = linha.strip()
            if linha_limpa:
                linhas.append(linha_limpa)
    return linhas

def formatar_cpf(cpf):
    """Aplica a máscara XXX.XXX.XXX-XX utilizando f-strings por eficiência de memória."""
    return f"{cpf[:3]}.{cpf[3:6]}.{cpf[6:9]}-{cpf[9:]}"

def processar_vencedores(linhas):
    """Aplica a interseção de conjuntos para verificação direta, sem custo de cast numérico."""
    # O uso de set() converte a lista de strings em uma tabela hash para busca O(1)
    sorteio_oficial = set(linhas[0].split())
    ganhadores = []

    indice = 1
    while indice + 1 < len(linhas): 
        cpf = linhas[indice]
        # set() elimina duplicatas acidentais e dispensa a necessidade de laços for aninhados
        aposta = set(linhas[indice + 1].split())
        
        # O operador de igualdade (==) em conjuntos garante precisão independentemente da ordem
        if sorteio_oficial == aposta:
            ganhadores.append(formatar_cpf(cpf))
        
        indice += 2
        
    return ganhadores

def escrever_saida(nome_arquivo, ganhadores):
    """Grava os resultados de forma contígua no disco utilizando f-strings."""
    with open(nome_arquivo, "w", encoding="utf-8") as arquivo:
        for cpf in ganhadores:
            arquivo.write(f"{cpf}\n")

def main():
    try:
        linhas = ler_linhas(ARQUIVO_ENTRADA)
    except FileNotFoundError:
        print(f"[Falha Crítica] O arquivo alvo '{ARQUIVO_ENTRADA}' não está presente no diretório atual.")
        return

    if not linhas:
        print(f"[Aviso] Processamento abortado: O arquivo '{ARQUIVO_ENTRADA}' está vazio.")
        return

    ganhadores = processar_vencedores(linhas)
    escrever_saida(ARQUIVO_SAIDA, ganhadores)
    print(f"[Operação Concluída] {len(ganhadores)} ganhador(es) registrado(s) em '{ARQUIVO_SAIDA}'.")

# Impede que o módulo execute rotinas de I/O de forma autônoma caso seja importado por scripts de teste
if __name__ == "__main__":
    main()