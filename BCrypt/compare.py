import bcrypt

# Contraseña en texto plano
password = "MiPassword123"

# Convertir a bytes
password_bytes = password.encode("utf-8")

# Generar salt y hash, 12 rondas para mayor seguridad
salt = bcrypt.gensalt(rounds=12)

hash_guardado = bcrypt.hashpw(password_bytes, salt)


print("Hash generado:",hash_guardado.decode())


hash_comprobacion = bcrypt.hashpw(password_bytes, bcrypt.gensalt())

print("Hash de comprobación:", hash_comprobacion.decode())

if hash_guardado == hash_comprobacion:
    print("Los hashes son iguales (esto no debería suceder).")
else:
    print("Los hashes son diferentes (esto es lo esperado).")


# Verificar la contraseña
if bcrypt.checkpw(password_bytes, hash_guardado):
    print("¡Contraseña correcta!")
else:
    print("Contraseña incorrecta.")

# Aunque el hash de comprobación es diferente, bcrypt.checkpw debería devolver True si la contraseña es correcta
if bcrypt.checkpw(password_bytes, hash_comprobacion):
    print("¡Contraseña correcta con hash de comprobación!")
else:
    print("Contraseña incorrecta con hash de comprobación.")