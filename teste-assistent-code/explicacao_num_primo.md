# Explicação: Número Primo (Versão Melhorada)

Um **número primo** é um número natural maior que 1 que possui exatamente dois divisores:

* 1
* Ele mesmo

## Exemplos

**Primos:**
2, 3, 5, 7, 11

**Não primos (compostos):**
4, 6, 8, 9, 10

---

## 🔍 Como o algoritmo foi melhorado

A versão anterior verificava divisões de `2` até `n-1`, o que é ineficiente.

A versão atual usa três otimizações importantes:

### 1. Eliminação de casos simples

* Números ≤ 1 → não são primos
* Número 2 → único primo par
* Números pares maiores que 2 → não são primos

### 2. Uso da raiz quadrada

Em vez de testar todos os números até `n`, verificamos apenas até:

√n

Isso funciona porque, se um número tiver um divisor maior que a raiz, necessariamente já teria um menor antes.

### 3. Verificação apenas de números ímpares

Após eliminar os pares, testamos apenas:

3, 5, 7, 9, ...

Isso reduz pela metade o número de verificações.

---

## ⚙️ Código explicado

```python id="z9n2ls"
limite = int(math.sqrt(numero)) + 1

for i in range(3, limite, 2):
```

* `math.sqrt(numero)` → calcula a raiz quadrada
* `range(3, limite, 2)` → percorre apenas números ímpares

---

## 🧠 Complexidade

* Antes: O(n)
* Agora: O(√n)

Isso torna o algoritmo muito mais eficiente para números grandes.

---

## ✅ Conclusão

A versão otimizada:

* É mais rápida
* Mais segura (trata erros de entrada)
* Mais legível (usa funções e documentação)

Esse tipo de melhoria é essencial para escrever código profissional e escalável.
