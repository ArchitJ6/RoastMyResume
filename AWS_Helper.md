## AWS EC2 Setup Guide 🚀

### 1. Launch EC2 Instance 🖥️
1. 🔑 Log into AWS Console
2. 📌 Go to EC2 Dashboard
3. 🚀 Click "Launch Instance"
4. 🏗️ Choose Ubuntu Server (20.04 LTS or newer)
5. 💰 Select t2.micro (free tier eligible)
6. 🔒 Configure Security Group:
   - 🛡️ Allow SSH (Port 22)
   - 🌐 Allow HTTP (Port 80)
   - 🔐 Allow HTTPS (Port 443)
   - 🚀 Allow Custom TCP (Port 8501) for Streamlit
7. 🎯 Launch instance and save your key pair (.pem file)
8. 🌍 Create Elastic IP and associate it with your instance

### 2. Install Required Software 📦
```bash
# 🔄 Update package list
sudo apt update
```

```bash
# 🐍 Install Python and pip
sudo apt install -y python3-pip
```

```bash
# 🔧 Install virtual environment
sudo apt install -y python3-venv
```

```bash
# 🛠️ Install git
sudo apt install -y git
```

### 3. Clone and Setup Project 🛠️
```bash
# 📥 Clone the repository
git clone https://github.com/ArchitJ6/RoastMyResume.git
cd RoastMyResume
```

```bash
# 📦 Create virtual environment
python3 -m venv env

# 🏗️ Activate virtual environment
source env/bin/activate

# 📜 Install dependencies
pip install -r requirements.txt
```

### 4. Create and Configure .env File 🔐

```bash
# 📄 Create .env file with content in one command
echo "GEMINI_API_KEY=<Your Gemini API Key>
AWS_ACCESS_KEY_ID=<Your AWS Access Key Id>
AWS_SECRET_ACCESS_KEY=<Your AWS Secret Access Key>
AWS_REGION=<Your AWS Region>
S3_BUCKET_NAME=<Your S3 Bucket Name>" > .env
```

```bash
# 🔒 Set proper permissions
chmod 600 .env
```

### 5. Run the Application with Custom Domain 🌐

#### A. Set Up Nginx as Reverse Proxy 🔄
```bash
# 🌍 Install Nginx
sudo apt install nginx

# 📝 Create Nginx configuration file
sudo nano /etc/nginx/sites-available/resume-roast
```

Add the following configuration:
```nginx
server {
    server_name roastmyresume.architj6.xyz;

    location / {
        proxy_pass http://localhost:8501;
        proxy_http_version 1.1;
        proxy_set_header Upgrade $http_upgrade;
        proxy_set_header Connection 'upgrade';
        proxy_set_header Host $host;
        proxy_cache_bypass $http_upgrade;
    }
}
```

```bash
# 🔗 Create symbolic link
sudo ln -s /etc/nginx/sites-available/resume-roast /etc/nginx/sites-enabled/

# ✅ Test Nginx configuration
sudo nginx -t

# 🔄 Restart Nginx
sudo systemctl restart nginx
```

#### B. Configure DNS on your domain registrar 🌍
1. 🔑 Log into your control panel
2. ⚙️ Go to DNS Zone Editor
3. 🏗️ Add an A record:
   - 📌 Type: A
   - 🏷️ Name: roastmyresume
   - 📍 Points to: Your EC2 instance IP
   - ⏳ TTL: 14400

#### C. Set Up SSL (Optional but Recommended) 🔐
```bash
# 🏗️ Install Certbot
sudo apt install certbot python3-certbot-nginx

# 🔒 Obtain SSL certificate
sudo certbot --nginx -d roastmyresume.architj6.xyz

# ✅ Certbot will automatically configure Nginx for HTTPS
```

#### D. Run the Application as a Service ⚙️
```bash
# 📝 Create a systemd service file
sudo nano /etc/systemd/system/resume-roast.service
```

Add the following content:
```ini
[Unit]
Description=Resume Roast Streamlit App
After=network.target

[Service]
User=ubuntu
WorkingDirectory=/home/ubuntu/RoastMyResume
Environment="PATH=/home/ubuntu/RoastMyResume/env/bin"
ExecStart=/home/ubuntu/RoastMyResume/env/bin/streamlit run app.py --server.address=0.0.0.0

[Install]
WantedBy=multi-user.target
```

```bash
# ▶️ Start and enable the service
sudo systemctl start resume-roast
sudo systemctl enable resume-roast

# 🔍 Check status
sudo systemctl status resume-roast
```

🎉 Your application should now be accessible at [https://roastmyresume.architj6.xyz](https://roastmyresume.architj6.xyz) 🚀