
window.onload = function(){
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
                            document.getElementById("msgServer").innerHTML=this.responseText;
                    }
                 };
                postRequest.open('POST' ,'http://127.0.0.1:5000/submit', true);
                postRequest.setRequestHeader("Content-type", "application/json")
                postRequest.send(id);

            }else{document.getElementById("msgServer").innerHTML='please insert 9 digits';}
          });

           const input = document.querySelector('input');
           input.addEventListener('change',
           function(){
                document.getElementById("msgServer").innerHTML='';
           });
}


