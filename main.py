from pyscript import web, when, window


# ============================================================
# CONFIGURAÇÃO
# ============================================================

CONFIG = {
    "titulo": "BACKROOMS - O ÚLTIMO CORREDOR",
    "subtitulo": "Uma aventura de suspense nas Backrooms",
    "autor": "Julia",
    "icone": "🟨",

    "capa": None,

    "trilha_inicial": None,
    "volume_inicial": 0.5,

    "vida_inicial": 3,
    "pontos_iniciais": 0,

    "cena_inicial": "inicio",
}


# ============================================================
# ESTADO DO JOGADOR
# ============================================================

state = {
    "vida": CONFIG["vida_inicial"],
    "inventario": [],
    "pontos": CONFIG["pontos_iniciais"],
    "cena": CONFIG["cena_inicial"],
}


# ============================================================
# CENAS
# ============================================================

SCENES = {

    "inicio": {
        "title": "🟨 BACKROOMS - O ÚLTIMO CORREDOR",
        "text": (
            "Você estava voltando para casa depois da escola.\n\n"
            "O corredor do prédio parecia completamente normal.\n\n"
            "Até que você percebeu uma coisa.\n\n"
            "As paredes estavam... diferentes.\n\n"
            "Quando você se apoiou em uma delas, a parede desapareceu.\n\n"
            "Você caiu.\n\n"
            "Quando abriu os olhos, estava em uma enorme sala "
            "com paredes amarelas, carpete úmido e lâmpadas "
            "fluorescentes fazendo um zumbido irritante.\n\n"
            "Seu celular estava com 0% de bateria.\n\n"
            "Mesmo assim, uma mensagem apareceu:\n\n"
            "\"VOCÊ ENTROU NAS BACKROOMS.\"\n\n"
            "Você escuta um barulho distante.\n\n"
            "Toc... Toc... Toc..."
        ),
        "options": [
            ("Seguir pelo corredor", "corredor"),
            ("Entrar em uma sala aberta", "sala_abandonada"),
        ],
    },


    "sala_abandonada": {
        "title": "🏚️ Sala Abandonada",
        "text": (
            "Você entra em uma pequena sala.\n\n"
            "As lâmpadas estão quase todas apagadas.\n\n"
            "No chão existem três objetos:\n\n"
            "🔦 Uma lanterna\n"
            "🗝️ Uma chave enferrujada\n"
            "🥤 Uma garrafa de água\n\n"
            "Você sente que esses objetos podem ser importantes."
        ),
        "options": [
            ("Pegar a lanterna", "pegar_lanterna"),
            ("Pegar a chave", "pegar_chave"),
            ("Pegar a água", "pegar_agua"),
        ],
    },


    "corredor": {
        "title": "🚪 O Corredor",
        "text": (
            "Você continua andando.\n\n"
            "O corredor parece não ter fim.\n\n"
            "Depois de alguns minutos, encontra duas opções.\n\n"
            "À esquerda existe uma porta vermelha.\n\n"
            "À direita existe uma escada que desce para um "
            "nível completamente escuro.\n\n"
            "Você sente que alguma coisa está observando você."
        ),
        "options": [
            ("Entrar pela porta vermelha", "porta_vermelha"),
            ("Descer a escada", "escada"),
        ],
    },


    "porta_vermelha": {
        "title": "🚨 A Porta Vermelha",
        "text": (
            "Você chega perto da porta.\n\n"
            "Ela possui uma pequena fechadura.\n\n"
            "Há uma inscrição:\n\n"
            "\"APENAS QUEM POSSUI A CHAVE PODE PASSAR.\"\n\n"
            "Você decide tentar abrir."
        ),
        "options": [
            ("Tentar abrir a porta", "abrir_porta"),
            ("Voltar", "corredor"),
        ],
    },


    "porta_falha": {
        "title": "💥 A Porta Reage",
        "text": (
            "Você não possui a chave.\n\n"
            "BANG!\n\n"
            "Alguma coisa bate do outro lado da porta.\n\n"
            "Você se assusta e sofre um ferimento.\n\n"
            "❤️ Você perdeu uma vida."
        ),
        "options": [
            ("Voltar para o corredor", "corredor"),
        ],
    },


    "estacionamento": {
        "title": "🚗 Estacionamento Infinito",
        "text": (
            "Você abre a porta vermelha e entra em um "
            "estacionamento gigantesco.\n\n"
            "Existem centenas de vagas.\n\n"
            "Nenhum carro possui motorista.\n\n"
            "Então você escuta:\n\n"
            "Toc... Toc... Toc...\n\n"
            "No final do estacionamento existe uma silhueta.\n\n"
            "Ela começa a andar na sua direção."
        ),
        "options": [
            ("Se esconder dentro de um carro", "esconder_carro"),
            ("Correr até o outro lado", "correr_estacionamento"),
        ],
    },


    "escada": {
        "title": "⬇️ A Escada",
        "text": (
            "Você começa a descer.\n\n"
            "Um degrau.\n"
            "Dois.\n"
            "Três.\n\n"
            "O som das lâmpadas desaparece.\n\n"
            "Agora existe apenas escuridão.\n\n"
            "Você não consegue enxergar absolutamente nada."
        ),
        "options": [
            ("Usar a lanterna", "usar_lanterna"),
            ("Continuar no escuro", "continuar_escuro"),
            ("Voltar", "corredor"),
        ],
    },


    "sala_seguranca": {
        "title": "📹 Sala de Segurança",
        "text": (
            "Você entra em uma sala cheia de monitores.\n\n"
            "Cada monitor mostra um lugar diferente.\n\n"
            "Corredores.\n"
            "Escadas.\n"
            "Estacionamentos.\n"
            "Salas amarelas.\n\n"
            "No último monitor aparece uma porta branca.\n\n"
            "Embaixo dela está escrito:\n\n"
            "\"SAÍDA\""
        ),
        "options": [
            ("Procurar a porta branca", "decidir_final"),
            ("Investigar os monitores", "investigar_monitores"),
        ],
    },


    "fim_bom": {
        "title": "🟢 FINAL BOM - VOCÊ ESCAPOU",
        "text": (
            "Você abre a porta branca.\n\n"
            "Uma luz enorme toma conta do lugar.\n\n"
            "Você fecha os olhos.\n\n"
            "Quando abre novamente, está de volta ao "
            "corredor do prédio.\n\n"
            "Tudo parece normal.\n\n"
            "Seu celular está funcionando.\n\n"
            "Só se passaram cinco minutos.\n\n"
            "Mas então seu celular recebe uma mensagem:\n\n"
            "\"VOCÊ REALMENTE ACHOU QUE TINHA ESCAPADO?\"\n\n"
            "A tela fica preta.\n\n"
            "Fim..."
        ),
        "options": [],
    },


    "fim_alternativo": {
        "title": "🟠 FINAL ALTERNATIVO - ESCAPOU POR POUCO",
        "text": (
            "Você encontra a porta branca e consegue escapar.\n\n"
            "Porém, percebe que deixou pistas importantes "
            "para trás.\n\n"
            "Talvez as Backrooms ainda estejam esperando "
            "por você.\n\n"
            "Fim..."
        ),
        "options": [],
    },


    "fim_secreto": {
        "title": "🟣 FINAL SECRETO - A VERDADE",
        "text": (
            "Você olha novamente para os monitores.\n\n"
            "Agora percebe algo assustador.\n\n"
            "Todos os monitores mostram a mesma pessoa.\n\n"
            "Você.\n\n"
            "Uma mensagem aparece:\n\n"
            "\"AS BACKROOMS NÃO SÃO UM LUGAR.\"\n\n"
            "\"ELAS SÃO UM CICLO.\"\n\n"
            "A tela apaga.\n\n"
            "Quando volta, você está sentado diante de "
            "um computador.\n\n"
            "Na tela está escrito:\n\n"
            "\"NOVO JOGADOR DETECTADO.\"\n\n"
            "Talvez você tenha feito parte das Backrooms "
            "desde o começo.\n\n"
            "Fim..."
        ),
        "options": [],
    },


    "fim_ruim": {
        "title": "🔴 FINAL RUIM - PRESO PARA SEMPRE",
        "text": (
            "As luzes começam a piscar.\n\n"
            "Você escuta passos atrás de você.\n\n"
            "Toc... Toc... Toc...\n\n"
            "Você tenta correr.\n\n"
            "Mas o corredor nunca termina.\n\n"
            "As luzes se apagam.\n\n"
            "Quando voltam, você está novamente no mesmo lugar.\n\n"
            "\"VOCÊ ENTROU NAS BACKROOMS.\"\n\n"
            "Fim..."
        ),
        "options": [],
    },
}


# ============================================================
# ACESSO AO HTML
# ============================================================

def el(id_elemento):
    return web.page[id_elemento]


# ============================================================
# IDENTIDADE
# ============================================================

def configurar_identidade():

    window.document.title = CONFIG["titulo"]

    el("titulo-jogo").innerText = CONFIG["titulo"]
    el("autor-jogo").innerText = f"Autor: {CONFIG['autor']}"

    el("titulo-abertura").innerText = CONFIG["titulo"]
    el("subtitulo-abertura").innerText = CONFIG["subtitulo"]
    el("autor-abertura").innerText = f"Criado por {CONFIG['autor']}"
    el("icone-abertura").innerText = CONFIG["icone"]

    capa = CONFIG.get("capa")

    if capa:
        el("capa-jogo").src = capa
        el("capa-jogo").style.display = "block"
        el("icone-abertura").style.display = "none"
    else:
        el("capa-jogo").style.display = "none"
        el("icone-abertura").style.display = "block"

    audio = el("audio-fundo")

    trilha = CONFIG.get("trilha_inicial")

    if trilha:
        audio.dataset.inicial = trilha
    else:
        audio.dataset.inicial = ""

    audio.dataset.volume = str(
        CONFIG.get("volume_inicial", 0.5)
    )


# ============================================================
# STATUS
# ============================================================

def atualizar_status():

    vida = state["vida"]

    if vida > 0:
        el("vida").innerText = " ".join(["❤️"] * vida)
        el("vida").classList.remove("danger")
    else:
        el("vida").innerText = "💀"
        el("vida").classList.add("danger")

    if state["inventario"]:
        el("inventario").innerText = ", ".join(
            state["inventario"]
        )
    else:
        el("inventario").innerText = "Vazio"

    el("pontos").innerText = str(state["pontos"])


# ============================================================
# MULTIMÍDIA
# ============================================================

def mostrar_imagem(caminho):

    window.frameworkVideo.stop()

    imagem = el("imagem-cena")

    if not caminho:
        imagem.style.display = "none"
        return

    imagem.src = caminho
    imagem.style.display = "block"


def trocar_audio(caminho):

    if not caminho:
        return

    window.frameworkAudio.play(
        caminho,
        CONFIG.get("volume_inicial", 0.5),
        True
    )


def parar_audio():

    window.frameworkAudio.stop()


# ============================================================
# BOTÕES
# ============================================================

def configurar_botao(numero, texto="", ativo=False):

    botao = el(f"opcao{numero}")

    botao.innerText = texto
    botao.disabled = not ativo

    if ativo:
        botao.style.display = "block"
    else:
        botao.style.display = "none"


def atualizar_botoes(opcoes):

    for i in range(1, 5):

        if i <= len(opcoes):

            configurar_botao(
                i,
                opcoes[i - 1][0],
                True
            )

        else:

            configurar_botao(
                i,
                "",
                False
            )


# ============================================================
# MOSTRAR CENA
# ============================================================

def mostrar_cena(nome):

    if nome not in SCENES:

        el("titulo-cena").innerText = "Erro de cena"

        el("texto-cena").innerText = (
            f"A cena '{nome}' não existe."
        )

        atualizar_botoes([])

        return

    state["cena"] = nome

    cena = SCENES[nome]

    el("titulo-cena").innerText = (
        cena.get("title", nome)
    )

    el("texto-cena").innerText = (
        cena.get("text", "")
    )

    mostrar_imagem(
        cena.get("image")
    )

    atualizar_botoes(
        cena.get("options", [])
    )

    atualizar_status()


# ============================================================
# INVENTÁRIO
# ============================================================

def adicionar_item(item, pontos=0):

    if item not in state["inventario"]:

        state["inventario"].append(item)
        state["pontos"] += pontos

    atualizar_status()


def remover_item(item):

    if item in state["inventario"]:
        state["inventario"].remove(item)

    atualizar_status()


def possui_item(item):

    return item in state["inventario"]


# ============================================================
# VIDA
# ============================================================

def perder_vida(
    quantidade=1,
    cena_sem_vida="fim_ruim"
):

    state["vida"] -= quantidade

    if state["vida"] <= 0:

        state["vida"] = 0

        atualizar_status()

        mostrar_cena(cena_sem_vida)

        return True

    atualizar_status()

    return False


# ============================================================
# PONTOS
# ============================================================

def ganhar_pontos(quantidade):

    state["pontos"] += quantidade

    atualizar_status()


# ============================================================
# AÇÕES ESPECIAIS
# ============================================================

def executar_acao(acao):

    # --------------------------------------------------------
    # ITENS
    # --------------------------------------------------------

    if acao == "pegar_lanterna":

        adicionar_item(
            "🔦 Lanterna",
            pontos=10
        )

        mostrar_cena("corredor")


    elif acao == "pegar_chave":

        adicionar_item(
            "🗝️ Chave",
            pontos=10
        )

        mostrar_cena("corredor")


    elif acao == "pegar_agua":

        adicionar_item(
            "🥤 Água",
            pontos=5
        )

        mostrar_cena("corredor")


    # --------------------------------------------------------
    # PORTA VERMELHA
    # --------------------------------------------------------

    elif acao == "abrir_porta":

        if possui_item("🗝️ Chave"):

            ganhar_pontos(20)

            mostrar_cena("estacionamento")

        else:

            morreu = perder_vida()

            if not morreu:
                mostrar_cena("porta_falha")


    # --------------------------------------------------------
    # LANERNA
    # --------------------------------------------------------

    elif acao == "usar_lanterna":

        if possui_item("🔦 Lanterna"):

            ganhar_pontos(15)

            mostrar_cena("sala_seguranca")

        else:

            mostrar_cena("escada")


    # --------------------------------------------------------
    # ESCADA SEM LANTERNA
    # --------------------------------------------------------

    elif acao == "continuar_escuro":

        morreu = perder_vida()

        if not morreu:

            mostrar_cena("sala_seguranca")


    # --------------------------------------------------------
    # ESTACIONAMENTO
    # --------------------------------------------------------

    elif acao == "esconder_carro":

        ganhar_pontos(10)

        mostrar_cena("sala_seguranca")


    elif acao == "correr_estacionamento":

        morreu = perder_vida(2)

        if not morreu:

            mostrar_cena("sala_seguranca")


    # --------------------------------------------------------
    # FINAL SECRETO
    # --------------------------------------------------------

    elif acao == "investigar_monitores":

        if possui_item("🥤 Água"):

            ganhar_pontos(30)

            mostrar_cena("fim_secreto")

        else:

            mostrar_cena("fim_alternativo")


    # --------------------------------------------------------
    # FINAL DEPENDENTE DO INVENTÁRIO
    # --------------------------------------------------------

    elif acao == "decidir_final":

        itens_necessarios = {
            "🗝️ Chave",
            "🔦 Lanterna",
            "🥤 Água"
        }

        itens_jogador = set(
            state["inventario"]
        )

        if itens_necessarios.issubset(
            itens_jogador
        ):

            ganhar_pontos(50)

            mostrar_cena("fim_bom")

        else:

            mostrar_cena("fim_alternativo")


    # --------------------------------------------------------
    # AÇÃO NORMAL
    # --------------------------------------------------------

    elif acao in SCENES:

        mostrar_cena(acao)


    # --------------------------------------------------------
    # AÇÃO INVÁLIDA
    # --------------------------------------------------------

    else:

        el("texto-cena").innerText = (
            f"A ação '{acao}' não foi cadastrada."
        )


# ============================================================
# ESCOLHAS
# ============================================================

def escolher_opcao(numero):

    cena = SCENES[
        state["cena"]
    ]

    opcoes = cena.get(
        "options",
        []
    )

    indice = numero - 1

    if indice < len(opcoes):

        acao = opcoes[
            indice
        ][1]

        executar_acao(acao)


# ============================================================
# BOTÕES
# ============================================================

@when("click", "#opcao1")
def clicar_opcao1(event):
    escolher_opcao(1)


@when("click", "#opcao2")
def clicar_opcao2(event):
    escolher_opcao(2)


@when("click", "#opcao3")
def clicar_opcao3(event):
    escolher_opcao(3)


@when("click", "#opcao4")
def clicar_opcao4(event):
    escolher_opcao(4)


@when("click", "#reiniciar")
def reiniciar(event):

    state["vida"] = CONFIG["vida_inicial"]
    state["inventario"] = []
    state["pontos"] = CONFIG["pontos_iniciais"]
    state["cena"] = CONFIG["cena_inicial"]

    trilha = CONFIG.get("trilha_inicial")

    if trilha:
        trocar_audio(trilha)

    mostrar_cena(
        CONFIG["cena_inicial"]
    )


# ============================================================
# INICIALIZAÇÃO
# ============================================================

configurar_identidade()

mostrar_cena(
    CONFIG["cena_inicial"]
)

el("botao-iniciar").disabled = False
el("botao-iniciar").innerText = "▶ INICIAR JOGO"
