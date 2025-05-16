import time
from concurrent.futures import ThreadPoolExecutor, ProcessPoolExecutor

# 🔹 Función que verifica si un número es primo
def es_primo(n):
    if n < 2:
        return False
    for i in range(2, int(n**0.5)+1):
        if n % i == 0:
            return False
    return True

# 🔹 Función CPU-intensiva
def contar_primos(hasta):
    total = sum(1 for i in range(2, hasta) if es_primo(i))
    return f"Primos hasta {hasta}: {total}"

# 🔹 Función para ejecutar cualquier método con medición de tiempo
def ejecutar_metodo(nombre, funcion_ejecutora, rangos):
    print(f"\n🔸 {nombre}")
    inicio = time.time()
    resultados = funcion_ejecutora(rangos)
    for r in resultados:
        print(r)
    print(f"⏱ Tiempo total ({nombre}): {time.time() - inicio:.2f} segundos")

# 🔹 Función para ejecución lineal
def ejecucion_lineal(rangos):
    return [contar_primos(r) for r in rangos]

# 🔹 Función para ejecución con hilos
def ejecucion_threadpool(rangos):
    with ThreadPoolExecutor(max_workers=len(rangos)) as executor:
        return list(executor.map(contar_primos, rangos))

# 🔹 Función para ejecución con procesos
def ejecucion_processpool(rangos):
    with ProcessPoolExecutor(max_workers=len(rangos)) as executor:
        return list(executor.map(contar_primos, rangos))

# 🔹 Punto de entrada principal
def main():
    rangos = [50000, 51000, 52000, 53000, 54000, 55000]

    ejecutar_metodo("Ejecución lineal", ejecucion_lineal, rangos)
    ejecutar_metodo("ThreadPoolExecutor", ejecucion_threadpool, rangos)
    ejecutar_metodo("ProcessPoolExecutor", ejecucion_processpool, rangos)

if __name__ == "__main__":
    main()
