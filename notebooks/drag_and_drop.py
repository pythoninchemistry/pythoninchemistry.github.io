from IPython.display import  HTML


class DDQuiz():
    """A class to hold the definitions of a drag and drop quiz to be deployed in a Jupyter Notebook
    The class requests a list of box names which will be the target areas and a dictionary of image sources with the target box name
    The class constructs the required HTML to display the quiz in a jupyter notebook environment.
    While each image will have a different div identity if you have multiple quizzes on the same page with the same box names it will 
    be possible to drag images to boxes in different parts of the notebook, however it is unlikely that users will try this
    The image can only be dropped into the correct box, attempts to drop it into a different box will fail and the box will flash red
    """

    div_counter = 1   # class based counter for divs to avoid id collision on the images to be moved around if multiple quizes

    def __init__(self, box_names:list, images:dict, question:str):
        """initialise class

        Args:
            box_names (list): A list of the target box names
            images (dict): A dictionary of src:target for the images where src is the image file src and the target is the name of the
                           target box as defined in the box_names list
            question (str): The question to be displayed above the quiz
        """
        self.box_names = box_names
        self.images=images
        self.question=question


    def quiz(self):
        """ Joins together the different elements of the Html and produces the final HTML object

        Returns:
            HTML: HTML object for display
        """
        quiz= self._jscript() + self._css() + self._html()
        return HTML(quiz)
    

    def _jscript(self)->str:
        """constructs the script component for teh necessary html

        Returns:
            str: the javascript passed as a string
        """


        script= '''
        <script>
            function allowDrop(ev) {
            ev.preventDefault();
            }
            function drag(ev) {
            ev.dataTransfer.setData("text", ev.target.id);
            }

            function drop(ev) {
            ev.preventDefault();
            var data = ev.dataTransfer.getData("text");
            var originalColor = getComputedStyle(document.getElementById(ev.target.id)).backgroundColor; // Store original color
            if (document.getElementById(data).classList.contains(ev.target.id)) {
                ev.target.style.backgroundColor= "rgba(32, 201, 151, 0.5)"
                ev.target.appendChild(document.getElementById(data));}
            else {
                ev.target.style.backgroundColor="rgba(220, 53, 69, 0.5)"
            }
            setTimeout(function(){
            document.getElementById(ev.target.id).style.backgroundColor = originalColor;  // Change the color back to the original
            }, 1000);

            }
        </script>'''
        return script
    
    def _css(self)->str:
        """generates the required css style components for the quiz

        Returns:
            str: the style as a string
        """

        css='''
        <style>
        .div1 
        {width: 200px;
        height: 200px;
        padding: 1px;
        margin:10px;
        border: 5px, grey, dotted, !important;
        text-align:center;
        } 

        .div2 
        {
        padding: 1px;
        margin:10px;
        border: 5px, grey, solid, !important;
        text-align:center;
        float:left} 

        .example {
        float:left;

        }
        <
        </style>'''
        return css

    def _html(self)->str:
        """generates the required html elements from the input parameter definitions

        Args:
            box_names (list): A list of the target box names
            images (dict): A dictionary of src:target for the images where src is the image file src and the target is the name of the
                           target box as defined in the box_names list

        Returns:
            str: the html string for the displayed elements
        """
        html = f'<div>{self.question}</div>\n'
        for src, cls in self.images.items():
            html += "<image class='example " + cls + "' id='drag_" + str(DDQuiz.div_counter) +"' src='" + src + "' draggable='true' ondragstart='drag(event)' width='150' height='69'>\n"
            DDQuiz.div_counter +=1
        html += "<div style='clear:left; margin-top:20px'>\n"
        for box in self.box_names:
            html+="<div class='div2'>" + box + "<div id='" + box +"' class='div1' ondrop='drop(event)' ondragover='allowDrop(event)'></div></div>\n"
        html += "</div>"
        return html


#  DEFINE A FUNCTION FOR EACH QUIZ



def quiz2()->HTML:
    """Constructs a drag and drop quiz based that tests understanding of variable types
    Define the box_names as a list of the target box names - use &nbsp; to add spaces in the names
    Define the images as a dictionary with the image src as the key and the target box name as the value
    pass the question text to be displayed above the quiz as a string to the DDQuiz object



    Returns:
        HTML: An HTML object for display of a drag and drop quiz 
    """

    box_names = ['Programming&nbsp;Language', 'Operating&nbsp;System', 'Technology&nbsp;Company']
    images = {'./javascript.png':'Programming&nbsp;Language',
              './linux.png':'Operating&nbsp;System',
              './ibm.png':'Technology&nbsp;Company',
              './matlab.png':'Programming&nbsp;Language',
              './visual_basic.png':'Programming&nbsp;Language',
              './intel.png':'Technology&nbsp;Company'}
    quiz = DDQuiz(box_names, images, 'Drag the images to the correct category')
    return quiz.quiz()