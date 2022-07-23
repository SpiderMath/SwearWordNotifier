from pynput.keyboard import Listener, Key, KeyCode
from plyer import notification


stack = ""
swear_words = []
count = 0

with open('swear_words.txt', 'r') as file:
	lines = file.readlines()
	swear_words = list(map(lambda t: t.strip().lower(), lines))


def on_press(key):
	global stack, count

	if isinstance(key, KeyCode) and 'a' < key.char < 'z':
		stack += key.char.lower()
	elif key == Key.backspace:
		stack = stack[0:-1]
	elif key == Key.space or key == Key.enter or key == Key.tab:
		stack = ""


	if stack in swear_words:
		count += 1
		notification.notify(
			title='Swear Word Detected',
			message=f"Swear word used: {stack}\nSwear word count: {count}",
			timeout=10,
		)


with Listener(on_press=on_press) as listener:
	listener.join()
