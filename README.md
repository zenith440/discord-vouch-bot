# Discord Vouch Bot

A Discord bot that allows users to vouch for each other on transactions, services, or items they've bought/sold.

## Features

- **`/vouch`** - Leave a vouch for another user
  - `user` - The user to vouch for
  - `item` - What item/thing did they sell or provide
  - `experience` - How the purchase went (your feedback)

- **`/vouches`** - Check all vouches for a user

## Setup

### 1. Clone the Repository
```bash
git clone https://github.com/zenith440/discord-vouch-bot.git
cd discord-vouch-bot
```

### 2. Install Dependencies
```bash
pip install -r requirements.txt
```

### 3. Create a Discord Bot

1. Go to [Discord Developer Portal](https://discord.com/developers/applications)
2. Click "New Application" and give it a name
3. Go to "Bot" tab and click "Add Bot"
4. Under TOKEN, click "Copy" to copy your bot token
5. Go to "OAuth2" → "URL Generator"
6. Select these scopes: `bot` and `applications.commands`
7. Select these permissions:
   - `Send Messages`
   - `Embed Links`
   - `Read Messages/View Channels`
8. Copy the generated URL and open it to invite the bot to your server

### 4. Configure Environment Variables

1. Rename `.env.example` to `.env`
2. Add your bot token:
```
DISCORD_TOKEN=your_bot_token_here
```

### 5. Run the Bot
```bash
python main.py
```

## Usage

### Leave a Vouch
```
/vouch user: @username item: Gaming Monitor experience: Great seller, fast shipping!
```

### Check Vouches
```
/vouches user: @username
```

## Commands

| Command | Description |
|---------|-------------|
| `/vouch` | Leave a vouch for another user |
| `/vouches` | View all vouches for a user |

## Future Improvements

- [ ] Database integration (SQLite/PostgreSQL)
- [ ] Vouch ratings (1-5 stars)
- [ ] Leaderboard command
- [ ] Negative vouches/reports
- [ ] Vouch verification
- [ ] Statistics dashboard

## License

MIT License
