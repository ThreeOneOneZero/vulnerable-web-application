# Relatório Técnico — Trabalho 1 (rascunho)

> Rascunho para virar o PDF da Entrega 1. As seções marcadas **[GRUPO]** dependem de todos
> (papéis, demais achados, conclusão). As seções abaixo já preenchidas são as partes comuns/feitas.
> Ordem segue a Seção 8 do roteiro.

---

## 1. Sumário executivo **[GRUPO — fechar no fim]**

_Escrever depois que as 6 categorias estiverem prontas. Esboço:_
Foram avaliadas as vulnerabilidades da aplicação deliberadamente vulnerável OWASP Juice Shop,
executada localmente em Docker. Identificaram-se N categorias do OWASP Top 10:2021, com destaque
para SQL Injection no login (Crítico, 9.1), armazenamento de senhas em MD5 (Alto, 7.5) e quebra de
controle de acesso via IDOR (Médio, 6.5).
_(Pendente em - achados V4–V6.)_

---

## 2. Configuração do ambiente (Docker)

Alvo instanciado via Docker Compose, com a porta ligada em `127.0.0.1` para manter o laboratório
isolado (acessível apenas na máquina local).

```bash
# na raiz do repositório
docker compose up -d      # sobe o Juice Shop
# acesso: http://127.0.0.1:3000
docker compose down       # derruba o ambiente
```

Conteúdo do `docker-compose.yml`: imagem `bkimminich/juice-shop`, porta `127.0.0.1:3000:3000`,
rede bridge isolada `labnet`.

---

## 3. Papéis da equipe **[GRUPO]**

| Integrante                  | Responsabilidade                                                      |
| --------------------------- | --------------------------------------------------------------------- |
| _(Leonardo Pacheco B Dias)_ | Subida do ambiente Docker; achados obrigatórios A01, A02, A03 (V1–V3) |
| _(preencher)_               | _(ex.: A05 / A06)_                                                    |
| _(preencher)_               | _(ex.: A07 / demais)_                                                 |
| _(preencher)_               | _(ex.: ...)_                                                          |

---

## 4. Arquitetura do laboratório

- **Alvo:** contêiner Juice Shop (Node.js/Express) exposto em `127.0.0.1:3000`.
- **Rede:** bridge Docker isolada `labnet` (sub-rede `172.19.0.0/16`).
- **Máquina de teste:** host local (Windows) + navegador com DevTools.

```
[ Navegador + DevTools ]  --HTTP-->  [ 127.0.0.1:3000 ]
        host Windows                   contêiner juice-shop
                                       rede labnet (172.19.0.0/16)
```

_[GRUPO: opcional trocar o diagrama-texto por uma imagem.]_

---

## 5. Endereços de rede utilizados

| Item             | Valor                                    |
| ---------------- | ---------------------------------------- |
| Alvo (URL)       | http://127.0.0.1:3000                    |
| Porta mapeada    | `127.0.0.1:3000:3000` (host → contêiner) |
| Rede Docker      | `labnet` (bridge, isolada)               |
| Sub-rede         | `172.19.0.0/16`                          |
| Máquina de teste | host local (Windows)                     |

Obtido com:

```bash
docker network inspect vulnerable-web-application_labnet
```

---

## 6. Ferramentas de apoio utilizadas

| Ferramenta                              | Uso neste trabalho                                                     |
| --------------------------------------- | ---------------------------------------------------------------------- |
| Docker / Docker Compose                 | Subir e isolar o alvo vulnerável                                       |
| Navegador + DevTools (Network/Console)  | Inspecionar requisições, cookies e o token JWT; executar o PoC do IDOR |
| `md5sum` (linha de comando)             | Confirmar que o hash vazado é MD5 de senha trivial                     |
| _sqlmap / OWASP ZAP / Nikto (opcional)_ | _[GRUPO, se usarem nos achados V4–V6]_                                 |

---

## 7. Achados

Ver [tabela-de-achados.md](tabela-de-achados.md) — descrição, evidência reprodutível, OWASP/CWE,
vetor CVSS e relação CID/LGPD de cada achado.

- **Feitos:** V1 (A03), V2 (A02), V3 (A01) — as três categorias obrigatórias.
- **[GRUPO]:** V4–V6 (três categorias entre A04–A10) + justificativa das categorias não cobertas.

---

## 8. Conclusão **[GRUPO — fechar no fim]**

_Priorização das correções (por severidade CVSS) e principais lições. Esboço de prioridade:
1º SQLi (Crítico), 2º MD5 (Alto), 3º IDOR (Médio), depois V4–V6._

---

## 9. Referências

- OWASP Foundation. **OWASP Top 10:2021**. Disponível em: owasp.org/Top10.
- OWASP Cheat Sheet Series; OWASP ASVS. Disponível em: owasp.org.
- FIRST. **CVSS — Common Vulnerability Scoring System**. Disponível em: first.org/cvss.
- MITRE. **CWE — Common Weakness Enumeration**. Disponível em: cwe.mitre.org.
- BRASIL. Lei nº 13.709/2018 (LGPD); Lei nº 12.737/2012 (crimes informáticos).
- Documentação: OWASP Juice Shop. Disponível em: owasp.org.
