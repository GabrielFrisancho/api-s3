import boto3
import json

def lambda_handler(event, context):
    try:
        # Entrada
        body = event.get('body', {})
        if isinstance(body, str):
            body = json.loads(body)
        
        nombre_bucket = body['bucket']
        nombre_archivo = body['archivo']
        tipo_contenido = body.get('tipo_contenido', 'application/octet-stream')
        
        # Proceso - generar URL firmada para subida
        s3 = boto3.client('s3')
        
        url_subida = s3.generate_presigned_url(
            ClientMethod='put_object',
            Params={
                'Bucket': nombre_bucket,
                'Key': nombre_archivo,
                'ContentType': tipo_contenido
            },
            ExpiresIn=3600  # 1 hora de validez
        )
        
        return {
            'statusCode': 200,
            'body': json.dumps({
                'message': 'URL generada exitosamente',
                'url_subida': url_subida,
                'archivo': nombre_archivo,
                'bucket': nombre_bucket,
                'instrucciones': 'Usa PUT request con la URL generada para subir el archivo'
            })
        }
    except Exception as e:
        return {
            'statusCode': 500,
            'body': json.dumps({
                'error': f'Error generando URL: {str(e)}'
            })
        }
