//jquery-click-scroll
//by syamsul'isul' Arifin
// if(window.location.href.split('8000/')==){}
var sectionArray = [1, 2, 3, 4, 5, 6, 7];
if(window.location.href.indexOf("%23section_") > -1){
    let section = window.location.href.split('%23section_')[1];
    window.location.href = "http://127.0.0.1:8000/#section_"+section;
}
    // for(let i=0;i<sectionArray.length;i++){
    //     if(window.location.href.split('8000/')[1]=='%23section_'+sectionArray[i]){
    //         // document.location.href='#'+'section_'+sectionArray[i];
    //         let newUrl = '#'+'section_'+sectionArray[i];
    //         document.location.href = newUrl;
    //     }
    // }
$.each(sectionArray, function(index, value){
          
     $(document).scroll(function(){
         var offsetSection = $('#' + 'section_' + value).offset().top - 83;
         var docScroll = $(document).scrollTop();
         var docScroll1 = docScroll + 1;
         
        
         if ( docScroll1 >= offsetSection ){
             $('.navbar-nav .nav-item .nav-link').removeClass('active');
             $('.navbar-nav .nav-item .nav-link:link').addClass('inactive');  
             $('.navbar-nav .nav-item .nav-link').eq(index).addClass('active');
             $('.navbar-nav .nav-item .nav-link').eq(index).removeClass('inactive');
         }
         
     });
    
    $('.click-scroll').eq(index).click(function(e){
        
        var offsetClick = $('#' + 'section_' + value).offset().top - 83;
        e.preventDefault();
        $('html, body').animate({
            'scrollTop':offsetClick
        }, 300)
    });
    
});

$(document).ready(function(){
    $('.navbar-nav .nav-item .nav-link:link').addClass('inactive');    
    $('.navbar-nav .nav-item .nav-link').eq(0).addClass('active');
    $('.navbar-nav .nav-item .nav-link:link').eq(0).removeClass('inactive');
});