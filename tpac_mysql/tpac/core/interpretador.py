import re
import unicodedata


PALAVRAS_ESTUDO = [
    "prova",
    "atividade",
    "trabalho",
    "pesquisa",
    "faculdade",
    "escola",
    "estudar",
    "estudo",
    "materia",
    "exercicio",
    "resumo",
    "ingles",
    "matematica",
    "portugues",
    "quimica",
    "fisica",
    "biologia"
]


INICIOS_DE_TAREFA = [
    r"^\s*preciso\s+",
    r"^\s*tenho que\s+",
    r"^\s*devo\s+",
    r"^\s*quero\s+",
    r"^\s*não posso esquecer de\s+",
    r"^\s*nao posso esquecer de\s+",
    r"^\s*me lembre de\s+",
    r"^\s*anote que\s+",
    r"^\s*anota que\s+",
    r"^\s*anote\s+",
    r"^\s*anota\s+"
]


def normalizar_texto(texto: str) -> str:
    texto = texto.lower().strip()

    texto_sem_acentos = unicodedata.normalize(
        "NFD",
        texto
    )

    return "".join(
        caractere
        for caractere in texto_sem_acentos
        if unicodedata.category(caractere) != "Mn"
    )


def identificar_intencao(texto: str) -> str:
    for padrao in INICIOS_DE_TAREFA:
        if re.search(padrao, texto, flags=re.IGNORECASE):
            return "registrar_tarefa"

    return "pergunta"


def identificar_categoria(texto: str) -> str:
    texto_normalizado = normalizar_texto(texto)

    for palavra in PALAVRAS_ESTUDO:
        if palavra in texto_normalizado:
            return "tarefas_educacionais"

    return "tarefas_diarias"


def extrair_titulo(texto: str) -> str:
    titulo = texto.strip()

    for padrao in INICIOS_DE_TAREFA:
        novo_titulo = re.sub(
            padrao,
            "",
            titulo,
            count=1,
            flags=re.IGNORECASE
        )

        if novo_titulo != titulo:
            titulo = novo_titulo
            break

    titulo = titulo.strip(" .;,")

    if titulo:
        titulo = titulo[0].upper() + titulo[1:]

    return titulo


def interpretar_mensagem(texto: str) -> dict:
    intencao = identificar_intencao(texto)

    if intencao == "pergunta":
        return {
            "intencao": "pergunta",
            "titulo": None,
            "categoria": None
        }

    return {
        "intencao": "registrar_tarefa",
        "titulo": extrair_titulo(texto),
        "categoria": identificar_categoria(texto)
    }