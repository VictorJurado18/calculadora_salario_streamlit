import streamlit as st
import datetime
import holidays

def verificar_feriado(data):
    br_holidays = holidays.Brazil()  # Defina o país desejado

    return data in br_holidays

def calcular_horas_trabalho_mes(mes, ano):
    if mes < 1 or mes > 12:
        st.error("Mês inválido. O valor do mês deve estar entre 1 e 12.")
        return 0

    if mes == 12:
        proximo_mes = 1
        proximo_ano = ano + 1
    else:
        proximo_mes = mes + 1
        proximo_ano = ano

    # Obtém o último dia do mês informado
    ultimo_dia_mes = datetime.date(proximo_ano, proximo_mes, 1) - datetime.timedelta(days=1)
    num_dias_mes = ultimo_dia_mes.day

    # Conta quantos dias úteis existem no mês, desconsiderando os feriados
    num_dias_uteis = 0
    for dia in range(1, num_dias_mes+1):
        data = datetime.date(ano, mes, dia)
        if data.weekday() < 5 and not verificar_feriado(data):  # Verifica se é um dia útil e não é feriado
            num_dias_uteis += 1

    # Calcula o número total de horas de trabalho no mês
    horas_trabalho_mes = num_dias_uteis * 8

    return horas_trabalho_mes



def calcular_salario_mensal(horas_trabalhadas, taxa_horaria):
    salario = horas_trabalhadas * taxa_horaria
    return salario


st.title('Calculadora de salário.')

# Widgets para entrada de dados
anos = list(range(2023, 2026))
ano = st.selectbox('Selecione o ano:', anos)
meses = list(range(1, 13))
mes = st.selectbox('Digite o mês (1-12):', meses)
taxa_horaria = st.number_input('Digite seu valor hora:')

horas_trabalho_mes = calcular_horas_trabalho_mes(mes, ano)


salario_mensal = calcular_salario_mensal(horas_trabalho_mes, taxa_horaria)
despesas_basicas = salario_mensal * 0.60
poupanca_investimento = salario_mensal * 0.20
gastos_pessoais = salario_mensal * 0.20


st.write("Número de horas de trabalho no mês:", horas_trabalho_mes)
st.write("Salário mensal estimado: R$", salario_mensal)

st.markdown("## Recomendação de divisão do salário")

st.write(f'Despesas Basicas: {despesas_basicas:.2f}')
st.write(f'Poupança e investimentos: {poupanca_investimento:.2f}')
st.write(f'Gastos Pessoais: {gastos_pessoais:.2f}')





