import streamlit as st
import os
import tabula as tb
import os
from pdfminer.high_level import extract_text


st.markdown('''
              <h4 style='text-align: center'> Gerador de tabela PSS </h4>
              <p style='text-align: center; background-color: lightgreen; font-weight: bold'>
                Selecione ou arraste o arquivo PDF gerado no CACOCONPSS:  
              </p>
              ''', unsafe_allow_html=True)

def limpa_tela():
   return

def cabecalho_tabela(nome_pdf):
  with open(f"{nome_pdf}.html", "w", encoding="utf-8") as pss:
    pss.write(f'''
          <table border="1" cellpadding="0" cellspacing="0">
            <thead>
              <tr>
                  <td style="text-align: center; padding: 5px;">&nbsp;&nbsp;Ano&nbsp;</td>
                  <td style="text-align: center; padding: 5px;">&nbsp;Janeiro&nbsp;</td>
                  <td style="text-align: center; padding: 5px;">&nbsp;Fevereiro&nbsp;</td>
                  <td style="text-align: center; padding: 5px;">&nbsp;Março&nbsp;</td>
                  <td style="text-align: center; padding: 5px;">&nbsp;Abril&nbsp;</td>
                  <td style="text-align: center; padding: 5px;">&nbsp;Maio&nbsp;</td>
                  <td style="text-align: center; padding: 5px;">&nbsp;Junho&nbsp;</td>
                  <td style="text-align: center; padding: 5px;">&nbsp;Julho&nbsp;</td>
                  <td style="text-align: center; padding: 5px;">&nbsp;Agosto&nbsp;</td>
                  <td style="text-align: center; padding: 5px;">&nbsp;Setembro&nbsp;</td>
                  <td style="text-align: center; padding: 5px;">&nbsp;Outubro&nbsp;</td>
                  <td style="text-align: center; padding: 5px;">&nbsp;Novembro&nbsp;</td>
                  <td style="text-align: center; padding: 5px;">&nbsp;Dezembro&nbsp;</td>
                  <td style="text-align: center; padding: 5px;">&nbsp;Grat.Natalina &nbsp;</td>
              </tr>
              <tr>
                  <td style="text-align: center; padding: 5px;">&nbsp;&nbsp;</td>
                  <td style="text-align: center; padding: 5px;">&nbsp;Valor&nbsp;</td>
                  <td style="text-align: center; padding: 5px;">&nbsp;Valor&nbsp;</td>
                  <td style="text-align: center; padding: 5px;">&nbsp;Valor&nbsp;</td>
                  <td style="text-align: center; padding: 5px;">&nbsp;Valor&nbsp;</td>
                  <td style="text-align: center; padding: 5px;">&nbsp;Valor&nbsp;</td>
                  <td style="text-align: center; padding: 5px;">&nbsp;Valor&nbsp;</td>
                  <td style="text-align: center; padding: 5px;">&nbsp;Valor&nbsp;</td>
                  <td style="text-align: center; padding: 5px;">&nbsp;Valor&nbsp;</td>
                  <td style="text-align: center; padding: 5px;">&nbsp;Valor&nbsp;</td>
                  <td style="text-align: center; padding: 5px;">&nbsp;Valor&nbsp;</td>
                  <td style="text-align: center; padding: 5px;">&nbsp;Valor&nbsp;</td>
                  <td style="text-align: center; padding: 5px;">&nbsp;Valor&nbsp;</td>
                  <td style="text-align: center; padding: 5px;">&nbsp;Valor&nbsp;</td>
              </tr>
            </thead>
            <tbody border="1" cellpadding="0" cellspacing="0">''')
    

def corpo_tabela(dados_pss, ano, nome_pdf):
  with open(f"{nome_pdf}.html", "a") as pss:
    pss.write(f'''
                  <tr>
                    <td style="text-align: center; padding: 5px;">&nbsp;{ano}&nbsp;</td>
                    <td style="text-align: center; padding: 5px;">&nbsp;{dados_pss[0][1]}&nbsp;</td>
                    <td style="text-align: center; padding: 5px;">&nbsp;{dados_pss[1][1]}&nbsp;</td>
                    <td style="text-align: center; padding: 5px;">&nbsp;{dados_pss[2][1]}&nbsp;</td>
                    <td style="text-align: center; padding: 5px;">&nbsp;{dados_pss[3][1]}&nbsp;</td>
                    <td style="text-align: center; padding: 5px;">&nbsp;{dados_pss[4][1]}&nbsp;</td>
                    <td style="text-align: center; padding: 5px;">&nbsp;{dados_pss[5][1]}&nbsp;</td>
                    <td style="text-align: center; padding: 5px;">&nbsp;{dados_pss[6][1]}&nbsp;</td>
                    <td style="text-align: center; padding: 5px;">&nbsp;{dados_pss[7][1]}&nbsp;</td>
                    <td style="text-align: center; padding: 5px;">&nbsp;{dados_pss[8][1]}&nbsp;</td>
                    <td style="text-align: center; padding: 5px;">&nbsp;{dados_pss[9][1]}&nbsp;</td>
                    <td style="text-align: center; padding: 5px;">&nbsp;{dados_pss[10][1]}&nbsp;</td>
                    <td style="text-align: center; padding: 5px;">&nbsp;{dados_pss[11][1]}&nbsp;</td>
                    <td style="text-align: center; padding: 5px;">&nbsp;{dados_pss[12][1]}&nbsp;</td>
                  </tr>
                  
                  ''')

def fechamento_tabela(nome_pdf):
  with open(f"{nome_pdf}.html", "a") as pss:
    pss.write(f'''</tbody>
              </table>''')

# Fazer download de arquvios
def baixar_arquivos(nome_do_arq):
  
      try:
          with open(str(nome_do_arq), "rb") as file:
              st.download_button(
                  label="CLIQUE AQUI PARA BAIXAR A TABELA GERADA EM FORMATO HTML",
                  data=file,
                  file_name=nome_do_arq,
                  mime="text/html")
      except:
        st.error("ARQUIVO NÃO LOCALIZADO! REPITA O PROCESSO.")
 
      os.remove(nome_do_arq)

# limpar console
def limpa_tela():
  return os.system('Clear')

# capturar ano
def captura_ano(texto):
  inicio = texto.find("CONSULTA  :  ")
  termino = texto.find("                                                                    CONTINUA... ") - 3
  ano = texto[(inicio + 13):(inicio + 17)]
  return ano


def gerar_tabela_pss(nome_arq, arquivo_pdf):

  # carregar o arquivo
  tabela = tb.read_pdf(arquivo_pdf, pages="all") # gerando uma lista com as tabelas
  # capturando ano do arquivo
  texto_arquivo = extract_text(arquivo_pdf)
  ano_arquivo = captura_ano(texto_arquivo)
  ano = ano_arquivo
  # Gerando cabeçalho do arquivo
  cabecalho_tabela(nome_arq)
  # percorrendo tabelas
  for ind, tab in enumerate(tabela):
    # retirando coluna desnecessária
    tabela[ind] = tabela[ind].drop(columns=["Unnamed: 1", "REMUN.INFORMADA", "REMUN.REAJUSTADA"])
  
    # Mudando nome das colunas (CABEÇALHO DA TABELA)
    tabela[ind].columns = ['MES', 'REMUN.CONSIDERADA']
  
    # dicionário para guardar os dados
    dados_pss = []
  
    # colocando as demais linhas dentro da lista
    for row in range(13):
      dados_pss.append([tabela[ind]['MES'][row].replace(":",""), tabela[ind]["REMUN.CONSIDERADA"][row]])
  
    # inserindo informações na tabela
    corpo_tabela(dados_pss, ano, nome_arq)
  
    # incrementando o ano
    ano = int(ano) + 1

  # fechando a parte final do arquivo e fazendo download
  fechamento_tabela(nome_arq)
  baixar_arquivos(f'{nome_arq}.html')
  

# solicitando o carregamento do arquivo
uploaded_file = st.file_uploader("Selecionar arquivo:")  
if uploaded_file is not None:
  gerar_tabela_pss(uploaded_file.name, uploaded_file)
  st.rerun()
  
 
