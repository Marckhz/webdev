import React, { useCallback, useState } from "react";



const addUsersBulk = async (user_data) => {
  console.log(user_data);
  await fetch("http://127.0.0.1:8000/api/users", {
    method: "POST",
    body:JSON.stringify({"name":user_data}),
    headers:{
      'Accept':'application/json',
      'Content-Type':'application/json'
    }
  });
};

export default function AddUsers({ refetch, user_data,}) {
  const onClick = useCallback(() => {
    addUsersBulk(user_data).then(refetch);
  }, [refetch, user_data]);
  return <button onClick={onClick}>Add Users</button>;
}
