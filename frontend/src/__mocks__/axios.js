const fake = [
    {
        id:1,
        name:"test"
    }
]
const fetchDataUsers = async () =>{
    return Promise.resolve(fake)
}

export { fetchDataUsers };