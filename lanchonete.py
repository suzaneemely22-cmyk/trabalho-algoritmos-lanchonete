print("================================")
print("     LANCHONETE BURGER")
print("================================")

nome = input("Digite seu nome: ")

print()
print("Olá,", nome, "!")
print("Seja bem-vindo(a) à nossa lanchonete!")

print()
print("========== CARDÁPIO ==========")
print("1 - X-Burguer ........ R$ 15,00")
print("2 - X-Salada ......... R$ 18,00")
print("3 - Batata Frita .... R$ 10,00")
print("4 - Refrigerante ..... R$ 6,00")
print("5 - Suco ............. R$ 8,00")
print("0 - Finalizar pedido")
print("==============================")

opcao = int(input("Digite o código do produto: "))

if opcao == 1:
    produto = "X-Burguer"
    preco = 15.00
    codigo_valido = True

elif opcao == 2:
    produto = "X-Salada"
    preco = 18.00
    codigo_valido = True

elif opcao == 3:
    produto = "Batata Frita"
    preco = 10.00
    codigo_valido = True

elif opcao == 4:
    produto = "Refrigerante"
    preco = 6.00
    codigo_valido = True

elif opcao == 5:
    produto = "Suco"
    preco = 8.00
    codigo_valido = True

else:
    print("Código inválido.")
    codigo_valido = False


if codigo_valido:
    quantidade = int(input("Digite a quantidade desejada: "))

    subtotal = preco * quantidade

    print()
    print("Produto:", produto)
    print("Preço unitário: R$", preco)
    print("Quantidade:", quantidade)
    print("Subtotal: R$", subtotal)
    
