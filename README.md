# vissionaiallinone1.0
A free uncensored all in one AI system. This project aims to create a locally run AI system that integrates an Avatar GUI, GPT-based Chat, Uncensored Image &amp; Video Generation, Lip Sync, Morphing Videos, and Enhancement Tools. It will be open-source and packaged as an all-in-one app to boost productivity.

# Deployment Guide for AI Avatar & Media Generation System

## **1. Prerequisites**
Before deploying, ensure you have:
- **Git** installed ([Download Git](https://git-scm.com/downloads))
- **Node.js** and **npm** installed ([Download Node.js](https://nodejs.org/))
- **Python 3.9+** installed ([Download Python](https://www.python.org/downloads/))
- A **GitHub account** ([Sign Up](https://github.com/))

## **2. Clone the Repository**
```bash
git clone https://github.com/YourUsername/AI-Avatar-Generator.git
cd AI-Avatar-Generator
```

## **3. Backend Setup**
Navigate to the backend folder:
```bash
cd backend
```
Install dependencies:
```bash
pip install -r requirements.txt
```
Run the backend server:
```bash
python main.py
```

## **4. Frontend Setup**
Navigate to the frontend folder:
```bash
cd frontend
```
Install dependencies:
```bash
npm install
```
Run the frontend application:
```bash
npm run dev
```

## **5. Running the Full System**
Ensure both backend and frontend are running in separate terminals:
- **Backend:** `python main.py`
- **Frontend:** `npm run dev`

## **6. Deploying to a Server**
### **Option 1: Deploy with Docker**
Ensure Docker is installed ([Download Docker](https://www.docker.com/))

```bash
docker-compose up --build
```

### **Option 2: Deploy on AWS EC2**
1. Launch an **Ubuntu EC2 instance**
2. Install dependencies:
   ```bash
   sudo apt update && sudo apt install -y python3-pip nodejs npm git
   ```
3. Clone the repository and run backend/frontend

### **Option 3: Deploy on DigitalOcean**
1. Create a **Droplet** with Ubuntu
2. Follow the same steps as AWS

## **7. Contributing**
- Open a **GitHub Issue** for feature requests or bugs
- Submit a **Pull Request** to contribute
- Join our **Discord** for discussions

## **8. Future Enhancements**
- Automate deployment with **GitHub Actions**
- Enable **CI/CD pipelines** for updates



