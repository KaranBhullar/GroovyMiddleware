import spotipy;
from spotipy.oauth2 import SpotifyClientCredentials
import discord;
import os;

clientID = os.environ.get('SPOTIFY_GROOVYMIDDLEWARE_CLIENT_PUBLIC');
clientPrivate = os.environ.get('SPOTIFY_GROOVYMIDDLEWARE_CLIENT_PRIVATE');
spotify = spotipy.Spotify(client_credentials_manager=SpotifyClientCredentials());

class MyClient(discord.Client):
    async def on_message(self, message):
        if message.author == self.user:
            return

        if message.content.startswith('$hello'):
            await message.channel.send('Hello World!')
			

client = MyClient();
client.run(os.environ.get('DISCORD_GROOVYMIDDLEWARE_TOKEN'));