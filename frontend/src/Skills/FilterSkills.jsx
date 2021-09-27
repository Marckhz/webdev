import React from "react";

import { useCallback, useEffect, useState } from "react"
import { getRequest } from "../Services/general"

const SKILLS_URL = "http://127.0.0.1:8000/api/skills";

export default function FilterSKill(props) {
    const [skills, setSkills] = useState([]);

    const loadSkills = useCallback(()=>{
        getRequest(SKILLS_URL).then(setSkills);
    },[]);
    useEffect(loadSkills, [ loadSkills]);
    console.log(skills)
    return (
            <select  onChange={e=>props.search(e.target.value)}>
                <option value={""}>-----</option>
                {skills.map((s)=>(
                    <option defaultValue={""} key={s.id} value={s.skill}>{s.skill}</option>
                ))}
            </select>
    )
}