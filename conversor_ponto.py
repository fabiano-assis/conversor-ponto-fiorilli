import os
import tkinter as tk
from tkinter import filedialog, messagebox

# --- CONFIGURAÇÃO ---
CODIGO_EMPRESA = "001"

def gerar_nome_saida(caminho_arquivo):
    nome_original = os.path.basename(caminho_arquivo)
    nome_sem_extensao = os.path.splitext(nome_original)[0]

    nome_saida = f"{nome_sem_extensao}_convertido.txt"
    return nome_saida

def converter_arquivo_matricula(caminho_arquivo):
    registros_convertidos = []

    try:
        with open(caminho_arquivo, 'r', encoding='latin-1') as f_entrada:
            for linha in f_entrada:
                partes = linha.strip().split()

                if len(partes) >= 4:
                    data = partes[0]
                    hora = partes[1]
                    matricula = partes[3]

                    linha_formatada = f"{CODIGO_EMPRESA} {matricula} {data} {hora}"
                    registros_convertidos.append(linha_formatada)

        pasta_saida = os.path.dirname(caminho_arquivo)
        nome_saida = gerar_nome_saida(caminho_arquivo)
        caminho_saida = os.path.join(pasta_saida, nome_saida)


        with open(caminho_saida, 'w', encoding='utf-8') as f_saida:
            for registro in registros_convertidos:
                f_saida.write(registro + '\n')

        messagebox.showinfo(
            "Sucesso",
            f"Conversão concluída!\nArquivo gerado:\n{caminho_saida}"
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

# --- INTERFACE ---
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