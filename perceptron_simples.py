def ativacao_degrau(z):
    if z >= 0:
        return 1
    return 0

def decidir_upgrade(x1, x2):
    # Parâmetros definidos manualmente
    w1 = 0.8      # Peso para dias hospedados
    w2 = 0.3      # Peso para gasto total
    bias = -7.0   # Resistência natural para conceder o upgrade

    # Cálculo linear (z)
    z = (x1 * w1) + (x2 * w2) + bias

    # Aplicação da ativação
    decisao = ativacao_degrau(z)
    return decisao

# Validação com cenários de teste
print("Hóspede com dias=8, gasto=7:", decidir_upgrade(8, 7)) # Esperado: 1
print("Hóspede com dias=4, gasto=3:", decidir_upgrade(4, 3)) # Esperado: 0

def ativacao_degrau(z):
    if z >= 0:
        return 1
    return 0

def prever(entradas, pesos, bias):
    # Cálculo linear (z = x1*w1 + x2*w2 + ... + bias) usando listas e loop for
    z = bias
    for i in range(len(entradas)):
        z += entradas[i] * pesos[i]

    decisao = ativacao_degrau(z)
    return decisao, z

if __name__ == "__main__":
    pesos_modelo = [0.8, 0.3]
    bias_modelo = -7.0

    # Cenário de teste (entradas correspondentes a dias hospedados e gasto total)
    cenarios = [
        {"nome": "Ana", "entradas": [8, 7.0]},
        {"nome": "Pedro", "entradas": [4, 3.0]}
    ]

    for c in cenarios:
        resultado, valor_z = prever(c["entradas"], pesos_modelo, bias_modelo)
        status = "Upgrade Concedido!" if resultado == 1 else "Upgrade Negado."
        print(f"Hóspede: {c['nome']:5} | Entradas: {c['entradas']} -> Z: {valor_z:5.2f} | Decisão: {status}")