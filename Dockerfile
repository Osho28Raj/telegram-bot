FROM Osho28Raj/telegram-bot:latest

#clonning repo 
RUN git clone https://github.com/Osho28Raj/telegram-bot.git /root/bot
#working directory 
WORKDIR /root/bot

# Install requirements
RUN pip3 install -U -r requirements.txt

ENV PATH="/home/bot:$PATH"

CMD ["python3","bot.py"]
