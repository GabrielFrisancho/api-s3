import boto3
import base64
import json

def upload_base64_to_s3(s3_bucket_name, s3_file_name, base64_str):
    """
    Upload base64 string to S3 - Based on the gist provided
    """
    s3 = boto3.resource('s3')
    s3.Object(s3_bucket_name, s3_file_name).put(Body=base64.b64decode(base64_str))
    return (s3_bucket_name, s3_file_name)

def lambda_handler(event, context):
    try:
        # Entrada
        body = event.get('body', {})
        if isinstance(body, str):
            body = json.loads(body)
        
        nombre_bucket = body['bucket']
        nombre_archivo = body['archivo']
        datos_base64 = body['datos_base64']
        
        # Proceso - subir usando función del gist
        bucket, archivo = upload_base64_to_s3(nombre_bucket, nombre_archivo, datos_base64)
        
        return {
            'statusCode': 200,
            'body': json.dumps({
                'message': f'Archivo {archivo} subido exitosamente a {bucket}',
                'bucket': bucket,
                'archivo': archivo
            })
        }
    except Exception as e:
        return {
            'statusCode': 500,
            'body': json.dumps({
                'error': f'Error subiendo archivo: {str(e)}'
            })
        }
