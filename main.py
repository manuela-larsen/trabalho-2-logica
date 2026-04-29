def obter_valor(mensagem):
    valor_texto = input(mensagem)
    return float(valor_texto.replace(",", "."))

def calcular_total(valor_conta, porcentagem):
    gorjeta = valor_conta * (porcentagem / 100)
    return valor_conta + gorjeta

def mostrar_resumo(total):
    print(f"\n--- Resultado Final ---")
    print(f"O valor total com gorjeta é: R$ {total:.2f}")
    print("Obrigado por usar nosso sistema!")

conta = obter_valor("Qual o valor da conta? R$ ")
taxa = obter_valor("Qual a porcentagem da gorjeta? (ex: 10, 15): ")

total_com_taxa = calcular_total(conta, taxa)
mostrar_resumo(total_com_taxa)
