# N back Game

<p float="left">
  <img width="280" alt="Screenshot 2022-12-15 at 5 19 04 PM" src="https://user-images.githubusercontent.com/96529477/207994238-0635367d-a038-43d1-9bf9-0d5e2d864c72.png">
  <img width="280" alt="Screenshot 2022-12-15 at 5 26 31 PM" src="https://user-images.githubusercontent.com/96529477/207994639-78b21f5a-4a44-4dbb-b528-1039ab67cd8f.png">
  <img width="280" alt="Screenshot 2022-12-15 at 5 27 47 PM" src="https://user-images.githubusercontent.com/96529477/207994648-a2cd124c-866c-49d5-862e-ff3da6b033f1.png">
</p>


# The purpose of the project

### I believe that an individual's intelligence can increase with practice the same way you would exercise and build muscle. I created this game with some hope to improve my intelligence and I want everyone to try this game and get smarter. Or just have fun.

### This game is my first project that I have ever created since I started learning python. I heard that people can make games with [pygame module](https://www.pygame.org/news), and creating games can teach a lot about programming in general so I decided to give it a try.

# What is 'N back'?

Here is some brief information about the game if you'd like to know what 'N back' is.

> The n-back task is a continuous performance task that is commonly used as an assessment in psychology and cognitive neuroscience to measure a part of working memory and working memory capacity. The n-back was introduced by Wayne Kirchner in 1958. N-Back can also be used as a training method to improve working memory and working memory capacity and also increase fluid intelligence.
>
> ...
>
> The n-back task was developed by Wayne Kirchner for his research into short-term memory; he used it to assess age differences in memory tasks of "rapidly changing information".

source - https://en.wikipedia.org/wiki/N-back

# How to play

We can play 2 back, 3 back, 4 back, and so on.. But, let's say we are playing 2 back right now.

In the game, there will be numbers shown to us.

One number will show at a time and will disappear after it is shown.

### `3`

### `5`

### `3`

### `2`

### `4`

We are playing 2 back, we have to memorize two sequence back and if that two sequence back number is the same as the current number, we press `O`, if not press `X`.

In this case, the correct answer would be `O`, `X`, `X`.

|3|5|3|2|4|
|--|--|--|--|--|
| | |O|X|X|

There will be tutorial inside the game for a clearer explanation.

[N - back on Wikipedia](https://en.wikipedia.org/wiki/N-back)

## Key control

'X' : `<` or `mouse click` on 'X' button

'O' : `>` or `mouse click` on 'O' button

In the game, press `ESC` key to pause. `ESC` again to resume.

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

## Download Python. Python should already be installed to play the game.

> If you already have python 3.0 or higher, skip this part. If you don't have python, download python first [https://www.python.org](https://www.python.org/downloads/).

To check the version of the python installed in your computer,

For window user, open command prompt and type

```
python --version
```

For mac user, open terminal and type

```
python3 --version
```

## To play the game, download `pygame` module please.

## 1. Install `pygame`

For **Windows** users, write the code below in the command prompt,

```
py -m pip install -U pygame --user
```

For **Mac** users, write the code below in the terminal

```
python3 -m pip install -U pygame --user
```

or

```
pip3 install pygame --pre
```

for users who use python 3.11.

More information on [https://www.pygame.org](https://www.pygame.org/wiki/GettingStarted)

## 2. Download git (If you downloaded git already, skip this part)

### Download git

> Go to [https://git-scm.com](https://git-scm.com) and download git.

## 3. Create a folder to clone (download) the game files.

### - Create a folder 
or on Command Prompt / Terminal
```
$ mkdir programming
```

### - Open the Command Prompt / Terminal
### - Make sure that you are at folder directory in there and type
```
cd programming
git clone https://github.com/kjs29/nback.git
```
### - You will see that the files are downloaded
### - Open `main.py` and run it.
