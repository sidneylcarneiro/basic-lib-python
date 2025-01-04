#pip install tzdata
from datetime import datetime, timedelta

import zoneinfo

hoje = datetime.now()
print("data completa:", hoje)
input()

#imprime todas as zonas disponiveis
#print(zoneinfo.available_timezones())

zona = zoneinfo.ZoneInfo("Portugal")
agora_portugal = hoje.astimezone(zona)

print(agora_portugal)
input()
