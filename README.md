# 💰 Sistema Bancário em Python

Projeto desenvolvido como parte do bootcamp da **DIO (Digital Innovation One)** com o objetivo de praticar os conceitos básicos de Python, como controle de fluxo, laços de repetição, validação de entrada e manipulação de variáveis.

---

## 📋 Funcionalidades

O sistema bancário implementa as seguintes operações:

- **[1] Depositar**: Permite ao usuário realizar depósitos em sua conta.
- **[2] Sacar**: Permite realizar saques com as seguintes regras:
  - Limite de **R$ 500,00** por saque;
  - Máximo de **5 saques por sessão**;
  - Não permite saque com valor negativo ou maior que o saldo.
- **[3] Extrato**: Exibe o histórico de transações e o saldo atual.
- **[4] Sair**: Encerra o programa.

---

## 🧠 Regras de Negócio

- O valor do depósito deve ser **positivo**;
- O valor do saque deve ser **positivo e não exceder** o saldo ou o limite por saque;
- O número máximo de saques permitidos por sessão é de **5 saques**;
- Todas as movimentações (depósitos e saques) são registradas no extrato.

---

## 🛠 Tecnologias Utilizadas

- **Python 3.12**
- Terminal/Console (sem interface gráfica)

---

## 🚀 Como Executar

1. Certifique-se de ter o Python instalado.
2. Clone este repositório ou copie o código para um arquivo `.py`:

```bash
git clone https://github.com/seu-usuario/sistema-bancario-dio.git
