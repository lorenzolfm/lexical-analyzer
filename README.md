# lexical-analyzer

---
## Objetivo

---
O objetivo deste trabalho é o desenvolvimento de um framework para gerar analisadores
léxicos e sintáticos. Faremos a execução em 2 passos, análise léxica e sintática separadamente.
Para a construção de um gerador de analisador léxico são necessários os seguintes 
algoritmos (Parte I do trabalho):

1. Conversão de Expressão Regular para Autômato Finito Determinístico (livro do Aho).
2. União de Autômatos via &epsilon;-transição.
3. Determinização de Autômatos.
4. Construção da TS (incluir palavras reservadas e outras informações pertinentes).