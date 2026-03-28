from livro import filtrar_livros
from bd import livros_disponiveis

def test_filtrar_livros_lista_vazia(): # Primeiro teste desenvolvido (histórico)
    criterios_filtro = {}
    resultado = filtrar_livros(livros=[], criterios=criterios_filtro)
    assert resultado == [] # deve ser uma lista vazia

def test_filtrar_livros_genero():
    criterios_filtro = {"genero": "Romance"} # Atenção aos critérios
    resultado = filtrar_livros(livros=livros_disponiveis, criterios=criterios_filtro)
    assert resultado == [
        {"titulo": "Dom Casmurro", "autor": "Machado de Assis", "genero": "Romance", "preco": 29.90,
         "data_publicacao": "1899"},
        {"titulo": "Memórias Póstumas", "autor": "Machado de Assis", "genero": "Romance", "preco": 24.90,
         "data_publicacao": "1881"},
        {"titulo": "Orgulho e Preconceito", "autor": "Jane Austen", "genero": "Romance", "preco": 34.90,
         "data_publicacao": "1813"},
    ] # espera-se o retorno desses três livros do nosso "banco"

def test_filtrar_livros_autor():
    criterios_filtro = {"autor": "Machado de Assis"} # Atenção ao critério
    resultado = filtrar_livros(livros=livros_disponiveis, criterios=criterios_filtro)
    assert resultado == [
        {"titulo": "Dom Casmurro", "autor": "Machado de Assis", "genero": "Romance", "preco": 29.90,
         "data_publicacao": "1899"},
        {"titulo": "Memórias Póstumas", "autor": "Machado de Assis", "genero": "Romance", "preco": 24.90,
         "data_publicacao": "1881"},
    ]

def test_filtrar_livros_inexistentes():
    generos_existentes = []
    for genero in livros_disponiveis: # Pegando todos os gêneros do BD mockado
        generos_existentes.append(genero["genero"])

    genero_inexistente = "Terror"
    while genero_inexistente in generos_existentes:
        genero_inexistente += "_inexistente" # a ideia é garantir que o gênero teste nunca coincida com o gênero real, caso houver atualização do BD.

    criterios_filtro = {"genero": genero_inexistente}
    resultado = filtrar_livros(livros=livros_disponiveis, criterios=criterios_filtro)
    assert resultado == []

def test_filtrar_livros_retorna_informacao_completa():
    criterios_filtro = {"titulo": "O Hobbit"}
    resultado = filtrar_livros(livros=livros_disponiveis, criterios=criterios_filtro)
    # Exibir livros no terminal
    print("\nLivros encontrados:")
    for livro in resultado:
        print(f"  Título:           {livro['titulo']}")
        print(f"  Autor:            {livro['autor']}")
        print(f"  Género:           {livro['genero']}")
        print(f"  Preço:            R$ {livro['preco']:.2f}")
        print(f"  Data publicação:  {livro['data_publicacao']}")
        print()
    assert resultado == [
        {"titulo": "O Hobbit", "autor": "J.R.R. Tolkien", "genero": "Fantasia", "preco": 49.90, "data_publicacao": "1937"},
    ]
