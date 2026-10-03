import requests

SITIOS = {
    "GitHub": "https://github.com/{}",
    "GitLab": "https://gitlab.com/{}",
    "Reddit": "https://www.reddit.com/user/{}",
}


def comprobar_usuario(username):
    resultados = {}

    for sitio, url in SITIOS.items():
        direccion = url.format(username)

        try:
            respuesta = requests.get(
                direccion,
                timeout=5,
                headers={
                    "User-Agent": "OSINT-Educational-Bot/1.0"
                }
            )

            resultados[sitio] = (
                respuesta.status_code == 200
            )

        except requests.RequestException:
            resultados[sitio] = False

    return resultados


def main():
    print("=" * 40)
    print("       OSINT SECURITY BOT")
    print("=" * 40)

    username = input("\nUsuario a investigar: ")

    if not username.strip():
        print("Debes introducir un usuario.")
        return

    print(f"\n🔎 Buscando información pública sobre: {username}\n")

    resultados = comprobar_usuario(username)

    for sitio, encontrado in resultados.items():
        if encontrado:
            print(f"🟢 {sitio}: encontrado")
        else:
            print(f"🔴 {sitio}: no encontrado")


if __name__ == "__main__":
    main()
