import os
# Cria os arquivos
def criar_tarefas():
    if os.path.exists('tarefas.txt'):
       pass
    else:
        with open('tarefas.txt', 'a', encoding='utf-8') as arquivoT:
            pass

def criar_usuarios():
    if os.path.exists('usuarios.txt'):
       pass
    else:
        with open('usuarios.txt', 'a', encoding='utf-8') as arquivoU:
            pass