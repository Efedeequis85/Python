import subprocess

try:
  # El metodo run ejecuta el comando que recibe como elementos separados en una lista
  result = subprocess.run(['mkdir', 'testdir'], text=True)
  print("Comando ejecutado exitosamente.")

except subprocess.CalledProcessError as e:
  print(f"Error al crear el directorio.")
