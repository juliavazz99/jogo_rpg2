# ==========================================
# BACKROOMS - O ÚLTIMO CORREDOR
# Jogo de aventura em texto
# ==========================================


# Estado do jogador
jogador = {
    "vida": 3,
    "inventario": []
}


# ------------------------------------------
# Função para validar as escolhas
# ------------------------------------------

def escolher(mensagem, opcoes):
    while True:
        escolha = input(mensagem).strip()

        if escolha in opcoes:
            return escolha

        print("⚠️ Opção inválida. Escolha uma das opções disponíveis.")


# ------------------------------------------
# Função para adicionar itens
# ------------------------------------------

def pegar_item(item):
    if item not in jogador["inventario"]:
        jogador["inventario"].append(item)
        print(f"🎒 Você pegou: {item}")


# ------------------------------------------
# CENA 1 - INÍCIO
# ------------------------------------------

def inicio():

    print("\n" + "=" * 50)
    print("🟨 BACKROOMS - O ÚLTIMO CORREDOR")
    print("=" * 50)

    print("""
Você estava voltando para casa depois da escola.

O corredor do prédio parecia completamente normal.

Até que você percebeu uma coisa.

As paredes estavam... diferentes.

O corredor parecia muito mais comprido do que deveria.

Você colocou a mão na parede.

Ela parecia real.

Mas quando você se apoiou nela...

A parede desapareceu.

Você caiu.

...

Quando abriu os olhos, estava em uma enorme sala
com paredes amarelas, carpete úmido e lâmpadas
fluorescentes fazendo um zumbido irritante.

Você tentou voltar.

Não havia porta.

Seu celular estava com 0% de bateria.

Mesmo assim, uma mensagem apareceu:

"VOCÊ ENTROU NAS BACKROOMS."

Você escuta um barulho distante.

Toc...

Toc...

Toc...
""")

    escolha = escolher(
        """
O que você vai fazer?

1 - Seguir pelo corredor
2 - Entrar em uma sala aberta

Escolha: """,
        ["1", "2"]
    )

    if escolha == "1":
        return "corredor"

    return "sala_abandonada"


# ------------------------------------------
# CENA 2 - SALA ABANDONADA
# ------------------------------------------

def sala_abandonada():

    print("\n" + "=" * 50)
    print("🏚️ SALA ABANDONADA")
    print("=" * 50)

    print("""
Você entra em uma pequena sala.

Diferente do corredor, as lâmpadas aqui estão
quase todas apagadas.

No chão existem três objetos:

🔦 Uma lanterna
🗝️ Uma chave enferrujada
🥤 Uma garrafa de água

Você sente que esses objetos podem ser importantes.
""")

    escolha = escolher(
        """
O que você quer pegar?

1 - Lanterna
2 - Chave
3 - Garrafa de água

Escolha: """,
        ["1", "2", "3"]
    )

    if escolha == "1":
        pegar_item("lanterna")

    elif escolha == "2":
        pegar_item("chave")

    else:
        pegar_item("água")

    print("""
Antes de sair da sala, você escuta um barulho.

Toc...

Toc...

Toc...

O som está ficando mais próximo.
""")

    return "corredor"


# ------------------------------------------
# CENA 3 - CORREDOR
# ------------------------------------------

def corredor():

    print("\n" + "=" * 50)
    print("🚪 O CORREDOR")
    print("=" * 50)

    print("""
Você continua andando.

O corredor parece não ter fim.

Depois de alguns minutos, você encontra duas opções.

À esquerda existe uma porta vermelha.

À direita existe uma escada que desce para um
nível completamente escuro.

Você sente que alguma coisa está observando você.
""")

    escolha = escolher(
        """
1 - Entrar pela porta vermelha
2 - Descer a escada

Escolha: """,
        ["1", "2"]
    )

    if escolha == "1":
        return "porta_vermelha"

    return "escada"


# ------------------------------------------
# CENA 4 - PORTA VERMELHA
# ------------------------------------------

def porta_vermelha():

    print("\n" + "=" * 50)
    print("🚨 A PORTA VERMELHA")
    print("=" * 50)

    print("""
Você chega perto da porta.

Ela possui uma pequena fechadura.

Você tenta abrir.

Nada.

A porta está trancada.

Há uma pequena inscrição:

"APENAS QUEM POSSUI A CHAVE PODE PASSAR."
""")

    if "chave" in jogador["inventario"]:

        print("""
Você lembra da chave que encontrou na sala.

Você coloca a chave na fechadura.

CLIC.

A porta se abre lentamente.

Atrás dela existe um enorme estacionamento.
""")

        return "estacionamento"

    else:

        print("""
Você não possui a chave.

De repente...

BANG!

Alguma coisa bate do outro lado da porta.

Você se assusta e corre de volta.
""")

        jogador["vida"] -= 1

        print(f"❤️ Vida restante: {jogador['vida']}")

        if jogador["vida"] <= 0:
            return "fim_ruim"

        return "corredor"


# ------------------------------------------
# CENA 5 - ESCADA
# ------------------------------------------

def escada():

    print("\n" + "=" * 50)
    print("⬇️ A ESCADA")
    print("=" * 50)

    print("""
Você começa a descer.

Um degrau.

Dois.

Três.

O som das lâmpadas desaparece.

Agora existe apenas escuridão.

Você não consegue enxergar absolutamente nada.
""")

    if "lanterna" in jogador["inventario"]:

        print("""
Você lembra da lanterna.

Você a liga.

A luz ilumina o caminho.

Nas paredes existem dezenas de mensagens:

"ELE ESTÁ AQUI."

"CORRA."

"NÃO OLHE PARA TRÁS."

Você continua andando.

Depois de alguns metros encontra uma porta.
""")

        return "sala_seguranca"

    else:

        print("""
Você tenta continuar no escuro.

De repente...

Você tropeça.

Você cai no chão e machuca a perna.

❤️ -1 vida.
""")

        jogador["vida"] -= 1

        print(f"❤️ Vida restante: {jogador['vida']}")

        if jogador["vida"] <= 0:
            return "fim_ruim"

        escolha = escolher(
            """
Você pode:

1 - Voltar
2 - Continuar no escuro

Escolha: """,
            ["1", "2"]
        )

        if escolha == "1":
            return "corredor"

        return "fim_ruim"


# ------------------------------------------
# CENA 6 - ESTACIONAMENTO
# ------------------------------------------

def estacionamento():

    print("\n" + "=" * 50)
    print("🚗 ESTACIONAMENTO INFINITO")
    print("=" * 50)

    print("""
Você entra no estacionamento.

Existem centenas de vagas.

Nenhum carro possui motorista.

Alguns carros estão abandonados.

Você começa a procurar uma saída.

Então...

Toc...

Toc...

Toc...

Você olha para trás.

No final do estacionamento existe uma
silhueta parada.

Ela está olhando diretamente para você.

Você não consegue ver o rosto.

A criatura começa a andar.
""")

    escolha = escolher(
        """
O que você faz?

1 - Se esconder dentro de um carro
2 - Correr até o outro lado do estacionamento

Escolha: """,
        ["1", "2"]
    )

    if escolha == "1":

        print("""
Você entra rapidamente em um carro.

A criatura passa perto.

Você prende a respiração.

Depois de alguns segundos...

Ela desaparece.

No painel do carro existe um botão escrito:

"SAÍDA"
""")

        return "sala_seguranca"

    else:

        print("""
Você começa a correr.

A criatura percebe você.

Você corre cada vez mais rápido.

Mas o estacionamento parece ficar maior.

Você não consegue encontrar uma saída.
""")

        jogador["vida"] -= 2

        print(f"❤️ Vida restante: {jogador['vida']}")

        if jogador["vida"] <= 0:
            return "fim_ruim"

        return "sala_seguranca"


# ------------------------------------------
# CENA 7 - SALA DE SEGURANÇA
# ------------------------------------------

def sala_seguranca():

    print("\n" + "=" * 50)
    print("📹 SALA DE SEGURANÇA")
    print("=" * 50)

    print("""
Você entra em uma sala cheia de monitores.

Cada monitor mostra um lugar diferente.

Corredores.

Escadas.

Estacionamentos.

Salas amarelas.

No último monitor aparece algo diferente.

Uma porta branca.

Embaixo dela está escrito:

"SAÍDA"
""")

    escolha = escolher(
        """
Você encontra duas opções:

1 - Procurar a porta branca
2 - Investigar os monitores

Escolha: """,
        ["1", "2"]
    )

    if escolha == "1":

        print("""
Você decide procurar a porta.

Depois de andar por vários corredores,
finalmente encontra uma porta branca.

Ela está aberta.

Uma luz forte vem de dentro.
""")

        return "fim_bom"

    else:

        print("""
Você começa a investigar os monitores.

Em um deles aparece uma gravação.

É você.

Mas a gravação mostra você andando
pelas Backrooms há horas.

Você percebe algo assustador.

A gravação mostra alguém atrás de você.

Você olha para trás.

Não há ninguém.

Quando olha novamente para o monitor...

A criatura está muito mais perto.
""")

        return "fim_secreto"


# ------------------------------------------
# FINAL BOM
# ------------------------------------------

def fim_bom():

    print("\n" + "=" * 50)
    print("🟢 FINAL BOM - VOCÊ ESCAPOU")
    print("=" * 50)

    print("""
Você abre a porta branca.

Uma luz enorme toma conta do lugar.

Você fecha os olhos.

Quando abre novamente...

Está de volta ao corredor do prédio.

Tudo parece normal.

Seu celular está funcionando.

Você olha para a hora.

Só se passaram cinco minutos.

Mas então...

Seu celular recebe uma mensagem.

"VOCÊ REALMENTE ACHOU QUE TINHA ESCAPADO?"

A tela fica preta.

Fim...
""")

    mostrar_inventario()

    return "fim"


# ------------------------------------------
# FINAL RUIM
# ------------------------------------------

def fim_ruim():

    print("\n" + "=" * 50)
    print("🔴 FINAL RUIM - PRESO PARA SEMPRE")
    print("=" * 50)

    print("""
As luzes começam a piscar.

Você escuta passos atrás de você.

Toc...

Toc...

Toc...

Você tenta correr.

Mas o corredor nunca termina.

As luzes se apagam.

Quando voltam...

Você está novamente no mesmo lugar onde começou.

A mensagem aparece novamente:

"VOCÊ ENTROU NAS BACKROOMS."

Só que agora existe uma sombra atrás de você.

Fim...
""")

    mostrar_inventario()

    return "fim"


# ------------------------------------------
# FINAL SECRETO
# ------------------------------------------

def fim_secreto():

    print("\n" + "=" * 50)
    print("🟣 FINAL SECRETO - A VERDADE")
    print("=" * 50)

    print("""
Você olha novamente para os monitores.

Agora percebe algo que não tinha notado.

Todos os monitores mostram a mesma pessoa.

Você.

Mas em cada monitor existe uma versão diferente
de você.

Uma delas está entrando nas Backrooms.

Outra está tentando escapar.

Outra está observando você.

Então uma mensagem aparece no monitor principal:

"AS BACKROOMS NÃO SÃO UM LUGAR."

"ELAS SÃO UM CICLO."

A tela apaga.

Quando volta...

Você está sentado em uma cadeira.

Na sua frente existe um computador.

No computador está escrito:

"NOVO JOGADOR DETECTADO."

Você percebe que talvez nunca tenha sido
o jogador.

Talvez você tenha sido parte das Backrooms
desde o começo.

Fim...
""")

    mostrar_inventario()

    return "fim"


# ------------------------------------------
# MOSTRAR INVENTÁRIO
# ------------------------------------------

def mostrar_inventario():

    print("\n🎒 INVENTÁRIO FINAL:")

    if len(jogador["inventario"]) == 0:
        print("Vazio.")

    else:
        for item in jogador["inventario"]:
            print(f"- {item}")


# ------------------------------------------
# DICIONÁRIO DE CENAS
# ------------------------------------------

cenas = {
    "inicio": inicio,
    "sala_abandonada": sala_abandonada,
    "corredor": corredor,
    "porta_vermelha": porta_vermelha,
    "escada": escada,
    "estacionamento": estacionamento,
    "sala_seguranca": sala_seguranca,
    "fim_bom": fim_bom,
    "fim_ruim": fim_ruim,
    "fim_secreto": fim_secreto
}


# ------------------------------------------
# PROGRAMA PRINCIPAL
# ------------------------------------------

def main():

    cena_atual = "inicio"

    # O while continua executando enquanto o jogador
    # ainda estiver percorrendo as cenas.
    while cena_atual != "fim":

        cena_atual = cenas[cena_atual]()


# ------------------------------------------
# INICIAR O JOGO
# ------------------------------------------

if __name__ == "__main__":
    main()