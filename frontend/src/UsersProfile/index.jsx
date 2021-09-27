import React, { useCallback, useEffect, useState } from "react";
import { useParams} from "react-router-dom";
import './UserProfile.css'
import { UserRow, UsersActions, UsersTable, UsersTableHeade } from "../Users";
import { getRequest } from "../Services/general";
import { postRequest } from "../Services/general"; 

//import AddUsers from "../Users/AddUsers";
/*
Profile
*/

const USER_URL = `http://localhost:8000/api/users/`;
const CREATE_SKILL_URL = `http://127.0.0.1:8000/api/users/create-skill`;


function AddUsers({ refetch, user, skill, text }) {
    const data={user:{}, skill:{} }
    data.user = user;
    data.skill.skill = skill;
    const onClick = useCallback(() => {
        postRequest(CREATE_SKILL_URL, data).then(refetch);
      text("")
    }, [refetch, data]);
    return <button onClick={onClick} >Add Skill</button>;
  }


export default function(){
    const [user, setUser] = useState({subscriptions:[]});
    const [text, setText] = useState();
    const { id }  = useParams();
    console.log(`id ${id}`);
    const loadUser = useCallback(()=>{
        getRequest(USER_URL+id).then(setUser) 
    },[])
    useEffect(loadUser,[loadUser])
    return (
        <div>
            <div className="profile-container">
                <div>
                    <h2>User: </h2>
                </div>
                <div>
                    <h2>{user.name}</h2>
                </div>
            </div>
            <div className="skills-container">
                <div className="row">
                    <h3>Skills</h3>
                    <ul>
                        {user.subscriptions.map((s)=>(
                            <li key={s.id}>{s.skill} </li>    
                        ))}
                    </ul>
                    <div className="profile-container">
                        <div className="row">
                            <div className="item">
                                <input placeholder="add skill" value={text}  onChange={e=>{setText(e.target.value)}} />
                            </div>
                            <div className="item">
                                <AddUsers refetch={loadUser} skill={text} user={user} text={setText}  />
                            </div>
                        </div>
                    </div>
                </div>
            </div> 
        </div>
    )
}