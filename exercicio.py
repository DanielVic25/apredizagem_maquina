livros = (1, "Inperfeitos - Christina Lauren", 
          2, "Arte da Guerra - garnie", 
          3, "o garoto do lago -  Charlie Donlea")
print(livros)

class Livro:
    def __init__(self, id, titulo, autor, disponibilidade = True):
        self.id = id 
        self.titulo = titulo
        self.autor = autor
        self.disponibilidade = disponibilidade

        def __str__(self):
            s = "Disponivel" if self.disp else "Emprestado"
            return f"{self.id}: {self.titulo}: ({self.autor}) - {s}"

class Usuario:
    def __init__(self, id, nome, matricula):
        self.id = id
        self.nome = nome
        self.matricula = matricula
        self.livro = []

class  biblioteca:
    def __init__(self):
        self.livros = []
        self.usuarios = []

    def adicionar_livro(self, titulo):
        Livro = Livro(titulo)
        self.livros.append(Livro)

    def adicionar_usuario(self, nome):
        usuario = Usuario(nome)
        self.usuarios.append(usuario)

    def emprestar_livro(self, nome_usuario, titulo_livro):
        for usuario in self.usuarios:
            if usuario.nome == nome_usuario:
                if len(usuario.livros) >= 3:
                    print("Esse usuário já pegou 3 livros.")
                    return
                
                for livro in self.livros:
                    if livro.titulo == titulo_livro and not livro.emprestimo:
                        livro.emprestimo = True
                        usuario.livros.append(livro)
                        print(f"{titulo_livro} foi emprestado para {nome_usuario}.")
                        return

                print("Livro não disponível.")
                return
        print("Usuário não encontrado.")

    def listar_livros_disponiveis(self):
        print("Livros disponíveis:")
        for livro in self.livros:
            if not livro.emprestado:
                print(f"- {livro.titulo}")

    def listar_livros_emprestados(self):
        print("Livros emprestados:")
        for livro in self.livros:
            if livro.emprestado:
                print(f"- {livro.titulo}")

    def listar_livros_do_usuario(self, nome_usuario):
        for usuario in self.usuarios:
            if usuario.nome == nome_usuario:
                print(f"Livros de {nome_usuario}:")
                for livro in usuario.livros:
                    print(f"- {livro.titulo}")
                return
        print("Usuário não encontrado.")


        