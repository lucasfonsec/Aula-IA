import math


def eh_primo(numero: int) -> bool:
    """
    Verifica se um número é primo.

    Um número primo é maior que 1 e divisível apenas por 1 e por ele mesmo.
    """
    if numero <= 1:
        return False

    if numero == 2:
        return True

    if numero % 2 == 0:
        return False

    limite = int(math.sqrt(numero)) + 1

    for i in range(3, limite, 2):
        if numero % i == 0:
            return False

    return True


def main():
    try:
        num = int(input("Digite um número inteiro: "))

        if eh_primo(num):
            print(f"{num} é um número primo.")
        else:
            print(f"{num} não é um número primo.")

    except ValueError:
        print("Por favor, digite um número inteiro válido.")


if __name__ == "__main__":
    main()