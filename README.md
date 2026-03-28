# Lab-TDD — Livraria com Filtro de Livros

Projeto desenvolvido no âmbito da disciplina de **Engenharia de Software**, com o objetivo de aplicar o método **Test-Driven Development (TDD)** na implementação de uma funcionalidade de filtragem de livros.

---

## Objetivo

Implementar, seguindo o ciclo TDD (Red -> Green -> Refactor), uma função que devolva uma lista de livros filtrada por critérios fornecidos pelo utilizador.

---

## Estrutura do Projeto

```
Lab-TDD/
│
├── livro.py          # Função principal de filtragem
├── test_livro.py     # Testes TDD
├── bd.py             # Base de dados mockada
├── main.py           # Servidor Flask
└── templates/
    └── index.html    # Interface web
```

---

## Funcionalidades

- Filtrar livros por **autor**
- Filtrar livros por **gênero**
- Filtrar livros por **autor e gênero** simultaneamente
- Retornar **informação completa** dos livros filtrados (título, autor, género, preço e data de publicação)
- Interface web simples via **Flask**

---

## Ciclos TDD Realizados

| Ciclo | Teste | Descrição |
|-------|-------|-----------|
| 1 | `test_filtrar_livros()` | Lista vazia sem critérios retorna lista vazia |
| 2 | `test_filtrar_livros_por_genero()` | Filtra corretamente por gênero |
| 3 | `test_filtrar_livros_por_autor()` | Filtra corretamente por autor |
| 4 | `test_filtrar_livros_por_genero_inexistente()` | Gênero inexistente retorna lista vazia |
| 5 | `test_filtrar_livros_retorna_informacao_completa()` | Retorna todos os atributos do livro filtrado |

---

## Como Executar

### 1. Instalar dependências

```
py -m pip install flask
```

### 2. Executar os testes

```
py -m pytest test_livro.py -v -s
```

### 3. Executar a aplicação web

```
py main.py
```

Acede a http://127.0.0.1:5000 no browser.

---

## Tecnologias Utilizadas

- **Python** — Linguagem principal
- **Flask** — Servidor web
- **pytest** — Execução dos testes

---

## Sobre o TDD

O desenvolvimento seguiu rigorosamente o ciclo TDD:

- **Red** — Escrever um teste que falha
- **Green** — Implementar o mínimo de código para o teste passar
- **Refactor** — Melhorar o código sem quebrar os testes

