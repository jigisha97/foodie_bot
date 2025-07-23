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
