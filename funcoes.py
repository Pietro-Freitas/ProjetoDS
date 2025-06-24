import streamlit as st
def cadastrar():
    st.title("Cadastrar Tarefa")
    lista_usuarios=[]
    with open("usuarios.txt", "r", encoding='utf-8') as arquivo:
        lista_usuarios = [linha.strip() for linha in arquivo]

        nome = st.selectbox("Nome: ", lista_usuarios)
        descricao = st.text_area(label="Descrição: ", placeholder="Digite Aqui...")
        prioridade = st.radio("Prioridade: ", ["Alta", "Média", "Baixa"])
        data_limite = st.date_input("Data Limite: ")
        duracao_estimada = st.time_input("Duração Estimada: ")
        salvar = st.button("Salvar")

        if salvar:
            st.balloons()
            if nome and descricao and prioridade and data_limite and duracao_estimada:
                with open ('tarefas.txt', 'a', encoding='utf-8') as arquivo:
                    arquivo.write(f'{nome} | {descricao} | {prioridade} | {data_limite} | {duracao_estimada}\n')
                    st.success('Dados salvos com sucesso!')
                    st.markdown('### Último cadastro:')
                    st.write(f'**Nome:** {nome}')
                    st.write(f'**Descrição:** {descricao}')
                    st.write(f'**Prioridade:** {prioridade}')
                    st.write(f'**Data Limite:** {data_limite}')
                    st.write(f'**Duração Estimada:** {duracao_estimada}')
            else:
                st.warning('Preencha os dados primeiro!')




def visualizar():
    st.title("Visualizar Tarefas")

    lista_usuarios=[]
    with open("usuarios.txt", "r", encoding='utf-8') as arquivo:
        lista_usuarios = [linha.strip() for linha in arquivo]

    nome = st.selectbox("Nome: ", lista_usuarios)

    with open("tarefas.txt", "r", encoding='utf-8') as arquivo:
        for linha in arquivo:
            campos=linha.split(" | ")
            if nome==campos[0]:
                st.markdown("- " + linha)
            
            


def editar():
    st.title("Editar Tarefas")

    with open("tarefas.txt", "r", encoding="utf-8") as f:
        linhas = f.readlines()

    descricoes = []
    for linha in linhas:
        partes = linha.strip().split(" | ")
        if len(partes) == 5:
            descricoes.append(partes[1])

    if not descricoes:
        st.info("Nenhuma tarefa para editar.")
        return

    tarefa_escolhida = st.selectbox("Escolha a tarefa:", descricoes)

    for i, linha in enumerate(linhas):
        partes = linha.strip().split(" | ")
        if partes[1] == tarefa_escolhida:
            nome_atual, _, _, _, _ = partes
            break

    nome = st.text_input("Nome:", nome_atual)
    descricao = st.text_area("Descrição:", tarefa_escolhida)
    prioridade = st.radio("Prioridade:", ["Alta", "Média", "Baixa"])
    data = st.date_input("Data Limite:")
    duracao = st.time_input("Duração Estimada:")

    if st.button("Salvar"):
        nova = f"{nome} | {descricao} | {prioridade} | {data} | {duracao}\n"
        linhas[i] = nova

        with open("tarefas.txt", "w", encoding="utf-8") as f:
            f.writelines(linhas)

        st.success("Tarefa atualizada com sucesso!")