
window.onload = function(){
    //CODEREVIEW: code duplication
    function changeResponseText(textToPresent){
        document.getElementById("msgServer").innerHTML = textToPresent;
    }
    document.getElementById("sumbit_button").addEventListener("click",
        function () {
            var id = document.getElementById('id_num').value;
            const pattern = /^[0-9]{9}$/g;
            const match = pattern.test(id);
            if (match){
                var postRequest = new XMLHttpRequest();
                postRequest.onreadystatechange =
                    function(){
                        if (this.readyState == 4 && this.status == 200) {
                            // CODREVIEW: response
                            document.getElementById("msgServer").innerHTML=this.responseText;
                    }
                 };
                // CODREVIEW: move to json
                postRequest.open('POST' ,'/submit', true);
                postRequest.setRequestHeader("Content-type", "application/json")
                var body = {"id": id };

                postRequest.send(JSON.stringify(body));

            }else{document.getElementById("msgServer").innerHTML='please insert 9 digits';}
          });

           const input = document.querySelector('input');
           input.addEventListener('change',
           function(){
                document.getElementById("msgServer").innerHTML='';
           });
}


