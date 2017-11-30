class Tweet:
    def __init__(self, s, i):
        self.status=s
        self.imageName = i;


def printTweetToConsole(tw):
    print tw.status
