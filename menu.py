import fontes.requisita_menu as req
import fontes.classifica_menu as cla

print("Insira '1' para fazer as requisições, '2' para classificações e 'q' para sair:")
entrada = input("(1 = requisição; 2 = classificação; q = sair): ")

verifica = 0

if (entrada == '1'):
    verifica = 1
    req.executa()
    print("\nGostaria de fazer a classificação?:")
    outra = input("(s = sim): ")
    if (outra == 's'):
        cla.executa()


if (entrada == '2'):
    verifica = 1
    cla.executa()

if (entrada == 'q'):
    exit()

while (verifica == 0):
    print("Digite uma entrada válida.")
    entrada = input("(1 = requisição; 2 = classificação; q = sair): ")

    if (entrada == '1'):
        verifica = 1
        req.executa()
        print("\nGostaria de fazer a classificação?:")
        outra = input("(s = sim): ")
        if (outra == 's'):
            cla.executa()

    if (entrada == '2'):
        verifica = 1
        cla.executa()

    if (entrada == 'q'):
        verifica = 1
        exit()
