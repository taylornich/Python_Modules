def mood_response(mood):
    responses = {
        'happy' : "That's great to hear!",
        'excited' : "That's great to hear!",
        'sad' : "I'm sorry to hear that, I hope your day gets better!",
        'unhappy' : "I'm sorry to hear that, I hope your day gets better!",
        'depressed': "I'm sorry to hear that, I hope your day gets better!",
        'angry' : "Oh no! Take some deep breaths, nothing is worth the energy.",
        'upset' : "Oh no! Take some deep breaths, nothing is worth the energy.",
        'bored' : "Try something new that can occupy your time!"
    }
    
    return responses.get(mood, "Well I hope the rest of your day is fantastic!")
    
