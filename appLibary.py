import subprocess
import webbrowser


patterns = {
    "open browser": lambda: webbrowser.open("https://www.google.com"),
    "open youtube": lambda: webbrowser.open("https://www.youtube.com"),
    "open facebook": lambda: webbrowser.open("https://www.facebook.com"),
    "open github": lambda: webbrowser.open("https://www.github.com"),
    "open linkedin": lambda: webbrowser.open("https://www.linkedin.com"),
    "open instagram": lambda: webbrowser.open("https://www.instagram.com/"),
    "open figma": lambda: webbrowser.open("https://www.figma.com/"),
    
    # Windows specific applications
    "open edge": lambda: subprocess.Popen([r"C:\Program Files (x86)\Microsoft\Edge\Application\msedge.exe"]),
    "open calculator": lambda: subprocess.Popen(["calc.exe"]),
    "open chrome": lambda: subprocess.Popen([r"C:\Program Files\Google\Chrome\Application\chrome.exe"]),
    "open firefox": lambda: subprocess.Popen(["firefox.exe"]),
    "open vs code": lambda: subprocess.Popen([r"C:\Users\Abib Ahmmed\AppData\Local\Programs\Microsoft VS Code\Code.exe"]),  # Visual Studio Code
    "open telegram": lambda: subprocess.Popen([r"C:\Users\Abib Ahmmed\AppData\Roaming\Telegram Desktop\Telegram.exe"]),  # Telegram Desktop
    "open terabox": lambda: subprocess.Popen([r"C:\Users\Abib Ahmmed\AppData\Roaming\TeraBox\TeraBox.exe"]),
    "open messenger": lambda: subprocess.Popen([r"C:\Users\Abib Ahmmed\AppData\Local\Programs\Messenger\Messenger.exe"]),  # Facebook Messenger if installed
    "open postman": lambda: subprocess.Popen([r"C:\Users\Abib Ahmmed\AppData\Local\Postman\Postman.exe"]),  # Slack Desktop
    "open github desktop": lambda: subprocess.Popen([r"C:\Users\Abib Ahmmed\AppData\Local\GitHubDesktop\GitHubDesktop.exe"]),  # Zoom application
    "open zoom": lambda: subprocess.Popen([r"C:\Users\Abib Ahmmed\AppData\Roaming\Zoom\bin\Zoom.exe"]),
    "open mongo compass": lambda: subprocess.Popen([r"C:\Users\Abib Ahmmed\AppData\Local\MongoDBCompass\MongoDBCompass.exe"]),
    "open vlc": lambda: subprocess.Popen([r"C:\Program Files\VideoLAN\VLC\vlc.exe"]),
    "open any desk": lambda: subprocess.Popen([r"C:\Program Files (x86)\AnyDesk\AnyDesk.exe"]),
    


}