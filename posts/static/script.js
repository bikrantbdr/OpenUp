const quizData = [
    {
        question: "Did you ever have a feeling of fear of some specific object or situation?",
        a: "Yes",
        b: "No",
        correct: "a",
        disorder_type:"Anxiety Disorder",
    },
    {
        question: "Do you ever have a fear of being in unsafe circumstances surrounding your life?",
        a: "Yes",
        b: "No",
        correct: "a",
        disorder_type:"Anxiety Disorder",
    },
    // {
    //     question: "Do you often feel lonely?",
    //     a: "Yes",
    //     b: "No",
    //     correct: "a",
    //     disorder_type:"Depression",
    // },
    // {
    //     question: "Have you felt your works and accomplishments of being of no value in any measure?",
    //     a: "Yes",
    //     b: "No",
    //     correct: "a",
    //     disorder_type:"Depression",
    // },
    // {
    //     question: "Do you have frequent reactions to distractions when you should be concentrating hard on something?",
    //     a: "Yes",
    //     b: "No",
    //     correct: "a",
    //     disorder_type:"BIpolar Disorder",
    // },
    // {
    //     question: "There are times when some individuals have gone through moments when they are either seeing things or imagining events that are too real to distinguish from real life. Have you ever been in those situations?",
    //     a: "Yes",
    //     b: "No",
    //     correct: "a",
    //     disorder_type:"BIpolar Disorder",
    // },
    // {
    //     question: "Have you ever had sudden episodes of impulsive, aggressive, violent behavior or angry verbal outbursts in which you reacted grossly out of proportion to the situation?",
    //     a: "Yes",
    //     b: "No",
    //     correct: "a",
    //     disorder_type:"Personality disorder",
    // },
    // {
    //     question: "Do you find yourself running away from your responsibilities or procrastinating on them?",
    //     a: "Yes",
    //     b: "No",
    //     correct: "a",
    //     disorder_type:"Personality disorder",
    // },
    // {
    //     question: "Do you usually loathe unnecessary touches or others being around you, close in proximity?",
    //     a: "Yes",
    //     b: "No",
    //     correct: "a",
    //     disorder_type:"Trauma and stress related",
    // },
    // {
    //     question: "Do you ever relive your old sad or hurtful days or get affected by the bad old memories affecting your current happiness and mental condition?",
    //     a: "Yes",
    //     b: "No",
    //     correct: "a",
    //     disorder_type:"Trauma and stress related",
    // },
    // {
    //     question: "Have you ever questioned the reality of your life, second guessing if you even made the decision that brought you where you are now?",
    //     a: "Yes",
    //     b: "No",
    //     correct: "a",
    //     disorder_type:"Dissociatiave and somatic disorder",
    // },
    // {
    //     question: "Do you usually stand by your decisions and trust your instincts or do you second guess yourself and are anxious when you decide for something?",
    //     a: "Yes",
    //     b: "No",
    //     correct: "a",
    //     disorder_type:"Dissociatiave and somatic disorder",
    // },
    // {
    //     question: "Are you conscious of your food consumption amount with the fear of gaining too much weight or affecting your body appearance?",
    //     a: "Yes",
    //     b: "No",
    //     correct: "a",
    //     disorder_type:"Feeding and eating disorder",
    // },
    // {
    //     question: "Do you have a wide range of areas of interest and hobbies or are you only interested in a handful of activities and are not interested in trying out anything new?",
    //     a: "Yes",
    //     b: "No",
    //     correct: "a",
    //     disorder_type:"Neurodevelopmental dissorder",
    // },
    // {
    //     question: "If you are really getting the hang of doing something, is it a bit hard for you to stop doing it or taking a break from it healthily?",
    //     a: "Yes",
    //     b: "No",
    //     correct: "a",
    //     disorder_type:"Addictive disorder",
    // },
    // {
    //     question: "Have you ever been engaged in long sessions of gaming or gambling or other addictive hobbies?",
    //     a: "Yes",
    //     b: "No",
    //     correct: "a",
    //     disorder_type:"Addictive disorder",
    // },
];
  

let maximum_likelihood=[{
        type:"",
        probablity_value:0,
    },
];


const quiz= document.getElementById('quiz')
const answerEls = document.querySelectorAll('.answer')
const questionEl = document.getElementById('question')
const a_text = document.getElementById('a_text')
const b_text = document.getElementById('b_text')
const submitBtn = document.getElementById('submit')

let disorder_type_count=[
    {
        type:"Anxiety Disorder",
        count:0,
        probablity_count:0,
        probablity_value:0,
    },
    {
        type:"Depression",
        count:0,
        probablity_count:0,
        probablity_value:0,
    },
    {
        type:"BIpolar Disorder",
        count:0,
        probablity_count:0,
        probablity_value:0, 
    },
    {
        type:"Personality disorder",
        count:0,
        probablity_count:0,
        probablity_value:0,
    },
    {
        type:"Trauma and stress related",
        count:0,
        probablity_count:0,
        probablity_value:0,
    },
    {
        type:"Dissociatiave and somatic disorder",
        count:0,
        probablity_count:0,
        probablity_value:0,
    },
    {
        type:"Feeding and eating disorder",
        count:0,
        probablity_count:0,
        probablity_value:0,
    },
    {
        type:"Neurodevelopmental dissorder",
        count:0,
        probablity_count:0,
        probablity_value:0,
    },
    {
        type:"Addictive disorder",
        count:0,
        probablity_count:0,
        probablity_value:0,
    },
];
let currentQuiz = 0

loadQuiz()

function loadQuiz() {

    deselectAnswers()

    const currentQuizData = quizData[currentQuiz]

    questionEl.innerText = currentQuizData.question
    a_text.innerText = currentQuizData.a
    b_text.innerText = currentQuizData.b
}

function deselectAnswers() {
    answerEls.forEach(answerEl => answerEl.checked = false)
}

function getSelected() {
    let answer
    answerEls.forEach(answerEl => {
        if(answerEl.checked) {
            answer = answerEl.id
        }
    })
    return answer
}

function proceed(){
    console.log("proceed")
    window.location.replace("home?ans=maximum_likelihood.type");
}


submitBtn.addEventListener('click', () => {
    const answer = getSelected()
    for (x=0;x < disorder_type_count.length;x++){
        if(disorder_type_count[x].type ==  quizData[currentQuiz].disorder_type){
        disorder_type_count[x].count ++
        // console.log(disorder_type_count[x].count)
        }
    
    }

    if(answer) {
       if(answer === quizData[currentQuiz].correct) {
        console.log("correct")
        for (x=0;x < disorder_type_count.length;x++){
            if(disorder_type_count[x].type ==  quizData[currentQuiz].disorder_type){
            disorder_type_count[x].probablity_count ++
            // console.log(disorder_type_count[x].probablity_count)
            }
        }
       }

       currentQuiz++

       if(currentQuiz < quizData.length) {
           loadQuiz()
       } else {
           for (x=0;x < disorder_type_count.length;x++){
            disorder_type_count[x].probablity_value= disorder_type_count[x].probablity_count/disorder_type_count[x].count
            if(disorder_type_count[x].probablity_value> maximum_likelihood.probablity_value){
                maximum_likelihood.type=disorder_type_count[x].type
                maximum_likelihood.probablity_value=disorder_type_count[x].probablity_value
            }
            }
            console.log(disorder_type_count,maximum_likelihood)   
            quiz.innerHTML = `
           <h2>Thank you for answering</h2>

           <button onclick="proceed()">Proceed</button>
           `        
       }
    }
})
