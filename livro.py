def filtrar_livros(livros, criterios):
    resultado = livros # retorna a lista de livros que serão filtradas

    for chave, valor in criterios.items():
        livros_filtrados = []
        for livro in resultado:
            if livro.get(chave) == valor:
                livros_filtrados.append(livro)
        resultado = livros_filtrados
    return resultado
