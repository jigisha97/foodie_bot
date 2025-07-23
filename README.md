# Foodie_Bot
foodieBot is a lightweight yet intelligent food ordering assistant built using Streamlit, LangChain, and the Mistral-7B Instruct model via Together.ai. It allows users to view a menu, place food orders using natural language, and stores orders in a local SQLite database — all through a clean, right-aligned, image-backed UI.

# How It Works?
- User opens the app and sees a title, input box, and background image.
- User types a query, like "show me the menu" or "2 pasta and 1 coke".
- LangChain agent evaluates the prompt and decides which tool to use:
  If it's a menu query → uses ShowMenu
  If it's an order → uses PlaceOrder, parses input, calculates total, and saves it
- Response is shown in chat format, and added to chat history


<img width="1787" height="975" alt="foodie_bot" src="https://github.com/user-attachments/assets/bfddfbe4-91af-476d-847e-9f611d231709" />

# How to Run the Project – foodieBot
### Step 1: Clone the Repository
git clone https://github.com/your-username/foodieBot.git
cd foodieBot

### Step 2: Set Up a Virtual Environment (Optional)
python -m venv venv
source venv/bin/activate 
### Step 3: Install Dependencies 
pip install -r requirements.txt
**Note**: If you encounter any errors, try installing the packages individually using pip install <package-name>.

### Step 4: Create Your Together.ai API Key from - https://api.together.ai/

### Step 5: Add Your Together.ai API Key
export TOGETHER_API_KEY=your_api_key_here  # Linux/macOS
set TOGETHER_API_KEY=your_api_key_here  

### Step 6: Run Application
streamlit run main.py

### Step 7: View Results
Visit -  http://localhost:8501

### Step 8: Chat with Foodie_Bot
Ask for menu:
Show me the menu
Place an order:
I want 2 pizza and 3 fries
