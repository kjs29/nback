# N back Game

<p float="left">
  <img width="250" alt="Screenshot 2022-12-15 at 5 19 04 PM" src="https://user-images.githubusercontent.com/96529477/207994238-0635367d-a038-43d1-9bf9-0d5e2d864c72.png">
  <img width="250" alt="Screenshot 2022-12-15 at 5 26 31 PM" src="https://user-images.githubusercontent.com/96529477/207994639-78b21f5a-4a44-4dbb-b528-1039ab67cd8f.png">
  <img width="250" alt="Screenshot 2022-12-15 at 5 27 47 PM" src="https://user-images.githubusercontent.com/96529477/207994648-a2cd124c-866c-49d5-862e-ff3da6b033f1.png">
</p>


# The purpose of the project

### There are probably several aspects of one's intelligence.

### I believe that an individual's intelligence can increase with practice the same way you would exercise and build muscle. I was watching a show that introduced this game called 'N back' and it looked challenging but interesting.

### This game is my first project after learning Python. I heard that people can make games with [pygame](https://www.pygame.org/news), and creating games can teach a lot about programming in general so I decided to give it a try.

# What is 'N back'?

### The n-back game is a fun and challenging brain exercise. 

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

source - https://en.wikipedia.org/wiki/N-back

# How to play

We can play 2 back, 3 back, 4 back, and so on.. The higher the N is, more difficult it gets!

But, let's say we are playing 2 back right now.

In the game, there will be numbers shown to us.

One number will show at a time and will disappear after it is shown.

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

'X' : `<(Left Key)` or `mouse click` on 'X' button

'O' : `>(Right Key)` or `mouse click` on 'O' button

In the game, press `ESC` key to pause. `ESC` again to unpause or resume the gameplay.

## Game Menu

- Start

- How to play

- Credits

- Options

    - #N (2~6)

    - Number of questions (Low, Med, High)
        > Low : #N * 2
        >
        > Med : #N * 4
        >
        > High : #N * 6

- Exit

---

# Download the game 

## Clone the repo from Github (Windows, MacOS)

On your terminal type the commands below

```
cd ~/Desktop
mkdir pygame_nback
cd pygame_nback
python3 -m venv env
source env/bin/activate
git clone https://github.com/kjs29/nback.git
cd nback
pip install -r requirements.txt
python main.py
```

## Download from itch.io (Windows only)

https://kjs29.itch.io/nback

