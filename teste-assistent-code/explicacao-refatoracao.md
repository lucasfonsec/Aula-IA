# Refatoração do código em Python

Este documento apresenta a refatoração de um código que calcula estatísticas básicas de uma lista de números, aplicando boas práticas de **clean code**, legibilidade e organização.

---

## Código original (resumo do problema)

O código original realizava:
- Soma dos elementos
- Cálculo da média
- Identificação do maior valor
- Identificação do menor valor

Porém, apresentava alguns problemas:
- Nomes de variáveis pouco claros
- Uso de loops manuais desnecessários
- Baixa legibilidade
- Falta de organização em funções

---

## Código refatorado

```python
from typing import Sequence


def calcular_estatisticas(numeros: Sequence[float]) -> tuple[float, float, float, float]:
    """
    Calcula estatísticas básicas de uma lista de números:
    soma, média, maior valor e menor valor.
    """

    if not numeros:
        raise ValueError("A lista não pode estar vazia.")

    total = sum(numeros)
    media = total / len(numeros)
    maior_valor = max(numeros)
    menor_valor = min(numeros)

    return total, media, maior_valor, menor_valor


def main() -> None:
    numeros = [23, 7, 45, 2, 67, 12, 89, 34, 56, 11]

    total, media, maior, menor = calcular_estatisticas(numeros)

    print(f"Total: {total}")
    print(f"Média: {media}")
    print(f"Maior: {maior}")
    print(f"Menor: {menor}")


if __name__ == "__main__":
    main()
Melhorias aplicadas
1. Nomes mais descritivos

Variáveis e funções foram renomeadas para facilitar o entendimento:

Original	Refatorado
c(l)	calcular_estatisticas
l	numeros
t	total
mx	maior_valor
mn	menor_valor
2. Uso de funções nativas do Python

Foram substituídos loops manuais por funções built-in:

sum() → soma total
max() → maior valor
min() → menor valor

Isso reduz código e melhora performance e legibilidade.

3. Organização do código

O código foi dividido em:

calcular_estatisticas() → lógica principal
main() → execução do programa
4. Boas práticas adicionais
Uso de type hints
Adição de docstring
Proteção contra lista vazia
Estrutura padrão com if __name__ == "__main__"
Resultado

O código final ficou:

Mais legível
Mais curto
Mais seguro
Mais fácil de manter
Mais alinhado com padrões profissionais de Python