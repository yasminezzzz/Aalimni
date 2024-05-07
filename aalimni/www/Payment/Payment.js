$(document).ready(function(){
    $('#offer_select').change(function(){
        var price = $(this).find(':selected').data('price');
        $('#offer_price').val(price);
        $('#pay_button').text('Pay $' + price);
    });

    $('#paymentForm').submit(function(e){
        e.preventDefault();
        var firstName = $('#cc_first_name').val(); 
        var lastName = $('#cc_last_name').val(); 

        $.ajax({
            type: 'POST',
            url: 'process_payment',  
            data: {
                first_name: firstName, 
                last_name: lastName 
            },
            success: function(response) {
                if (response.success) {
                    alert('Payment successful!');
                } else {
                    alert('Error: Payment could not be processed.');
                }
            },
            error: function(xhr, status, error) {
                console.error(error);
                alert('Error: Payment could not be processed.');
            }
        });
    });
});