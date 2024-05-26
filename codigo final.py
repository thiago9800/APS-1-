import random
import sympy

def mdc(n1, n2):
    while n2 != 0:
        r = n1 % n2
        n1 = n2
        n2 = r
    return n1

def gerar_chave_publica(y):
    while True:
        x = random.randrange(2, y)
        if mdc(y, x) == 1:
            return x

def gerar_chave_privada(y, cpu):
    cpr = 1
    while True:
        if (cpu * cpr) % y == 1:
            return cpr
        cpr += 1

def cifrar(mensagem, cpu, n):
    msg_cifrada = []
    for letra in mensagem:
        k = (ord(letra) ** cpu) % n
        msg_cifrada.append(k)
    return msg_cifrada

def decifrar(mensagem, cpr, n):
    msg_decifrada = ""
    for k in mensagem:
        letra = (k ** cpr) % n
        msg_decifrada += chr(letra)
    return msg_decifrada

def rsa(bits):
    while True:
        p = sympy.randprime(2 ** (bits // 2 - 1), 2 ** (bits // 2))
        q = sympy.randprime(2 ** (bits // 2 - 1), 2 ** (bits // 2))
        n = p * q
        y = (p - 1) * (q - 1)
        
        if n.bit_length() == bits:
            cpu = gerar_chave_publica(y)
            cpr = gerar_chave_privada(y, cpu)
            return n, cpu, cpr

def criptografar(msg, n, cpu):
    msg = cifrar(msg, cpu, n)
    print("Mensagem cifrada: " + " ".join(map(str, msg)))

def descriptografar(msg, n, cpr):
    msg = msg.split() #pega a frase criptografada e a trasforma em uma lista de cracteres separando cada item pelo espaço
    msg = [int(x) for x in msg] #trasforma a lista de cracteres em uma lista de numeros inteiros 
    msg = decifrar(msg, cpr, n)
    print("Mensagem decifrada: " + msg)

bits_chave = 8 # Tamanho da chave em bits
n, cpu, cpr = rsa(bits_chave)

while True:
    fim = 1
    print("Selecione uma opção:")
    print("1- criptografar uma mensagem")
    print("2- descriptografar uma mensagem")
    print("0- Fechar o programa")

    print()
    escolha = input("Digite o número da opção desejada: ")
    print()


    match escolha:
        case '1':
            criptografar(input("Digite a frase que você quer criptografar: "), n, cpu)
            print()
        case '2':
            descriptografar(input("Digite a cifra que você quer descriptografar: "), n, cpr)
            print()
        case '0':
            print("Fechando o programa...")
            break
        case _:
            print("Opção inválida. Tente novamente.")
            print()
            fim = 0

    if fim == 1:
        print("Voltar ao menu?")
        print("1- Para Sim")
        print("2- Para Não")
        con = int(input())
        print()

        if con != 1:
            print("Fechando o programa...")
            print()
            break
