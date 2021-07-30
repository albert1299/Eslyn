$('body').on('click', '.button', function (e) {
    addToCartItem(e);
});

const tbody = document.querySelector('.tbody');
console.log(tbody);
let cart = [];

function addToCartItem(e) {
    console.log('llamando a funcion')
    const button = e.target
    const item = button.closest('.current_product');
    const id = item.querySelector('#product_id').textContent;
    const image = item.querySelector('#product_image').src;
    const name = item.querySelector('#product_name').textContent;
    //const description = item.querySelector('#product_description').textContent;
    //const category = item.querySelector('#product_category').textContent;
    const price = item.querySelector('#product_price').textContent;

    const newProduct = {
        id,
        image,
        name,
        price,
        quantity: 1
    }

    addProductCart(newProduct);
}

function addProductCart(newProduct) {

    const alert = document.querySelector('.alert')
    setTimeout(function () {
        alert.classList.add('hide')
    }, 2000)
    alert.classList.remove('hide')

    const InputQuantity = tbody.getElementsByClassName('input__quantity');
    for (let i = 0; i < cart.length; i++) {
        if (cart[i].id.trim() === newProduct.id.trim()) {
            cart[i].quantity++;
            const InputQuantityValue = InputQuantity[i]
            InputQuantityValue.value++;
            cartTotal();
            return null;
        }
    }

    cart.push(newProduct);
    renderCart()
}

function renderCart() {
    console.log(cart)
    tbody.innerHTML = '';
    cart.map(item => {
        const tr = document.createElement('tr')
        tr.classList.add('ItemCart')
        const Content = `
        <th scope="row" class="table__id">${item.id}</th>
                <td class="table__products">
                    <img src=${item.image}  alt="">
                    <h6 class="name">${item.name}</h6>
                </td>
                <td class="table__price"><p>${item.price}</p></td>
                <td class="table__quantity">
                    <input type="number" min="1" value=${item.quantity} class="input__quantity">
                    <button class="delete btn btn-danger">x</button>
                </td>
      `
        tr.innerHTML = Content;
        tbody.append(tr)

        tr.querySelector(".delete").addEventListener('click', removeProductCart);
        tr.querySelector(".input__quantity").addEventListener('change', sumaCantidad)
    })
    cartTotal();
}

function cartTotal() {
    let total = 0;
    const CartTotal = document.querySelector('.CartTotal');
    cart.forEach((item) => {
        console.log(item.price);
        const price = parseFloat(item.price.replace("$", ''));
        console.log('precio', price);
        total = total + price * item.quantity
    })
    console.log('total', total);
    CartTotal.innerHTML = `Total $${total}`;
    addLocalStorage();
}

function removeProductCart(e) {
    const buttonDelete = e.target;
    const tr = buttonDelete.closest(".ItemCart");
    const product_id = tr.querySelector('.table__id').textContent;
    for (let i = 0; i < cart.length; i++) {
        if (cart[i].id.trim() === product_id.trim()) {
            cart.splice(i, 1);
        }
    }

    const alert = document.querySelector('.remove');
    setTimeout(function () {
        alert.classList.add('remove')
    }, 2000)
    alert.classList.remove('remove')
    tr.remove();
    cartTotal();
}

function sumaCantidad(e) {
    const sumInput = e.target
    const tr = sumInput.closest(".ItemCart")
    const product_id = tr.querySelector('.table__id').textContent;
    cart.forEach(item => {
        if (item.id.trim() === product_id) {
            sumInput.value < 1 ? (sumInput.value = 1) : sumInput.value;
            item.quantity = sumInput.value;
            cartTotal()
        }
    })

}

function addLocalStorage() {
    sessionStorage.setItem('cart', JSON.stringify(cart))
}

window.onload = function () {
    const storage = JSON.parse(sessionStorage.getItem('cart'));
    if (storage) {
        cart = storage;
        renderCart()
    }
}