"""
- Constante = "variaveis que não vão mudar
- Muitas condições if (ruim)
"""
velocidade = 60
local_carro = 99

radar_1 = 60    # velocidade maxima do radar 1.
local_1 = 100   # local onde o 1 radar está.
radar_range = 1 # a distancia onde o radar pega.

carro_acima_da_velocidade = velocidade > radar_1
carro_em_zona_de_multa_1 = local_carro ==  (local_1 + radar_range)
carro_em_zona_de_multa_2 = local_carro == (local_1 - radar_range)

if carro_acima_da_velocidade and carro_em_zona_de_multa_1 :
    print("carro multado")
elif carro_acima_da_velocidade and carro_em_zona_de_multa_2 :
    print("carro multado")
else:
    print("carro passou pelo radar na velocidade permitida")
    