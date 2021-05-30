$('#slider1, #slider2, #slider3').owlCarousel({
    loop: true,
    margin: 20,
    responsiveClass: true,
    responsive: {
        0: {
            items: 1,
            nav: false,
            autoplay: true,
        },
        600: {
            items: 3,
            nav: true,
            autoplay: true,
        },
        1000: {
            items: 5,
            nav: true,
            loop: true,
            autoplay: true,
        }
    }
})


$(document).ready(function(){
    var cart=document.getElementsByClassName('basecart');
    console.log(cart[0]);
    $.ajax({
        type:"GET",
        url:"/displaycart",
        data:{
            hy:'None'
        },
        success : function (data){
            cart[0].innerText=data.lencartobj

        }
    }
);







    /////////////////////////////////////////////////////////////////////
    $(".plus-cart").click(function(){
        var prod_id=$(this).attr("pid").toString();
        console.log("djgdj");
        var ele=this.parentNode.children[2]
        console.log(ele)
        $.ajax({
                type:"GET",
                url:"/plcart/pl",
                data:{
                    pid:prod_id
                },
                success : function (data){
                    console.log(data.totalAmount)
                    console.log(data.amount)
                    console.log(data.quantity)
                    ele.innerText=data.quantity
                    document.getElementById('amount').innerText=data.amount
                    document.getElementById('totalAmount').innerText=data.totalAmount
    
                }
            }
        );

    });
    ///////////////////////////////////////////////////
    $(".minus-cart").click(function(){
        var prod_id=$(this).attr("pid").toString();
        console.log("djgdj");
        var ele=this.parentNode.children[2]
        console.log(ele.textContent)
        if(parseInt(ele.textContent)>0)
        {
            console.log("dddddddddddddddddd")
            $.ajax({
                type:"GET",
                url:"/mncart/mn",
                data:{
                    pid:prod_id
                },
                success : function (data){
                    console.log(data.totalAmount)
                    console.log(data.amount)
                    console.log(data.quantity)
                    ele.innerText=data.quantity
                    document.getElementById('amount').innerText=data.amount
                    document.getElementById('totalAmount').innerText=data.totalAmount
    
                }
            }
        );
        
        }
        

    });

/////////////////////////////////////////////////////////////////////////////////////////
    $(".removebtn").click(function(){
        var prod_id=$(this).attr("pid").toString();
        console.log("djgdj");
        var ele=this.parentNode.parentNode.children[2].children[2];
        var removeEle=this.parentNode.parentNode.parentNode.parentNode;
        console.log(ele);
        console.log(ele);
        console.log(removeEle);
        
        $.ajax({
                type:"GET",
                url:"/removecart/rm",
                data:{
                    pid:prod_id
                },
                success : function (data){
                    console.log(data.totalAmount)
                    console.log(data.amount)
                    console.log(data.quantity)
                    ele.innerText=data.quantity
                    document.getElementById('amount').innerText=data.amount
                    document.getElementById('totalAmount').innerText=data.totalAmount
                    removeEle.remove()
    
                }
            }
        );

    });
});