import csv
import io
import random

import pandas as pd
import streamlit as st


st.set_page_config(page_title="Tech Case | Sorteio de Duplas", page_icon="🎲")


def carregar_estudantes(arquivo) -> list[str]:
    """Lê o CSV, escolhe a coluna de nomes e retorna valores limpos e únicos."""
    conteudo = arquivo.read()
    try:
        separador = csv.Sniffer().sniff(
            conteudo.decode("utf-8-sig"), delimiters=",;"
        ).delimiter
    except csv.Error:
        separador = ","
    dados = pd.read_csv(io.BytesIO(conteudo), sep=separador)

    if dados.empty and len(dados.columns) == 0:
        raise ValueError("o arquivo não contém colunas ou dados.")

    colunas_por_nome = {
        str(coluna).strip().lower(): coluna for coluna in dados.columns
    }
    coluna_nomes = next(
        (
            colunas_por_nome[nome_coluna]
            for nome_coluna in ("nome", "aluno", "estudante")
            if nome_coluna in colunas_por_nome
        ),
        dados.columns[0],
    )

    estudantes = []
    for valor in dados[coluna_nomes]:
        if pd.isna(valor):
            continue
        nome = str(valor).strip()
        if nome and nome not in estudantes:
            estudantes.append(nome)

    return estudantes


def exibir_resultado(dupla: list[str]) -> None:
    st.subheader("Dupla sorteada")
    colunas = st.columns(2)
    for coluna, estudante in zip(colunas, dupla):
        coluna.success(f"👤 {estudante}")


if "dupla_sorteada" not in st.session_state:
    st.session_state.dupla_sorteada = None
if "arquivo_carregado" not in st.session_state:
    st.session_state.arquivo_carregado = None


st.markdown(
    """
    <style>
    .block-container { max-width: 760px; padding-top: 3rem; }
    .app-footer { color: #6b7280; font-size: 0.85rem; margin-top: 3rem; text-align: center; }
    </style>
    """,
    unsafe_allow_html=True,
)

st.title("🎲 Tech Case")
st.subheader("Sorteio de duplas")
st.write(
    "Envie a lista de estudantes e sorteie a dupla responsável por mediar "
    "o próximo Tech Case."
)

arquivo = st.file_uploader("Envie a lista de estudantes", type=["csv"])

if arquivo is not None:
    identificador_arquivo = (arquivo.name, arquivo.size)
    if identificador_arquivo != st.session_state.arquivo_carregado:
        st.session_state.arquivo_carregado = identificador_arquivo
        st.session_state.dupla_sorteada = None

    try:
        estudantes = carregar_estudantes(io.BytesIO(arquivo.getvalue()))
    except Exception as erro:
        st.error(
            "Não foi possível ler o CSV. Verifique se o arquivo está em um "
            f"formato válido: {erro}"
        )
    else:
        st.info(f"{len(estudantes)} estudante(s) carregado(s).")
        with st.expander("Visualizar estudantes", expanded=True):
            st.dataframe(
                pd.DataFrame({"Estudante": estudantes}),
                hide_index=True,
                use_container_width=True,
            )

        if len(estudantes) < 2:
            st.error(
                "É necessário ter pelo menos dois estudantes válidos para "
                "sortear uma dupla."
            )
        elif st.button("Sortear dupla", type="primary", use_container_width=True):
            st.session_state.dupla_sorteada = random.sample(estudantes, 2)

        if st.session_state.dupla_sorteada:
            exibir_resultado(st.session_state.dupla_sorteada)

st.markdown(
    '<div class="app-footer">Tech Case • Fundamentos e Manutenção de Computadores</div>',
    unsafe_allow_html=True,
)