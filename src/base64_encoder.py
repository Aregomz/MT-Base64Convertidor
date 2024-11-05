# src/base64_encoder.py

# Definimos la tabla de caracteres Base64
BASE64_CHARACTERS = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789+/"

def to_binary_string(text):
    """Convierte el texto a una cadena binaria de 8 bits por carácter."""
    return ''.join(format(ord(char), '08b') for char in text)

def pad_binary_string(binary_string):
    """Rellena la cadena binaria hasta que su longitud sea un múltiplo de 24."""
    while len(binary_string) % 24 != 0:
        binary_string += '0'
    return binary_string

def encode_base64(binary_string):
    """Convierte la cadena binaria a Base64."""
    base64_encoded = ''
    
    # Procesar bloques de 24 bits
    for i in range(0, len(binary_string), 24):
        block = binary_string[i:i + 24]
        
        # Dividir el bloque en 4 bloques de 6 bits
        for j in range(0, 24, 6):
            six_bits = block[j:j + 6]
            # Convertir los 6 bits a un número
            index = int(six_bits, 2)
            # Agregar el carácter correspondiente de Base64
            base64_encoded += BASE64_CHARACTERS[index]
    
    # Añadir caracteres de relleno si es necesario
    padding_needed = (len(binary_string) // 8) % 3
    if padding_needed > 0:
        base64_encoded += '=' * (3 - padding_needed)
    
    return base64_encoded

def text_to_base64(text):
    """Función principal para convertir texto a Base64."""
    # Convertir el texto a binario
    binary_string = to_binary_string(text)
    # Rellenar la cadena binaria
    padded_binary_string = pad_binary_string(binary_string)
    # Codificar en Base64
    return encode_base64(padded_binary_string)
