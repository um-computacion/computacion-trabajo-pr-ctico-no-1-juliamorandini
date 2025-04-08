def decimal_to_roman(decimal):
    valores = [1000, 900, 500, 400, 100, 90, 50, 40, 10, 9, 5, 4, 1]
    simbolos = ["M", "CM", "D", "CD", "C", "XC", "L", "XL", "X", "IX", "V", "IV", "I"]
    resultado = "" #inica cadena vacia para que cuando almacene los datos no haya nada
    for i in range(len(valores)):
        while decimal >= valores[i]: #mientras el decimal sea mayor o igual a los valores
            resultado += simbolos[i] #almacena el simbolo en la cadena resultado
            decimal -= valores[i] #resta el valor al decimal
    print(resultado)
    return resultado