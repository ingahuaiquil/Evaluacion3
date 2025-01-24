from flask import Flask, render_template, request

app = Flask(__name__)

#locahost
@app.route('/')
def index():
    return render_template('index.html')

#enrutamiento
@app.route('/ejercicio1', methods=['GET', 'POST'])

def ejercicio1():
    resultado = ""
    promedio = 0

    if request.method == 'POST':
        try:
            # Obtener datos
            nota1 = float(request.form['nota1'])
            nota2 = float(request.form['nota2'])
            nota3 = float(request.form['nota3'])
            asistencia = float(request.form['asistencia'])

            # Validar notas rango de 0 a 7
            if not (0 <= nota1 <= 7) or not (0 <= nota2 <= 7) or not (0 <= nota3 <= 7):
                resultado = "Por favor, ingrese notas válidas entre 0 y 7."
            # Validar asistencia entre 0 y 100
            elif not (0 <= asistencia <= 100):
                resultado = "Por favor, ingrese un porcentaje de asistencia válido (entre 0 y 100)."
            else:
                # Promedio de notas
                promedio = (nota1 + nota2 + nota3) / 3

                # Determinar aprobado o reprobado
                if promedio >= 4 and asistencia >= 50:
                    resultado = "APROBADO"
                else:
                    resultado = "REPROBADO"
        except ValueError:
            resultado = "Por favor, ingrese valores numéricos válidos."

    return render_template('ejercicio1.html', promedio=promedio, resultado=resultado)


@app.route('/ejercicio2', methods=['GET', 'POST'])
def ejercicio2():
    mensaje = ""
    nombres_mas_largos = []

    if request.method == 'POST':
        nombre1 = request.form['nombre1'].strip()
        nombre2 = request.form['nombre2'].strip()
        nombre3 = request.form['nombre3'].strip()

        # Validar que todos los nombres sean distintos y contengan solo letras
        if not all(nombre.isalpha() for nombre in [nombre1, nombre2, nombre3]):
            mensaje = "Por favor, ingrese solo nombres válidos (sin números ni caracteres especiales)."
        elif len({nombre1, nombre2, nombre3}) < 3:
            mensaje = "Por favor, ingrese 3 nombres distintos."
        else:
            # Encontrar el/los nombres con mayor número de caracteres
            max_length = max(len(nombre1), len(nombre2), len(nombre3))
            nombres_mas_largos = [nombre for nombre in [nombre1, nombre2, nombre3] if len(nombre) == max_length]

    return render_template('ejercicio2.html', mensaje=mensaje, nombres_mas_largos=nombres_mas_largos)


if __name__ == '__main__':
    app.run(debug=True)