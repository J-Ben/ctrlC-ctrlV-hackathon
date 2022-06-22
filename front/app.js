function getList() {

    var myHeaders = new Headers();

var myInit = { method: 'GET',
               headers: myHeaders,
               mode: 'no-cors',
               cache: 'no-cache' };

    fetch('./assets/data/projects.json',myInit)
    .then(response => {
        
        console.log(response)
    } );
   

}

function render() {
    console.log('click')
    $(".test").on("click",function(event){
     var id = $(this).data('id'); 
    var dataId = $(this).attr("data-id");
    console.log("The data-id of clicked item is: " + dataId + " "+ id);
  });
    
  $(".copyx").on("click",function(event){
    var id = $(this).data('id'); 
   var dataId = $(this).attr("data-id");
   console.log("The data-id of clicked item is: " + dataId + " "+ id);
   $("#ctrl-modal-audit").addClass("is-active"); 
 });
    
}


function archiver() {
    
   
}

function restaure() {
    
   
}

function audit() {
    
   
}
