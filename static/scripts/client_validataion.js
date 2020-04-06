
window.onload = function(){
    var response = document.getElementById('msgServer');
    document.getElementById('sumbit_button').addEventListener('click',
        function () {
            var id = document.getElementById('id_num').value;
            const pattern = /^[0-9]{9}$/g;
            const match = pattern.test(id);
            if (match){
                var postRequest = new XMLHttpRequest();
                postRequest.onreadystatechange =
                    function(){
                        if (this.readyState == 4 && this.status == 200) {
                        var responseJSON= JSON.parse(this.responseText);
                        var colorResponse=  (responseJSON['status']) ? 'green' : 'red';
                        response.style.color= colorResponse;
                        response.innerHTML = responseJSON['msg'];
                    }
                 };
                postRequest.open('POST' ,'/submit', true);
                postRequest.setRequestHeader('Content-type', 'application/json');
                var body_request = {'id': id};
                postRequest.send(JSON.stringify(body_request));
            }else{
            var typeError= {'typeError':'please insert 9 digits'};
            response.style.color= '121222';
            response.innerHTML= typeError['typeError'];
            }
          });

           const input = document.querySelector('input');
           input.addEventListener('input',
           function(){
                response.innerHTML='';
           });
}


