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
                    +'<button onclick="copyRender()" class="copyx button is-ctrl-no-border js-modal-trigger" data-id="' + id + '" data-target="ctrl-modal-copy"><span class="icon is-small is-ctrl-color toto"><i class="fa-regular fa-copy"></i> </span> </button>'
                            + '<button onclick="render()" class="button"> <span class="icon is-small is-ctrl-color"> <i class="fa-solid fa-download"></i> </span></button>'
                            + '<button onclick="restaureRender()" class="restaurex button is-ctrl-no-border js-modal-trigger"  data-id="' + id + '" data-target="ctrl-modal-restore"><span class="icon is-small is-ctrl-color"> <i class="fa-solid fa-arrows-rotate"></i> </span>  </button>'
                            + '<button onclick="auditRender()" class="auditx button is-ctrl-no-border js-modal-trigger" data-target="ctrl-modal-audit" data-id="' + id + '" data-name="'+ this.name +'"><span class="icon is-small is-ctrl-color"><i class="fa-solid fa-circle-info"></i> </button>'
                            + '</td>'
                    + '</tr>')
            });
        })
}

const copyProject = () => {
    console.log($(".projectNameOld").val())
    console.log($(".projectNameNew").val())

    if($(".projectNameOld").val() == $(".projectNameNew").val() ) {
        alert("Attention c'est le même nom");
    }else {
        alert("Votre copie a été crée");
    }


    // save in base


    //close modal
    //$("#ctrl-modal-copy").removeClass("is-active");
    // refresh table
    getList();
}


const auditRender = () => {

    $(".auditx").on("click", function (event) {
        var id = $(this).data('id');
        var dataId = $(this).attr("data-id");
        var dataName = $(this).attr("data-name");
        //console.log("The data-id of clicked item is: " + dataId + " " + id);
        
        audit(dataId, dataName);
    });
}

const copyRender = () => {
    $(".copyx").on("click", function (event) {
        var id = $(this).data('id');
       
        fetch("http://127.0.0.1:5000/test")
        .then(response => response.json())
        .then(data => {
           const obj = data.projects.find(data => data.id == id)
           $(".projectNameOld").val(obj.name);
        })
        $("#ctrl-modal-copy").addClass("is-active");
    });
}

const restaureRender = () => {
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

const audit = (id, nameProject) => {
    // clear field
    $(".projectNameA").val("");
    $(".projectNombreJobs").val("");
    $(".projectNombreApp").val("");
    $(".projectNamePipeline").val(""); 
    
    console.log("id : "+ id);
    console.log(nameProject);
    $('.loader-wrapper').addClass('is-active');
    fetch(`http://127.0.0.1:5000/audit_count/${id}`)
        // fetch('./assets/data/projets.json')
        .then(response => response.json())
        .then(data => {
            console.log(data)
           $(".projectNameA").val(nameProject);
           $(".projectNombreJobs").val(data.countjob);
           $(".projectNombreApp").val(data.countapp);
           $(".projectNamePipeline").val(data.countpipeline);
        }).finally(() => $('.loader-wrapper').removeClass('is-active'))
        .catch(err => console.log(err))
        $("#ctrl-modal-audit").addClass("is-active")
        
}
