📄 explicação-debug.md
🔎 Erros encontrados no código
1. Erro de sintaxe no input do item 1
item1 = float(input(Preço do item 1? ))

Problema: falta de aspas na string.
Correção: toda string em Python deve estar entre aspas.

2. desconto_cupom não convertido para número
desconto_cupom = (input("Você tem um cupom de desconto? (Digite o percentual ou 0): "))

Problema: input() retorna string, mas depois é usado em cálculo matemático.
Erro resultante: TypeError.

Correção: converter para float ou int.

3. Cálculo do desconto com tipo errado
desconto = subtotal * (desconto_cupom / 100)

Problema: desconto_cupom é string, não número.

4. Falta de f-string no print do item 2
print(" Item 2:        R$ {total_item2:.2f}")

Problema: não está usando f"", então não formata o valor.

5. Erro de indentação no if
if desconto_cupom > 0: 
print(f" Desconto ({desconto_cupom:.0f}%): -R$ {desconto:.2f}")

Problema: Python exige indentação dentro de blocos.

6. Comparação inválida no if
if desconto_cupom > 0:

Problema: comparação entre string e número (caso não convertido).

7. Uso redundante de round() com formatação
print(f" TOTAL:         R$ {round(total, 2):.2f}")

Problema: desnecessário usar round() junto com :.2f (já faz formatação).

✅ Resumo das correções
Corrigir strings do input
Converter entradas numéricas corretamente
Ajustar f-strings
Corrigir indentação
Garantir tipos numéricos nas operações