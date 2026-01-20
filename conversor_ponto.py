import os
import tkinter as tk
from tkinter import filedialog, messagebox


CODIGO_EMPRESA = "001"

def converter_arquivo_matricula(caminho_arquivo):
    # Criação de dicionário
    registros_por_data = {}

    try:
        with open(caminho_arquivo, 'r', encoding='latin-1') as f_entrada:
            # Dividindo a linha em partes (o arquivo tem espaços em branco entre matricula, data e etc)
            for linha in f_entrada:
                partes = linha.strip().split()

                if len(partes) >= 4:
                    data = partes[0]       # 11/12/2025
                    hora = partes[1]       # 00:00
                    matricula = partes[3]

                    linha_formatada = f"{CODIGO_EMPRESA} {matricula} {data} {hora}"
                    # Criando nova chave no dicionário para cada data diferente
                    if data not in registros_por_data:
                        registros_por_data[data] = []

                    registros_por_data[data].append(linha_formatada)

        pasta_saida = os.path.dirname(caminho_arquivo)

        for data, registros in registros_por_data.items():
            nome_saida = gerar_nome_saida_por_data(data)
            caminho_saida = os.path.join(pasta_saida, nome_saida)

            with open(caminho_saida, 'w', encoding='utf-8') as f_saida:
                for registro in registros:
                    f_saida.write(registro + '\n')

        messagebox.showinfo(
            "Sucesso",
            "Conversão concluída!\nArquivos gerados por data."
        )

    except Exception as e:
        messagebox.showerror("Erro", f"Ocorreu um erro:\n{e}")

def selecionar_arquivo():
    arquivo = filedialog.askopenfilename(
        title="Selecione o arquivo TXT",
        filetypes=[("Arquivos TXT", "*.txt")]
    )

    if arquivo:
        converter_arquivo_matricula(arquivo)

# O arquivo origem tem datas em ordem cronológica e para a importação eu preciso do agrupamento de datas por arquivo
def gerar_nome_saida_por_data(data):
    data_formatada = data.replace("/", "-")
    return f"{data_formatada}.txt"

# INTERFACE
janela = tk.Tk()
janela.title("Conversor de Ponto - Fiorilli")
janela.geometry("400x200")
janela.resizable(False, False)

label = tk.Label(
    janela,
    text="Selecione o arquivo de ponto\npara converter:",
    font=("Arial", 11)
)
label.pack(pady=20)

botao = tk.Button(
    janela,
    text="Selecionar arquivo TXT",
    font=("Arial", 11),
    width=25,
    command=selecionar_arquivo
)
botao.pack(pady=10)

janela.mainloop()
