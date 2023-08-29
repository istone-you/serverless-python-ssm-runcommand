import boto3

def lambda_handler(event, context):
    # SSM Clientを作成
    ssm_client = boto3.client('ssm')
    
    # 実行するコマンド
    command = "echo random_number $RANDOM > /etc/prometheus/textfile/random_number.prom"
    
    # SSM Run Commandを設定
    response = ssm_client.send_command(
        InstanceIds=['i-0fda56cbd5b981a63'],  # 実行対象のEC2インスタンスのIDを指定
        DocumentName='AWS-RunShellScript',
        Parameters={'commands': [command]},
    )
    
    # コマンド実行結果の情報を表示
    command_id = response['Command']['CommandId']
    instance_id = response['Command']['InstanceIds'][0]
    
    return {
        'statusCode': 200,
        'body': f'Command {command_id} sent to instance {instance_id}'
    }