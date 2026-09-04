# Trabalho 1 — Avaliação de Vulnerabilidades em Aplicação Web

**Disciplina:** Segurança de Sistemas Computacionais — 2026/2 (UNIVALI)
**Case Prático 1 — Módulo M1** · OWASP Top 10:2021 · Docker · CVSS · CWE

Alvo escolhido: **Cenário A — OWASP Juice Shop** (loja online deliberadamente vulnerável, mantida pela OWASP).

> ⚠️ **Ética e legalidade.** O alvo é propositalmente vulnerável e roda em rede isolada,
> acessível apenas em `127.0.0.1`. Testar sistemas de terceiros sem autorização é crime (conforme professor falou em aula)
> (Lei 12.737/2012). Todo teste deste trabalho é feito no próprio ambiente local.

---

## Equipe

| Nome                        | Papel na execução           |
| --------------------------- | --------------------------- |
| _(Leonardo Pacheco B Dias)_ | _(A01/A02/A03)_             |
| _(preencher)_               | _(ex.: exploração A02/A05)_ |
| _(preencher)_               | _(ex.: CVSS e relatório)_   |
| _(preencher)_               | _(ex.: ...)_                |

---

## Como subir o ambiente

Pré-requisitos: **Docker Desktop** aberto e com o motor rodando ("Engine running").

```bash
docker compose up
```

Acesse: **http://127.0.0.1:3000**

Para derrubar:

```bash
docker compose down
```

### Endereços de rede a documentar no relatório

- **Alvo:** http://127.0.0.1:3000
- **Rede Docker:** bridge isolada `labnet` — obter sub-rede e detalhes com:
  ```bash
  docker network inspect vulnerable-web-application_labnet
  ```
- **Máquina de teste:** host local (Windows).

**ANOTANDO DADOS PRA DEPOIS PREENCHER README**
rede -> labnet
sub-rede 172.19.0.0/16

---

## Cobertura de vulnerabilidades (mínimo 6 categorias)

Obrigatórias: **A01**, **A02**, **A03**. As demais para fechar 6.

| ID  | OWASP                            | Categoria       | Status | Onde procurar no Juice Shop                                         |
| --- | -------------------------------- | --------------- | ------ | ------------------------------------------------------------------- |
| A01 | Broken Access Control            | **obrigatória** | ⬜     | cesta/pedidos por ID (`/rest/basket/{id}`), painel admin, feedbacks |
| A02 | Cryptographic Failures           | **obrigatória** | ⬜     | hashes de senha fracos, cookies sem flags, tokens                   |
| A03 | Injection (SQLi/XSS)             | **obrigatória** | ⬜     | busca de produtos, login (`/rest/user/login`)                       |
| A05 | Security Misconfiguration        | opcional        | ⬜     | erros verbosos, arquivos/endpoints expostos                         |
| A06 | Vulnerable & Outdated Components | opcional        | ⬜     | libs JS do front, `package.json`, versões                           |
| A07 | Identification & Auth Failures   | opcional        | ⬜     | senhas fracas, sem bloqueio de brute force, JWT                     |

> Para categorias não encontradas no alvo, o relatório deve **explicar por que não se aplicam ou não foram observadas**.

---

## Estrutura do repositório

```
.
├── README.md            # este arquivo
├── docker-compose.yml   # ambiente do alvo (Juice Shop)
├── scripts/             # comandos sqlmap/ZAP, exploracao.py, requisições
├── evidencias/          # prints e capturas por achado (V1, V2, ...)
└── relatorio/           # relatório técnico (PDF) e fontes
```

---

## Entregas

- **Entrega 1 (AVA) até 05/09/2026:** relatório PDF + scripts + este repositório Git.
- **Entrega 2 (seminário, em aula) 14/09/2026:** slides + demonstração ao vivo.
