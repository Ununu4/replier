import click

# Define a dictionary with stage-text mappings
stage_messages = {
    "welcome challenge": "Hey {name}! Lauren Here! So excited to have you on the challenge! 🧡 Are you also a fellow career-driven mom?",
    "yes challenge": "Awesome! Just making sure you got the most out of what we share!😊",
    "goals?": "Any current fitness goals you are pursuing, {name}?",
    "goal!": "Solid goals, {name}! Loving that drive. ",
    "awesome past": "Awesome! Liking those goals already, momma. Now, what have you tried before to make them work?",
    "awesome past 2": "Awesome, liking those goals already, momma! Now, What have you tried before that has given effective results on them",
    "mindset": "Have you considered trying mindset coaching to create a simple and sustainable way to tackle those goals for good, {name}?🤔",
    "strategy": "Nice, all those activities definitely can be integrated into a structure that can be flexible, but still solid enough to keep you on track, momma. Our moms deploy similar strategies all the time.",
    "get it": "I get that you haven't heard of it, tho. Sadly, the importance of mindset in fitness isn't talked about enough outside of sports. And its funny because the stakes out here in the real world are even higher, you know?",
    "clarity call": "You know {name}, we do have a 15-min clarity call available with one of my coaches for depth. She is amazing and will guide you on what we do here and how we can help. Makes sense if I leave my calendar here for it?😊",
    "calendar win": "Awesome!! You can go ahead and select your best time here: https://api.leadconnectorhq.com/widget/booking/1sbsyzMlP8EUoq7H3XGi and I will see it on my end!🥳",
    "done": (
        "Just saw your appointment come in {name}! Super excited to hear more about you!🥳 "
        "If you haven't joined my FB community, you can join here <3: https://www.facebook.com/groups/strongmommovement "
        "After that, please make sure you watch this video so you can have an idea of what we do here and what we’re going to be talking about on the call! "
        "https://www.facebook.com/100008001136700"
    ),
    "calendar fu": "Hey, {name}! I just got some time to get back to you. Sorry about that! Did you have a chance to check the calendar and book the call? I haven't seen your name come in yet.💎",
    "no show": (
        "Hey, {name}! We weren't able to reach you for our call! 💔 Hope everything is alright! "
        "I am going to forward our team calendar link, so you can pick a new time to connect. "
        "https://api.leadconnectorhq.com/widget/booking/1sbsyzMlP8EUoq7H3XGi 💫 "
    ),
    "1x fu": "Hey there, {name}! Bumping this message to the top of your inbox as I know how crazy it all can get💎",
    "3x fu": "Hey {name}! Are you still interested in hearing more about the program, momma? 💎",
    "ads inbound": "Hey {name}! I noticed your comment on my post. I wanted to personally invite you to join the Strong Mom Facebook Group. It's an awesome community for career-driven moms who are looking to feel their best and navigate life's challenges together. Would you like to join? 💎",
    "delay": "So sorry for the delayed reply, {name}! Lots of messages coming my way, but haven't forgotten about you, momma.💎",

}

def generate_message(date):
    name = click.prompt("Enter LEAD name")
    stage = click.prompt("Select CONVO stage", type=click.Choice(stage_messages.keys()))

    # Retrieve the message based on the selected stage
    message = stage_messages[stage]

    # Replace the "{name}" placeholder with the provided name
    message = message.format(name=name)

    # Print the formatted message with the provided date
    click.echo(f"Event Date: {date}")
    click.echo(message)

if __name__ == "__main__":
    date = click.prompt("Enter the event date")
    while True:
        generate_message(date)
        choice = click.prompt("Do you want to add another message? (yes/no)", default="no")
        if choice.lower() != "yes":
            break
