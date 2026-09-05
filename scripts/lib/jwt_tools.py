"""Utilidades para inspecionar tokens JWT sem verificar a assinatura.

Um JWT é assinado, não cifrado: qualquer parte pode decodificar o payload
em base64 e lê-lo, sem precisar da chave de assinatura. As provas de
conceito deste projeto usam essa propriedade para inspecionar o conteúdo
que o servidor coloca no token, não para forjar ou validar assinaturas.
"""

from __future__ import annotations

import base64
import json


def decodificar_payload(token: str) -> dict:
    """Decodifica o payload de um JWT sem verificar a assinatura.

    Args:
        token: JWT completo, no formato `header.payload.assinatura`.

    Returns:
        O payload decodificado como dicionário.
    """
    payload_b64 = token.split(".")[1]
    # JWT usa base64url sem padding; o padding precisa ser recalculado
    # manualmente antes de chamar o decodificador padrão da biblioteca.
    payload_b64 += "=" * (-len(payload_b64) % 4)
    return json.loads(base64.urlsafe_b64decode(payload_b64))
