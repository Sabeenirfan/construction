FROM python:3.12-slim

# Install dependencies for Chrome
RUN apt-get update && apt-get install -y \
    wget unzip curl gnupg2 fonts-liberation libappindicator3-1 libasound2 libatk-bridge2.0-0 \
    libatk1.0-0 libcups2 libdbus-1-3 libgdk-pixbuf2.0-0 libnspr4 libnss3 libx11-xcb1 \
    libxcomposite1 libxdamage1 libxrandr2 xdg-utils --no-install-recommends

# Install Google Chrome
RUN curl -sSL https://dl.google.com/linux/direct/google-chrome-stable_current_amd64.deb -o chrome.deb && \
    apt install -y ./chrome.deb && rm chrome.deb

# Install ChromeDriver
RUN CHROME_VERSION=$(google-chrome --version | cut -d ' ' -f 3 | cut -d '.' -f 1) && \
    DRIVER_VERSION=$(curl -s https://chromedriver.storage.googleapis.com/LATEST_RELEASE_$CHROME_VERSION) && \
    wget -O /tmp/chromedriver.zip "https://chromedriver.storage.googleapis.com/${DRIVER_VERSION}/chromedriver_linux64.zip" && \
    unzip /tmp/chromedriver.zip -d /usr/local/bin && chmod +x /usr/local/bin/chromedriver && rm /tmp/chromedriver.zip

# Set display env variable
ENV DISPLAY=:99

# Set working directory
WORKDIR /app

# Copy files
COPY . /app

# Install Python dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Run tests
CMD ["pytest", "--headless", "--html=report.html", "--self-contained-html"]
