# **📰 AI-Powered News Chatbot**  

News Generator App is a Python-based application that leverages Hugging Face Transformers and NLP models to generate and summarize news articles. Built with Streamlit, it provides an interactive UI for users to input news content and receive AI-generated summaries. The app supports BART-based summarization, PDF export using ReportLab, and seamless text processing for quick insights.

A **free AI chatbot application** built using **Streamlit** that:  
✅ **Chats with users about news topics** using a **free AI model**  
✅ **Fetches real-time news** from free APIs  
✅ **Generates a PDF report of selected news**  

---

## **📂 Project Structure**  
```
news_chatbot/
│── src/
│   ├── python/
│   │   ├── app/
│   │   │   ├── common/
│   │   │   │   ├── utils.py  
│   │   │   ├── const/
│   │   │   │   ├── constants.py 
│   │   │   ├── config/
│   │   │   │   ├── config.py  
│   │   │   ├── models/
│   │   │   │   ├── chatbot.py 
│   │   │   ├── app.py  
│── requirements.txt
│── README.md
```

---

## **📌 Features**
- 💬 **Chatbot** that answers news-related queries using a free AI model  
- 📢 **Fetches real-time news** from free news APIs  
- 📄 **Generates PDF reports** for selected news categories  
- 🎨 **Simple Streamlit UI** for user interaction  

---

## **📥 Installation & Setup**
1️⃣ **Clone the Repository**  
```bash
git clone https://github.com/your-username/news-chatbot.git
cd news-chatbot
```

2️⃣ **Create & Activate Virtual Environment**  
```bash
python -m venv venv
source venv/bin/activate   # For macOS/Linux
venv\Scripts\activate      # For Windows
```

3️⃣ **Install Dependencies**  
```bash
pip install -r requirements.txt
```

4️⃣ **Run the Streamlit App**  
```bash
streamlit run src/python/app/app.py
```

---

## **🔑 API Configuration**
- Sign up for a **free News API key** from [GNews](https://gnews.io)  
- Add the API key in `src/python/app/const/constants.py`  

```python
NEWS_API_KEY = "YOUR_NEWS_API_KEY"
```

---

## **📌 Usage**
1. **Start the chatbot** and type your news-related question  
2. **Select a news category** to fetch recent news  
3. **Generate a PDF report** based on selected categories  
4. **Read summarized news articles** directly in the app  

---

## **📦 Dependencies**
```txt
streamlit
transformers
torch
requests
pandas
pdfkit
```

---

## **🤖 AI Model Used**
We use **Meta's Blenderbot 3B (Llama 2 Alternative)**, a free chatbot model:  
```python
from transformers import pipeline

chat_model = pipeline("text-generation", model="facebook/blenderbot-3B")

def chat_with_bot(user_input):
    """Generate chatbot response."""
    response = chat_model(user_input, max_length=100, do_sample=True)
    return response[0]['generated_text']
```

---

## **📢 Screenshots**
| Chatbot UI | News Fetching UI |
|------------|-----------------|
| ![Chatbot](https://via.placeholder.com/400) | ![News](https://via.placeholder.com/400) |

---  

---

## **🔗 Contributing**
1. Fork the repo  
2. Create a new branch: `git checkout -b feature-name`  
3. Commit changes: `git commit -m "Added feature"`  
4. Push to GitHub: `git push origin feature-name`  
5. Open a Pull Request  

---

## **📧 Contact**
For queries, email: **sk04m2001@gmail.com**  

🚀 **Enjoy your AI-powered News Chatbot!**
