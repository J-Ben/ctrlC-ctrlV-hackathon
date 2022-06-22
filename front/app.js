


const getList = () => {

    var myHeaders = new Headers();
    var myInit = {
        method: 'GET',
        headers: myHeaders,
        mode: 'no-cors',
        cache: 'no-cache'
    };

    fetch('http://127.0.0.1:5000/test', myInit)
        .then(response => { 
            console.log(response)
        });


}



const render = () => {
    console.log('click')
    $(".test").on("click", function (event) {
        var id = $(this).data('id');
        var dataId = $(this).attr("data-id");
        console.log("The data-id of clicked item is: " + dataId + " " + id);
    });

    $(".copyx").on("click", function (event) {
        var id = $(this).data('id');
        var dataId = $(this).attr("data-id");
        console.log("The data-id of clicked item is: " + dataId + " " + id);
    });

}


const archiver = () => {


}

const restaure = () => {


}

const audit = () => {


}
