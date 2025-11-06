import boto3
import json

def lambda_handler(event, context):
    # Entrada
    body = event.get('body', {})
    if isinstance(body, str):
        body = json.loads(body)
    
    nombre_bucket = body['bucket']
    nombre_directorio = body['directorio']
    
    # Asegurar que el directorio termine con /
    if not nombre_directorio.endswith('/'):
        nombre_directorio += '/'
    
    # Proceso
    s3 = boto3.client('s3')
    
    try:
        response = s3.put_object(
            Bucket=nombre_bucket,
            Key=nombre_directorio,
            Body=b''
        )
        
        return {
            'statusCode': 200,
            'body': json.dumps({
                'message': f'Directorio {nombre_directorio} creado en bucket {nombre_bucket}',
                'response': str(response)
            })
        }
    except Exception as e:
        return {
            'statusCode': 500,
            'body': json.dumps({
                'error': f'Error creando directorio: {str(e)}'
            })
        }
