# Tech Case | Sorteio de Duplas

Aplicação web simples para que professores carreguem uma lista de estudantes e
sorteiem aleatoriamente uma dupla para mediar uma atividade Tech Case.

## Requisitos

- Python 3.12 ou superior
- `pip`

As dependências da aplicação estão no arquivo `requirements.txt`.

## Formato esperado do CSV

O arquivo deve conter uma lista de estudantes, preferencialmente em uma coluna
chamada `nome`. Também são aceitas as colunas `aluno` e `estudante`. Se nenhuma
delas existir, a primeira coluna será utilizada.

Arquivos separados por vírgula ou ponto e vírgula são aceitos. Linhas vazias e
nomes duplicados são ignorados.

Exemplo:

```csv
nome
Ana Souza
Bruno Lima
```

## Execução local

```bash
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
streamlit run app.py
```

No Windows, ative o ambiente virtual com `.venv\\Scripts\\activate`.

## Execução no GitHub Codespaces

Abra este repositório em um Codespace e execute:

```bash
streamlit run app.py
```

A porta 8501 será encaminhada automaticamente e o preview do Streamlit poderá
ser aberto pelo Codespaces.

## Estrutura do projeto

```text
tech-case-sorteio/
├── app.py
├── requirements.txt
├── README.md
├── .gitignore
├── .devcontainer/
│   └── devcontainer.json
└── exemplos/
	└── alunos.csv
```

## Ideias para futuras funcionalidades

- Impedir a repetição de estudantes até que todos tenham participado.
- Manter histórico das duplas sorteadas.
- Permitir sorteios individuais ou de grupos.
- Cadastrar várias turmas e associar o sorteio a um tema.
- Marcar estudantes ausentes.
- Exportar o histórico e persistir os dados.
- Adicionar um painel de configurações.
