import pdfkit

# Guarda el HTML en un archivo
html_content = '''
<!DOCTYPE html>
<html lang="es">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Reporte Diario de Ventas</title>
    <style>
        body {
            font-family: Arial, sans-serif;
            margin: 20px;
        }
        h1 {
            text-align: center;
            color: #333;
        }
        table {
            width: 100%;
            border-collapse: collapse;
            margin-bottom: 20px;
        }
        th, td {
            padding: 10px;
            border: 1px solid #ddd;
            text-align: left;
        }
        th {
            background-color: #f8f8f8;
            color: #333;
        }
    </style>
</head>
<body>
    <h1>Reporte Diario de Ventas</h1>
    <table>
        <thead>
            <tr>
                <th>Fecha</th>
                <th>Hora</th>
                <th>Nombre del Alumno</th>
                <th>Producto</th>
                <th>Precio</th>
                <th>Empleado</th>
            </tr>
        </thead>
        <tbody>
            <tr>
                <td>31/05/2024</td>
                <td>10:00 AM</td>
                <td>Juan Pérez</td>
                <td>Sandwich</td>
                <td>$2000</td>
                <td>Ana López</td>
            </tr>
            <tr>
                <td>31/05/2024</td>
                <td>10:15 AM</td>
                <td>María Gómez</td>
                <td>Jugo</td>
                <td>$4500</td>
                <td>José Díaz</td>
            </tr>
             <tr>
                <td>31/05/2024</td>
                <td>10:15 AM</td>
                <td>Juan Almeida</td>
                <td>doritos</td>
                <td>$4500</td>
                <td>José Díaz</td>
            </tr>
             <tr>
                <td>31/05/2024</td>
                <td>10:15 AM</td>
                <td>María Gómez</td>
                <td>pastel pollo</td>
                <td>$3500</td>
                <td>José Díaz</td>
            </tr>
             <tr>
                <td>31/05/2024</td>
                <td>10:15 AM</td>
                <td>Salomon Barrera</td>
                <td>Coca Cola</td>
                <td>$4500</td>
                <td>José Díaz</td>
            </tr>
        </tbody>
    </table>
</body>
</html>
'''

with open('report.html', 'w') as file:
    file.write(html_content)

# Convertir HTML a PDF
pdfkit.from_file('report.html', 'report.pdf')