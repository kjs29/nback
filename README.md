# N back Game

<p float="left">
  <img width="250" alt="Screenshot 2022-12-15 at 5 19 04 PM" src="https://user-images.githubusercontent.com/96529477/207994238-0635367d-a038-43d1-9bf9-0d5e2d864c72.png">
  <img width="250" alt="Screenshot 2022-12-15 at 5 26 31 PM" src="https://user-images.githubusercontent.com/96529477/207994639-78b21f5a-4a44-4dbb-b528-1039ab67cd8f.png">
  <img width="250" alt="Screenshot 2022-12-15 at 5 27 47 PM" src="https://user-images.githubusercontent.com/96529477/207994648-a2cd124c-866c-49d5-862e-ff3da6b033f1.png">
</p>

# Download the game 

## Method 1 - Clone the repo from Github (MacOS or Windows)

Copy & Paste the following code below in your terminal.

The game will be downloaded in the folder named `~/Desktop/pygame_nback`, wait a few seconds, and it will start playing automatically.

<em>MacOS or Linux</em>

```
cd ~/Desktop && mkdir pygame_nback && cd pygame_nback
python3 -m venv env && source env/bin/activate
git clone https://github.com/kjs29/nback.git
cd nback && pip install -r requirements.txt && python main.py
```

<em>Windows</em>

Replace <username> with your own username.

```
cd C:\Users\<username>\Desktop && mkdir pygame_nback && cd pygame_nback
python -m venv env && .\env\Scripts\activate
git clone https://github.com/kjs29/nback.git
cd nback && pip install -r requirements.txt && python main.py
```

## Method 2 (Windows only for now) - Download from itch.io

1. Go to https://kjs29.itch.io/nback and click download button

2. Unzip the file you downloaded 

3. Run `main.exe` file

## How to run the game once the game is downloaded

<em>MacOS or Linux</em>

Go to terminal and type

```
cd ~/Desktop/pygame_nback && python main.py
```

<em>Windows</em>

Replace <username> with your own username.

```
cd C:\Users\<username>\Desktop\pygame_nback && python main.py
```

# The purpose of the project

TLDR; 1. To increase intelligence 2. To have fun with my Python knowledge

### There are probably several aspects of one's intelligence, but I believe that an individual's intelligence can increase with practice the same way you would exercise and build muscle. I was watching a show that introduced this game called 'N back' as a brain activity to increase one's IQ.

### This game is my first project after learning the basics of Python. I heard that people can make games with [pygame](https://www.pygame.org/news), and creating games can teach a lot about programming in general so I decided to give it a try.

# What is 'N back'? Can you tell me how to play it?

## What is N back?

#### The n-back game is a fun and challenging brain exercise. 

The game involves remembering a sequence of items (like colors, letters, or shapes) that are presented to you, one at a time, 

and then recalling an item that occurred "n" positions back in the sequence.

For example,

if the game is set to "2-back," you'll need to remember the current item, as well as the item that appeared two positions back. 

If the current item is a blue square, and two items back was a red triangle, you would need to remember "red triangle" as your response.

As you get better at the game, you can increase the "n" value to make it more challenging. 

It's a great way to exercise your memory and attention skills, and can be a fun way to challenge yourself and see how far you can go!



> The n-back task is a continuous performance task that is commonly used as an assessment in psychology and cognitive neuroscience to measure a part of working memory and working memory capacity. The n-back was introduced by Wayne Kirchner in 1958. N-Back can also be used as a training method to improve working memory and working memory capacity and also increase fluid intelligence.
>
> ...
>
> The n-back task was developed by Wayne Kirchner for his research into short-term memory; he used it to assess age differences in memory tasks of "rapidly changing information".

> source - https://en.wikipedia.org/wiki/N-back

## How to play 

We can play 2 back, 3 back, 4 back, and so on.. The higher the N is, more difficult the game gets!

But, for now let's say we are playing 2 back right now.

In the game, there will be numbers shown to us, the order matters so you should memorize both the number and the order as well.

One number will show at a time for 5 seconds and will disappear after 5 secs.

### `3`

### `5`

### `3`

### `2`

### `4`

We are playing 2 back, we have to memorize two sequence back and if that two sequence back number is the same as the current number, we press `O`, if not press `X`.

In this case, the correct answer would be `O` (3 == 3), `X` (5 != 2), `X` (3 != 4). 

|3|5|3|2|4|
|--|--|--|--|--|
| | |O|X|X|

There will be tutorial inside the game for a clearer explanation.

Or here is the detailed explanation from Wikipedia.org. [N - back on Wikipedia](https://en.wikipedia.org/wiki/N-back)

## Key control

In Game:

`<(Left Key)` or `mouse click`: Click on 'X' button.

`>(Right Key)` or `mouse click`: Click on 'O' button.

`ESC`: Pause the game. `ESC` again to unpause or resume the gameplay.

Game Menu:

Upkey, Downkey to move up/down in the menu.

`ESC` key to exit the game.

## Game Menu

- Start

- How to play

- Credits

- Options

    - #N (2~6)

    - Number of questions (Low, Med, High)
        > Low : #N * 2
        > 
        > For example, if #N = 4 then there will be 8 arbitrary numbers. 
        >
        > Med : #N * 4
        >
        > High : #N * 6

- Exit

---
If you have any questions, please contact me at jsk.jinsung@gmail.com
