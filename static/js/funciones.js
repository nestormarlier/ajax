function mensaje_error(obj) {
    var html = '<ul style="text-align: left">';
    $.each(obj, function(key,value){
        html+='<li>'+key+': '+value+'</li>';
    });
    html+='</ul>';
    Swal.fire({
        icon: 'error',
        title: 'Atención ha ocurrido un error',
        html: html
    })
}