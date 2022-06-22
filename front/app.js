const getList = () => {
    $("tbody tr").remove();
    fetch('http://127.0.0.1:5000/test')
        // fetch('./assets/data/projets.json')
        .then(response => response.json())
        .then(data => {
            $(data.projects).each(function (index) {
                var id = this.id;
                console.log(id)
                $('tbody').append(
                    '<tr><td>' + (index + 1)
                    + '</td><td>'
                    + this.id
                    + '</td><td>'
                    + this.name
                    + '</td>'
                    + '<td>'
                    + '<button onclick="render()" class="copyx button is-ctrl-no-border js-modal-trigger" data-id="' + id + '" data-target="ctrl-modal-copy"><span class="icon is-small is-ctrl-color toto"><i class="fa-regular fa-copy"></i> </span> </button>'
                    + '<button onclick="render()" class="button"> <span class="icon is-small is-ctrl-color"> <i class="fa-solid fa-download"></i> </span></button>'
                    + '<button onclick="render()" class="restaurex button is-ctrl-no-border js-modal-trigger"  data-id="' + id + '" data-target="ctrl-modal-restore"><span class="icon is-small is-ctrl-color"> <i class="fa-solid fa-arrows-rotate"></i> </span>  </button>'
                    + '<button onclick="render()" class="auditx button is-ctrl-no-border js-modal-trigger" data-target="ctrl-modal-audit" data-id="' + id + '"><span class="icon is-small is-ctrl-color"><i class="fa-solid fa-circle-info"></i> </button>'
                    + '</td>'
                    + '</tr>')
            });
        })
}

const copyProject = () => {
    console.log("copyProject")
    // save in base


    //close modal
    $("#ctrl-modal-copy").removeClass("is-active");
    // refresh table
    getList();
}


const render = () => {

    $(".auditx").on("click", function (event) {
        var id = $(this).data('id');
        var dataId = $(this).attr("data-id");
        console.log("The data-id of clicked item is: " + dataId + " " + id);
        
        audit(dataId);
    });

    $(".copyx").on("click", function (event) {
        var id = $(this).data('id');
        var dataId = $(this).attr("data-id");
        console.log("The data-id of clicked item is: " + dataId + " " + id);
        $("#ctrl-modal-copy").addClass("is-active");

    });

    $(".restaurex").on("click", function (event) {
        var id = $(this).data('id');
        var dataId = $(this).attr("data-id");
        console.log("The data-id of clicked item is: " + dataId + " " + id);
        $("#ctrl-modal-restore").addClass("is-active");

    });

}


const archiver = () => {


}

const restaure = () => {


}

const audit = (id) => {

    fetch('http://127.0.0.1:5000/test')
        // fetch('./assets/data/projets.json')
        .then(response => response.json())
        .then(data => {
            const obj = data.projects.find(data => data.id == id)
           $(".projectNameA").val(obj.name);
           $(".projectNombreJobs").val(obj.jobsCount);
        })
    $("#ctrl-modal-audit").addClass("is-active");
}
