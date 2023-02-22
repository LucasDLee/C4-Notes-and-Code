# Activity Instructions

## Event Listeners in JavaScript

Event listeners in JavaScript are quite hard to fully understand. We'll want to follow some steps to try it out ourselves. In this activity, we're going to ask the user for a title and then display it on our website:

1) HTML
    1) Make a heading 1 (h1) in HTML with any sort of text you like in it. Assign an id called *"title"* to the h1 you just made.
    2) Make a button in HTML with any sort of text you want in it. Attach a function called ``"findTitle()"`` to the button through an onclick item (``onclick="findTitle()"``)
2) JS
    1) Go to your JavaScript file and make a variable called ``getTitle`` and attach it to your h1 HTML element by its ID
    2) Make a function called ``findTitle()``. This function takes no parameters. Put your ``getTitle`` variable in ``findTitle()``
    3) In the function, make a variable called ``yourTitle`` and assign it a prompt with the words "What is your title?"
        1) Note that a ``prompt()`` **returns** whatever the user inputs
    4) Change the innerHTML of your getTitle variable so that it is equal to the answer your user answers in the prompt
    5) The end. Try it out yourself to make sure it's working!
