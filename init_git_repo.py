import os


commands = []
commands.append("git init")
commands.append("git add -A ")
commands.append("git commit -m " + '"first commit"')
commands.append("git branch -M main")
commands.append("git remote add origin ")
commands.append("git push -u origin main")

for command in commands:
    if command == "git remote add origin ":
        url = input("Enter link to repo (ex. https://github.com/<username>/hello-world.git): ")
        command += url
        print("****************" + command + "******************")
    os.system(command)