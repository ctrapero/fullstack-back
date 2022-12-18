from flask import Flask, request, redirect
import persistencia

app = Flask(__name__, template_folder=".")

@app.route('/pizza', methods=['POST'])
def pizza():
  data = request.form.get("datos1")
  data2 = request.form.get("datos2")
  
  persistencia.guardar_pedido(nombre=data, apellidos=data2)
  print(f"{data} {data2}")
  
  return redirect("http://localhost/solicita_pedido.html", code=302)
        
if __name__ == "__main__":
    app.run(host='127.0.0.1', port=5000, debug=True)

