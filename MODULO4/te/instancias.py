from te import Te

te_1 = Te()
te_2 = Te()

tipo_1 = type(te_1)
tipo_2 = type(te_2)


if(tipo_1 == tipo_2):
    print('Ambos tecitos son del mismo tipo objeto')
else:
    print('Lamentablemente los tecitos no son el mismo tipo de objeto')