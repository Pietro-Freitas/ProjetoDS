import streamlit as st

st.set_page_config(page_title='CadastroTarefas', layout='wide', initial_sidebar_state="expanded")

pagina = st.sidebar.selectbox('Escolha uma página:', ['Cadastrar', 'Entrar', 'Tarefas'])

paginas = {
    'Cadastrar': 'cadastrar.py',
    'Entrar': 'entrar.py',
    'Tarefas': 'tarefas.py'
}


with open(paginas[pagina], 'r', encoding='utf-8') as arquivo:
    exec(arquivo.read())