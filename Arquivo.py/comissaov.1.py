func = 'marcelo'
func = 'jefferson'
func = 'tais'
func ='rodrigo'
func = 'leandro'


login = 'Comissao'
senha = 'vencedores'
soma = 0
total = 0
p_Piso = 1.188

login = str(input("Informe o login de acesso: "))
senha = str(input("Digite a senha: "))
if login != 'Comissao' and senha != 'vecendores':
    print("Seja bem vindo(a)! ao Sistema de calculo de comissões")
    
else:
    exit()

while (True):
    func = str(input("Digite sua seu nome: "))   
    print("Solicito que todos os valores que estão sendo inseridos sejam colocados com o (.) e não com (,) certo? ")
        # Consultora_de_Serviços = Tais
    if func == "tais":
        print("Vamos lá Thais função: CONSULTORA DE SERVIÕS calcular os seus ganhos!")
        print("Voce recebe o percentual de Serviços_Geral de 2,4% / Mercadoria_Balcão 2,0% / Mercadoria_Oficina 2,4% / Mercadoria_Atacado e Mercadoria _Garantia 1,2%")
        # Pegando todos os valores conforme o relatorio da empresa repassado dos seus determinados serviços
        mercadoria_Balcao = float(input("Qual o seu valor de mercadoria(Venda Balcão)R$: "))
        mercadoria_Oficina = float(input("Qual o seu valor de mercadoria(Venda Oficina)R$: "))
        mercadoria_Atacado = float(input("Qual o seu valor de mercadoria (Venda Atacado) R$: "))
        mercadoria_Garantia = float(input("Qual o seu valor de mercadoria(Garantia) R$: "))
        servico = float(input("Qual o seu valor de Serviços (Garantia,Revisão Gratuita, Outros)R$: "))
        ### Somandos os valores conforme os seus percetuais de servicos (valores) realizados
        desc1 = mercadoria_Balcao - (mercadoria_Balcao * 2.0/100)
        result1 = mercadoria_Balcao - desc1
        desc2 = mercadoria_Oficina - (mercadoria_Oficina * 2.4/100)
        result2 = mercadoria_Oficina - desc2
        desc3 = mercadoria_Atacado - (mercadoria_Atacado * 1.2/100)
        result3 = mercadoria_Atacado - desc3
        desc4 = mercadoria_Garantia - (mercadoria_Garantia * 1.2/100)
        result4 = mercadoria_Garantia - desc4
        desc5 = servico - (servico * 2.4/100)
        result5 = servico - desc5
        print("Mercadoria_Balcão:{:.3f} / Mercadoria_Oficina:{:.3f} / Mercadoria_Atacado:{:.3f} / Mercadoria_Garantia:{:.3f} /Serviço:{:.3f}".format(result1,result2,result3,result4,result5))
        soma = result1 + result2 + result3 + result4 + result5 
        total  = soma + (soma * 20/100)
        print(func, "Seu salário ficou da seguinte forma R${:.3f} + 20% do dsr ficou no total de R${:.3f}".format(soma,total))

        # Vendedor_de_Peças: Rodrigo
    if func == "rodrigo":
        print("Vamos lá Rodrigo função: VENDENDOR DE PEÇAS calcular os seus ganhos!")
        print("Voce recebe o percentual de Serviços_Geral de 2,4% / Mercadoria_Balcão 2,4% / Mercadoria_Oficina 2,0% / Mercadoria_Atacado e Mercadoria _Garantia 1,2%")
        # Pegando todos os valores conforme o relatorio da empresa repassado dos seus determinados serviços
        mercadoria_Balcao = float(input("Qual o seu valor de mercadoria(Venda Balcão)R$: "))
        mercadoria_Oficina = float(input("Qual o seu valor de mercadoria(Venda Oficina)R$: "))
        mercadoria_Atacado = float(input("Qual o seu valor de mercadoria (Venda Atacado) R$: "))
        mercadoria_Garantia = float(input("Qual o seu valor de mercadoria(Garantia) R$: "))
        servico = float(input("Qual o seu valor de Serviços (Garantia,Revisão Gratuita, Outros)R$: "))
        ### Somandos os valores conforme os seus percetuais de servicos (valores) realizados
        desc1 = mercadoria_Balcao - (mercadoria_Balcao * 2.4/100)
        result1 = mercadoria_Balcao - desc1
        desc2 = mercadoria_Oficina - (mercadoria_Oficina * 2.0/100)
        result2 = mercadoria_Oficina - desc2
        desc3 = mercadoria_Atacado - (mercadoria_Atacado * 1.2/100)
        result3 = mercadoria_Atacado - desc3
        desc4 = mercadoria_Garantia - (mercadoria_Garantia * 1.2/100)
        result4 = mercadoria_Garantia - desc4
        desc5 = servico - (servico * 2.4/100)
        result5 = servico - desc5
        print("Mercadoria_Balcão:{:.3f} / Mercadoria_Oficina:{:.3f} / Mercadoria_Atacado:{:.3f} / Mercadoria_Garantia:{:.3f} /Serviço:{:.3f}".format(result1,result2,result3,result4,result5))
        soma = result1 + result2 + result3 + result4 + result5 
        total  = soma + (soma * 20/100)
        print(func,"Seu salário ficou da seguinte forma R${:.3f} + 20% do dsr ficou no total de R${:.3f}".format(soma,total))

        # Aux.Mecânico: Jefferson
    if func == "jefferson":
        print("Vamos lá Jefferson função: AUX.MECÂNICO calcular os seus ganhos!")
        print("Voce recebe o percentual de Serviços_Geral de 7.0% / Mercadoria_Oficina 1.5% / Mercadoria_Garantia 1.5%")
        # Pegando todos os valores conforme o relatorio da empresa repassado dos seus determinados serviços
        mercadoria_Oficina = float(input("Qual o seu valor de mercadoria(Venda Oficina)R$: "))
        mercadoria_Garantia = float(input("Qual o seu valor de mercadoria(Garantia) R$: "))
        servico = float(input("Qual o seu valor de Serviços (Garantia,Revisão Gratuita, Outros)R$: "))
        ### Somandos os valores conforme os seus percetuais de servicos (valores) realizados
        desc1 = mercadoria_Oficina - (mercadoria_Oficina * 1.5/100)
        result1 = mercadoria_Oficina - desc1
        desc2 = mercadoria_Garantia - (mercadoria_Garantia * 1.5/100)
        result2 = mercadoria_Garantia - desc2
        desc3 = servico - (servico * 7.0/100)
        result3 = servico - desc3
        print("Mercadoria_Oficina:{:.3f} / Mercadoria_Garantia:{:.3f} /Serviço:{:.3f}".format(result1,result2,result3,))
        soma = result1 + result2 + result3
        total  = soma + (soma * 20/100)
        print(func,"Seu salário ficou da seguinte forma R${:.3f} + 20% do dsr ficou no total de R${:.3f}".format(soma,total))

        # Mecânico: Marcelo
    if func == "Marcelo":
        print("Vamos lá Marcelo função: MECÂNICO calcular os seus ganhos!")
        print("Voce recebe o percentual de Serviços_Geral de 10.0% / Mercadoria_Oficina 2.0% / Mercadoria_Garantia 2.0%")
        # Pegando todos os valores conforme o relatorio da empresa repassado dos seus determinados serviços
        mercadoria_Oficina = float(input("Qual o seu valor de mercadoria(Venda Oficina)R$: "))
        mercadoria_Garantia = float(input("Qual o seu valor de mercadoria(Garantia) R$: "))
        servico = float(input("Qual o seu valor de Serviços (Garantia,Revisão Gratuita, Outros)R$: "))
        ### Somandos os valores conforme os seus percetuais de servicos (valores) realizados
        desc1 = mercadoria_Oficina - (mercadoria_Oficina * 2.0/100)
        result1 = mercadoria_Oficina - desc1
        desc2 = mercadoria_Garantia - (mercadoria_Garantia * 2.0/100)
        result2 = mercadoria_Garantia - desc2
        desc3 = servico - (servico * 7.0/100)
        result3 = servico - desc3
        print("Mercadoria_Oficina:{:.3f} / Mercadoria_Garantia:{:.3f} /Serviço:{:.3f}".format(result1,result2,result3,))
        soma = result1 + result2 + result3
        total  = soma + (soma * 20/100)
        print(func,"Seu salário ficou da seguinte forma R${:.3f} + 20% do dsr ficou no total de R${:.3f}".format(soma,total))

        # Mecânico de Diagnóstico: Leandro
    if func == "leandro":
        print("Vamos lá Leandro função: MECÂNICO DE DIAGNÓSTICO calcular os seus ganhos!")
        print("Voce recebe o percentual de Serviços_de_Garantia de 15.0% / Serviço_Revisão_Gratuita e outros 10.0% / Mercadoria_Oficina 2.5% / Mercadoria_Garantia 2.5%")
        # Pegando todos os valores conforme o relatorio da empresa repassado dos seus determinados serviços
        mercadoria_Oficina = float(input("Qual o seu valor de mercadoria(Venda Oficina)R$: "))
        mercadoria_Garantia = float(input("Qual o seu valor de mercadoria(Garantia) R$: "))
        servicog = float(input("qual o seu valor de servico(em Garantia) R$: "))
        servico = float(input("Qual o seu valor de Serviços (Revisão Gratuita e outros)R$: "))
        ### Somandos os valores conforme os seus percetuais de servicos realizados
        desc1 = mercadoria_Oficina - (mercadoria_Oficina * 2.5/100)
        result1 = mercadoria_Oficina - desc1
        desc2 = mercadoria_Garantia - (mercadoria_Garantia * 2.5/100)
        result2 = mercadoria_Garantia - desc2
        desc3 = servicog - (servicog * 15.0/100)
        result3 = servicog - desc3
        desc4 = servico - (servico * 10.0/100)
        result4 = servico - desc4
        print("Mercadoria_Oficina:{:.3f} / Mercadoria_Garantia:{:.3f} / Serviço_Garantia:{:.3f} /Serviço:{:.3f}".format(result1,result2,result3,result4))
        soma = result1 + result2 + result3 + result4
        total  = soma + (soma * 20/100)
        print(func,"Seu salário ficou da seguinte forma R${:.3f} + 20% do dsr ficou no total de R${:.3f}".format(soma,total))
        # Condicional si o valor for maior que o salario de 1.188.
    if soma >= p_Piso:
        # Se o funcionario(a) ultrpassar o limite do piso salario de R$ 1.188 será mostrado essa mensagem logo abaixo.
        print("Parabéns você passou do piso salarial de R$ 1.188, Continue buscando sempre elevar os seus numeros.")
        print("Gostou vamos alavancar esse mês que vem novamente? CONTO COM VOCÊ!!! :)")
    else:
        # Mensagem de insetivo para que o funcionario(a) continue buscando atigir suas metas.
        print("EU ACREDITO EM VOCÊ,",func,"vamos próximo mês aumentar esses numeros e ter boas remunerações!")
    # Informando logo abaixo o fim do execultável do programa
    print("Fim")
    # Mostrando o autor(a) da criação do Sistema. 
    print("""Sistema criado por Adalberto Fernandes todos os direitos Reservados 2022""")
    print("---------------------------------------------------------------------------------------------------------------------------------------------------------------------")
    break


