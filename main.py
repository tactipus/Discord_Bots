import subprocess

#applescript = """display dialogue "Someone has left or joined the server." with title "Discord Event" with icon caution buttons {"OK"}"""

member = "Invisible Monster"
button = "OK"

applescript = """
display dialog "{} has either been removed or has joined." ¬
with title "Discord Alert" ¬
with icon caution ¬
buttons "{}"
""".format(member, button)

subprocess.call("osascript -e '{}'".format(applescript), shell=True)