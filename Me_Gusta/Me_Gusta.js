function contador(identificador){
    let btnLike = document .querySelector(identificador);
    let cant = btnLike.innerText;
    cant++;
    btnLike.innerText=cant;
}