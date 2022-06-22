
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


    /*   try {
          var myHeaders = new Headers();
          let res = fetch('http://127.0.0.1:5000/test')
          .then((res)  => res.json())
          .then(data =>{
              console.log(data);
          }) 
          .catch(const(error) {
              console.log(error);
          })
          
      } catch (error) {
          console.log(error);
  
      } */
}

const render = () => {

    let projects = getList();
    console.log(projects);
}


const archiver = () => {


}

const restaure = () => {


}

const audit = () => {


}
