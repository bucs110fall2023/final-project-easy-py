[![Open in Visual Studio Code](https://classroom.github.com/assets/open-in-vscode-718a45dd9cf7e7f842a935f5ebbe5719a5e09af4491e668f4dbf3b35d5cca122.svg)](https://classroom.github.com/online_ide?assignment_repo_id=12803291&assignment_repo_type=AssignmentRepo)
:warning: Everything between << >> needs to be replaced (remove << >> after replacing)

#  Easy-py 
## CS110 Final Project   fall, 2023 

## Team Members

Chuma Ogwulumba, Joshua Medina

***

## Project Description

An rpg with stats attack options, and a modicum of plot

***    

## GUI Design

### Initial Design

![initial gui](assets/gui.jpg)

### Final Design

![final gui](assets/finalgui.jpg)

## Program Design

### Features

1.  moveable character 
2.  boss battles  
3.  scrolling text
4.  in battle narration
5.  save data 

### Classes

- Unit: Template for the Hero and Enemy class. Holds the stats for the RPG unit and can attact another unit.
- Hero: Inherites from Unit can accumulate Exp for a level up and when hp reaches zero a boolean is returned for a game over.
- Enemy: Inherites from Unit and holds an Exp value and when hp reaches zero a boolean is returned for vicotry.

## ATP

Test Case 1: Save management

    Test steps:
    1. Press Start through the title screen.
    2. Press a number on the keyboard for a save.
    3. verify that the savefile is selectable and is altered when the file is written to.
    Expected Outcome: The player should be able to select a file and the file is changed when the player saves.

Test Case 2: Player movement

    Test steps:
    1. Get to the overworld in the game.
    2. press the left, up, down, right arrow keys.
    3. verify the the character the player controls moves in the respective direction.
    Expected Outcome: The player should be able to move the character in accordence to the arrow key inputs given.

Test Case 3: Scrolling text
    Test steps:
    1. Get past save selection and start the game.
    2. read the story scrolling upwards (like Star Wars).
    3. verify that all of the text is there and in the correct order.
    Expected Outcome: The player should be able to read and understand the story by plain observation after entering it.

Test Case 4: Conflict Resolution
    Test steps;
    1. Enter into and RPG battle.
    2. Select the attack option.
    3. verify that the enemy's health goes down.
    4. Get the enemy's health to 0.
    5. verify that the battle ends in player victory.
    6. the enemy attacks the player character.
    7. verify that the player's health goes down.
    8. the enemy gets the player's health to go to 0.
    9. verify the battle ends in a gameover.
    Expected Outcome: The battle should terminated when either combatants health goes to zero and go to the appropriate screen in accordance with the player's success.


