import requests

SITIOS = {
    "GitHub": "https://github.com/{}",
    "GitLab": "https://gitlab.com/{}",
    "Reddit": "https://www.reddit.com/user/{}/",
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

            resultados[sitio] = {
                "encontrado": respuesta.status_code == 200,
                "url": direccion
            }

        except requests.RequestException:
            resultados[sitio] = {
                "encontrado": False,
                "url": direccion
            }

    return resultados


def main():
    print("=" * 40)
    print("       OSINT SECURITY BOT")
    print("=" * 40)

    username = input("\nUsuario a investigar: ").strip()

    if not username:
        print("Debes introducir un usuario.")
        return

    print(f"\n🔎 Buscando información pública sobre: {username}\n")

    resultados = comprobar_usuario(username)

    for sitio, datos in resultados.items():
        if datos["encontrado"]:
            print(f"🟢 {sitio}: encontrado")
            print(f"   🔗 {datos['url']}\n")
        else:
            print(f"🔴 {sitio}: no encontrado\n")


if __name__ == "__main__":
    main()
