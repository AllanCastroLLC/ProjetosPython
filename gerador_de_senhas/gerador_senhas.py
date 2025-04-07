# Gera senhas seguras e aleatórias

import random
import string

def gerar_senha(tamanho=12):
    caracteres = string.ascii_letters + string.digits + string.punctuation
    senha = ''.join(random.choice(caracteres) for _ in range(tamanho))
    return senha

# Geração de uma senha com 16 caracteres
print("Senha gerada:", gerar_senha(16))
