# Protótipo Python (simplificado)
from datetime import datetime, timedelta

inicio_prazo = datetime(2023, 9, 14)  # ex.: intimação
dias_uteis = 10

# Função (com feriados e fins de semana, usando biblioteca workalendar)
prazo_final = calcula_prazo(inicio_prazo, dias_uteis)

print(f"Prazo final: {prazo_final.strftime('%d/%m/%Y')}")
