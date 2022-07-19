let $word = $("#word");
let score = 0;
let usedWords = [];
let time = 2;
let timer = setInterval (() => {
    if(time > 0){
        time -= 1;
        $(".time").text(time);
    }
    else{ 
        endGame();  
    }
}, 1000);

if (time > 0){
    $("form").on("submit"), handleclick();
}


async function handleclick(e){
    $("form").on("submit", async function(e){
        e.preventDefault();
    
        
        console.log($word.val());
    
         let response = await axios.get('/check-word', {params: {word: $word.val() }});
         console.log(response.data)
    
         
         
         
    
         if(response.data === "ok" && usedWords.includes($word.val()) == false){
            updateScore($word.val())
            updateValidator(response.data);
            usedWords.push($word.val());
         }
         else if(usedWords.includes($word.val()) === true){
            updateValidator("Word already used");
         }
         else{
            updateValidator(response.data)
         }
         
        
        $word.val('');
    })
}
    
function updateValidator(res){
        let $message = $(".message"); 
        $message.text(res)
}
    
function updateScore(word){
        score += word.length
    
        $(".score").text(score)
}

function resetGame(e){
    e.preventDefault();
    window.location.replace("http://127.0.0.1:5000/");
}

function endGame(){
    clearInterval(timer);
    updateValidator("GAME OVER");
    const $resetBtn = $("<button>Reset</button>");
    $("form").append($resetBtn);
    $("form").off()
    $resetBtn.on("submit"), resetGame.bind(this);
}
