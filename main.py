import discord
from discord.ext import commands
from discord import app_commands
import os
from dotenv import load_dotenv

# Load environment variables
load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')

# Create bot with intents
intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix="!", intents=intents)

# Store vouches in memory (you can upgrade to a database later)
vouches = {}

@bot.event
async def on_ready():
    print(f'{bot.user} has connected to Discord!')
    try:
        synced = await bot.tree.sync()
        print(f'Synced {len(synced)} command(s)')
    except Exception as e:
        print(e)

@bot.tree.command(name="vouch", description="Leave a vouch for another user")
@app_commands.describe(
    user="The user to vouch for",
    item="What item/thing did they sell or provide",
    experience="How the purchase went (your feedback)"
)
async def vouch(
    interaction: discord.Interaction,
    user: discord.User,
    item: str,
    experience: str
):
    """Leave a vouch for another user"""
    
    # Prevent vouching yourself
    if user == interaction.user:
        await interaction.response.send_message(
            "❌ You cannot vouch for yourself!",
            ephemeral=True
        )
        return
    
    # Initialize user vouch list if they don't have one
    if user.id not in vouches:
        vouches[user.id] = []
    
    # Add the vouch
    vouch_data = {
        "voucher": interaction.user,
        "item": item,
        "experience": experience,
        "timestamp": interaction.created_at
    }
    vouches[user.id].append(vouch_data)
    
    # Create embed for the vouch
    embed = discord.Embed(
        title="✅ New Vouch!",
        description=f"{interaction.user.mention} vouches for {user.mention}",
        color=discord.Color.green()
    )
    embed.add_field(name="📦 Item/Service", value=item, inline=False)
    embed.add_field(name="📝 Experience", value=experience, inline=False)
    embed.add_field(name="⭐ Total Vouches", value=str(len(vouches[user.id])), inline=True)
    embed.set_footer(text=f"Requested by {interaction.user}")
    embed.timestamp = interaction.created_at
    
    await interaction.response.send_message(embed=embed)

@bot.tree.command(name="vouches", description="Check vouches for a user")
@app_commands.describe(user="The user to check vouches for")
async def check_vouches(interaction: discord.Interaction, user: discord.User):
    """Check all vouches for a user"""
    
    if user.id not in vouches or len(vouches[user.id]) == 0:
        embed = discord.Embed(
            title=f"📊 Vouches for {user.name}",
            description="No vouches yet!",
            color=discord.Color.greyple()
        )
        await interaction.response.send_message(embed=embed, ephemeral=True)
        return
    
    user_vouches = vouches[user.id]
    
    # Create main embed
    embed = discord.Embed(
        title=f"📊 Vouches for {user.name}",
        description=f"Total vouches: **{len(user_vouches)}**",
        color=discord.Color.blue()
    )
    
    # Add vouches (limit to 25 fields to avoid embed limits)
    for i, vouch in enumerate(user_vouches[-25:], 1):
        embed.add_field(
            name=f"Vouch #{len(user_vouches) - 25 + i} - {vouch['voucher'].name}",
            value=f"**Item:** {vouch['item']}\n**Feedback:** {vouch['experience']}",
            inline=False
        )
    
    embed.set_thumbnail(url=user.avatar.url if user.avatar else None)
    
    await interaction.response.send_message(embed=embed, ephemeral=True)

# Run the bot
bot.run(TOKEN)
