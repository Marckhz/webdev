const getRequest = async (url) => {
    const response = await fetch(url);
    const  items  = await response.json();
    return items;
  };


  const postRequest = async (url, data) => {
    console.log(data);
    await fetch(url, {
    method: "POST",
        body:JSON.stringify(data),
        headers:{
            'Accept':'application/json',
            'Content-Type':'application/json'
        }
        });
  };


  export {getRequest, postRequest}