import { useCallback, useEffect, useState } from "react";
import { Link } from "react-router-dom";
import AddUsers from "./AddUsers";
import RemoveUsers from "./RemoveUsers";
import { getRequest } from "../Services/general";
import "./Users.css";
import FilterSKill from "../Skills/FilterSkills";


const USER_URL = `http://127.0.0.1:8000/api/users`;
const USER_SKILL_URL = `http://127.0.0.1:8000/api/users/skills/`;

const UsersTable = ({ children }) => (
  <div className="users-table">{children}</div>
);

const UsersTableHeader = () => (
  <div className="users-table__row">
    <div className="users-table__col-header">Id</div>
    <div className="users-table__col-header">Name</div>
  </div>
);


const UserRow = ({ id, name }) => (
  <div className="users-table__row">
    <div>{id}</div>
    <Link to={`user/${id}`}>
      <div>{name}</div>
    </Link>
  </div>
);

const UsersActions = ({ children }) => (
  <div className="users-actions">{children}</div>
);

export default function Users() {
  const [users, setUsers] = useState([]);
  const [text, setText] = useState("");
  const [skill, setSkill] = useState("");
  const loadUsers = useCallback(() => {
    let url = skill.length > 0 ? USER_SKILL_URL+skill : USER_URL;
    console.log(url);
    getRequest(url).then(setUsers);
   }, [skill]);

  useEffect(loadUsers, [loadUsers]);
  console.log(skill.length > 0)
  return (
    <div>
      <UsersActions>
        <h5>Filter by skill</h5>
        <FilterSKill testid="dropdown" search={setSkill}/>
      </UsersActions>
      <UsersTable>
        <UsersTableHeader />
        {users.map((user) => (
          <UserRow data-testid="resolved" key={user.id} {...user} />
        ))}
      </UsersTable>
      <UsersActions>
        <input placeholder="user name" onChange={e=>setText(e.target.value)}/>
        <AddUsers refetch={loadUsers} user_data={text} text={"Add User"}/>
        <RemoveUsers refetch={loadUsers} search={setSkill}/>
      </UsersActions>
    </div>
  );
}
export { UsersActions, UserRow, UsersTable, UsersTableHeader}