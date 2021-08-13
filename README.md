# Geradores de Analisadores Léxicos e Sintáticos

---
## Requisitos

Python 3.8 ou superior e tkinter.

---

## Execução

Na raíz do projeto.
```python3 main.py```

---

## Instruções de Uso

* O usuário deve entrar com definições regulares na janela "Regular Definition Input"
* O formato de uma definição regular é `NOME : REGEX`.
* Para adicionar a definição regular, clique em "Add Regex".
* Ao terminar de entrar com as definições regulares clique em "Done". Ao clicar nesse botão, serão geradas todas as árvores sintáticas, em seguida seus respectivos autômatos. Esses autômatos serão unidos e determinizados para possibilitar o parsing.

* Em seguida, você pode entrar com as palavras reservadas na janela "Keywords Input".
* As palavras reservadas devem ser digitadas com espaços separando-as. Exemplo `if else return`
* Ao terminar, aperte em "Enter Keywords". Ao pressionar esse botão, a tabela de símbolos será atualizada com as palavras reservadas.

* Finalmente, você pode usar a janela "Source Code Input" para digitar o texto que deseja analisar.
* Clique em "Enter Source Code" para fazer a análise.

---


## Objetivo

---
O objetivo deste trabalho é o desenvolvimento de um framework para gerar analisadores
léxicos e sintáticos. Faremos a execução em 2 passos, análise léxica e sintática separadamente.

---

### Parte I - Analisador Léxico

Para a construção de um gerador de analisador léxico são necessários os seguintes
algoritmos:

- [x] Conversão de Expressão Regular para Autômato Finito Determinístico (livro do Aho).
- [x] União de Autômatos via &epsilon;-transição.
- [x] Determinização de Autômatos.
- [x] Construção da Tabela de Símbolos (incluir palavras reservadas e outras informações pertinentes).

#### Fluxo de Execução

- A interface **de projeto** deve permitir a inclusão de expressões regulares para todos 
  os padrões de tokens.
- Para cada ER deve ser gerado o AFD correspondente.
- Os AFD devem ser unidos.
- O AFND resultante deve ser determinizado gerando a tabela de análise léxica.
- A interface **de execução** deve permitir a entrada de um texto fonte.
- O texto fonte será analisado e deve gerar um arquivo de saída com todos os tokens
  encontrados.
  
---

### Parte II - Analisador Sintático

Para a construção de um gerador de analisador sintático são necessários os seguintes
algoritmos, a depender do algoritmo de análise implementado:

- [ ] Se preditivo LL(1): Eliminação de recursão à esquerda, Fatoração, Cálculo de First 
  e Follow, Geração da tabela de análise; Autômato de pilha para análise de sentenças.
- [ ] Se LR Canônico: Cálculo de First e Follow, Algoritmos correspondentes ao 
  analisador LR Canônico (conforme livro do Aho).
  

#### Fluxo de Execução

- A interface **de projeto** deve receber e validar a Gramática Livre de Contexto 
  que descreve a linguagem, identificando terminais (tokes) e não terminais.
- Leitura token a token do arquivo resultante da parte I.
- Uso da tabela de análise para validação da sentença de entrada.
- Saída: Mensagem validando ou invalidando o código.
  
---

### Observações

- Para notacionar &epsilon; usar o &.
- As tabelas de análise, tanto léxica quanto sintática, devem poder ser "visualizadas".

---
