# CryptoPriceAlert-Telegram Bot
Telegram bot that tracks and sends alerts for cryptocurrency prices.

## Roadmap 
---

### **Phase 1: Set Up the Telegram Bot with Basic Price Alerts (Python)**

**Prerequisites to Learn:**
1. **Python Basics:**
   - Master functions, loops, conditionals, and basic error handling.
2. **APIs and HTTP Requests:**
   - Learn how to make API calls using the `requests` library in Python.
   - Understand JSON data and how to parse it in Python.
3. **Telegram Bot Basics:**
   - Familiarize yourself with the basics of Telegram bots and the `python-telegram-bot` library.

**Suggested Resources:**
   - Python basics: [Python Docs](https://docs.python.org/3/tutorial/)
   - `requests` library: [Requests Documentation](https://docs.python-requests.org/en/master/)
   - Telegram Bot API: [Telegram Bot API Documentation](https://core.telegram.org/bots)

**Roadmap Steps:**
1. **Create and Configure the Telegram Bot:**
   - Register your bot on Telegram via [BotFather](https://core.telegram.org/bots#botfather) and get the bot token.
   - Set up a basic Python script to connect to Telegram using `python-telegram-bot`.
2. **Fetch Cryptocurrency Price Data:**
   - Use a cryptocurrency API like CoinGecko or CoinMarketCap to fetch real-time price data.
   - Write basic functions to retrieve prices based on cryptocurrency symbols.
3. **Set Up Price Monitoring:**
   - Implement a feature to monitor prices at regular intervals.
   - Create functions to check if a specific price threshold is met.
4. **Send Alerts via Telegram:**
   - Add functionality to send price alerts directly to users when the target price is reached.
5. **Add Basic User Commands:**
   - Implement commands like `/start`, `/help`, `/setalert`, and `/cancelalert` for user interaction.
   - Store user preferences (like price threshold and alert frequency) in a file or lightweight database (e.g., SQLite).

---

### **Phase 2: Enhance Bot Functionality and Refine Alert System (Python)**

**Prerequisites to Learn:**
1. **Threading and Asynchronous Programming:**
   - Learn Python’s threading and `asyncio` modules to improve bot responsiveness and handle multiple users.
2. **Database Basics (SQLite or PostgreSQL):**
   - Understand basic database operations like inserting, retrieving, and updating records.
   - Practice basic SQL commands with SQLite.
3. **File Handling in Python:**
   - Review Python’s `os` and `json` libraries for storing data if a database is not yet needed.

**Suggested Resources:**
   - Asynchronous Python: [Asyncio Documentation](https://docs.python.org/3/library/asyncio.html)
   - Databases in Python: [SQLite Tutorial](https://www.sqlitetutorial.net/sqlite-python/)

**Roadmap Steps:**
1. **Multiple Alert Support:**
   - Enable users to set multiple alerts for different cryptocurrencies.
   - Store and retrieve each user’s alert settings in a database or file.
2. **Improve Alert Precision and Efficiency:**
   - Use threading or asynchronous programming to handle multiple users efficiently.
3. **User Management and State Storage:**
   - Consider using SQLite or PostgreSQL to manage user data and alert histories.
4. **Advanced Commands:**
   - Implement commands like `/listalerts`, `/removealert`, and `/clearalerts`.

---

### **Phase 3: Implement Error Handling, Testing, and Optimization (Python)**

**Prerequisites to Learn:**
1. **Error Handling and Logging:**
   - Learn Python’s `try`, `except` statements and explore the `logging` library to manage errors and track activity.
2. **Testing in Python:**
   - Understand unit testing with the `unittest` module.
3. **Basic Caching:**
   - Learn caching techniques like memoization with `functools.lru_cache` to avoid excessive API calls.

**Suggested Resources:**
   - Python logging: [Logging in Python](https://docs.python.org/3/howto/logging.html)
   - Unit Testing: [Unittest Documentation](https://docs.python.org/3/library/unittest.html)
   - Caching: [Python functools](https://docs.python.org/3/library/functools.html)

**Roadmap Steps:**
1. **Add Error Handling:**
   - Handle potential API request errors, network issues, and Telegram connection interruptions.
2. **Test the Bot:**
   - Conduct testing under different conditions to ensure stability.
3. **Optimize Performance:**
   - Implement caching to reduce repetitive API calls, especially if there are many users tracking the same coins.

---

### **Phase 4: Build a Backend API for GUI Integration (Python - Flask/FastAPI)**

**Prerequisites to Learn:**
1. **REST API Concepts:**
   - Understand REST principles, HTTP methods (GET, POST, etc.), and JSON data format.
2. **Flask or FastAPI Basics:**
   - Learn to set up a basic server, create endpoints, and return data in JSON format.
3. **WebSockets (Optional):**
   - Familiarize yourself with WebSocket basics for real-time updates.

**Suggested Resources:**
   - REST API: [REST API Basics](https://restfulapi.net/)
   - Flask: [Flask Documentation](https://flask.palletsprojects.com/)
   - FastAPI: [FastAPI Documentation](https://fastapi.tiangolo.com/)

**Roadmap Steps:**
1. **Create a REST API:**
   - Set up a backend API using Flask or FastAPI to expose bot functionalities.
2. **Connect the API to Bot’s Data:**
   - Ensure alerts and user data from the bot can be accessed and modified through the API.
3. **Enable WebSocket for Real-time Updates (Optional):**
   - Use WebSocket (with Flask-SocketIO or FastAPI) to push updates to the frontend.

---

### **Phase 5: Build the Frontend GUI with React**

**Prerequisites to Learn:**
1. **JavaScript Fundamentals:**
   - Master JavaScript basics, ES6+ features (arrow functions, destructuring), and async programming.
2. **React Basics:**
   - Set up a React project, understand components, props, state, and hooks (especially `useState` and `useEffect`).
3. **Frontend Styling:**
   - Basic CSS and UI principles for creating a simple and user-friendly interface.

**Suggested Resources:**
   - JavaScript: [JavaScript Tutorial](https://www.w3schools.com/js/)
   - React: [React Documentation](https://reactjs.org/docs/getting-started.html)
   - Fetch API: [MDN Fetch API](https://developer.mozilla.org/en-US/docs/Web/API/Fetch_API)

**Roadmap Steps:**
1. **Set Up the Frontend:**
   - Set up a React project using `create-react-app` or Next.js.
2. **Design the User Interface:**
   - Plan a UI where users can add, view, and delete price alerts.
3. **Fetch Data from the Backend API:**
   - Use `fetch` or Axios to make API requests to the Python backend.
4. **Real-time Data Handling:**
   - Implement periodic fetching or connect via WebSocket (if available) for real-time updates.

---

### **Phase 6: Finalize and Deploy**

**Prerequisites to Learn:**
1. **Deployment Concepts:**
   - Understand server hosting (e.g., AWS, DigitalOcean) and frontend hosting (e.g., Vercel, Netlify).
2. **Docker (Optional):**
   - Learn Docker basics for containerizing the app.
3. **Web Security Basics:**
   - Understand best practices for API key management and securing web servers.

**Suggested Resources:**
   - Deployment: [Deploying Python Applications](https://realpython.com/python-deployment/)
   - Docker: [Docker Getting Started](https://docs.docker.com/get-started/)

**Roadmap Steps:**
1. **Front-to-Back Integration Testing:**
   - Test the full workflow, from setting an alert in the GUI to receiving it in Telegram.
2. **Deployment:**
   - Deploy the Python backend and Telegram bot on a server (e.g., Heroku, AWS, or DigitalOcean).
   - Deploy the React frontend on a hosting service like Vercel or Netlify.
3. **Maintenance and Monitoring:**
   - Set up logging and monitoring for both the backend and the bot.
