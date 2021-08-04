def analisaConsumo(modelos,consumo):
    var = consumo[0]
    for kml in consumo:
        if kml > var:
            var = kml
    
    print("Modelo mais econômico: " + modelos[consumo.index(var)])
    print("Consumo: " + str(var) + "Km/l")
    
    print(" ")
    
    print("Consumo de gasolina para 1000Km:")
    print("--------------------------------")
    for gas in consumo:
        print("Modelo: " + modelos[consumo.index(gas)])
        print("Vol. gas: " + str(1000/gas) + " [litros]")
        print("-----")
        
modelos = ['Cruiser', 'Roadster', 'Scrambler', 'Custom'] 
consumo = [14, 13, 17, 12] # Km/l

analisaConsumo(modelos, consumo)
