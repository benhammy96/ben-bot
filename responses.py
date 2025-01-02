from random import choice, randint

# Initialize the game state globally
game_state = {}

def get_response(user_input: str) -> str:
    #I can replace this with my own logic to get the chatbot to talk to me

    global game_state
    lowered: str = user_input.lower().strip()

    # Handle no input
    if lowered == '':
        return 'Well, you\'re awfully quiet...'


    # Starting the game
    if 'start game' in lowered:
        game_state = {'step': 1}
        return (
            "Welcome to the adventure game! 🚀\n"
            "You find yourself at the entrance of a dark cave. Do you:\n"
            "1. Enter the cave\n"
            "2. Walk away"
        )

    # Game logic: Step 1
    if game_state.get('step') == 1:
        if '1' in lowered or 'enter' in lowered:
            game_state['step'] = 2
            return (
                "You step into the cave, and it's eerily quiet. Suddenly, you hear a growl in the distance. Do you:\n"
                "1. Investigate the growl\n"
                "2. Look for another path"
            )
        elif '2' in lowered or 'walk away' in lowered:
            game_state = {}  # Reset game state
            return "You decide it's best not to mess with mysterious caves. Game over! Type 'start game' to play again."

    # Game logic: Step 2
    if game_state.get('step') == 2:
        if '1' in lowered or 'investigate' in lowered:
            game_state['step'] = 3
            return (
                "You cautiously approach the source of the growl and find a wounded wolf. Do you:\n"
                "1. Help the wolf\n"
                "2. Back away slowly"
            )
        elif '2' in lowered or 'look for another path' in lowered:
            game_state['step'] = 4
            return (
                "You find another path that leads to a shimmering treasure chest. Do you:\n"
                "1. Open the chest\n"
                "2. Leave it alone"
            )

    # Game logic: Step 3 (Helping the wolf)
    if game_state.get('step') == 3:
        if '1' in lowered or 'help' in lowered:
            game_state = {}  # Reset game state
            return "The wolf licks your hand and leads you to a hidden treasure. You win! 🎉 Type 'start game' to play again."
        elif '2' in lowered or 'back away' in lowered:
            game_state = {}  # Reset game state
            return "You back away, but the wolf chases you out of the cave. Game over! Type 'start game' to try again."

    # Game logic: Step 4 (Treasure chest)
    if game_state.get('step') == 4:
        if '1' in lowered or 'open' in lowered:
            game_state = {}  # Reset game state
            return "The chest contains a cursed amulet! You feel yourself turning into stone. Game over! Type 'start game' to play again."
        elif '2' in lowered or 'leave' in lowered:
            game_state = {}  # Reset game state
            return "You wisely leave the chest untouched and escape safely. You win! 🎉 Type 'start game' to play again."

    # Regular responses for non-game-related input
    elif 'hello' in lowered:
        return 'Hello there! Type "start game" to begin a fun adventure!'
    elif 'bye' in lowered:
        return 'Goodbye! Come back soon for another adventure!'
    else:
        return 'I didn\'t understand that. Type "start game" to begin an adventure or say hello!'