# Quest: Escape Room 

# You woke up on the couche. 
# Unlock Door A with the key at the Piano 
# Bedroom 1 has door A, B and C. Underneath the queen bed is a key to go through door B. Unlock door B. 
# Bedroom 2 has a double bed, a dresser and door B. Hidden under the double bed is the key for door C. WIthin the dresser is a key for door D. 
# Living Room. Exploration reveals a dining table, Door C, and Door D. With the key for Door D in your grasp, you unlock it. Ourside is the freedom

####### Defining rooms #######

living_room = {
    "name": "living room", 
    "type": "room", 
    "description" : "a big room with a big sofa and a TV", 
    "items": ["sofa", "tv"], 
    "position": "east"}

game_room = {
    "name": "game room", 
    "type": "room", 
    "description": "a room with a piano", 
    "items": ["piano"], 
    "position": "west"}

bedroom = {
    "name": "bedroom", 
    "type": "room", 
    "description": "a room with a bed", 
    "items": ["bed"], 
    "position": "north"}

bathroom = {
    "name": "bathroom", 
    "type": "room", 
    "description": "a room with a shower and a toilet", 
    "items": ["showe", "toilet"], 
    "position": "south"}

game_room = {
    "name": "game_room", 
    "type": "room"}

bedroom_1 = {
    "name": "bedroom_1", "type" : "room"}

bedroom_2 = {
    "name": "bedroom_2", 
    "type": "room"}

livingroom = {"name": "livingroom", "type" : "room"}
####### Definining items #######

couch = {
    "name": "couch",
    "type": "item"}

piano = {
    "name": "piano", 
    "type": "item"}

double_bed = {
    "name": "double_bed", 
    "type" : "item"}

queen_bed = {
    "name": "queen_bed", 
    "type" : "item"}

dresser = {
    "name":"dresser",
    "type" : "item"}

dining_table = {
    "name":"dining_table",
    "type" : "item"}

####### Doors #######

door_a = {
    "name": "door_a", 
    "type": "door"}

door_b = {
    "name": "door_b", 
    "type": "door"}

door_c = {
    "name": "door_c", 
    "type": "door"}

door_d = {
    "name": "door_d", 
    "type": "door"}

key_a = {"name": "key_a", "type": "key", "target" : door_a}
key_b = {"name": "key_b", "type": "key", "target" : door_b}
key_c = {"name": "key_c", "type": "key", "target" : door_c}
key_d = {"name": "key_d", "type": "key", "target" : door_d}

outside = {"name": "outside"}

all_rooms = [game_room,bedroom_1,bedroom_2,livingroom, outside]
all_doors = [door_a,door_b,door_c,door_d]

object_relations = {
    "game_room": [couch, piano, door_a],
    "piano": [key_a],
    "door_a": [game_room, bedroom_1],

    "bedroom_1": [queen_bed, door_a, door_b, door_c],
    "queen_bed": [key_b],
    "door_b": [bedroom_1, bedroom_2],

    "bedroom_2": [double_bed, dresser, door_b],
    "double_bed": [key_c],
    "dresser": [key_d],
    "door_c": [bedroom_1, livingroom],

    "livingroom": [dining_table, door_c, door_d],
    "dining_table": [],
    "door_d": [livingroom, outside],

    "outside": [door_d]
}

INIT_GAME_STATE = {
    "current_room": game_room,
    "keys_collected": [],
    "target_room": outside,
    "Alive": True 
}

game_state = INIT_GAME_STATE
def linebreak():
    """
    Print a line break
    """
    print("\n\n")

def start_game():
    """
    Start the game
    """
    print("You wake up on a couch and find yourself in a strange house with no windows which you have never been to before.")
    print("You don't remember why you are here and what had happened before. You feel some unknown danger is approaching and you must get out of the house, NOW!")
    play_room(game_state["current_room"])

def play_room(room):
    """
    Play a room. First check if the room being played is the target room.
    If it is, the game will end with success. Otherwise, let player either 
    explore (list all items in this room) or examine an item found here.
    """
    game_state["current_room"] = room
    if (game_state["current_room"] == game_state["target_room"]):
        print("Congrats! You escaped the room!") 
    else:
        print("You are now in " + room["name"])
        intended_action = input("What would you like to do? Type 'explore' or 'examine'?").strip()
        if intended_action == "explore":
            explore_room(room)
            play_room(room)
        elif intended_action == "examine":
            examine_item(input("What would you like to examine?").strip())
            if examine_item in {"piano", "double_bed", "queen_bed", "dresser"}:
                print("you found the key to unlock the door")
        else:
            print("Not sure what you mean. Type 'explore' or 'examine'.")
            play_room(room)
        linebreak()

def explore_room(room):
    """
    Explore a room. List all items belonging to this room.
    """
    items = [i["name"] for i in object_relations[room["name"]]]
    print("You explore the room. This is " + room["name"] + ". You find " + ", ".join(items))

def get_next_room_of_door(door, current_room):
    """
    From object_relations, find the two rooms connected to the given door.
    Return the room that is not the current_room.
    """
   # connected_rooms = object_relations[door["name"]]
   # for room in connected_rooms:
   #     if(not current_room == room):
   #         return room

    return next(room for room in object_relations[door["name"]] if room != current_room)

def examine_item(item_name):
    """
    Examine an item which can be a door or furniture.
    First make sure the intended item belongs to the current room.
    Then check if the item is a door. Tell player if key hasn't been 
    collected yet. Otherwise ask player if they want to go to the next
    room. If the item is not a door, then check if it contains keys.
    Collect the key if found and update the game state. At the end,
    play either the current or the next room depending on the game state
    to keep playing.
    """
    current_room = game_state["current_room"]
    next_room = ""
    output = None
    
    for item in object_relations[current_room["name"]]:
        if(item["name"] == item_name):
            output = f"You examine {item_name}. "
            if (item["type"] == "door"):
                have_key = False 
                for key in game_state["keys_collected"]:
                    if(key["target"] == item):
                        have_key = True
                if (have_key):
                    output += "You unlock it with a key you have."
                    next_room = get_next_room_of_door(item, current_room)
                else:
                    output += "It is locked but you don't have the key."
            else:
                if(item["name"] in object_relations and len(object_relations[item["name"]])>0):
                    item_found = object_relations[item["name"]].pop()
                    game_state["keys_collected"].append(item_found)
                    output += "You find " + item_found["name"] + "."
                else:
                    output += "There isn't anything interesting about it."
                print(output)
            break
        
    if(output is None):
        print("The item you requested is not found in the current room.")
    
    if(next_room and input("Do you want to go to the next room? Enter 'yes' or 'no'").strip() == 'yes'):
        play_room(next_room)
        if next_room == outside:
            print("You won the game!")
    else:
        play_room(current_room)   

start_game()
