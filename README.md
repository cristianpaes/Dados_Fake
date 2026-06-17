# 📊 Projeto BI Vendas - Data Warehouse Completo com SQL Server + Python

## 🚀 Sobre o Projeto

Este projeto simula um ambiente corporativo de Business Intelligence utilizando arquitetura dimensional (Star Schema) em SQL Server.

O objetivo é gerar uma base de dados realista para análises de vendas, estoque, metas comerciais e devoluções, permitindo a criação de dashboards em Power BI, consultas SQL analíticas e estudos de Data Warehouse.

Os dados são gerados automaticamente através de Python utilizando a biblioteca Faker.

---

## 🏗 Arquitetura do Projeto

### Tabelas Dimensão

- Dim_Cliente
- Dim_Produto
- Dim_Vendedor
- Dim_Regiao
- Dim_Tempo
- Dim_CategoriaProduto

### Tabelas Fato

- Fato_Vendas
- Fato_Estoque
- Fato_Devolucao
- Meta_Vendedor

---

## 🛠 Tecnologias Utilizadas

- Python
- SQL Server
- PyODBC
- Faker
- Data Warehouse
- Modelagem Dimensional
- ETL


---

## 📌 Funcionalidades

### Geração automática de dados

O script cria:

✔ 100 Produtos

✔ 500 Clientes

✔ 20 Vendedores

✔ 10 Regiões

✔ 12 Meses

✔ 10.000 Vendas

✔ Controle de Estoque

✔ Metas Comerciais

✔ Devoluções de Produtos

---

## 📈 Indicadores que podem ser analisados

### Comercial

- Faturamento Total
- Ticket Médio
- Lucro por Produto
- Lucro por Região
- Ranking de Vendedores
- Metas x Realizado

### Clientes

- Clientes por Estado
- Faixa Etária
- Renda Média
- Perfil de Consumo

### Estoque

- Giro de Estoque
- Produtos com Baixo Estoque
- Valor Financeiro em Estoque

### Devoluções

- Taxa de Devolução
- Principais Motivos
- Impacto Financeiro

---

## 🔄 Fluxo do Processo

```text
Python
   ↓
Geração de Dados Fake
   ↓
Carga SQL Server
   ↓
Data Warehouse
   ↓
Consultas SQL
   ↓
Power BI
```

---

## 📂 Estrutura do Projeto

```text
BI_VENDAS/
│
├── scripts/
│   ├── carga_dados.py
│
├── sql/
│   ├── criacao_tabelas.sql
│   ├── consultas_analiticas.sql
│
├── dashboard/
│   ├── dashboard_powerbi.pbix
│
└── README.md
```

---

## ▶ Como Executar

### Instalar dependências

```bash
pip install pyodbc faker
```

### Configurar conexão SQL Server

```python
conexao = pyodbc.connect(
    'DRIVER={ODBC Driver 17 for SQL Server};'
    'SERVER=localhost;'
    'DATABASE=BI_VENDAS;'
    'Trusted_Connection=yes;'
)
```

### Executar o script

```bash
python carga_dados.py
```

---

## 🎯 Objetivos Técnicos Demonstrados

Este projeto demonstra experiência em:

- Administração SQL Server
- Criação de Data Warehouse
- Modelagem Star Schema
- ETL com Python
- Geração Massiva de Dados
- Consultas Analíticas
- Business Intelligence
- Preparação de Dados para Power BI
- Automação de Carga de Dados

---

## 👨‍💻 Autor

### Cristian Camargo

Profissional de TI com mais de 28 anos de experiência atuando com:

- SQL Server
- Administração de Bancos de Dados
- ERP Sankhya
- Business Intelligence
- Análise de Dados
- Desenvolvimento Backend
- Infraestrutura e Segurança

### Conecte-se comigo

LinkedIn: https://www.linkedin.com/in/cristiancamargo

---

⭐ Se este projeto foi útil, deixe uma estrela no repositório.
