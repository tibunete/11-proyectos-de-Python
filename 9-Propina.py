total_bill = float(input("Ingrese total de la factura: "))

tip_18_percent = total_bill * 0.18
tip_20_percent = total_bill * 0.20
tip_25_percent = total_bill * 0.25

print(f"Propina del 18%: ${tip_18_percent:.2f}")
print(f"Propina del 20%: ${tip_20_percent:.2f}")
print(f"Propina del 25%: ${tip_25_percent:.2f}")
