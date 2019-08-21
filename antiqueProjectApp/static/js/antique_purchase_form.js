//JS functionality to show live pay button once paymentForm is valid

$(document).ready(function(){
         
    $('#pay-button').hide();
    $('#disabled-pay').show();

    $('#paymentForm').keyup(function(){
        var form = document.getElementById('paymentForm')
      
        if(form.checkValidity()){
            $('#pay-button').show();
            $('#disabled-pay').hide();
        }else
        {
            $('#pay-button').hide();
            $('#disabled-pay').show();
        }
    })    
 
});