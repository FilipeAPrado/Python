class Produto:
    idProduto = None
    descricao = None
    custo = None
    def __init__(self, idProduto,descricao,custo):
        self.idProduto = idProduto
        self.descricao = descricao
        self.custo = custo
        

class AlbumMusica(Produto):
    artista = None
    nomeAlbum = None
    faixaExecucao = None
    def __init__(self, artista,nomeAlbum,faixaExecucao,idProduto,descricao,custo):
        self.artista = artista
        self.nomeAlbum = nomeAlbum
        self.faixaExecucao = faixaExecucao
        super(AlbumMusica,self).__init__(idProduto,descricao,custo) 
        

class Livro(Produto):
    autor = None
    titulo = None
    isbn = None
    def __init__(self, autor,titulo,isbn,idProduto,descricao,custo):
        self.autor = autor
        self.titulo = titulo
        self.isbn = isbn
        super(Livro,self).__init__(idProduto,descricao,custo)     
        
        
alice = Livro('bonequito','Alice','45487518946',35,'infantil',35.00)  