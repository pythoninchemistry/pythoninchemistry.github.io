# Formatting Guide
All of the following formatting works in BOTH raw Jupyter Book ipynb and as a built website. 

## Built-in Jupyter Books formatting

Hashtags # dictate header levels. The more hashtags, the lower the header level. 
Single asterisk * makes text *italic*
Double asterisk ** makes text **bold**
Ticks ` ` Makes text into code `code`
Three dashes --- on their own line inserts a line break
Single dollar signs $ $ makes things into $ maths\ using\ latex $
Double dollar signs $$ $$ on a new line place the maths block into the centre
Tables are written by separating with | and headers separated with ----
    |Header 1 | Header 2 | Header 3 |
    | ----- | ----- | ----- |
    | Row 1 | Row 1 | Row 1 |
    | Row 2 || Row 2 | Row 2 |
- Bullet points are written using - 
1. Numbered lists written using 1., 2., etc




## Code

```Python
All code between these ticks
Is formatted like Python code
var = "hello"
This has a transparent background
```

`Inline monospaced code can be written with a single tick` This has a dark highlighted background. ```Multiple ticks are the same```

>```Python
>Python formatted code with a dark background
>Can be written with three ticks and 'Python' on the first line
>And arrows > before every line




## Images

Built-in Jupyter method: 
    ![Optional description of image. Image must include directory if in a folder](logo.png). Cannot adjust size. 

HTML method (allows for image sizing):
    <img src="logo.png" alt="fishy" class="image" width="200px">

The <img> tag only takes 
- src (soure location of image, filepath if not in same directory), 
- alt (alternate text for an image), 
- width (width in pixels), 
- height (height in pixels), and 
- class (further styles for the image, defined with CSS) attributes. Anything further requires a class (example below, defined using <style></style>). 
    <style>
    .image {align:"center"; border:4px solid #1b6b6f; padding:15px; display:"block"}
    .image-rounded { border-radius: 10px; }
    </style>




## Maths

Written in LaTex inbetween $ signs. Double dollar signs $$ $$ create centred maths. 
- \theta for a symbol
- \ to insert a small space
- \frac{}{} to insert a fraction, with the numerator in the first brackets and denominator in the second




## Clear examples menu

<details style="padding: 10px; border-radius: 2px; border: 1.5px solid gray"> 
<summary style= "font-size:130%;"> Title</summary>

Content

```Python
Code

More code
```

Content. ``Inline code``

</details><br/>




## Green exercise box

<div class="alert alert-success" style="padding:6px; border-radius:5px">
<details><summary style="padding-left:4px"> Exercise: Write some code for... </summary>

--- 

Question content. Question content. Question content.

Question content. Question content. Question content.

Useful information:

$equation\ in\ latex$ 

The ``math`` function for $sin^-1$ is: ``asin()``.

<b>Hint:</b> Here is a hint.

</details>
</div>




## Answers box

<details style="padding: 4px; border: 1.5px solid #c8e4cc; border-radius:5px"> 
<summary style="padding-left:6px"> Click to view answer</summary>

Answer explanation, potentially.

Can add a line break if you want. 
---
```Python
import answer

Code answer.
This might be quite long.

it is auto-for-matted
```

More answer explanation, potentially. ``inline code``. <code>inline code</code> <tt>inline code or print</tt> in a different style.

</details><br/>