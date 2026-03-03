'''
CRUD

AÇAI
'''




print('\n === sistema de açaiteria ===\n')


print("\n===🧊açaiteria🧊===")

print("1 .cadastro dos clientes")
print("2. cardapio da loja" )
print("3. pedidos")
print("4. chat da loja de açai")
print("0. ajuda")


while True:

 escolha_menu = input("escolher opção do açai: ")
 if escolha_menu == '1':
  

     print("Agendando cliente...")
     nome_cliente  = input("digite o nome do cliente: ")
     telefone_cliente = input("Digite o telefone do cliente: ")
     #codigo para agendar cliente


 elif escolha_menu == '0':
 
    print("saindo do sistema Ate logo!")
    break
 

 else:
    print("opção invalida. Por favor, tente novamente.")