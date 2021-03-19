import spotipy;
import spotipy.util as util
import discord;
import os;

scope = "user-library-read"
user = input("Enter Name: ")
token = util.prompt_for_user_token(user, scope, os.environ.get('SPOTIFY_GROOVYMIDDLEWARE_CLIENT_PUBLIC'),
									os.environ.get('SPOTIFY_GROOVYMIDDLEWARE_CLIENT_PRIVATE'), 'http://localhost:8888/callback')


class MyClient(discord.Client):
    async def on_message(self, message):
        if message.author == self.user:
            return

        if message.content.startswith('$hello'):
            await message.channel.send('Hello World!');


client = MyClient();
client.run(os.environ.get('DISCORD_GROOVYMIDDLEWARE_TOKEN'));