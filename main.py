import re
import json
import sqlite3
import pandas as pd
import streamlit as st
from langchain.agents import initialize_agent, Tool
from langchain.agents.agent_types import AgentType
from langchain_community.llms import Together
from langchain.schema import SystemMessage

# Load Together.ai model
llm = Together(
    model="mistralai/Mistral-7B-Instruct-v0.2",
    temperature=0.3, # no more random ans
    max_tokens=512
)

menu_df = pd.read_csv("menu.csv")

def store_order(user_input, parsed_order, total_price):
    with sqlite3.connect("orders.db") as conn:
        cursor = conn.cursor()
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS orders (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                user_input TEXT,
                parsed_order TEXT,
                total_price REAL,
                timestamp DATETIME DEFAULT CURRENT_TIMESTAMP
            )
        """)
        cursor.execute("""
            INSERT INTO orders (user_input, parsed_order, total_price)
            VALUES (?, ?, ?)
        """, (user_input, json.dumps(parsed_order), total_price))
        conn.commit()
    return "Order stored successfully!"

def show_menu(_):
    return menu_df.to_string(index=False)

def process_order(user_input):
    #item pattern can also take from orders.db so dynamic
    item_pattern = re.compile(r'(\d+)\s*(pizza|burger|fries|pasta|coke)', re.IGNORECASE)
    matches = item_pattern.findall(user_input)

    if not matches:
        return "Sorry, no menu items matched your input."

    parsed_order = []
    total = 0

    for qty, item in matches:
        qty = int(qty)
        item = item.lower()
        price = int(menu_df[menu_df['item'] == item]['price'].values[0])
        parsed_order.append(str(qty) + " x " + item + " - Rs " + str(qty * price))
        total = total + (qty * price)

    summary = "\n".join(parsed_order)
    store_order(user_input, parsed_order, total)
    return f"You ordered:\n{summary}\nTotal: ₹{total}"

tools = [
    Tool(name="ShowMenu", func=show_menu, description="Use when user asks for the restaurant menu."),
    Tool(name="PlaceOrder", func=process_order, description="Use when the user places a food order.")
]

agent = initialize_agent(
    tools=tools,
    llm=llm,
    agent=AgentType.ZERO_SHOT_REACT_DESCRIPTION,
    verbose=True,
    handle_parsing_errors=True,
    agent_kwargs={
        "system_message": SystemMessage(
            content="You are a food ordering assistant. Use tools to respond. Format: Action: <tool name>\nAction Input: <input>."
        )
    }
)

st.title("Food Ordering Chatbot")

if "chat_history" not in st.session_state:
    st.session_state.chat_history = []

user_input = st.text_input("What would you like to order? (e.g., '3 pizza and 2 fries')")

st.markdown(
    """
    <style>
    .stApp {
        background-image: url("https://img.freepik.com/premium-photo/different-fast-food-gray-textured-table_185193-48535.jpg");
        background-size: cover;
        background-position: center;
    }
    </style>
    """,
    unsafe_allow_html=True
)

if st.button("Send"):
    if user_input:
        response = agent.run(user_input)
        st.session_state.chat_history.append((user_input, response))

for msg in st.session_state.chat_history:
    st.markdown(f"**You:** {msg[0]}")
    st.markdown(f"**foodieBot:** {msg[1]}")