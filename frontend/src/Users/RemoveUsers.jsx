import React, { useCallback } from "react";

const deleteUsersBulk = async () => {
  await fetch("http://127.0.0.1:8000/api/users", {
    method: "DELETE",
  });
};

export default function RemoveUsers({ refetch, search }) {
  const onClick = useCallback(() => {
    deleteUsersBulk().then(refetch);
    search("")
  }, [refetch]);
  return <button onClick={onClick}>Remove Users</button>;
}
