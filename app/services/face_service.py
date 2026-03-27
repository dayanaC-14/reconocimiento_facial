import face_recognition

def analizar_rostro(ruta_imagen):
    
    # 1. Cargar imagen
    imagen = face_recognition.load_image_file(ruta_imagen)
    
    # 2. Detectar puntos del rostro (ojos, nariz, etc.)
    landmarks = face_recognition.face_landmarks(imagen)

    # 3. Validar si detectó rostro
    if not landmarks:
        return {"error": "No se detectó ningún rostro"}

    # 4. Simulación de análisis (luego se mejora)
    tipo_rostro = "ovalado"
    recomendacion = "Montura rectangular"

    # 5. Retornar resultado
    return {
        "tipo_rostro": tipo_rostro,
        "recomendacion": recomendacion
    }