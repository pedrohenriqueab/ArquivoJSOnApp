import json
def main(args=[]):
    while True:
        try:
            f = open("contatos.txt", encoding="utf8")

            jsonObjs = json.load(f)
            print(jsonObjs)

            break

        except FileNotFoundError:
            print("Arquivo não encontrado")

if __name__ == '__main__':
    main()
