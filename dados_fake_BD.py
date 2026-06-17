import pyodbc
from faker import Faker
import random

# ==========================================
# CONEXÃO SQL SERVER
# ==========================================

conexao = pyodbc.connect(
    'DRIVER={ODBC Driver 17 for SQL Server};'
    'SERVER=localhost;'
    'DATABASE=BI_VENDAS;'
    'Trusted_Connection=yes;'
)

cursor = conexao.cursor()

fake = Faker('pt_BR')

print("Conectado ao SQL Server!")

# ==========================================
# LIMPAR TABELAS
# ==========================================

print("Limpando tabelas...")

cursor.execute("DELETE FROM Fato_Devolucao")
cursor.execute("DELETE FROM Fato_Estoque")
cursor.execute("DELETE FROM Meta_Vendedor")
cursor.execute("DELETE FROM Fato_Vendas")

cursor.execute("DELETE FROM Dim_Produto")
cursor.execute("DELETE FROM Dim_Cliente")
cursor.execute("DELETE FROM Dim_Vendedor")
cursor.execute("DELETE FROM Dim_Regiao")
cursor.execute("DELETE FROM Dim_Tempo")
cursor.execute("DELETE FROM Dim_CategoriaProduto")

conexao.commit()

print("Tabelas limpas!")

# ==========================================
# INSERIR CATEGORIAS
# ==========================================

print("Inserindo categorias...")

categorias = [
    'Eletrônicos',
    'Informática',
    'Celulares',
    'Periféricos',
    'Acessórios'
]

for categoria in categorias:

    cursor.execute("""
        INSERT INTO Dim_CategoriaProduto (
            nome_categoria
        )
        VALUES (?)
    """, categoria)

conexao.commit()

print("Categorias inseridas!")

# ==========================================
# BUSCAR IDS DAS CATEGORIAS
# ==========================================

cursor.execute("""
    SELECT id_categoria
    FROM Dim_CategoriaProduto
""")

categorias_ids = [
    x[0]
    for x in cursor.fetchall()
]

# ==========================================
# INSERIR PRODUTOS
# ==========================================

print("Inserindo produtos...")

marcas = [
    'Samsung',
    'Apple',
    'LG',
    'Dell',
    'Lenovo',
    'Asus'
]

for i in range(100):

    nome = fake.word()

    marca = random.choice(marcas)

    preco_custo = round(
        random.uniform(100, 3000), 2
    )

    preco_venda = round(
        preco_custo * 1.4, 2
    )

    categoria = random.choice(categorias_ids)

    cursor.execute("""
        INSERT INTO Dim_Produto (
            nome_produto,
            marca,
            preco_custo,
            preco_venda,
            id_categoria
        )
        VALUES (?, ?, ?, ?, ?)
    """,
    nome,
    marca,
    preco_custo,
    preco_venda,
    categoria)

conexao.commit()

print("Produtos inseridos!")

# ==========================================
# INSERIR CLIENTES
# ==========================================

print("Inserindo clientes...")

for i in range(500):

    nome_cliente = fake.name()

    sexo = random.choice(['M', 'F'])

    idade = random.randint(18, 70)

    cidade = fake.city()

    estado = fake.estado_sigla()

    renda = round(
        random.uniform(1500, 25000), 2
    )

    cursor.execute("""
        INSERT INTO Dim_Cliente (
            nome_cliente,
            sexo,
            idade,
            cidade,
            estado,
            renda_mensal
        )
        VALUES (?, ?, ?, ?, ?, ?)
    """,
    nome_cliente,
    sexo,
    idade,
    cidade,
    estado,
    renda)

conexao.commit()

print("Clientes inseridos!")

# ==========================================
# INSERIR VENDEDORES
# ==========================================

print("Inserindo vendedores...")

equipes = [
    'Equipe Norte',
    'Equipe Sul',
    'Equipe Comercial',
    'Equipe Enterprise'
]

cargos = [
    'Vendedor',
    'Consultor',
    'Executivo de Contas'
]

for i in range(20):

    nome_vendedor = fake.name()

    equipe = random.choice(equipes)

    cargo = random.choice(cargos)

    meta = round(
        random.uniform(50000, 300000), 2
    )

    cursor.execute("""
        INSERT INTO Dim_Vendedor (
            nome_vendedor,
            equipe,
            cargo,
            meta_mensal
        )
        VALUES (?, ?, ?, ?)
    """,
    nome_vendedor,
    equipe,
    cargo,
    meta)

conexao.commit()

print("Vendedores inseridos!")

# ==========================================
# BUSCAR IDS DOS VENDEDORES
# ==========================================

cursor.execute("""
    SELECT id_vendedor
    FROM Dim_Vendedor
""")

vendedores_ids = [
    x[0]
    for x in cursor.fetchall()
]

# ==========================================
# INSERIR METAS DOS VENDEDORES
# ==========================================

print("Inserindo metas...")

for vendedor in vendedores_ids:

    for mes in range(1, 13):

        valor_meta = round(
            random.uniform(80000, 300000), 2
        )

        percentual_bonus = round(
            random.uniform(5, 20), 2
        )

        cursor.execute("""
            INSERT INTO Meta_Vendedor (
                id_vendedor,
                ano,
                mes,
                valor_meta,
                percentual_bonus
            )
            VALUES (?, ?, ?, ?, ?)
        """,
        vendedor,
        2025,
        mes,
        valor_meta,
        percentual_bonus)

conexao.commit()

print("Metas inseridas!")

# ==========================================
# INSERIR REGIÕES
# ==========================================

print("Inserindo regiões...")

regioes = [
    ('Sudeste', 'RJ', 'Brasil'),
    ('Sudeste', 'SP', 'Brasil'),
    ('Sul', 'PR', 'Brasil'),
    ('Sul', 'SC', 'Brasil'),
    ('Nordeste', 'BA', 'Brasil'),
    ('Nordeste', 'PE', 'Brasil'),
    ('Centro-Oeste', 'GO', 'Brasil'),
    ('Norte', 'AM', 'Brasil'),
    ('Sudeste', 'MG', 'Brasil'),
    ('Sul', 'RS', 'Brasil')
]

for regiao in regioes:

    cursor.execute("""
        INSERT INTO Dim_Regiao (
            nome_regiao,
            estado,
            pais
        )
        VALUES (?, ?, ?)
    """,
    regiao[0],
    regiao[1],
    regiao[2])

conexao.commit()

print("Regiões inseridas!")

# ==========================================
# INSERIR DATAS
# ==========================================

print("Inserindo datas...")

for mes in range(1, 13):

    id_tempo = int(f"2025{mes:02}01")

    nome_mes = [
        'Janeiro',
        'Fevereiro',
        'Março',
        'Abril',
        'Maio',
        'Junho',
        'Julho',
        'Agosto',
        'Setembro',
        'Outubro',
        'Novembro',
        'Dezembro'
    ][mes - 1]

    trimestre = ((mes - 1) // 3) + 1

    cursor.execute("""
        INSERT INTO Dim_Tempo (
            id_tempo,
            data_completa,
            dia,
            mes,
            nome_mes,
            trimestre,
            ano,
            dia_semana
        )
        VALUES (?, ?, ?, ?, ?, ?, ?, ?)
    """,
    id_tempo,
    f'2025-{mes:02}-01',
    1,
    mes,
    nome_mes,
    trimestre,
    2025,
    'Segunda-feira')

conexao.commit()

print("Datas inseridas!")

# ==========================================
# BUSCAR IDS
# ==========================================

print("Carregando IDs...")

cursor.execute("SELECT id_produto FROM Dim_Produto")
produtos = [x[0] for x in cursor.fetchall()]

cursor.execute("SELECT id_cliente FROM Dim_Cliente")
clientes = [x[0] for x in cursor.fetchall()]

cursor.execute("SELECT id_vendedor FROM Dim_Vendedor")
vendedores = [x[0] for x in cursor.fetchall()]

cursor.execute("SELECT id_regiao FROM Dim_Regiao")
regioes_ids = [x[0] for x in cursor.fetchall()]

cursor.execute("SELECT id_tempo FROM Dim_Tempo")
tempos = [x[0] for x in cursor.fetchall()]

print("IDs carregados!")

# ==========================================
# INSERIR ESTOQUE
# ==========================================

print("Inserindo estoque...")

for produto in produtos:

    for tempo in tempos:

        quantidade = random.randint(50, 1000)

        estoque_minimo = random.randint(10, 50)

        estoque_maximo = random.randint(1000, 5000)

        custo_estoque = round(
            quantidade * random.uniform(50, 3000), 2
        )

        cursor.execute("""
            INSERT INTO Fato_Estoque (
                id_produto,
                id_tempo,
                quantidade_estoque,
                estoque_minimo,
                estoque_maximo,
                custo_estoque
            )
            VALUES (?, ?, ?, ?, ?, ?)
        """,
        produto,
        tempo,
        quantidade,
        estoque_minimo,
        estoque_maximo,
        custo_estoque)

conexao.commit()

print("Estoque inserido!")

# ==========================================
# INSERIR VENDAS
# ==========================================

print("Inserindo vendas...")

for i in range(10000):

    produto = random.choice(produtos)

    cliente = random.choice(clientes)

    vendedor = random.choice(vendedores)

    regiao = random.choice(regioes_ids)

    tempo = random.choice(tempos)

    quantidade = random.randint(1, 10)

    valor_unitario = round(
        random.uniform(50, 5000), 2
    )

    valor_total = round(
        quantidade * valor_unitario, 2
    )

    desconto = round(
        valor_total * random.uniform(0, 0.1), 2
    )

    lucro = round(
        valor_total * random.uniform(0.15, 0.4), 2
    )

    cursor.execute("""
        INSERT INTO Fato_Vendas (
            id_produto,
            id_cliente,
            id_vendedor,
            id_regiao,
            id_tempo,
            quantidade,
            valor_unitario,
            valor_total,
            desconto,
            lucro
        )
        VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
    """,
    produto,
    cliente,
    vendedor,
    regiao,
    tempo,
    quantidade,
    valor_unitario,
    valor_total,
    desconto,
    lucro)

conexao.commit()

print("Vendas inseridas!")

# ==========================================
# BUSCAR IDS DAS VENDAS
# ==========================================

cursor.execute("""
    SELECT TOP 1000
        id_venda,
        id_produto,
        id_cliente,
        id_tempo
    FROM Fato_Vendas
""")

vendas = cursor.fetchall()

# ==========================================
# INSERIR DEVOLUÇÕES
# ==========================================

print("Inserindo devoluções...")

motivos = [
    'Produto com defeito',
    'Cliente desistiu',
    'Produto errado',
    'Atraso na entrega',
    'Embalagem danificada'
]

for venda in vendas:

    if random.random() < 0.1:

        quantidade = random.randint(1, 3)

        valor_devolvido = round(
            random.uniform(100, 5000), 2
        )

        cursor.execute("""
            INSERT INTO Fato_Devolucao (
                id_venda,
                id_produto,
                id_cliente,
                id_tempo,
                motivo_devolucao,
                quantidade,
                valor_devolvido
            )
            VALUES (?, ?, ?, ?, ?, ?, ?)
        """,
        venda.id_venda,
        venda.id_produto,
        venda.id_cliente,
        venda.id_tempo,
        random.choice(motivos),
        quantidade,
        valor_devolvido)

conexao.commit()

print("Devoluções inseridas!")

# ==========================================
# FINALIZAR
# ==========================================

cursor.close()

conexao.close()

print("Processo finalizado com sucesso!")