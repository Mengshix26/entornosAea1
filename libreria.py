import json

class Libreria:
    """
    Clase para genestionar una libreria virtual.
    
    Atributos:
        libros (list): Lista de libros en la libreria.
    """
    
    
    def __init__(self):
        """Inicializa una libreria sin libros."""
        self.libros = []


    def anadir_libro(self, titulo, autor, genero, anio):
        """
        Añade un libro a la libreria.
        
        Args:
            titulo (str): Título del libro.
            autor (str): Autor del libro.
            genero (str): Género del libro.
            anio (int): Año de publicación del libro.
            
        Returns:
            str: Mensaje que confirma que se añadió el libro.
        """
        self.libros.append({'titulo': titulo, 'autor': autor, 'genero': genero, 'anio': anio})
        return "Libro añadido"


    def buscar_libro(self, titulo):
        """
        Busca un libro por su título.
        
        Args:
            titulo (str): Título del libro a buscar.
            
        Returns:
            list: Lista de libros que coinciden con el título buscado.
        """
        return [libro for libro in self.libros if libro['titulo'].lower() == titulo.lower()]


    def buscar_por_autor(self, autor):
        """
        Busca libros por el nombre del autor.

        Args:
            autor (str): Nombre del autor del libro buscado.

        Returns:
            list: Lista de libros escritos por el autor.
        """
        return [libro for libro in self.libros if autor.lower() in libro['autor'].lower()]


    def eliminar_libro(self, titulo):
        """
        Elimina libros de la libreria por el título.
        
        Se compara el número de libros que había al principio con la cantidad que hay
        después de filtrar para verificar si un libro es eliminado o no encontrado.

        Args:
            titulo (str): Título del libro a eliminar.

        Returns:
            str: Mensaje deconfirmación de que el libro es eliminado.
        """
        original_count = len(self.libros)
        self.libros = [libro for libro in self.libros if libro['titulo'].lower() != titulo.lower()]
        return "Libro eliminado" if len(self.libros) < original_count else "Libro no encontrado"


    def guardar_libros(self, archivo):
        """
        Guarda los libros de la libreria en un archivo JSON.

        Args:
            archivo (str): Nombre del archivo donde se guardarán los libros.

        Returns:
            str: Mensaje de confirmación.
        """
        with open(archivo, 'w') as f:
            json.dump(self.libros, f)
        return "Libros guardados"


    def cargar_libros(self, archivo):
        """
        Carga los libros desde un archivo JSON a la libreria.

        Args:
            archivo (str): Nombre del archivo desde donde se cargarán los libros.

        Returns:
            str: Mensaje de confirmación, si no es encontrado salta el mensaje de 
                 archivo no encontrado.
        """
        try:
            with open(archivo, 'r') as f:
                self.libros = json.load(f)
            return "Libros cargados"
        except FileNotFoundError:
            return "Archivo no encontrado"


mi_libreria = Libreria()
mi_libreria.anadir_libro("Cien años de soledad", "Gabriel García Márquez", "Novela", 1967)
mi_libreria.guardar_libros('libreria.json')
print(mi_libreria.cargar_libros('libreria.json'))
print(mi_libreria.buscar_por_autor("Gabriel García Márquez"))