# Tabela de achados (modelo — Seção 7.3 do roteiro)

Preencher conforme a exploração. Registrar o **vetor CVSS completo**, não só o número.
Faixas: None 0.0 · Low 0.1–3.9 · Medium 4.0–6.9 · High 7.0–8.9 · Critical 9.0–10.0.
Calculadora oficial: https://www.first.org/cvss/calculator/3.1

| ID | Achado | OWASP | CWE | CVSS (vetor / score) | CID / LGPD |
|----|--------|-------|-----|----------------------|------------|
| V1 | _ex.: SQLi no login_ | A03 | CWE-89 | `AV:N/AC:L/...` (ex.: 9.1 Crítico) | Integr./Confid.; dados pessoais |
| V2 | _ex.: IDOR na cesta_ | A01 | CWE-639 | _(ex.: 6.5 Médio)_ | Confidencialidade; dados de terceiros |
| V3 | _..._ | A02 | CWE-327 | _..._ | _..._ |
| V4 | _..._ | | | | |
| V5 | _..._ | | | | |
| V6 | _..._ | | | | |

## Seções obrigatórias do relatório final (Seção 8 do roteiro)

1. Sumário executivo
2. Passo a passo da configuração do ambiente (Docker)
3. Papel de cada membro da equipe
4. Arquitetura da solução de laboratório (alvo, rede, máquina de teste — com diagrama)
5. Endereços de rede utilizados (IPs, portas, rede Docker)
6. Ferramentas de apoio e como foram empregadas
7. Explicação de cada achado: descrição, evidências, OWASP/CWE, CVSS, CID/LGPD
8. Conclusão (priorização das correções e lições)
9. Referências (norma culta)
