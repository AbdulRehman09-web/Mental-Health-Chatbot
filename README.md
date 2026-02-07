# 🧠 Mental Health Chatbot

A supportive **AI Mental Health Chatbot** built with **FastAPI**, **OpenRouter GPT-5**, and **LlamaIndex**. The bot can provide helpful advice, respond to crisis situations, and answer user queries based on indexed documents. The chatbot also includes a simple **frontend interface** for real-time interaction.

---

## **Features**

- ✅ AI-powered conversational agent for mental health support  
- ✅ Handles user crisis detection with safety messages  
- ✅ Document-based query support using **LlamaIndex**  
- ✅ Enforces bullet point responses (max 5 points per response)  
- ✅ Frontend chat interface with typing indicator  
- ✅ Fully deployable with **Docker**  
- ✅ CI/CD ready for **Render Cloud**

---

## **Tech Stack**

- **Backend**: FastAPI, Python 3.11  
- **AI Models**: OpenRouter GPT-5-Nano, OpenRouter Embeddings  
- **Vector Store**: LlamaIndex  
- **Frontend**: HTML, CSS, JavaScript  
- **Deployment**: Docker, Render  
- **CICD**: Auto-deploy on GitHub `main` branch using CI/CD Pipeline

---

## **Project Structure**

```

mental-health-chatbot/
│
├─ main.py                 # FastAPI backend
├─ chat_engine.py          # LLM conversation engine with memory
├─ doc_engine.py           # Document-based query engine
├─ models.py               # Pydantic models
├─ crisis.py               # Crisis keyword detection
├─ logger.py               # Interaction logging
├─ requirements.txt        # Python dependencies
├─ Dockerfile              # Dockerfile for deployment
├─ frontend/               # Chatbot UI files
│   ├─ index.html
│   ├─ chatbot.js
│   └─ style.css
├─ .github/               # CI/CD 
│    ├─ workflows/               
│        └─ deploy.yml    # For GitHub actions 
└─ data/                  # Documents for LlamaIndex

````

---

## **Installation & Setup (Local)**

1. Clone the repo:

```bash
git clone https://github.com/YourUsername/YourRepoName.git
cd mental-health-chatbot
````

2. Create a virtual environment and activate it:

```bash
python -m venv myenv
source myenv/bin/activate    # Linux/macOS
myenv\Scripts\activate       # Windows
```

3. Install dependencies:

```bash
pip install -r requirements.txt
```

4. Create a `.env` file in the project root:

```env
OPENROUTER_API_KEY=your_api_key_here
OPENROUTER_URL=https://openrouter.ai/api/v1
```

5. Run the FastAPI server:

```bash
uvicorn main:app --host 127.0.0.1 --port 8001 --reload
```

6. Open the frontend in your browser:

```
http://127.0.0.1:8001/frontend/index.html
```

---

## **Usage**

### Chat Endpoint:

* URL: `/chat`
* Method: POST
* Request JSON:

```json
{
  "session_id": "user_1234",
  "message": "I feel anxious about exams"
}
```

* Response JSON:

```json
{
  "reply": "1. Practice mindfulness or meditation.\n2. Take short breaks.\n3. Stay organized.\n4. Drink water and eat healthy.\n5. Share your feelings with someone you trust.",
  "crisis": false
}
```

---

### Document Chat Endpoint:

* URL: `/doc-chat`
* Method: POST
* Request JSON:

```json
{
  "session_id": "user_1234",
  "message": "Tips for exam preparation"
}
```

* Response JSON:

```json
{
  "reply": "1. Realistic study blocks with breaks.\n2. Calming breathing exercises.\n3. Sleep well and eat regularly.\n4. Short daily movement.\n5. Skim easy questions first in exams.",
  "crisis": false
}
```

---

## **Deployment on Render**

1. Push your code to GitHub (`main` branch).
2. Go to [Render](https://render.com/) → **New Web Service** → Connect GitHub repo.
3. Select **Docker** as the environment.
4. Add environment variables:

```
OPENROUTER_API_KEY
OPENROUTER_URL
```

5. Enable **Auto-Deploy**.
6. Render will automatically build and deploy your service.
7. Access the bot via `https://your-service-name.onrender.com/frontend/index.html`

---

## **Docker Usage**

Build the Docker image locally:

```bash
docker build -t chatbot .
```

Run the container:

```bash
docker run -p 8000:8000 chatbot
```

---

## **Safety & Crisis Handling**

The bot automatically detects potential crises and responds with safety messages:

* Emergency hotlines in multiple countries
* Encouragement to reach out to friends, family, or professionals
* Calm, supportive, and non-judgmental responses

---

## **Contributing**

1. Fork the repository
2. Create a feature branch: `git checkout -b feature/YourFeature`
3. Commit your changes: `git commit -m "Add your message"`
4. Push to the branch: `git push origin feature/YourFeature`
5. Open a pull request

---

## **License**

This project is licensed under the Apache License.

---

## **Contact**

- GitHub: [AbdulRehman09-web](https://github.com/AbdulRehman09-web)
- Email: [abdulrehmannadeem825@gmail.com](mailto:abdulrehmannadeem825@gmail.com)
- LinkedIn: [Abdul Rehman Nadeem](https://www.linkedin.com/in/abdul-rehman-nadeem-18ba4928a/)