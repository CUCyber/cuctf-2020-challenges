#  Discord

The challenge description provides us with some hints on how to approach this challenge.

The key words are `guild`, `attached` and `flag`. 

The source says that the flag is attached to some numbers, these numbers are simply a discord `attachment id` assigned to files attached to messages. 

The format for file attachments in discord is `https://discord.storage.googleapis.com/attachments/channel.id/attachment.id/filename`.

So far, we have `https://discord.storage.googleapis.com/attachments/channel.id/761144056486559744/filename`

Flags are usually in the format `flag.txt`, and since this is an attachment id and holds a file, we will assume for now that the filename is `flag.txt` giving us `https://discord.storage.googleapis.com/attachments/channel.id/761144056486559744/flag.txt`.

The channel id is a bit tricky, we have no idea what channel the attachment was in, or if we even have access to it because it could be restricted behind a role. 

We know the channel must be in the CUCTF Discord server (guild), so we can grab a list of channels and their ids through the API (even private ones) with `https://discordapp.com/api/v6/guilds/741453575573733388/channels`

This will output all channel objects in the given guild, at this point it's a bit of guess and check to figure out which one contained the attachment, enumeration with a script and checking the response should be sufficient. You should find that `753862170537754624` #challenge-devs is the correct channel.

You will then find the correct url is `https://discord.storage.googleapis.com/attachments/753862170537754624/761144056486559744/flag.txt`.

and your flag `CUCTF{You_found_me!}`.
