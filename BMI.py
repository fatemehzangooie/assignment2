a=float(input("vazn ra bar hasb kg vared konid: "))
b=float(input("ghad ra bar hasb metr vared konid: "))
BMI=(a/(b*b))
if 16<BMI<18.5:
    print("shoma kambood vazn darid. lotfan moragheb barname ghazaietoon bashid")
elif 18.5<BMI<24:
    print("vazn shoma normal ast. varzesh faramoosh nashavad.")
elif 24<BMI<30:
    print("vazn shoma ziad ast! varzesh konid va barnameh ghazaie monaseb dashteh bashid!")
elif 30<BMI<35:
    print("shoma daraye ezafe vazn hastid. moragheb ravand ghazatoon bashid va bishtar varzesh konid!")
elif BMI>40:
    print("shoma chagh hastid. hatman ba doctor taghzieh mashverat konid!")
    