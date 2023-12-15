
// if (localStorage.getItem('cart') == null) {
//     cart = {}
// }
// else {
//     cart = JSON.parse(localStorage.getItem('cart'))
// }

// cart_updation()
var updatebtns = document.querySelectorAll('.update-cart');
for (var i = 0; i < updatebtns.length; i++) {
    updatebtns[i].addEventListener('click', function () {
        product_id = this.dataset.product;
        action = this.dataset.action;

        if (user === 'AnonymousUser') {
            console.log('user not logged in')
        }
        else {
            updateUserOrder(product_id, action)
        }


        // if(cart[product_id] !=undefined)
        // {
        //     cart[product_id]+=1;
        // }
        // else
        // {
        //     cart[product_id]=1;
        // }
        // // console.log(cart)
        // localStorage.setItem('cart',JSON.stringify(cart))
        // cart_updation()

    })
}


// function cart_updation() {
//     var cart_total = document.querySelector('#cart-total');
//     a = JSON.parse(localStorage.getItem('cart'))
//     var mysum = 0;
//     for (var i in a) {
//         mysum += a[i];
//     }
//     cart_total.innerHTML = mysum

// }




// product_id=this.dataset.product;
// action=this.dataset.action;


function updateUserOrder(productId, action) {
    console.log('user is logged in')

    var url = '/store/update_item/'

    fetch(url, {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json',
            'X-CSRFToken': csrftoken,
        },
        body: JSON.stringify({ 'productId': productId, 'action': action })
    })
        .then((response) => { 
            return response.json() 
        })
        .then((data) => {
            location.reload()
        })
}