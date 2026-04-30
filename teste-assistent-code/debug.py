# ENTRADA DE DADOS
cliente = input("Qual é seu nome? ")

qtd1 = int(input("Quantidade do item 1: "))
item1 = float(input("Preço do item 1? "))

qtd2 = int(input("Quantidade do item 2: "))
item2 = float(input("Preço do item 2? "))

qtd3 = int(input("Quantidade do item 3: "))
item3 = float(input("Preço do item 3? "))

# CÁLCULOS DOS ITENS
total_item1 = qtd1 * item1
total_item2 = qtd2 * item2
total_item3 = qtd3 * item3

# soma de todos os itens antes de taxas/descontos (base para cálculos seguintes)
subtotal = total_item1 + total_item2 + total_item3

# imposto fixo de 10% aplicado sobre o subtotal
imposto = subtotal * 0.10

# DESCONTO
# usuário informa percentual (ex: 10 para 10%), não valor absoluto
desconto_cupom = float(input("Você tem um cupom de desconto? (Digite o percentual ou 0): "))

# conversão do percentual em valor monetário proporcional ao subtotal
desconto = subtotal * (desconto_cupom / 100)

# TOTAL FINAL
# ordem importa: primeiro soma imposto, depois aplica desconto
total = subtotal + imposto - desconto

# EXIBIÇÃO
linha = "=" * 31
separador = "-" * 31

print(linha)
print(f" Cliente: {cliente}")
print(linha)
print(f" Item 1:        R$ {total_item1:.2f}")
print(f" Item 2:        R$ {total_item2:.2f}")
print(f" Item 3:        R$ {total_item3:.2f}")
print(separador)
print(f" Subtotal:      R$ {subtotal:.2f}")
print(f" Imposto (10%): R$ {imposto:.2f}")

# exibe desconto apenas se realmente houver, evitando poluir a saída
if desconto_cupom > 0:
    print(f" Desconto ({desconto_cupom:.0f}%): -R$ {desconto:.2f}")

print(linha)
print(f" TOTAL:         R$ {total:.2f}")
print(linha)