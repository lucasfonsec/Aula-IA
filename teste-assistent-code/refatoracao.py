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