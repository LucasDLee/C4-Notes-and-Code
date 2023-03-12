# C4 Preteens Mini Calculator Instructions

## Description

In this final activity, you will be doing it yourselves through a combination of HTML, CSS, and JavaScript. Everything you have learned thus far will be combined into this one activity where you will be making a "Mini Calculator". What it does is you press a button and it will ask you to put in 2 numbers to do a calculation.

You should make a new Repl.it workplace for this final activity. Do not delete anything in HTML when you make a new workplace unless asked to.

## Part 1: HTML

1) Change the title of the website to "Mini Calculator" (look in the ``head`` section)
2) Do the following in the "body" HTML tag in order (and make sure its above ``<script src="script.js"></script>``):
    1) Delete the words "Hello World"
    2) Make a heading 1 with the words "Mini Calculator"
    3) In a paragraph tag, have the following code: ``Your calulation was: <span id="num1">0</span> <span id="operator">&plus;</span> <span id="num2">0</span> = <span id="result">0</span>``
    4) After that, make something called a ``<section id="math"></section>``. Inside of this section, make 4 buttons:
        1) This button will have an *onclick* equal to ``addNumbers()`` with the text ``&plus;``
        2) This button will have an *onclick* equal to ``subtractNumbers()`` with the text ``&minus;``
        3) This button will have an *onclick* equal to ``multiplyNumbers()`` with the text ``&times;``
        4) This button will have an *onclick* equal to ``divideNumbers()`` with the text ``&divide;``
    5) Make a paragraph with the copyright symbol (``&copy;``) with the words "My Website"

## Part 2: JavaScript

## Part 3: CSS

If you see

```css
html, body {
    height: 100%;
    width: 100%;
}
```

then remove it before you begin.
