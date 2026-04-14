import nltk
from nltk.corpus import wordnet
import random

# Isso aqui baixa os recursos necessários
nltk.download('wordnet')
nltk.download('omw-1.4')


def get_sinonimos(palavra):
    sinonimos = set()
    # muda a linguagem para português
    for syn in wordnet.synsets(palavra, lang='por'):
        for l in syn.lemmas(lang='por'):
            # Substitui o underline por espaço em palavras compostas
            nome_limpo = l.name().replace('_', ' ')
            # Evita que a própria palavra seja sugerida como sinônimo
            if nome_limpo.lower() != palavra.lower():
                sinonimos.add(nome_limpo)
    return list(sinonimos)


def substituir_com_nltk(frase):
    palavras = frase.split()

    # Filtra palavras com mais de 3 letras que possuam sinônimos disponíveis
    candidatos = [p for p in palavras if len(p) > 3 and get_sinonimos(p.strip(",.!?"))]

    if not candidatos:
        return "Nenhuma substituição possível encontrada."

    # Escolhe uma palavra aleatória entre os candidatos
    palavra_alvo = random.choice(candidatos)
    # Remove pontuação da palavra alvo para a busca
    palavra_limpa = palavra_alvo.strip(",.!?")

    sinonimos = get_sinonimos(palavra_limpa)

    if sinonimos:
        substituto = random.choice(sinonimos)
        # Substitui apenas a primeira vez que a palavra escolhida aparecer
        return frase.replace(palavra_alvo, substituto, 1)

    return frase

frase_usuario = input("Digite uma frase: ")
resultado = substituir_com_nltk(frase_usuario)
print("A frase original é '{}'".format(frase_usuario))
print("A frase modificada é '{}'".format(resultado))
