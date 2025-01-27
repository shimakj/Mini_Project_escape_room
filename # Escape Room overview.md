# Escape Room 

## First collaborative project from the Data Analytics Bootcamp from Ironhack. 
This project presents a map with four rooms (Game Room, Bedroom 1, Bedroom 2 and Living Rooms), Altough connencted, all of the doors are closed and needs to be unlocked. The objective of this game is to get out of the house by finding and collecting all the keys. 

Done by:
Sheryll Dumapal,
Michele Montalvo,
Shima Kashani Javid,
Ngoc-Phung Dang


## Project Overview 

### How is the game’s structure organized?
The game is organized with game state, rooms (name of the rooms, list of items and furniture in each room, adjacent rooms and the conditions to access them), items and game flow (see flowchart)

### Which functions do you have and how are they imported?

We have the following functions:

1. linebreak():

Purpose: 
This function prints two newline characters for creating a visual separation or break between different outputs in the console.

Usage: 
It helps to organize the visual flow of the text output, making it easier for players to read successive pieces of game text.

2. start_game():

Purpose: 
This function begins your game by setting up the game scenario and starting the first room interaction.

Usage: 
It prints a brief introduction to the game's situation and then calls play_room() with the initial room from the game_state.

3. play_room(room):

Purpose: 
Manages interaction with a room, allowing the player to explore or examine items.

How it Works:
Checks if the current room is the target room.
Provides options for the player to explore the room or examine items.
Calls explore_room() for listing room items or examine_item() to interact with an item.

4. explore_room(room):

Purpose: 
Lists all items present in the specified room.

Usage: 
This function is called within play_room() when the player chooses to explore, providing a list of visible items based on object_relations.
get_next_room_of_door(door, current_room):

Purpose: 
Determines the next room that can be accessed through a specific door.
Usage: Finds and returns a room connected by a given door, excluding the current room. Utilizes object relations to check door associations.

5. examine_item(item_name):

Purpose: 
Offers interactions with items in the room, such as attempting to unlock doors or discovering keys.

How it Works:
Checks if the item belongs to the current room.
Handles actions based on whether the item is a door or contains a key.
Updates game_state with collected keys and navigates to new rooms as appropriate.


### Which features did you add to the game?

//

## Tools
- Jupyter Notebook 
- VSC Code 
- BPMN Flowcharts 

## Technical Challenges (erros & mistakes)
 
#### What was the most important technical challenge you faced?
The most important technical challenge was to collaborate remotely and in real time and quickly get to grips with tools that you didn't even know existed 3 weeks ago.

### How did you overcome that challenge?
Team spirit, determination and good communication helped us overcome this challenge as a team. Researching the errors on Google and utilising the information during our classes. We also utilised AI to explain the errors.

### What was the biggest mistake you made during this project?
Failing to complete all the key variables mostly by omission. Lack of understanding in the nature of certain functions which turned into infinite loops. 

### What did you learn from it?
Attention to detail is vital in order to prevent mistakes and also augmenting the level of understanding of certain functions is key in order to correct mistake in a timely manner.

## Deliverables 
Presentation link: https://docs.google.com/presentation/d/1oYmg2ITy4pBsAfp-pujMsEL3S0EEeaQhwQJwokHyU0M/edit#slide=id.p
Trello link for Project Management: https://trello.com/b/3niexfMu/master-of-errors