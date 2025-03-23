# RoastMyResume 🚀

A fun and engaging web application that leverages Google's Gemini AI to provide a humorous, sarcastic take on your resume. Upload your resume and brace yourself for some brutally honest yet entertaining feedback! 😆📄🔥

<p align="center">
   <img src="resources/demo.gif" width="500">
</p>

---

## 🌟 Features

✅ Secure user authentication with password hashing 🔒  
✅ Supports PDF and TXT resume uploads 📂  
✅ AI-powered resume roasting using Google's Gemini model 🤖🔥  
✅ Intuitive and user-friendly web interface 🎨  
✅ Secure credential storage using AWS S3 ☁️  

---

## 📋 Prerequisites

- Python 3.8 or higher 🐍
- Google API Key for Gemini AI 🔑
- AWS account with S3 access ☁️
- Stable internet connection 🌍

---

## 🌐 Deployment on AWS EC2

Looking to deploy this app on AWS EC2? Check out our [AWS EC2 Setup Guide](./AWS_Helper.md) for step-by-step instructions. 🖥️☁️

---

## 🚀 Setup Instructions

### 1️⃣ Clone the Repository
```bash
git clone https://github.com/ArchitJ6/RoastMyResume.git
cd RoastMyResume
```

### 2️⃣ Create a Virtual Environment
```bash
python -m venv venv
```

### 3️⃣ Activate the Virtual Environment
- **Windows:**
  ```bash
  venv\Scripts\activate
  ```
- **macOS/Linux:**
  ```bash
  source venv/bin/activate
  ```

### 4️⃣ Install Dependencies
```bash
pip install -r requirements.txt
```

### 5️⃣ Get Your Google API Key 🔑
1. Visit the [Google AI Studio](https://aistudio.google.com/apikey)
2. Sign in with your Google account
3. Create a new API key and copy it

### 6️⃣ Set Up AWS S3 ☁️
1. Create an S3 bucket in your AWS account
2. Generate an IAM user with S3 access
3. Note down the AWS access key ID and secret access key

### 7️⃣ Configure Environment Variables
Create a `.env` file in the project root and add:
```ini
GEMINI_API_KEY=your_gemini_api_key_here
AWS_ACCESS_KEY_ID=your_aws_access_key_id
AWS_SECRET_ACCESS_KEY=your_aws_secret_access_key
AWS_REGION=your_aws_region
S3_BUCKET_NAME=your_s3_bucket_name
```

---

## 🖥️ Running the Application Locally

### 1️⃣ Activate the Virtual Environment
Ensure the virtual environment is activated before proceeding.

### 2️⃣ Start the Streamlit Server 🚀
```bash
python -m streamlit run app.py
```

### 3️⃣ Open the App in Your Browser 🌐
Navigate to:  
👉 `http://localhost:8501`

---

## 📖 Usage Guide

### 👤 First-Time Users
1. Click **Signup** in the sidebar
2. Create your account
3. Login with your credentials

### 🔄 Returning Users
1. Enter your username and password
2. Click **Login**

### 🔥 Roast Your Resume
1. Upload your resume (PDF or TXT format)
2. Click **Roast my resume**
3. Wait for the AI to generate its critique
4. Enjoy the roast! 😆🔥

---

## 🔒 Security Notes

✔️ Passwords are securely hashed using SHA-256 🔑

✔️ Keep your `.env` file private 🚨

✔️ Never share your API keys ❌

---

## 🔧 Troubleshooting

- **API Errors?** Check your API key in `.env` ✅
- **Dependency Issues?** Ensure all packages are installed via `pip install -r requirements.txt` 📦
- **File Format Issues?** Only PDF and TXT formats are supported 📜
- **Internet Issues?** Make sure you have a stable connection 🌐

---

## 🤝 Contributing

Feel free to fork this repository and submit pull requests. If you have a major feature in mind, open an issue to discuss it first. Contributions are always welcome! 🎉

---

## 📄 License

This project is licensed under the [MIT License](LICENSE). 📜

---

## 👏 Acknowledgments

🙏 Google Gemini AI for the roasting capabilities 🤖🔥  
🙏 Streamlit for the amazing web framework 🎨  
🙏 All contributors and users of this project 💙  