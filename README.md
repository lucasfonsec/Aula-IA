# 📁 Projeto: Aula-IA & Teste-Assistent

Este repositório reúne dois conjuntos principais de projetos:

1. **Aula-IA** → Aplicação web com visão computacional usando Teachable Machine
2. **Teste-assistente** → Scripts em Python para prática de lógica, algoritmos e boas práticas

---

# 🚀 1. Aula-IA (Visão Computacional)

## 📌 Descrição

Aplicação web que utiliza **TensorFlow.js** e **Teachable Machine** para realizar classificação de imagens em tempo real usando a webcam.

O modelo foi treinado para reconhecer cores:

* 🔵 Azul
* 🟢 Verde
* 🔴 Vermelho

---

## 🧠 Tecnologias utilizadas

* HTML5
* CSS3 (custom + Bootstrap 5)
* JavaScript
* TensorFlow.js
* Teachable Machine

---

## 📂 Estrutura

```
Aula-IA/
│
├── index.html
├── azul/
├── verde/
└── vermelho/
```

---

## ⚙️ Como funciona

1. O usuário clica em **"Ativar câmera"**
2. O modelo é carregado via Teachable Machine
3. A webcam é iniciada
4. O sistema analisa os frames em tempo real
5. As probabilidades de cada classe são exibidas na tela

---

## ▶️ Como executar

1. Baixe o projeto
2. Abra o arquivo `index.html` no navegador
3. Permita acesso à câmera
4. Teste com objetos coloridos

---

## ⚠️ Observações

* Necessário internet (modelo hospedado online)
* Permissão de câmera obrigatória
* Funciona melhor em navegadores modernos (Chrome recomendado)

---

# 🧪 2. Teste-assistente (Python)

## 📌 Objetivo

Coleção de scripts para अभ्यास de:

* Lógica de programação
* Estrutura de código
* Debug
* Refatoração
* Algoritmos

---

## 📂 Estrutura

```
Teste-assistente/
│
├── Debug.py
├── numprimos.py
├── refatoracao.py
├── explicacao-debug.md
├── explicacao_numprimo.md
└── explicacao.refatoracao.md
```

---

# 🧾 Scripts

## 🧮 Debug.py

Sistema simples de cálculo de compras:

### Funcionalidades:

* Entrada de dados do cliente
* Cálculo de subtotal
* Aplicação de imposto (10%)
* Aplicação de desconto via cupom
* Exibição formatada

---

## 🔢 numprimos.py

Verifica se um número é primo com algoritmo otimizado.

### Otimizações:

* Eliminação de pares
* Uso de √n
* Loop apenas com números ímpares

---

## 📊 refatoracao.py

Código refatorado para cálculo de estatísticas:

### Calcula:

* Soma
* Média
* Maior valor
* Menor valor

### Boas práticas:

* Funções organizadas
* Type hints
* Uso de funções nativas do Python

---

# 📚 Documentação

## 🔍 explicacao-debug.md

Lista erros comuns encontrados no código original e suas correções:

* Strings sem aspas
* Tipos incorretos
* Problemas de indentação
* Uso incorreto de f-string

---

## 🔢 explicacao_numprimo.md

Explica a otimização do algoritmo de número primo:

* Complexidade reduzida de O(n) → O(√n)

---

## 🧠 explicacao.refatoracao.md

Explica melhorias aplicadas:

* Legibilidade
* Organização
* Uso de boas práticas
* Clean Code

---

# 🎯 Aprendizados do projeto

✔ Integração de IA no frontend
✔ Uso de modelos treinados
✔ Manipulação de webcam no navegador
✔ Otimização de algoritmos
✔ Refatoração de código
✔ Identificação e correção de bugs

---

# 👨‍💻 Autor

**Lucas Fonseca**

---

# 📌 Considerações finais

Este projeto combina conceitos de:

* Inteligência Artificial
* Desenvolvimento Web
* Programação em Python

Servindo como base prática para aprendizado e evolução em tecnologia.
