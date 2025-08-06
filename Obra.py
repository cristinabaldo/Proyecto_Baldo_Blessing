class Obra():
    def __init__(self, titulo, nombre_artista, nacionalidad_artista, fecha_nacimiento, fecha_muerte, tipo, anio_creacion, imagen_url):
        self.titulo = titulo
        self.nombre_artista = nombre_artista
        self.nacionalidad_artista = nacionalidad_artista
        self.fecha_nacimiento = fecha_nacimiento
        self.fecha_muerte = fecha_muerte
        self.tipo = tipo
        self.anio_creacion = anio_creacion
        self.imagen_url = imagen_url

    def show(self):
        print(f"Título: {self.titulo}")
        print(f"Artista: {self.nombre_artista}")
        print(f"Nacionalidad: {self.nacionalidad_artista}")
        print(f"Nacimiento: {self.fecha_nacimiento}")
        print(f"Muerte: {self.fecha_muerte}")
        print(f"Tipo: {self.tipo}")
        print(f"Año de creación: {self.anio_creacion}")
        print(f"Imagen: {self.imagen_url}")
        print("")
        
