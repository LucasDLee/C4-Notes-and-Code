# CSS Notes

Here, you'll find my notes regarding basic CSS formatting. CSS is the "look" of our website. Just like a house has a windows, flooring, colour on the walls and so on, so does a website and that website needs to use CSS to make it look nice.

## Background Information

- CSS stands for ***Cascading Style Sheets***
- If you see `/* */`, that is a **comment**. Each coding language has their own form of comments and comments are used as notes to remind yourself (or your peers) what your code does.
- All CSS files ends with ".css". Unlike an HTML file, you cannot open up a CSS file normally.

## Using CSS

### Connecting Your CSS File to Your HTML File

In the "head" of your HTML file, that is where we keep all of our information about our website such as the title and alphabet. We also want to connect any other files that our website might need (like CSS or JavaScript (JS) files). If we don't do that, the CSS we write won't show up on our website. We do that like so:

```html
<!DOCTYPE html>

<html>
    <head>
        <title>My website</title>
        <meta charset="UTF-8">
        <link rel="stylesheet" href="style.css">
    </head>
</html>
```

- `link` looks for a file to connect to
- `rel="stylesheet"` specifies the relationship between the current document and the document you are connecting to
- `href="style.css"` connects to your CSS file
  - `href` looks for the location
  - `"style.css"` is the file's name
  - If your file is in a folder called "Stylings", then you would want to do `<link rel="stylesheet" href="Stylings/style.css">`
    - The `/` means we are going into another folder
    - To go backwards, use `../`. Example: `<link rel="stylesheet" href="../style.css">`

### Basic CSS

All CSS code follows the same format. We need 2 things:

1) **Selector**: This is the HTML tag we want to apply our changes to (e.g. p, img, body, etc.)
2) **Declaration**: We state what part of our HTML tag we want to change (e.g. colour, size, alignment, etc.) and how we are changing it (e.g. red, 16px, center, etc.)

In our declaration, we have 2 more things:

- **Property**: The part we are changing (e.g. colour, size, alignment, etc.)
- **Value**: How we are changing our HTML tag (e.g. red, 16px, center, etc.)
  - All values end with a semi-colon `;`
  - Not having a semi-colon makes errors

This is how we do that:

```css
    /* This first part is how its formatted. 
    Do not actually write these exact words */
    selector {
        property: value;
    }

    /* Examples */

    /* I am changing all paragraphs to the colour of red */
    p {
        color: red;
    }

    /* All unordered lists will not have bullet points anymore */
    ul {
        list-style-type: none;
    }
```

If I want to get something more specific, I have to write the CSS selectors together like so:

```css
    /* All list items in unordered lists will be orange */
    ul li {
        color: orange;
    }

    /* All list items in ordered lists will have a black border around it */
    ol li {
        border: 1px solid black;
    }
```

If you run this code on your computer(s), you'll notice how the list items do not interfere with each other.

### Formatting your Website

When we first make our websites, everything is from top-to-bottom. But what if we wanted to make everything go from left-to-right? We need to either use a `flex` or `grid` for that.

#### Flex

It is for **1-dimensional layouts** and mainly used for mobile devices. They can be used for larger screens like laptops or PCs. Here's how you make it:

```css
    body {
        display: flex;
        flex-direction: column;
    }
```

- We need to use `display: flex` to tell our website we are going to be using flex formatting
- After that, we need to specify a direction for our 1-D layout
- You do not need to display a flex in the body of your website. These stylings can apply to any HTML element.

#### Grid

It is for **2-dimensional layouts** and occasionally used on bigger screens. Here's how you make it:

```css
    body {
        display: grid;
        grid-template-columns: auto auto;
        grid-template-rows: auto auto auto;
    }
```

- We need to use `display: grid` to tell our website we are going to be using grid formatting
- As we are using a grid, we need to specify the number of columns and rows we are using
  - `grid-template-columns` generates these columns. `auto` tells the computer to automatically space the size of that columns. The number of values equals the number of columns
  - `grid-template-columns` generates these rows
  - You can replace `auto` with a specific size like `16px`, `1em`, etc.

### Ids and Classes

Sometimes we just want to apply a specific CSS styling to a word or a phrase. For that, we can use classes and ids to get around that

- Classes start with a dot `.`
- Ids start with a `#`
- The difference is that classes can be used as many times as you want but an id can only be used once on an HTML page

For example:

- `#locker` is an id called "locker"
- `.school` is a class called "school"

To apply classes and ids, we need to first apply it to HTML elements like so:

```html
<!DOCTYPE html>

<html>
    <body>
        <p>Hello, my name is <span id="my-name">Lucas</span> and I work at <span class="workplace">City Centre Community Centre</span>.</p>
        <p>The <span class="workplace">City Centre Community Centre</span> is located in Richmond</p>
    </body>
</html>
```

The `span` HTML element is used to find specific words or images and apply specific stylings to it. Next, we have to make our CSS:

```css
    p {
        color: blue;
    }

    .workplace {
        color: green;
    }

    #my-name {
        color: red;
    }
```

That's it. Run this code yourself and notice how all of my paragraphs are blue but when we get to my workplace or my name, it changes colour accordingly.
