class SocialMediaProfile:
    def __init__(self, username):
        self.username = username
        self.posts = []

    def add_post(self, content):
        post = content.split(",")
        self.posts.append(post)
        print(f"{self.username} added a new post: {content}")

    def display_timeline(self):
        print(f'Your username is:{self.username}')
        print(f'Your posts are: {self.posts}')

john = SocialMediaProfile('johndoe')
john.add_post("Hello, World!, Had a great day at the park!, What's up Natalie? How are you?")

