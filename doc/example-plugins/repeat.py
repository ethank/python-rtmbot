import time
crontable = []
outputs = []

def process_message(data):
	print data['channel']
    if data['channel'].startswith("D"):
        outputs.append([data['channel'], "from repeat1 \"{}\" in channel {}".format(data['text'], data['channel']) ])
        print data['text']

