from medida import Medida

try:
    print("--------------------------------------------------------------------------------")
    print("|                             Conversor de medidas                             |")
    print("|                                                                              |")
    print("|Por favor, selecione uma das opções abaixo:                                   |")
    print("|                                                                              |")
    print("|Digite 1 para converter um valor de  milhas para km,m,cm,ft e in.             |")
    print("|Digite 2 para converter um valor de  polegadas para km,m,cm,ft e mi.          |")
    print("|Digite 3 para converter um valor de  pes para km,m,cm,mi e in.                |")
    print("|Digite 4 para converter um valor de  quilometros para cm,m,mi,ft e in.        |")
    print("|Digite 5 para converter um valor de  centimetros para km,mi,m,ft e in.            |")
    print("|Digite 6 para converter um valor de  metros para mi,km,cm,ft e pl.        |")
    print("|Digite 7 para encerrar o programa.                                            |")
    print("|                                                                              |")
    print("--------------------------------------------------------------------------------")
    opcao = int(input("digite uma poção: "))
    if opcao == 1:
        while opcao == 1:
            print("--------------------------------------------------------------------------------")
            print("|                             Medidas em Milha                                 |")
            print("|                                                                              |")
            print("|Por favor, selecione uma das opções abaixo:                                   |")
            print("|                                                                              |")
            print("|Digite 1 para converter um valor de  milhas para pes(km).                     |")
            print("|Digite 2 para converter um valor de  milhas para polegadas(km).               |")
            print("|Digite 3 para converter um valor de  milhas para quilometros(km).             |")
            print("|Digite 4 para converter um valor de  milhas para centimetros:(cm).            |")
            print("|Digite 5 para converter um valor de  milhas para metros(m).                   |")
            print("|Digite 6 para encerrar o programa.                                            |")
            print("|                                                                              |")
            print("--------------------------------------------------------------------------------")
            milhas = float(input("insira uma opção: "))
            if milhas == 1:
                valor = int(input("insira um valor: "))
                medida = Medida(valor,0,0,0,0,0)
                print(f"O seu valor foi convertido para {medida.get_milhas_in(valor)} in")
                break
            if milhas == 2:
                valor = int(input("insira um valor: "))
                medida = Medida(valor,0,0,0,0,0)
                print(f"O seu valor foi convertido para {medida.get_milhas_ft(valor)} ft")
                break
            if milhas == 3:
                valor = int(input("insira um valor: "))
                medida = Medida(valor,0,0,0,0,0)
                print(f"O seu valor foi convertido para {medida.get_milhas_km(valor)} km")
                break
            if milhas == 4:
                valor = int(input("insira um valor: "))
                medida = Medida(valor,0,0,0,0,0)
                print(f"O seu valor foi convertido para {medida.get_milhas_cm(valor)} cm")
                break
            if milhas == 5:
                valor = int(input("insira um valor: "))
                medida = Medida(valor,0,0,0,0,0)
                print(f"O seu valor foi convertido para {medida.get_milhas_m(valor)} m")
                break
            if milhas == 6:
                print("--------------------------------------------------------------------------------")
                print("|                                                                              |")
                print("|                             Programa finalizado                              |")
                print("|                                                                              |")
                print("--------------------------------------------------------------------------------")
                break
    if opcao == 2:
        while opcao == 2:
            print("--------------------------------------------------------------------------------")
            print("|                             Medidas em Polegadas                             |")
            print("|                                                                              |")
            print("|Por favor, selecione uma das opções abaixo:                                   |")
            print("|                                                                              |")
            print("|Digite 1 para converter um valor de  polegadas para milhas(mi).               |")
            print("|Digite 2 para converter um valor de  polegadas para pés(ft).                  |")
            print("|Digite 3 para converter um valor de  polegadas para quilometros(km).          |")
            print("|Digite 4 para converter um valor de  polegadas para centimetros:(cm).         |")
            print("|Digite 5 para converter um valor de  polegadas para metros(m).                |")
            print("|Digite 6 para encerrar o programa.                                            |")
            print("|                                                                              |")
            print("--------------------------------------------------------------------------------")
            milhas = float(input("insira uma opção: "))
            if milhas == 1:
                valor = int(input("insira um valor: "))
                medida = Medida(valor,0,0,0,0,0)
                print(f"O seu valor foi convertido para {medida.get_polegadas_mi(valor)} mi")
                break
            if milhas == 2:
                valor = int(input("insira um valor: "))
                medida = Medida(valor,0,0,0,0,0)
                print(f"O seu valor foi convertido para {medida.get_polegadas_ft(valor)} ft")
                break
            if milhas == 3:
                valor = int(input("insira um valor: "))
                medida = Medida(valor,0,0,0,0,0)
                print(f"O seu valor foi convertido para {medida.get_polegadas_km(valor)} km")
                break
            if milhas == 4:
                valor = int(input("insira um valor: "))
                medida = Medida(valor,0,0,0,0,0)
                print(f"O seu valor foi convertido para {medida.get_polegadas_cm(valor)} cm")
                break
            if milhas == 5:
                valor = int(input("insira um valor: "))
                medida = Medida(valor,0,0,0,0,0)
                print(f"O seu valor foi convertido para {medida.get_polegadas_m(valor)} m")
                break
            if milhas == 6:
                print("--------------------------------------------------------------------------------")
                print("|                                                                              |")
                print("|                             Programa finalizado                              |")
                print("|                                                                              |")
                print("--------------------------------------------------------------------------------")
                break
    if opcao == 3:
        while opcao == 3:
            print("--------------------------------------------------------------------------------")
            print("|                             Medidas em Pés                                   |")
            print("|                                                                              |")
            print("|Por favor, selecione uma das opções abaixo:                                   |")
            print("|                                                                              |")
            print("|Digite 1 para converter um valor de pés para milhas(mi).                      |")
            print("|Digite 1 para converter um valor de pés para polegadas(in).                   |")
            print("|Digite 1 para converter um valor de pés para quilometros(km).                 |")
            print("|Digite 2 para converter um valor de pés para centimetros:(cm).                |")
            print("|Digite 3 para converter um valor de pés para metros(m).                       |")
            print("|Digite 4 para encerrar o programa.                                            |")
            print("|                                                                              |")
            print("--------------------------------------------------------------------------------")
            milhas = float(input("insira uma opção: "))
            if milhas == 1:
                valor = int(input("insira um valor: "))
                medida = Medida(valor,0,0,0,0,0)
                print(f"O seu valor foi convertido para {medida.get_pe_mi(valor)} mi")
                break
            if milhas == 2:
                valor = int(input("insira um valor: "))
                medida = Medida(valor,0,0,0,0,0)
                print(f"O seu valor foi convertido para {medida.get_pe_in(valor)} in")
                break
            if milhas == 3:
                valor = int(input("insira um valor: "))
                medida = Medida(valor,0,0,0,0,0)
                print(f"O seu valor foi convertido para {medida.get_pe_km(valor)} km")
                break
            if milhas == 4:
                valor = int(input("insira um valor: "))
                medida = Medida(valor,0,0,0,0,0)
                print(f"O seu valor foi convertido para {medida.get_pe_cm(valor)} cm")
                break
            if milhas == 5:
                valor = int(input("insira um valor: "))
                medida = Medida(valor,0,0,0,0,0)
                print(f"O seu valor foi convertido para {medida.get_pe_m(valor)} m")
                break
            if milhas == 6:
                print("--------------------------------------------------------------------------------")
                print("|                                                                              |")
                print("|                             Programa finalizado                              |")
                print("|                                                                              |")
                print("--------------------------------------------------------------------------------")
                break
    if opcao == 4:
        while opcao == 4:
            print("--------------------------------------------------------------------------------")
            print("|                             Medidas em Quilometros                           |")
            print("|                                                                              |")
            print("|Por favor, selecione uma das opções abaixo:                                   |")
            print("|                                                                              |")
            print("|Digite 1 para converter um valor de quilometros para milhas(mi).              |")
            print("|Digite 2 para converter um valor de quilometros para polegadas(in).           |")
            print("|Digite 3 para converter um valor de quilometros para pés(ft).                 |")
            print("|Digite 4 para converter um valor de quilometros para centimetros:(cm).        |")
            print("|Digite 5 para converter um valor de quilometros para metros(m).               |")
            print("|Digite 6 para encerrar o programa.                                            |")
            print("|                                                                              |")
            print("--------------------------------------------------------------------------------")
            milhas = float(input("insira uma opção: "))
            if milhas == 1:
                valor = int(input("insira um valor: "))
                medida = Medida(valor,0,0,0,0,0)
                print(f"O seu valor foi convertido para {medida.get_quilometros_mi(valor)} mi")
                break
            if milhas == 2:
                valor = int(input("insira um valor: "))
                medida = Medida(valor,0,0,0,0,0)
                print(f"O seu valor foi convertido para {medida.get_quilometros_in(valor)} in")
                break
            if milhas == 3:
                valor = int(input("insira um valor: "))
                medida = Medida(valor,0,0,0,0,0)
                print(f"O seu valor foi convertido para {medida.get_quilometros_ft(valor)} ft")
                break
            if milhas == 4:
                valor = int(input("insira um valor: "))
                medida = Medida(valor,0,0,0,0,0)
                print(f"O seu valor foi convertido para {medida.get_quilometros_cm(valor)} cm")
                break
            if milhas == 5:
                valor = int(input("insira um valor: "))
                medida = Medida(valor,0,0,0,0,0)
                print(f"O seu valor foi convertido para {medida.get_quilometros_cm(valor)} m")
                break
            if milhas == 6:
                print("--------------------------------------------------------------------------------")
                print("|                                                                              |")
                print("|                             Programa finalizado                              |")
                print("|                                                                              |")
                print("--------------------------------------------------------------------------------")
                break
    if opcao == 5:
        while opcao == 5:
            print("--------------------------------------------------------------------------------")
            print("|                             Medidas em Centimetros                           |")
            print("|                                                                              |")
            print("|Por favor, selecione uma das opções abaixo:                                   |")
            print("|                                                                              |")
            print("|Digite 1 para converter um valor de quilometros para milhas(mi).              |")
            print("|Digite 2 para converter um valor de quilometros para polegadas(in).           |")
            print("|Digite 3 para converter um valor de quilometros para pes(ft).                 |")
            print("|Digite 4 para converter um valor de quilometros para centimetros:(cm).        |")
            print("|Digite 5 para converter um valor de quilometros para metros(m).               |")
            print("|Digite 6 para encerrar o programa.                                            |")
            print("|                                                                              |")
            print("--------------------------------------------------------------------------------")
            milhas = float(input("insira uma opção: "))
            if milhas == 1:
                valor = int(input("insira um valor: "))
                medida = Medida(valor,0,0,0,0,0)
                print(f"O seu valor foi convertido para {medida.get_centimetros_mi(valor)} mi")
                break
            if milhas == 2:
                valor = int(input("insira um valor: "))
                medida = Medida(valor,0,0,0,0,0)
                print(f"O seu valor foi convertido para {medida.get_centimetros_in(valor)} in")
                break
            if milhas == 3:
                valor = int(input("insira um valor: "))
                medida = Medida(valor,0,0,0,0,0)
                print(f"O seu valor foi convertido para {medida.get_centimetros_ft(valor)} ft")
                break
            if milhas == 4:
                valor = int(input("insira um valor: "))
                medida = Medida(valor,0,0,0,0,0)
                print(f"O seu valor foi convertido para {medida.get_centimetros_km(valor)} cm")
                break
            if milhas == 5:
                valor = int(input("insira um valor: "))
                medida = Medida(valor,0,0,0,0,0)
                print(f"O seu valor foi convertido para {medida.get_centimetros_m(valor)} m")
                break
            if milhas == 6:
                print("--------------------------------------------------------------------------------")
                print("|                                                                              |")
                print("|                             Programa finalizado                              |")
                print("|                                                                              |")
                print("--------------------------------------------------------------------------------")
                break
    if opcao == 6:
        while opcao == 6:
            print("--------------------------------------------------------------------------------")
            print("|                             Medidas em Metros                                |")
            print("|                                                                              |")
            print("|Por favor, selecione uma das opções abaixo:                                   |")
            print("|                                                                              |")
            print("|Digite 1 para converter um valor de metros para milhas(mi).                   |")
            print("|Digite 2 para converter um valor de metros para polegadas(in).                |")
            print("|Digite 3 para converter um valor de metros para pes(ft).                      |")
            print("|Digite 4 para converter um valor de metros para centimetros:(cm).             |")
            print("|Digite 5 para converter um valor de metros para quilometros(km).              |")
            print("|Digite 6 para encerrar o programa.                                            |")
            print("|                                                                              |")
            print("--------------------------------------------------------------------------------")
            milhas = float(input("insira uma opção: "))
            if milhas == 1:
                valor = int(input("insira um valor: "))
                medida = Medida(valor,0,0,0,0,0)
                print(f"O seu valor foi convertido para {medida.get_metros_mi(valor)} mi")
                break
            if milhas == 2:
                valor = int(input("insira um valor: "))
                medida = Medida(valor,0,0,0,0,0)
                print(f"O seu valor foi convertido para {medida.get_metros_in(valor)} in")
                break
            if milhas == 3:
                valor = int(input("insira um valor: "))
                medida = Medida(valor,0,0,0,0,0)
                print(f"O seu valor foi convertido para {medida.get_metros_ft(valor)} ft")
                break
            if milhas == 4:
                valor = int(input("insira um valor: "))
                medida = Medida(valor,0,0,0,0,0)
                print(f"O seu valor foi convertido para {medida.get_metros_km(valor)} cm")
                break
            if milhas == 5:
                valor = int(input("insira um valor: "))
                medida = Medida(valor,0,0,0,0,0)
                print(f"O seu valor foi convertido para {medida.get_metros_km(valor)} km")
                break
            if milhas == 6:
                print("--------------------------------------------------------------------------------")
                print("|                                                                              |")
                print("|                             Programa finalizado                              |")
                print("|                                                                              |")
                print("--------------------------------------------------------------------------------")
                break
    if opcao == 7:
        print("--------------------------------------------------------------------------------")
        print("|                                                                              |")
        print("|                             Programa finalizado                              |")
        print("|                                                                              |")
        print("--------------------------------------------------------------------------------")
except ValueError:
    print("Por favor insira um valor ou opção valida!")