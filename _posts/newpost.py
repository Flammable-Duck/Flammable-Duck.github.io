#!/usr/bin/python3
import subprocess
from datetime import datetime
now = datetime.now()

print("New Post Name:")
title= input()
title= title.title()
formatTitle= title.replace(" ","-")
formatTitle=formatTitle.lower()
fileName=now.strftime("%Y-%m-%d")+ "-" + formatTitle + ".md"

f = open(fileName, "w")
f.write('---\nlayout: default\ntitle: "'+title+'"\n---\n')
f.close
subprocess.call(["nvim", fileName])
