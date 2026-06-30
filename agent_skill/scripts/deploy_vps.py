import paramiko
import time

def deploy_to_vps():
    host = 'YOUR_VPS_IP'
    port = 22
    username = 'root'
    password = 'YOUR_VPS_PASSWORD'
    
    # commands to run on VPS
    commands = [
        "apt-get update -y || yum update -y",
        "apt-get install -y git python3 python3-pip cron || yum install -y git python3 python3-pip cronie",
        "systemctl enable cron || systemctl enable crond",
        "systemctl start cron || systemctl start crond",
        "pip3 install --break-system-packages requests pandas fake_useragent || pip3 install requests pandas fake_useragent",
        "rm -rf /root/CNN-Fear-And-Greed-Pine",
        "git clone https://YOUR_GITHUB_USERNAME:YOUR_GITHUB_TOKEN@github.com/CasualStudy/CNN-Fear-And-Greed-Pine.git /root/CNN-Fear-And-Greed-Pine",
        "cd /root/CNN-Fear-And-Greed-Pine && git config --global user.name 'Automated Bot' && git config --global user.email 'bot@example.com'",
        '(crontab -l 2>/dev/null | grep -v "update.sh" ; echo "30 16 * * 1-5 /bin/bash /root/CNN-Fear-And-Greed-Pine/agent_skill/scripts/update.sh >> /root/CNN-Fear-And-Greed-Pine/cron.log 2>&1") | crontab -'
    ]

    client = paramiko.SSHClient()
    client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    
    print("Connecting to VPS...")
    client.connect(host, port=port, username=username, password=password)
    
    for cmd in commands:
        print(f"Executing: {cmd}")
        stdin, stdout, stderr = client.exec_command(cmd)
        
        # Wait for command to complete
        exit_status = stdout.channel.recv_exit_status()
        out = stdout.read().decode().strip()
        err = stderr.read().decode().strip()
        
        if out: print(out)
        if err: print("Error:", err)
        print(f"Exit status: {exit_status}\n")
        
    client.close()
    print("Deployment complete.")

if __name__ == '__main__':
    deploy_to_vps()
