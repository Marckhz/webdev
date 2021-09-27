import "./App.css";
import Users from "./Users";
import UserProfile from "./UsersProfile";


import {
  BrowserRouter as Router,
  Switch,
  Route,
  Link
} from "react-router-dom";



function App() {
  return (
    <Router>
      <Switch>
        <Route exact path="/">
          <div  className="container">
            <h3>Platform Users</h3>
            <Users />
          </div>
        </Route>
        <Route path="/user/:id" component={UserProfile}/>
      </Switch>
    </Router>
  );
}

export default App;
