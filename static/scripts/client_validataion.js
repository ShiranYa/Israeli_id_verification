window.onload = function(){
    var response = document.getElementById('msgServer');
    var loading= document.getElementById('loaderVisible');
    var submitting = document.getElementById('sumbit_button');

    document.getElementById('id_num').addEventListener('keyup',
        function(event){
            if(event.keyCode  === 13){
                event.preventDefault();
                submitting.click()
            }
    });
     submitting.onclick= function(){
            var id = document.getElementById('id_num').value;
            const pattern = /^[0-9]{9}$/g;
            const match = pattern.test(id);
            if (match){
                var postRequest = new XMLHttpRequest();
                postRequest.onreadystatechange =
                    function(){
                        if (this.readyState == 4 && this.status == 200) {
                        loading.style.visibility='hidden';
                        var responseJSON= JSON.parse(this.responseText);
                        var colorResponse=  (responseJSON['status']) ? 'green' : 'red';
                        response.style.color= colorResponse;
                        response.innerHTML = responseJSON['valid_msg'];
                    }
                 };
                postRequest.open('POST' ,'/submit', true);
                postRequest.setRequestHeader('Content-type', 'application/json');
                var body_request = {'id': id};
                loading.style.visibility='visible';
                postRequest.send(JSON.stringify(body_request));

            }else{
                loading.style.visibility='hidden';
                var typeError= {'typeError':'please insert 9 digits'};
                response.style.color= '#C4C4C4';
                response.innerHTML= typeError['typeError'];
            }
          };

           const input = document.querySelector('input');
           input.addEventListener('input',
           function(){
                response.innerHTML='';
           });
    }
