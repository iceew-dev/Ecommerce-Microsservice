# Microsserviços com Docker Compose e Locust

## Descrição

Este projeto implementa uma aplicação de comércio eletrônico baseada em arquitetura de microsserviços utilizando Docker Compose.

A arquitetura foi configurada seguindo o diagrama proposto na atividade, utilizando diferentes tecnologias para cada serviço:

- Product page → Python
- Reviews → Java
- Details → Ruby
- Ratings → Node.js

Além disso, foi adicionada a ferramenta Locust para realização de testes de carga na aplicação.

---

# Estrutura do Projeto

```text
.
├── docker-compose.yml
└── locust
    └── locustfile.py
