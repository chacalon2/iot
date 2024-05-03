pandas openpyx.
import pandas as pd from flask import Flask
app-Flask(name
base-pd.read excel ("Base1.xlsx")
fapp:router（"/）
def
principal()=
return "Esta app te enseña que modelo de auto es mejor"
@app.router(por nombre de cada auto/<Nombre de los autos>")
def pornombredeautos(nombredelauto):
numero=int(Numero):
fila-base[base[ "Nombre del auto"]==Nombredelauto]
respuesta-f"El Nombre es  {Nombredelauto} es (fila. lec/e, "Honbre"|1"
return respuesta
@app, router(* /Por_tipo de motor/<topodemotor>")
def tipodemotor(motor):
resultados=base[base["motor"]==motor]
resultadose str (resultados)
return resultados
@app. router ("/Por_Autonomia/<Autonomia>")
def porAutonomia(autonomia):
resultado=base[base["autonimia"]==autonomia]
resultado= str (resultado)
retur resultado
