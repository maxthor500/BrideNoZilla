$(document).ready(function() {
    /* from Code Institute Boutique ado */

    // Disable +/- buttons outside 1-99 range
    function handleEnableDisable(itemId) {
        let currentValue = parseInt($(`#id_qty_${itemId}`).val());
        let minusDisabled = currentValue < 2;
        let plusDisabled = currentValue > 98;
        $(`#decrement-qty_${itemId}`).prop('disabled', minusDisabled);
        $(`#increment-qty_${itemId}`).prop('disabled', plusDisabled);
    }

    // Ensure proper enabling/disabling of all inputs on page load
    let allQtyInputs = $('.qty_input');
    for(let i = 0; i < allQtyInputs.length; i++){
        let itemId = $(allQtyInputs[i]).data('item_id');
        handleEnableDisable(itemId);
    }

    // Check enable/disable every time the input is changed
    $('.qty_input').change(function() {
        let itemId = $(this).data('item_id');
        handleEnableDisable(itemId);
    });

    // Increment quantity
    $('.increment-qty').click(function(e) {
    e.preventDefault();
    let closestInput = $(this).closest('.input-group').find('.qty_input')[0];
    let currentValue = parseInt($(closestInput).val());
    $(closestInput).val(currentValue + 1);
    let itemId = $(this).data('item_id');
    handleEnableDisable(itemId);
    });

    // Decrement quantity
    $('.decrement-qty').click(function(e) {
    e.preventDefault();
    let closestInput = $(this).closest('.input-group').find('.qty_input')[0];
    let currentValue = parseInt($(closestInput).val());
    $(closestInput).val(currentValue - 1);
    let itemId = $(this).data('item_id');
    handleEnableDisable(itemId);
    });


    // Update quantity on click
    $('.update-link').click(function(e) {
        let form = $(this).parent().prev('.update-form');
        form.submit();
    });

    // Remove item and reload on click
    $('.remove-item').click(function(e) {
        let itemId = $(this).attr('id').split('remove_')[1];
        let url = `/cart/remove/${itemId}/`;
        // middleware requited by Django
        let data = {'csrfmiddlewaretoken': csrfToken};

        $.post(url, data)
            .done(function() {
                location.reload();
            });
    });
});
