n = int(input())
classname = {"Algorithm":	204,"DataAnalysis":	207,
"ArtificialIntelligence" :302,
"CyberSecurity" :	"B101",
"Network" :	303,
"Startup" :	501,
"TestStrategy":	105}

semina = []
for _ in range(n):
    semina.append(input())
for s in semina:
    print(classname[s])