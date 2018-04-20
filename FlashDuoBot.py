import praw
import config
import time

def botLogin():
	bot = praw.Reddit(username = config.username,
			password = config.password,
			client_id = config.client_id,
			client_secret = config.client_secret,
			user_agent = config.user_agent)
	print "Log in complete"
	return bot

def runBot(bot):
	while(True):
		f = open('LastCommentRead.txt', 'r')
		lastCommentTime = int(f.read())
		print lastCommentTime
		f.close()
		newLatestTime = lastCommentTime
		print "Awake!"
		for comment in bot.subreddit('FlashTV').comments(limit = 9999):
			if comment.created_utc > newLatestTime:
				newLatestTime = comment.created_utc
			if comment.created_utc <= lastCommentTime:
				continue
			body = comment.body.lower()
			if body.find("barry and iris") != -1 or body.find("iris and barry") != -1:
				print comment.id
				replyString = body.replace("barry and iris", "The Flash")
				replyString = replyString.replace("iris and barry", "The Flash")
				replyString = replyString.replace("\n\n", "\n")
				replyString = replyString.replace("\n\n", "\n")
				replyString = replyString.replace("\n\n", "\n")
				replyString = "> " + replyString
				replyString = replyString + "\n\n FTFY"
				print replyString
				comment.reply(replyString)
		f2 = open("LastCommentRead.txt", 'w');
		f2.write(str(int(newLatestTime)))
		f2.close()
		print("Sleeping...")
		time.sleep(30)

b = botLogin()
runBot(b)