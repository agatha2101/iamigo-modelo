from data.data_manager import salvar_dados


def adicionar_tarefa(
    dados: dict,
    usuario: str,
    chave: str,
    titulo: str,
    prioridade: str = "media",
    prazo=None,
    descricao=None
):
    nova_tarefa = {
        "titulo": titulo,
        "descricao": descricao,
        "prioridade": prioridade,
        "prazo": prazo,
        "concluida": False,
        "passos": []
    }

    dados[usuario][chave].append(nova_tarefa)
    salvar_dados(dados)

def alternar_status_tarefa(
    dados: dict,
    usuario: str,
    chave: str,
    indice_tarefa: int
):
    tarefas = dados[usuario][chave]

    if 0 <= indice_tarefa < len(tarefas):
        tarefas[indice_tarefa]["concluida"] = (
            not tarefas[indice_tarefa]["concluida"]
        )

        salvar_dados(dados)


def injetar_passos_ia(
    dados: dict,
    usuario: str,
    chave: str,
    indice_tarefa: int,
    passos: list
):
    tarefas = dados[usuario][chave]

    if 0 <= indice_tarefa < len(tarefas):
        tarefas[indice_tarefa]["passos"] = [
            {
                "texto": passo,
                "concluido": False
            }
            for passo in passos
        ]

        salvar_dados(dados)


def adicionar_passo(
    dados: dict,
    usuario: str,
    chave: str,
    indice_tarefa: int,
    texto: str
):
    tarefa = dados[usuario][chave][indice_tarefa]

    if "passos" not in tarefa:
        tarefa["passos"] = []

    tarefa["passos"].append({
        "texto": texto,
        "concluido": False
    })

    salvar_dados(dados)


def alternar_status_passo(
    dados: dict,
    usuario: str,
    chave: str,
    indice_tarefa: int,
    indice_passo: int
):
    passos = dados[usuario][chave][indice_tarefa].get("passos", [])

    if 0 <= indice_passo < len(passos):
        passos[indice_passo]["concluido"] = (
            not passos[indice_passo]["concluido"]
        )

        salvar_dados(dados)


def excluir_passo(
    dados: dict,
    usuario: str,
    chave: str,
    indice_tarefa: int,
    indice_passo: int
):
    passos = dados[usuario][chave][indice_tarefa].get("passos", [])

    if 0 <= indice_passo < len(passos):
        passos.pop(indice_passo)
        salvar_dados(dados)