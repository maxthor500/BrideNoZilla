
/* solution from https://stackoverflow.com/questions/18562265/remove-css-class-depending-on-screen-size-jquery */
$(function(){

    $(window).on("resize",function(){

        if($(this).width() < 767){
            $('#shop-now-section').removeClass('col').addClass('over-image')
            $('#carousel-section').removeClass('col')
        }
        else{
            $('#shop-now-section').removeClass('over-image').addClass('col')
            $('#carousel-section').addClass('col')
        }
    })
})