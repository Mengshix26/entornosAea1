import unittest
import os
from libreria import Libreria


class TestLibreria(unittest.TestCase):
    
    def setUp(self):
        """Configura un nuevo objeto Libreria antes de cada prueba."""
        self.libreria = Libreria()
        self.libreria.anadir_libro("El coronel no tiene quien le escriba", "Gabriel García Márquez", "Novela", 1961)
        
    def tearDown(self):
        """Elimina el archivo de prueba 'libreria.json' después de cada prueba si existe."""
        if os.path.exists('libreria.json'):
            os.remove('libreria.json')
    
    def test_anadir_libro(self):
        """Prueba la adición de un libro a la libreria."""
        resultado = self.libreria.anadir_libro("El Quijote", "Miguel de Cervantes", "Novela", 1605)
        self.assertEqual(resultado, "Libro añadido")  # Verifica que el libro se añadió correctamente
        self.assertEqual(len(self.libreria.libros), 2)
    
    def test_buscar_libro(self):
        """Prueba la búsqueda de un libro por su título."""
        self.libreria.anadir_libro("El principito", "Antoine de Saint-Exupéry", "Novela", 1943)
        resultado = self.libreria.buscar_libro("El principito")
        self.assertEqual(len(resultado), 1)
        self.assertEqual(resultado[0]['titulo'], "El principito")
        
    def test_buscar_por_autor(self):
        """Prueba la búsqueda de un libro por su autor."""
        resultado = self.libreria.buscar_por_autor("Gabriel García Márquez")
        self.assertEqual(len(resultado), 1)
        
    def test_eliminar_libro(self):
        """Prueba la eliminación de un libro de la libreria."""
        resultado = self.libreria.eliminar_libro("El coronel no tiene quien le escriba")
        self.assertEqual(resultado, "Libro eliminado") # Verifica que el libro es eliminado
        resultado = self.libreria.eliminar_libro("AAAAAAAA")
        self.assertEqual(resultado, "Libro no encontrado") # Verifica que el libro no es encontrado
        
    def test_guardar_y_cargar_libros(self):
        """Prueba si se guarda y se carga los libros de la librería de manera correcta"""
        archivo = 'test_libreria.json'
        self.libreria.guardar_libros(archivo)
        nueva_libreria = Libreria()
        resultado = nueva_libreria.cargar_libros(archivo)
        self.assertEqual(resultado, "Libros cargados")
        self.assertEqual(len(nueva_libreria.libros), 1)
        os.remove(archivo)  # Limpiar archivo de prueba
    
    def test_cargar_libros_archivo_no_encontrado(self):
        resultado = self.libreria.cargar_libros("archivo_inexistente.json")
        self.assertEqual(resultado, "Archivo no encontrado")

if __name__ == '__main__':
    unittest.main()