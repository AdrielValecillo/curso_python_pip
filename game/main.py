import random

def obtener_opcion_usuario():
    while True:
        opcion = input("Elige Piedra, Papel o Tijeras: ").strip().lower()
        if opcion in ["piedra", "papel", "tijeras"]:
            return opcion
        else:
            print("Opción no válida. Por favor, elige Piedra, Papel o Tijeras.")

def obtener_opcion_maquina():
    opciones = ["piedra", "papel", "tijeras"]
    return random.choice(opciones)

def determinar_ganador(opcion_usuario, opcion_maquina):
    if opcion_usuario == opcion_maquina:
        return "Empate"
    if (
        (opcion_usuario == "piedra" and opcion_maquina == "tijeras") or
        (opcion_usuario == "papel" and opcion_maquina == "piedra") or
        (opcion_usuario == "tijeras" and opcion_maquina == "papel")
    ):
        return "¡Ganaste!"
    return "¡La máquina gana!"

def jugar_piedra_papel_tijeras():
    print("Bienvenido al juego de Piedra, Papel o Tijeras.")
    while True:
        usuario = obtener_opcion_usuario()
        maquina = obtener_opcion_maquina()

        print(f"Tú elegiste: {usuario}")
        print(f"La máquina eligió: {maquina}")

        resultado = determinar_ganador(usuario, maquina)
        print(resultado)

        jugar_otra_vez = input("¿Quieres jugar de nuevo? (s/n): ").strip().lower()
        if jugar_otra_vez != "s":
            break

if __name__ == "__main__":
    jugar_piedra_papel_tijeras()
