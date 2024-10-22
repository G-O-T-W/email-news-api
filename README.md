# Daily News Email Automation

This project fetches the latest news headlines based on a topic and sends them via email using Python. It utilizes the News API to gather news articles and then sends the content as an email using SMTP.

## Features

- **Fetch Latest News**: Retrieves the top news articles related to a specific topic from the News API.
- **Automated Email Delivery**: Sends an email with the top news articles to a predefined recipient.
- **Error Handling**: Gracefully handles cases where no articles are found or certain fields are missing in the news data.
- **UTF-8 Encoding**: Ensures proper encoding of the news content to avoid issues with special characters in the email body.

## File Structure

- `main.py`: The main script that fetches the news articles and sends the email.
- `send_email.py`: A helper module that handles sending the email using SMTP.
  
## How to Use

1. Install the necessary dependencies:
   ```bash
   pip install requests
    ```
2. Get your News API key by signing up at [News API](https://newsapi.org/)
3. Set your environment variable for the email app password (required for the send_email.py script):
   ```bash
   export PASSWORD="your_password_here"
   ```
4. Replace the following in the send_email.py:
   - Sender's email: Replace rishavdiyali@gmail.com with the actual sender email.
   - Receiver's email: Replace diyali.rishav.22@gmail.com with the recipient's email.
5. Run the script:
   ```bash
   python3 main.py
   ```
## Technologies Used
- **Python**: The main programming language for scripting.
- **News API**: Used to fetch the latest news articles.
- **SMTP**: Utilized for sending emails via the Gmail SMTP server.
- **Requests**: A Python library to make HTTP requests to the News API.
- **smtplib and email modules**: Used for handling email communication.

## Environment Variables
To keep your email credentials secure, store the sender email's password in an environment variable:
```bash
export PASSWORD="your_email_password"
```





    
