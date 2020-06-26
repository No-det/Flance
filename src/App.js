import React from "react";
import { BrowserRouter, Route, Switch } from "react-router-dom";
import "./App.css";

//Importing Components
import Home from "./Components/Home";
import FreelancerHeader from "./Components/FreelancerHeader";

function App() {
  return (
    <BrowserRouter>
      <Switch>
        <Route exact path="/" component={Home} />
        <Route path="/test" component={FreelancerHeader} />
      </Switch>
    </BrowserRouter>
  );
}

export default App;
