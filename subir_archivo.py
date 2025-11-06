import boto3
import json
import base64

def lambda_handler(event, context):
    # Entrada
    body = event.get('body', {})
    if isinstance(body, str):
        body = json.loads(body)
    
    nombre_bucket = body['bucket']
    nombre_archivo = body['archivo']
    datos_base64 = body['datos_base64']
    
    # Proceso
    s3 = boto3.client('s3')
    
    try:
        # Decodificar base64
        datos_binarios = base64.b64decode(datos_base64)
        
        # Subir archivo
        response = s3.put_object(
            Bucket=nombre_bucket,
            Key=nombre_archivo,
            Body=datos_binarios,
            ContentType='image/png'  # Ajustar según tipo de archivo
        )
        
        return {
            'statusCode': 200,
            'body': json.dumps({
                'message': f'Archivo {nombre_archivo} subido exitosamente',
                'response': str(response)
            })
        }
    except Exception as e:
        return {
            'statusCode': 500,
            'body': json.dumps({
                'error': f'Error subiendo archivo: {str(e)}'
            })
        }
