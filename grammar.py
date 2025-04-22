import sys
from Lexic_ import lexer

def main():
    if len(sys.argv) != 2:
        print("Uso: python lexer_only.py MiLenguaje.compi")
        sys.exit(1)

    archivo = sys.argv[1]
    try:
        with open(archivo, 'r', encoding='utf-8') as f:
            data = f.read()
    except FileNotFoundError:
        print(f"No se encontró el archivo: {archivo}")
        sys.exit(1)

    # Alimentamos el contenido al lexer
    lexer.input(data)

    print(f"Tokens encontrados en '{archivo}':\n")
    for tok in lexer:
        print(f"{tok.type:20}  {tok.value!r}   (línea {tok.lineno})")

if __name__ == "__main__":
    main()
