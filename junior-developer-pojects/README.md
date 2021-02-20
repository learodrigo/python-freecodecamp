# 11 Python Projects Junior Developers Can Build for Coding Practice

Before starting, check that you understand how to do this:
* declare variables
* collect user input
* store information
* repeat an action through loops
* write functions to repeat blocks of code


## 1. Odd or even

Welcome a user then ask them for a number between 1 and 1000.
When the user gives you the number, you check if it's odd or even and then you print a message letting them know.

Example:
* Prompt: `What number are you thinking?`
* Input:  `25`
* Output: `That's an odd number! Have another?`

## 2. Mad libs game

Ask the user for an input.

This could be anything such as a name, an adjective, a pronoun or even an action. Once you get the input, you can rearrange it to build up your own story.

* Here's [youtube tutorial on mad libs in Python](https://www.youtube.com/watch?v=u7g9mRzQLYE)
* And [example code](https://github.com/ChalzZy/Mad-Libs-Generator/blob/master/Mad_Libs_Generator/main.py) on Github

## 3. Word count

Ask the user what's on their mind. Then after the user responds, count the number of words in the sentence and print that as an output.

Example:
* Prompt: `what's on your mind today?`
* Input: `well, it's just a day for me to be an expert in coding`
* Output: `oh nice, you just told me what's on your mind in 13 words!`

To take this a step further, open a file that is handed to you, count the number of words in there, then print it out.

## 4. Biography info

Ask a user for their personal information one question at a time. Then check that the information they entered is valid. Finally, print a summary of all the information they entered back to them.

Example: What is your name? If the user enters `*` you prompt them that the input is wrong, and ask them to enter a valid name.

At the end you print a summary that looks like this:
<br />
<br />
```
- Name: John Doe
- Date of birth: Jan 1, 1954
- Address: 24 fifth Ave, NY
- Personal goals: To be the best programmer there ever was.
```
<br />

## 5. What's my acronym?

Ask the user to enter the full meaning of an organization or concept and you'll provide the acronym to the user. For example:

* Input -> `As Soon As Possible`. Output -> `ASAP`.
* Input -> `World Health Organization`. Output -> `WHO`.
* Input -> `Absent Without Leave`. Output -> `AWOL`.

## 6. Rock, Paper, Scissors

This is a popular game played between two people. Each player gets to form one of three shapes using their hand:

* `rock` (a closed fist)
* `paper` (a flat hand)
* `scissors` (a fist with the index finger and middle finger extended, forming a V)

## 7. Guess the number

ou ask a user to guess a number between 1 and 50.

If they guess outside that range, you prompt with an error encouraging them to choose a number within the proper range.

Whenever they guess the wrong number you ask if they want to keep playing or if they'd like to quit.

Finally, when the user eventually guesses the right number you congratulate them and show the number of attempts they had.

## 8. Is a palindrome

Ask the user to give you five words. Then check if any of the five words is a palindrome.

A palindrome is a word that remains the same whether it's read forward or backward.

Example:

* `madam` is a palindrome.
* so is `malayalam`.
* But not `geeks`.

## 9. Calculate the tip

Your goal is to find out exactly how much tip you should give after receiving a service. In this scenario, ask for the total bill. Then display the tip for 18%, 20% and 25%.

Example:

* Prompt: `what's the total bill for today, please?`
* Input: `$55.87`
* Output: `18% tip is $10.06, which brings your total to $65.93`

Remember you want to be nice, so don't forget to round up. To push this more, ask for the number of people involved, then evenly split the tip and total cost among them.

To go even a step further, split unevenly (for example, one person pays 70% of the bill while the other pays 30%)

## 10. Email slicer

Collect an email address from the user and then find out if the user has a custom domain name or a popular domain name. For example:

* Input: `mary.jane@gmail.com`
* Output: `Hey Mary, I see your email is registered with Google. That's cool!.`
* Input: `peter.pan@myfantasy.com`
* Output: `Hey Peter, looks like you've got your own custom setup at MyFantasy. Impressive!`

This is a convenient python project that has a lot of use in the future. The program helps get you the username and domain name from an email address.

If you want to push this further, you can customize the application and send a message to the host with this information.

## 11. Lyrics generator

Ask a user to choose from a list of 10 songs. When the user does, you print out the lyrics to the song they selected.

Example:

```
Welcome, please select a select a song from this top 10 songs:

1. Baby by Bieber
2. Hotline Bling by Drake
3. Flawless by Beyonce
4. Fall by Eminem...
```

<br />

```
You chose Flawless by Beyonce. Here you go:

------- Flawless by Beyonce ------------
I'm out that H, town coming coming down
I'm coming down, drippin' candy on the ground
H, Town, Town, I'm coming down, coming down
Drippin' candy on the ground...

Press * to choose again.
```

To push it further, have at least 3 songs by the same artist.

Next, ask the user to put the name of the artist so you can show them only options by that artist. Then the user can select a specific song from that list.

<br />
<br />
<br />

All the exercises were taken from [a freecodecamp article](https://www.freecodecamp.org/news/python-projects-junior-developers/) from [Endy Austin](https://twitter.com/LifeTechPsych).
