import boto3
import json

def lambda_handler(event, context):
    try:
        # Entrada
        body = event.get('body', {})
        if isinstance(body, str):
            body = json.loads(body)
        
        nombre_bucket = body['bucket']
        
        # Proceso
        s3 = boto3.client('s3')
        
        # Para us-east-1 no se usa LocationConstraint
        response = s3.create_bucket(Bucket=nombre_bucket)
        
        return {
            'statusCode': 200,
            'body': json.dumps({
                'message': f'Bucket {nombre_bucket} creado exitosamente',
                'bucket': nombre_bucket
            })
        }
    except Exception as e:
        return {
            'statusCode': 500,
            'body': json.dumps({
                'error': f'Error creando bucket: {str(e)}'
            })
        }
