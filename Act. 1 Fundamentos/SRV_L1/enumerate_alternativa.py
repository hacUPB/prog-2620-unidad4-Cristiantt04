etapas = ["despegue", "ascenso", "crucero"]

# Aquí le decimos que empiece en 1 directamente
for i, etapa in enumerate(etapas, start=1):
    print(f"Etapa {i}: {etapa}")