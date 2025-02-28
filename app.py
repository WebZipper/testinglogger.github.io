import multiprocessing
from bot.bot import run_bot
from web.app import app

def start_bot():
    run_bot()

def start_web():
    app.run(debug=True, use_reloader=False)

if __name__ == "__main__":
    bot_process = multiprocessing.Process(target=start_bot)
    web_process = multiprocessing.Process(target=start_web)
    
    bot_process.start()
    web_process.start()
    
    bot_process.join()
    web_process.join()