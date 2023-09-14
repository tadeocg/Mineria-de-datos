import pandas as pd

def eliminar_columnas():

    df = pd.read_csv('playlist.csv')

    columnas_a_eliminar = ['track_add_date', 'track_add_time', 'multiple_artists_bool', 'album_release_date_precision', 'position_in_playlist', 'track_explicit', 'images_path', 'data_collection_date']

    df = df.drop(columnas_a_eliminar, axis=1)

    df.to_csv('playlist limpio.csv', index=False)

    print("Columnas eliminadas y archivo guardado como 'archivo_modificado.csv'")

def validacion():

    df = pd.read_csv('playlist limpio.csv')

    if df.isnull().values.any():
        print("El archivo CSV contiene valores nulos.")

    columna_duplicada = 'album_name'
    if df.duplicated(subset=[columna_duplicada]).any():
        print(f"El archivo CSV contiene valores duplicados en la columna '{columna_duplicada}'.")

    print("La validación de datos del archivo CSV ha sido exitosa.")

if __name__ == "__main__":
    opcion = input("Elije una opción (1 o 2): ")

    if opcion == "1":
        eliminar_columnas()
    elif opcion == "2":
        validacion()
    else:
        print("Opción no válida")


