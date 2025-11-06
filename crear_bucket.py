import boto3
import json

def lambda_handler(event, context):
    # Entrada
    body = event.get('body', {})
    if isinstance(body, str):
        body = json.loads(body)
    
    nombre_bucket = body['bucket']
    
    # Proceso
    s3 = boto3.client('s3')
    
    try:
        response = s3.create_bucket(
            Bucket=nombre_bucket,
            CreateBucketConfiguration={
                'LocationConstraint': 'us-east-1'
            }
        )
        
        return {
            'statusCode': 200,
            'body': json.dumps({
                'message': f'Bucket {nombre_bucket} creado exitosamente',
                'response': str(response)
            })
        }
    except Exception as e:
        return {
            'statusCode': 500,
            'body': json.dumps({
                'error': f'Error creando bucket: {str(e)}'
            })
        }
