import streamlit as st
from funcoes import cadastrar
from funcoes import visualizar
from funcoes import editar

with st.sidebar:
    st.title("Menu Lateral")
    opcao = st.selectbox("Opções:", ["Cadastrar Tarefas", "Visualizar Tarefas", "Editar Tarefas"])

if opcao == "Cadastrar Tarefas":
    cadastrar()
elif opcao == "Visualizar Tarefas":
    visualizar()
elif opcao == "Editar Tarefas":
    editar()