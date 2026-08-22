salario_bruto = float (input("ingrese su salario bruto :"))
porcentaje = float (input("ingrese el porcentaje :"))
deducciones = float (input("ingrese la deduccion :"))
impuesto = salario_bruto* (porcentaje / 100)
salario_neto = salario_bruto-impuesto-deducciones
print (f"su salario neto es de  : " , salario_neto) 