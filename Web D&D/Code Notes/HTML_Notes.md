# HTML Notes

Here, you'll find my notes regarding basic HTML formatting. HTML is the "bones" of our website. Just like a house has a framework, so does a website and that website needs to use HTML as its framework.

## Background Information

- HTML stands for "HyperText Markup Language" and is technically not considered as a programming language
- Almost all websites on the internet employ HTML to deliver their content to their users
- If you see `<!-- -->`, that is a **comment**. Each coding language has their own form of comments and comments are used as notes to remind yourself (or your peers) what your code does.
  - Think about what you ate for breakfast yesterday. Do you remember it? What about what you ate a week before? If you can't remember it, then having a note would help and that's the same thing here in HTML
- All HTML files end with ".html". You can open ".html" files just like you can with any other file by clicking on it

## Using HTML

### Basics of HTML

- All HTML tags must start with an `<` and end with a `>`. Within these two arrows must be the HTML element we are using. In HTML, the `<` and `>` are called *angle brackets*
- All HTML documents must start with `<!DOCTYPE html>` which tells the document we are using HTML, specifically HTML5 which is the most recent version
- After `<!DOCTYPE html>`, all of the HTML we write must be written between `<html>` and `</html>`

```html
    <!DOCTYPE html>

    <html>
        <!-- Your HTML goes here --> 
    </html>
```

- Some HTML tags require something called an **opening** and **closing** tag. Opening and closing tags are used when you want to put some "content" within the tag. "Content" refers to any images or text you want to show on your website. Closing tags have a `/` while opening tags do not have the `/`
  - Opening: `<html>`
  - Closing: `</html>`

For example, here's a paragraph tag:

```html
    <p>This sentence is an example of "content"</p>
```

### Head

In the human body, your head stores all of your information. The same applies to HTML where we need to keep things like the coding alphabet the computer can use, the title of our website and/or any other files we need to connect to our HTML file.

- Head: `<head><!-- YOUR HTML here --></head>`
- Title: `<title>Your title here</title>`
  - The title defines what your HTML file is called. For example, open up the YouTube home page. Notice at the top it says "YouTube" when you hover your mouse over the tab. That is YouTube's HTML title
- `<meta charset="UTF-8">` specifies the character encoding for our HTML document. In other words, this is the "alphabet" our computer is allowed to use
- As mentioned above, we can connect other files. The most common ones are CSS and JavaScript files:
  - CSS: `<link rel="stylesheet" href="style.css">`
  - JavaScript: `<script src="script.js"></script>`

```html
    <!DOCTYPE html>

    <html>
        <head>
            <title>My website!</title>
            <meta charset="UTF-8">
            <link rel="stylesheet" href="style.css">
            <script src="script.js"></script>
        </head>
    </html>
```

### Body

Almost all of the HTML that we want to show up on our website lies within the body section. The body is denoted by `<body></body>`

- Headings
  - Goes from heading 1 to 6 and defined by `<h1>`, `<h2>`, `<h3>`, `<h4>`, `<h5>`, `<h6>`, these headings are used in various ways to make content stand out in a website. For example, using a `<h1>` will make whatever text that is stand out the most as it is the largest
- Paragraphs
  - `<p></p>`
  - Paragraph elements contain text that describes what’s being shown on the website. Other elements such as images can be contained within the paragraphs
- Italics
  - `<i></i>`
  - Can be placed in any text element such as the headings or paragraphs
    - Example: `<p>This text is <i>italic</i></p>` is correct
    - Example: `This text is <i>italic</i>` is incorrect because there is no `<p>` or `<h1>` to `<h6>` tags surrounding it
- Bolded text
  - `<b></b>`
  - Can be placed in any text element such as the headings or paragraphs
- Lists
  - Unordered (bullet point) list defined by `<ul> </ul>`
  - Ordered (numbered) list defined by `<ol> </ol>`
  - Within these different types of lists, we use `<li> </li>` to insert a bullet point
- Anchor tags
  - Shown by using `<a>` and ending with `</a>`
  - We use anchor elements as hyperlinks
    - Example: `<a href="google.ca">`
    - When I click on the link on my HTML page, it will take me to the website that I have linked it to
  - You can also use anchor elements to link to different parts of your website
- Images
  - To enhance your website, we may want to add images. Visual aids are really helpful to someone who may be viewing your website.
  - `<img src="cat.jpg" alt="cat" width="100" height="100">`
    - Src: where the image is located in our files
    - Alt: the text associated with the image. Sometimes the image might not load or a person with visual disabilities may have problems with looking at the image so adding extra (BUT SHORT) text that goes with the image helps
    - Width: how wide the image is
    - Height: how tall the image is
- Tables
  - Start off with creating a `<table> </table>`
  - Within each table, there are table rows `<tr> </tr>`
  - Within table rows are `<td> </td>` known as "table data"
  - We use tables to organize information

```html
<!DOCTYPE html>

<html lang="en">
    <!-- "Brain" of our website; stores all our info like language, styling, JavaScript, etc. -->
    <head>
        <title>My Website</title>
        <meta charset="UTF-8">
        <link rel="stylesheet" href="style.css">
    </head>
    <body>
        <h1>Heading 1</h1>
        <h2>Heading 2</h2>
        <h3>Heading 3</h3>
        <h4>Heading 4</h4>
        <h5>Heading 5</h5>
        <h6>Heading 6</h6>
        <p>Insert</p>
        <p>This word will now be <b>bolded with other words</b> and this other word will now be <i>italisized</i></p>
        <p><u>This entire line will be underlined</u></p>
        <ol>
            <li>Apples</li>
            <li>Banana</li>
            <li>Blueberries</li>
        </ol>
        <ul>
            <li>City Centre</li>
            <li>Minoru</li>
            <li>Steveston</li>
        </ul>
        <a href="www.google.ca">Google</a>
        <img src="cat.jpg" alt="Cat" width="150" height="300">
        <table>
            <tr>
                <td>Monday</td>
                <td>Tuesday</td>
                <td>Wednesday</td>
                <td>Thursday</td>
                <td>Friday</td>
            </tr>
            <tr>
                <td>School</td>
                <td>Activities</td>
                <td>School</td>
                <td>School</td>
                <td>School</td>
            </tr>
        </table>
    </body>
</html>
```
